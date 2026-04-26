
from datetime import datetime
from typing import Dict, List, Optional, Union

import pyrogram
from pyrogram import enums, raw, types, utils
from pyrogram.types.messages_and_media.message import Str

from ..object import Object
from ..update import Update


class Poll(Object, Update):
    """A Poll.

    Parameters:
        id (``str``):
            Unique poll identifier.

        question (:obj:`~pyrogram.types.FormattedText`, *optional*):
            Poll question, 1-300 characters.

        options (List of :obj:`~pyrogram.types.PollOption`):
            List of poll options.

        total_voter_count (``int``, *optional*):
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
            True, if the poll allows to change the chosen answer options.

        chosen_option_ids (List of ``int``, *optional*):
            Array of 0-based index of the chosen option), None in case of no vote yet.

        correct_option_ids (List of ``int``, *optional*):
            Array of 0-based identifiers of the correct answer options.
            Available only for polls in quiz mode which are closed or were sent (not forwarded) by the bot or to the private chat with the bot.

        explanation (:obj:`pyrogram.types.FormattedText`, *optional*):
            Text that is shown when a user chooses an incorrect answer or taps on the lamp icon in a quiz-style poll,
            0-200 characters.

        open_period (``int``, *optional*):
            Amount of time in seconds the poll will be active after creation.

        close_date (:py:obj:`~datetime.datetime`, *optional*):
            Point in time when the poll will be automatically closed.

        description (:obj:`~pyrogram.types.FormattedText`, *optional*):
            Description of the poll.
            Only for polls inside the :obj:`~pyrogram.types.Message` object.

        voter (:obj:`~pyrogram.types.User`, *optional*):
            The user that voted in the poll.
    """

    def __init__(
        self,
        *,
        client: "pyrogram.Client" = None,
        id: str,
        question: Optional["types.FormattedText"] = None,
        options: List["types.PollOption"],
        total_voter_count: Optional[int] = None,
        is_closed: bool,
        is_anonymous: Optional[bool] = None,
        type: Optional["enums.PollType"] = None,
        allows_multiple_answers: Optional[bool] = None,
        allows_revoting: Optional[bool] = None,
        chosen_option_ids: Optional[List[int]] = None,
        correct_option_ids: Optional[List[int]] = None,
        explanation: Optional["types.FormattedText"] = None,
        open_period: Optional[int] = None,
        close_date: Optional[datetime] = None,
        description: Optional["types.FormattedText"] = None,
        voter: Optional["types.User"] = None,
    ):
        super().__init__(client)

        self.id = id
        self.question = question
        self.options = options
        self.total_voter_count = total_voter_count
        self.is_closed = is_closed
        self.is_anonymous = is_anonymous
        self.type = type
        self.allows_multiple_answers = allows_multiple_answers
        self.allows_revoting = allows_revoting
        self.chosen_option_ids = chosen_option_ids
        self.correct_option_ids = correct_option_ids
        self.explanation = explanation
        self.open_period = open_period
        self.close_date = close_date
        self.description = description
        self.voter = voter

    @staticmethod
    def _parse(
        client,
        media_poll: Union["raw.types.MessageMediaPoll", "raw.types.UpdateMessagePoll"],
        description: Optional["types.FormattedText"] = None,
        users: Dict[int, "raw.types.User"] = {},
        chats: Dict[int, "raw.types.Chat"] = {},
    ) -> "Poll":
        poll: raw.types.Poll = media_poll.poll
        poll_results: raw.types.PollResults = media_poll.results
        results: List[raw.types.PollAnswerVoters] = poll_results.results

        chosen_option_ids = []
        correct_option_ids = []
        options = []

        vote_percentages = Poll.get_vote_percentage(
            [(results[i].voters if results else 0) for i in range(len(poll.answers))],
            media_poll.results.total_voters or 0,
        )

        for i, answer in enumerate(poll.answers):
            voter_count = 0

            result = None

            if results:
                result = results[i]
                voter_count = result.voters

                if result.chosen:
                    chosen_option_ids.append(i)

                if result.correct:
                    correct_option_ids.append(i)

            options.append(
                types.PollOption(
                    persistent_id=answer.option.decode(),
                    text=types.FormattedText._parse(client, answer.text),
                    voter_count=voter_count,
                    vote_percentage=vote_percentages[i],
                    recent_voters=types.List(
                        [
                            types.Chat._parse_chat(
                                client,
                                users.get(
                                    utils.get_raw_peer_id(voter_peer)
                                    or chats.get(utils.get_raw_peer_id(voter_peer))
                                ),
                            )
                            for voter_peer in result.recent_voters
                        ]
                    )
                    if result and result.recent_voters
                    else None,
                    added_by_user=types.User._parse(
                        client, users.get(utils.get_raw_peer_id(answer.added_by))
                    ),
                    added_by_chat=types.Chat._parse_chat(
                        client, chats.get(utils.get_raw_peer_id(answer.added_by))
                    ),
                    addition_date=utils.datetime_to_timestamp(getattr(answer, "date", None)),
                    client=client,
                )
            )

        return Poll(
            id=str(poll.id),
            question=types.FormattedText._parse(client, poll.question),
            options=options,
            total_voter_count=media_poll.results.total_voters,
            is_closed=poll.closed,
            is_anonymous=not poll.public_voters,
            type=enums.PollType.QUIZ if poll.quiz else enums.PollType.REGULAR,
            allows_multiple_answers=poll.multiple_choice,
            allows_revoting=not poll.revoting_disabled,
            chosen_option_ids=chosen_option_ids or None,
            correct_option_ids=correct_option_ids or None,
            explanation=types.FormattedText._parse(
                client,
                raw.types.TextWithEntities(
                    text=poll_results.solution,
                    entities=poll_results.solution_entities
                )
            )
            if poll_results.solution
            else None,
            open_period=poll.close_period,
            close_date=utils.timestamp_to_datetime(poll.close_date),
            description=description,
            client=client,
        )

    @staticmethod
    def _parse_update(
        client,
        update: Union["raw.types.UpdateMessagePoll", "raw.types.UpdateMessagePollVote"],
        users: Dict[int, "raw.types.User"] = {},
        chats: Dict[int, "raw.types.Chat"] = {},
    ) -> "Poll":
        if isinstance(update, raw.types.UpdateMessagePoll):
            if update.poll is not None:
                return Poll._parse(client, update)

            results = update.results.results
            chosen_option_ids = []
            correct_option_ids = []
            options = []

            for i, result in enumerate(results):
                if result.chosen:
                    chosen_option_ids.append(i)

                if result.correct:
                    correct_option_ids.append(i)

                options.append(
                    types.PollOption(
                        persistent_id=result.option.decode(), voter_count=result.voters, client=client
                    )
                )

            return Poll(
                id=str(update.poll_id),
                options=options,
                total_voter_count=update.results.total_voters,
                is_closed=False,
                chosen_option_ids=chosen_option_ids or None,
                correct_option_ids=correct_option_ids or None,
                client=client,
            )

        if isinstance(update, raw.types.UpdateMessagePollVote):
            return Poll(
                id=str(update.poll_id),
                options=[
                    types.PollOption(persistent_id=option.decode(), client=client)
                    for option in update.options
                ],
                is_closed=False,
                voter=types.User._parse(client, users[update.peer.user_id]),
                client=client,
            )

    @staticmethod
    def get_vote_percentage(voter_counts: List[int], total_voter_count: int) -> List[int]:
        total = sum(voter_counts)

        total_voter_count = min(total_voter_count, total)

        result = [0] * len(voter_counts)

        if total_voter_count == 0:
            return result

        if total_voter_count != total:
            for i, vc in enumerate(voter_counts):
                result[i] = (vc * 200 + total_voter_count) // total_voter_count // 2
            return result

        percent_sum = 0
        gap = [0] * len(voter_counts)
        for i, vc in enumerate(voter_counts):
            multiplied = vc * 100
            result[i] = multiplied // total_voter_count
            gap[i] = (result[i] + 1) * total_voter_count - multiplied
            percent_sum += result[i]

        if percent_sum == 100:
            return result

        options: Dict[int, Dict] = {}
        for i, vc in enumerate(voter_counts):
            key = vc + 1
            if key not in options:
                options[key] = {"pos": i, "count": 0}
            options[key]["count"] += 1

        sorted_options = []
        for key, opt in options.items():
            pos = opt["pos"]
            vc = voter_counts[pos]
            g = gap[pos]

            if g > total_voter_count / 2:
                continue
            if total_voter_count % 2 == 0 and g == total_voter_count // 2 and result[pos] >= 50:
                continue
            sorted_options.append(opt)

        sorted_options.sort(key=lambda o: (gap[o["pos"]], -o["count"], o["pos"]))

        left_percent = 100 - percent_sum
        for opt in sorted_options:
            if opt["count"] <= left_percent:
                left_percent -= opt["count"]
                pos = opt["pos"]
                target_vc = voter_counts[pos]
                for i, vc in enumerate(voter_counts):
                    if vc == target_vc:
                        result[i] += 1
                if left_percent == 0:
                    break

        return result

    async def stop(
        self,
        chat_id: Union[int, str] = None,
        message_id: int = None
    ):
        """Bound method *stop* of :obj:`~pyrogram.types.Poll`.

        Use as a shortcut for:

        .. code-block:: python

            await client.stop_poll(
                chat_id=chat_id,
                message_id=message_id
            )

        Example:
            .. code-block:: python

               await poll.stop()
        """
        return await self._client.stop_poll(
            chat_id=chat_id or self.chat.id if hasattr(self, "chat") else chat_id,
            message_id=message_id or self.id if hasattr(self, "id") else message_id
        )
