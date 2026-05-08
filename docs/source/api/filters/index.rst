Update Filters
==============

Filters are used to selectively handle only certain types of updates.

.. code-block:: python

    from pyrogram import Client, filters

    app = Client("my_account")

    @app.on_message(filters.private & filters.text)
    async def handler(client, message):
        await message.reply(message.text)

-----

.. automodule:: pyrogram.filters
    :members:
    :undoc-members:
    :exclude-members: all_filter,me_filter,bot_filter,incoming_filter,outgoing_filter,text_filter,reply_filter,reaction_filter,forwarded_filter,caption_filter,audio_filter,document_filter,photo_filter,sticker_filter,animation_filter,game_filter,giveaway_filter,giveaway_result_filter,gift_code_filter,star_gift_filter,video_filter,media_group_filter,voice_filter,video_note_filter,contact_filter,location_filter,venue_filter,web_page_filter,poll_filter,dice_filter,media_spoiler_filter,private_filter,group_filter,channel_filter,new_chat_members_filter,left_chat_member_filter,new_chat_title_filter,new_chat_photo_filter,delete_chat_photo_filter,group_chat_created_filter,supergroup_chat_created_filter,channel_chat_created_filter,migrate_to_chat_id_filter,migrate_from_chat_id_filter,pinned_message_filter,game_high_score_filter,reply_keyboard_filter,inline_keyboard_filter,mentioned_filter,via_bot_filter,video_chat_started_filter,video_chat_ended_filter,video_chat_members_invited_filter,successful_payment_filter,service_filter,media_filter,scheduled_filter,from_scheduled_filter,linked_channel_filter,forum_topic_closed_filter,forum_topic_created_filter,forum_topic_edited_filter,forum_topic_reopened_filter,general_topic_hidden_filter,general_topic_unhidden_filter, Filter, InvertFilter, AndFilter, OrFilter
