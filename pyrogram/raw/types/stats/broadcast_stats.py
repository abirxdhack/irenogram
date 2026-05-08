
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class BroadcastStats(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.stats.BroadcastStats`.

    Details:
        - Layer: ``224``
        - ID: ``396CA5FC``

    Parameters:
        period (:obj:`StatsDateRangeDays <pyrogram.raw.base.StatsDateRangeDays>`):
            N/A

        followers (:obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`):
            N/A

        views_per_post (:obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`):
            N/A

        shares_per_post (:obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`):
            N/A

        reactions_per_post (:obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`):
            N/A

        views_per_story (:obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`):
            N/A

        shares_per_story (:obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`):
            N/A

        reactions_per_story (:obj:`StatsAbsValueAndPrev <pyrogram.raw.base.StatsAbsValueAndPrev>`):
            N/A

        enabled_notifications (:obj:`StatsPercentValue <pyrogram.raw.base.StatsPercentValue>`):
            N/A

        growth_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        followers_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        mute_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        top_hours_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        interactions_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        iv_interactions_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        views_by_source_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        new_followers_by_source_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        languages_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        reactions_by_emotion_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        story_interactions_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        story_reactions_by_emotion_graph (:obj:`StatsGraph <pyrogram.raw.base.StatsGraph>`):
            N/A

        recent_posts_interactions (List of :obj:`PostInteractionCounters <pyrogram.raw.base.PostInteractionCounters>`):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            stats.GetBroadcastStats
    """

    __slots__: List[str] = ["period", "followers", "views_per_post", "shares_per_post", "reactions_per_post", "views_per_story", "shares_per_story", "reactions_per_story", "enabled_notifications", "growth_graph", "followers_graph", "mute_graph", "top_hours_graph", "interactions_graph", "iv_interactions_graph", "views_by_source_graph", "new_followers_by_source_graph", "languages_graph", "reactions_by_emotion_graph", "story_interactions_graph", "story_reactions_by_emotion_graph", "recent_posts_interactions"]

    ID = 0x396ca5fc
    QUALNAME = "types.stats.BroadcastStats"

    def __init__(self, *, period: "raw.base.StatsDateRangeDays", followers: "raw.base.StatsAbsValueAndPrev", views_per_post: "raw.base.StatsAbsValueAndPrev", shares_per_post: "raw.base.StatsAbsValueAndPrev", reactions_per_post: "raw.base.StatsAbsValueAndPrev", views_per_story: "raw.base.StatsAbsValueAndPrev", shares_per_story: "raw.base.StatsAbsValueAndPrev", reactions_per_story: "raw.base.StatsAbsValueAndPrev", enabled_notifications: "raw.base.StatsPercentValue", growth_graph: "raw.base.StatsGraph", followers_graph: "raw.base.StatsGraph", mute_graph: "raw.base.StatsGraph", top_hours_graph: "raw.base.StatsGraph", interactions_graph: "raw.base.StatsGraph", iv_interactions_graph: "raw.base.StatsGraph", views_by_source_graph: "raw.base.StatsGraph", new_followers_by_source_graph: "raw.base.StatsGraph", languages_graph: "raw.base.StatsGraph", reactions_by_emotion_graph: "raw.base.StatsGraph", story_interactions_graph: "raw.base.StatsGraph", story_reactions_by_emotion_graph: "raw.base.StatsGraph", recent_posts_interactions: List["raw.base.PostInteractionCounters"]) -> None:
        self.period = period
        self.followers = followers
        self.views_per_post = views_per_post
        self.shares_per_post = shares_per_post
        self.reactions_per_post = reactions_per_post
        self.views_per_story = views_per_story
        self.shares_per_story = shares_per_story
        self.reactions_per_story = reactions_per_story
        self.enabled_notifications = enabled_notifications
        self.growth_graph = growth_graph
        self.followers_graph = followers_graph
        self.mute_graph = mute_graph
        self.top_hours_graph = top_hours_graph
        self.interactions_graph = interactions_graph
        self.iv_interactions_graph = iv_interactions_graph
        self.views_by_source_graph = views_by_source_graph
        self.new_followers_by_source_graph = new_followers_by_source_graph
        self.languages_graph = languages_graph
        self.reactions_by_emotion_graph = reactions_by_emotion_graph
        self.story_interactions_graph = story_interactions_graph
        self.story_reactions_by_emotion_graph = story_reactions_by_emotion_graph
        self.recent_posts_interactions = recent_posts_interactions

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "BroadcastStats":
        
        period = TLObject.read(b)
        
        followers = TLObject.read(b)
        
        views_per_post = TLObject.read(b)
        
        shares_per_post = TLObject.read(b)
        
        reactions_per_post = TLObject.read(b)
        
        views_per_story = TLObject.read(b)
        
        shares_per_story = TLObject.read(b)
        
        reactions_per_story = TLObject.read(b)
        
        enabled_notifications = TLObject.read(b)
        
        growth_graph = TLObject.read(b)
        
        followers_graph = TLObject.read(b)
        
        mute_graph = TLObject.read(b)
        
        top_hours_graph = TLObject.read(b)
        
        interactions_graph = TLObject.read(b)
        
        iv_interactions_graph = TLObject.read(b)
        
        views_by_source_graph = TLObject.read(b)
        
        new_followers_by_source_graph = TLObject.read(b)
        
        languages_graph = TLObject.read(b)
        
        reactions_by_emotion_graph = TLObject.read(b)
        
        story_interactions_graph = TLObject.read(b)
        
        story_reactions_by_emotion_graph = TLObject.read(b)
        
        recent_posts_interactions = TLObject.read(b)
        
        return BroadcastStats(period=period, followers=followers, views_per_post=views_per_post, shares_per_post=shares_per_post, reactions_per_post=reactions_per_post, views_per_story=views_per_story, shares_per_story=shares_per_story, reactions_per_story=reactions_per_story, enabled_notifications=enabled_notifications, growth_graph=growth_graph, followers_graph=followers_graph, mute_graph=mute_graph, top_hours_graph=top_hours_graph, interactions_graph=interactions_graph, iv_interactions_graph=iv_interactions_graph, views_by_source_graph=views_by_source_graph, new_followers_by_source_graph=new_followers_by_source_graph, languages_graph=languages_graph, reactions_by_emotion_graph=reactions_by_emotion_graph, story_interactions_graph=story_interactions_graph, story_reactions_by_emotion_graph=story_reactions_by_emotion_graph, recent_posts_interactions=recent_posts_interactions)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        
        b.write(self.period.write())
        
        b.write(self.followers.write())
        
        b.write(self.views_per_post.write())
        
        b.write(self.shares_per_post.write())
        
        b.write(self.reactions_per_post.write())
        
        b.write(self.views_per_story.write())
        
        b.write(self.shares_per_story.write())
        
        b.write(self.reactions_per_story.write())
        
        b.write(self.enabled_notifications.write())
        
        b.write(self.growth_graph.write())
        
        b.write(self.followers_graph.write())
        
        b.write(self.mute_graph.write())
        
        b.write(self.top_hours_graph.write())
        
        b.write(self.interactions_graph.write())
        
        b.write(self.iv_interactions_graph.write())
        
        b.write(self.views_by_source_graph.write())
        
        b.write(self.new_followers_by_source_graph.write())
        
        b.write(self.languages_graph.write())
        
        b.write(self.reactions_by_emotion_graph.write())
        
        b.write(self.story_interactions_graph.write())
        
        b.write(self.story_reactions_by_emotion_graph.write())
        
        b.write(Vector(self.recent_posts_interactions))
        
        return b.getvalue()
