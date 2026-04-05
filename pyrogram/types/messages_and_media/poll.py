from datetime import datetime
from typing import List, Union, Optional

import pyrogram
from pyrogram import raw, enums, utils
from pyrogram import types
from ..object import Object
from ..update import Update


class Poll(Object, Update):
    """A Poll.

    Parameters:
        id (``str``):
            Unique poll identifier.

        question (``str``):
            Poll question, 1-255 characters.

        options (List of :obj:`~pyrogram.types.PollOption`):
            List of poll options.

        question_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities like usernames, URLs, bot commands, etc. that appear in the poll question.

        total_voter_count (``int``):
            Total number of users that voted in the poll.

        is_closed (``bool``):
            True, if the poll is closed.

        is_anonymous (``bool``, *optional*):
            True, if the poll is anonymous.

        type (:obj:`~pyrogram.enums.PollType`, *optional*):
            Poll type.

        allows_multiple_answers (``bool``, *optional*):
            True, if the poll allows multiple answers.

        allows_revoting (``bool``, *optional*):
            True, if voters can change their vote (revoting enabled).

        hide_results_until_close (``bool``, *optional*):
            True, if results are hidden until the poll is closed.

        shuffle_answers (``bool``, *optional*):
            True, if poll answers are shuffled for each voter.

        open_answers (``bool``, *optional*):
            True, if users can add new answer options dynamically.

        chosen_option_id (``int``, *optional*):
            0-based index of the chosen option. None if no vote cast yet.

        correct_option_ids (List of ``int``, *optional*):
            0-based identifiers of all correct answer options.
            Available only for quiz-mode polls.

        correct_option_id (``int``, *optional*):
            0-based identifier of the first correct answer option, for backward compatibility.

        explanation (``str``, *optional*):
            Text shown when a user chooses an incorrect answer in a quiz-style poll.

        explanation_entities (List of :obj:`~pyrogram.types.MessageEntity`, *optional*):
            Special entities in the explanation.

        open_period (``int``, *optional*):
            Amount of time in seconds the poll will be active after creation.

        close_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time when the poll will be automatically closed.

        recent_voters (List of :obj:`~pyrogram.types.User`, *optional*):
            List of users who recently voted.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        question: str,
        options: List["types.PollOption"],
        question_entities: List["types.MessageEntity"] = None,
        total_voter_count: int,
        is_closed: bool,
        is_anonymous: bool = None,
        type: "enums.PollType" = None,
        allows_multiple_answers: bool = None,
        allows_revoting: bool = None,
        hide_results_until_close: bool = None,
        shuffle_answers: bool = None,
        open_answers: bool = None,
        chosen_option_id: Optional[int] = None,
        correct_option_ids: Optional[List[int]] = None,
        correct_option_id: Optional[int] = None,
        explanation: Optional[str] = None,
        explanation_entities: Optional[List["types.MessageEntity"]] = None,
        open_period: Optional[int] = None,
        close_date: Optional[datetime] = None,
        recent_voters: List["types.User"] = None,
    ):
        super().__init__(client)

        self.id = id
        self.question = question
        self.options = options
        self.question_entities = question_entities
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.allows_revoting = allows_revoting
        self.hide_results_until_close = hide_results_until_close
        self.shuffle_answers = shuffle_answers
        self.open_answers = open_answers
        self.chosen_option_id = chosen_option_id
        self.correct_option_ids = correct_option_ids or (
            [correct_option_id] if correct_option_id is not None else None
        )
        self.correct_option_id = correct_option_id
        self.explanation = explanation
        self.explanation_entities = explanation_entities
        self.open_period = open_period
        self.close_date = close_date
        self.recent_voters = recent_voters

    @staticmethod
    async def _parse(
        client,
        media_poll: Union["raw.types.MessageMediaPoll", "raw.types.UpdateMessagePoll"],
        users: dict,
    ) -> "Poll":
        poll: raw.types.Poll = media_poll.poll
        poll_results: raw.types.PollResults = media_poll.results
        results: List[raw.types.PollAnswerVoters] = poll_results.results or []

        chosen_option_id = None
        correct_option_ids = []
        options = []

        for i, answer in enumerate(poll.answers):
            voter_count = 0

            if results and i < len(results):
                result = results[i]
                voter_count = result.voters or 0

                if result.chosen:
                    chosen_option_id = i

                if result.correct:
                    correct_option_ids.append(i)

            o_entities = (
                [types.MessageEntity._parse(client, entity, {}) for entity in answer.text.entities]
                if answer.text.entities
                else []
            )
            option_entities = types.List(filter(lambda x: x is not None, o_entities))

            options.append(
                types.PollOption(
                    text=answer.text.text,
                    voter_count=voter_count,
                    data=answer.option,
                    entities=option_entities,
                )
            )

        q_entities = (
            [types.MessageEntity._parse(client, entity, {}) for entity in poll.question.entities]
            if poll.question.entities
            else []
        )
        question_entities = types.List(filter(lambda x: x is not None, q_entities))

        recent_voters = []
        for peer in (poll_results.recent_voters or []):
            try:
                peer_user_id = getattr(peer, "user_id", None)
                if peer_user_id and peer_user_id in users:
                    voter = types.User._parse(client, users[peer_user_id])
                    recent_voters.append(voter)
            except Exception:
                pass

        correct_option_id = correct_option_ids[0] if correct_option_ids else None

        return Poll(
            id=str(poll.id),
            question=poll.question.text,
            options=options,
            question_entities=question_entities or None,
            total_voter_count=poll_results.total_voters or 0,
            is_closed=poll.closed or False,
            is_anonymous=not poll.public_voters,
            type=enums.PollType.QUIZ if poll.quiz else enums.PollType.REGULAR,
            allows_multiple_answers=poll.multiple_choice or False,
            allows_revoting=not (poll.revoting_disabled or False),
            hide_results_until_close=poll.hide_results_until_close or False,
            shuffle_answers=poll.shuffle_answers or False,
            open_answers=poll.open_answers or False,
            chosen_option_id=chosen_option_id,
            correct_option_ids=correct_option_ids if correct_option_ids else None,
            correct_option_id=correct_option_id,
            explanation=poll_results.solution,
            explanation_entities=(
                [types.MessageEntity._parse(client, i, {}) for i in poll_results.solution_entities]
                if poll_results.solution_entities
                else None
            ),
            open_period=poll.close_period,
            close_date=utils.timestamp_to_datetime(poll.close_date),
            recent_voters=recent_voters if recent_voters else None,
            client=client,
        )

    @staticmethod
    async def _parse_update(
        client,
        update: "raw.types.UpdateMessagePoll",
        users: dict,
    ) -> "Poll":
        if update.poll is not None:
            return await Poll._parse(client, update, users)

        results = (update.results.results or []) if update.results else []
        chosen_option_id = None
        correct_option_ids = []
        options = []

        for i, result in enumerate(results):
            if result.chosen:
                chosen_option_id = i

            if result.correct:
                correct_option_ids.append(i)

            options.append(
                types.PollOption(
                    text="",
                    voter_count=result.voters or 0,
                    data=result.option,
                )
            )

        recent_voters = []
        if update.results and update.results.recent_voters:
            for peer in update.results.recent_voters:
                try:
                    peer_user_id = getattr(peer, "user_id", None)
                    if peer_user_id and peer_user_id in users:
                        voter = types.User._parse(client, users[peer_user_id])
                        recent_voters.append(voter)
                except Exception:
                    pass

        correct_option_id = correct_option_ids[0] if correct_option_ids else None

        return Poll(
            id=str(update.poll_id),
            question="",
            options=options,
            total_voter_count=(update.results.total_voters or 0) if update.results else 0,
            is_closed=False,
            chosen_option_id=chosen_option_id,
            correct_option_ids=correct_option_ids if correct_option_ids else None,
            correct_option_id=correct_option_id,
            recent_voters=recent_voters if recent_voters else None,
            client=client,
        )
