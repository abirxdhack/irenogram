Bound Methods
=============

Bound methods are shortcuts available directly on Irenogram types.

-----

.. currentmodule:: pyrogram.types

Message
-------

.. hlist::
    :columns: 2

    - :meth:`~Message.click`
    - :meth:`~Message.delete`
    - :meth:`~Message.download`
    - :meth:`~Message.forward`
    - :meth:`~Message.copy`
    - :meth:`~Message.pin`
    - :meth:`~Message.unpin`
    - :meth:`~Message.edit`
    - :meth:`~Message.edit_text`
    - :meth:`~Message.edit_caption`
    - :meth:`~Message.edit_media`
    - :meth:`~Message.edit_reply_markup`
    - :meth:`~Message.reply`
    - :meth:`~Message.reply_text`
    - :meth:`~Message.reply_animation`
    - :meth:`~Message.reply_audio`
    - :meth:`~Message.reply_cached_media`
    - :meth:`~Message.reply_chat_action`
    - :meth:`~Message.reply_contact`
    - :meth:`~Message.reply_document`
    - :meth:`~Message.reply_game`
    - :meth:`~Message.reply_inline_bot_result`
    - :meth:`~Message.reply_location`
    - :meth:`~Message.reply_media_group`
    - :meth:`~Message.reply_photo`
    - :meth:`~Message.reply_poll`
    - :meth:`~Message.reply_sticker`
    - :meth:`~Message.reply_venue`
    - :meth:`~Message.reply_video`
    - :meth:`~Message.reply_video_note`
    - :meth:`~Message.reply_voice`
    - :meth:`~Message.react`
    - :meth:`~Message.read`

.. toctree::
    :hidden:

    click <Message.click>
    delete <Message.delete>
    download <Message.download>
    forward <Message.forward>
    copy <Message.copy>
    pin <Message.pin>
    unpin <Message.unpin>
    edit <Message.edit>
    edit_text <Message.edit_text>
    edit_caption <Message.edit_caption>
    edit_media <Message.edit_media>
    edit_reply_markup <Message.edit_reply_markup>
    reply <Message.reply>
    reply_text <Message.reply_text>
    reply_animation <Message.reply_animation>
    reply_audio <Message.reply_audio>
    reply_cached_media <Message.reply_cached_media>
    reply_chat_action <Message.reply_chat_action>
    reply_contact <Message.reply_contact>
    reply_document <Message.reply_document>
    reply_game <Message.reply_game>
    reply_inline_bot_result <Message.reply_inline_bot_result>
    reply_location <Message.reply_location>
    reply_media_group <Message.reply_media_group>
    reply_photo <Message.reply_photo>
    reply_poll <Message.reply_poll>
    reply_sticker <Message.reply_sticker>
    reply_venue <Message.reply_venue>
    reply_video <Message.reply_video>
    reply_video_note <Message.reply_video_note>
    reply_voice <Message.reply_voice>
    react <Message.react>
    read <Message.read>

Chat
----

.. hlist::
    :columns: 2

    - :meth:`~Chat.archive`
    - :meth:`~Chat.unarchive`
    - :meth:`~Chat.set_title`
    - :meth:`~Chat.set_description`
    - :meth:`~Chat.set_photo`
    - :meth:`~Chat.ban_member`
    - :meth:`~Chat.unban_member`
    - :meth:`~Chat.restrict_member`
    - :meth:`~Chat.promote_member`
    - :meth:`~Chat.get_member`
    - :meth:`~Chat.get_members`
    - :meth:`~Chat.add_members`
    - :meth:`~Chat.join`
    - :meth:`~Chat.leave`
    - :meth:`~Chat.mark_unread`
    - :meth:`~Chat.set_protected_content`
    - :meth:`~Chat.unpin_all_messages`

.. toctree::
    :hidden:

    archive <Chat.archive>
    unarchive <Chat.unarchive>
    set_title <Chat.set_title>
    set_description <Chat.set_description>
    set_photo <Chat.set_photo>
    ban_member <Chat.ban_member>
    unban_member <Chat.unban_member>
    restrict_member <Chat.restrict_member>
    promote_member <Chat.promote_member>
    get_member <Chat.get_member>
    get_members <Chat.get_members>
    add_members <Chat.add_members>
    join <Chat.join>
    leave <Chat.leave>
    mark_unread <Chat.mark_unread>
    set_protected_content <Chat.set_protected_content>
    unpin_all_messages <Chat.unpin_all_messages>

User
----

.. hlist::
    :columns: 2

    - :meth:`~User.archive`
    - :meth:`~User.unarchive`
    - :meth:`~User.block`
    - :meth:`~User.unblock`

.. toctree::
    :hidden:

    archive <User.archive>
    unarchive <User.unarchive>
    block <User.block>
    unblock <User.unblock>

Callback Query
--------------

.. hlist::
    :columns: 2

    - :meth:`~CallbackQuery.answer`
    - :meth:`~CallbackQuery.edit_message_text`
    - :meth:`~CallbackQuery.edit_message_caption`
    - :meth:`~CallbackQuery.edit_message_media`
    - :meth:`~CallbackQuery.edit_message_reply_markup`
    - :meth:`~ChosenInlineResult.edit_message_text`
    - :meth:`~ChosenInlineResult.edit_message_caption`
    - :meth:`~ChosenInlineResult.edit_message_media`
    - :meth:`~ChosenInlineResult.edit_message_reply_markup`

.. toctree::
    :hidden:

    answer <CallbackQuery.answer>
    edit_message_text <CallbackQuery.edit_message_text>
    edit_message_caption <CallbackQuery.edit_message_caption>
    edit_message_media <CallbackQuery.edit_message_media>
    edit_message_reply_markup <CallbackQuery.edit_message_reply_markup>
    edit_message_text <ChosenInlineResult.edit_message_text>
    edit_message_caption <ChosenInlineResult.edit_message_caption>
    edit_message_media <ChosenInlineResult.edit_message_media>
    edit_message_reply_markup <ChosenInlineResult.edit_message_reply_markup>

InlineQuery
-----------

.. hlist::
    :columns: 2

    - :meth:`~InlineQuery.answer`

.. toctree::
    :hidden:

    answer <InlineQuery.answer>

PreCheckoutQuery
----------------

.. hlist::
    :columns: 2

    - :meth:`~PreCheckoutQuery.answer`

.. toctree::
    :hidden:

    answer <PreCheckoutQuery.answer>

ShippingQuery
-------------

.. hlist::
    :columns: 2

    - :meth:`~ShippingQuery.answer`

.. toctree::
    :hidden:

    answer <ShippingQuery.answer>

ChatJoinRequest
---------------

.. hlist::
    :columns: 2

    - :meth:`~ChatJoinRequest.approve`
    - :meth:`~ChatJoinRequest.decline`

.. toctree::
    :hidden:

    approve <ChatJoinRequest.approve>
    decline <ChatJoinRequest.decline>

Story
-----

.. hlist::
    :columns: 2

    - :meth:`~Story.react`
    - :meth:`~Story.download`
    - :meth:`~Story.forward`
    - :meth:`~Story.export_link`

.. toctree::
    :hidden:

    react <Story.react>
    download <Story.download>
    forward <Story.forward>
    export_link <Story.export_link>

ActiveSession
-------------

.. hlist::
    :columns: 2

    - :meth:`~ActiveSession.terminate`

.. toctree::
    :hidden:

    terminate <ActiveSession.terminate>

Poll
----

.. hlist::
    :columns: 2

    - :meth:`~Poll.stop`

.. toctree::
    :hidden:

    stop <Poll.stop>

ChatMemberUpdated
-----------------

.. hlist::
    :columns: 2

    - :meth:`~ChatMemberUpdated.get_chat`
    - :meth:`~ChatMemberUpdated.get_member`

.. toctree::
    :hidden:

    get_chat <ChatMemberUpdated.get_chat>
    get_member <ChatMemberUpdated.get_member>
