Available Methods
=================

All methods listed here are bound to a :class:`~pyrogram.Client` instance.

.. code-block:: python

    from pyrogram import Client

    app = Client("my_account")

    with app:
        app.send_message(chat_id="me", text="Hi!")

-----

Account
-------

.. hlist::
    :columns: 3

    * :meth:`add_profile_audio <pyrogram.Client.add_profile_audio>`
    * :meth:`get_account_ttl <pyrogram.Client.get_account_ttl>`
    * :meth:`get_global_privacy_settings <pyrogram.Client.get_global_privacy_settings>`
    * :meth:`get_privacy <pyrogram.Client.get_privacy>`
    * :meth:`remove_profile_audio <pyrogram.Client.remove_profile_audio>`
    * :meth:`set_account_ttl <pyrogram.Client.set_account_ttl>`
    * :meth:`set_global_privacy_settings <pyrogram.Client.set_global_privacy_settings>`
    * :meth:`set_inactive_session_ttl <pyrogram.Client.set_inactive_session_ttl>`
    * :meth:`set_privacy <pyrogram.Client.set_privacy>`
    * :meth:`set_profile_audio_position <pyrogram.Client.set_profile_audio_position>`

.. toctree::
    :hidden:

    add_profile_audio <add_profile_audio>
    get_account_ttl <get_account_ttl>
    get_global_privacy_settings <get_global_privacy_settings>
    get_privacy <get_privacy>
    remove_profile_audio <remove_profile_audio>
    set_account_ttl <set_account_ttl>
    set_global_privacy_settings <set_global_privacy_settings>
    set_inactive_session_ttl <set_inactive_session_ttl>
    set_privacy <set_privacy>
    set_profile_audio_position <set_profile_audio_position>

Advanced
--------

.. hlist::
    :columns: 3

    * :meth:`invoke <pyrogram.Client.invoke>`
    * :meth:`recover_gaps <pyrogram.Client.recover_gaps>`
    * :meth:`resolve_peer <pyrogram.Client.resolve_peer>`
    * :meth:`save_file <pyrogram.Client.save_file>`

.. toctree::
    :hidden:

    invoke <invoke>
    recover_gaps <recover_gaps>
    resolve_peer <resolve_peer>
    save_file <save_file>

Authorization
-------------

.. hlist::
    :columns: 3

    * :meth:`accept_terms_of_service <pyrogram.Client.accept_terms_of_service>`
    * :meth:`change_phone_number <pyrogram.Client.change_phone_number>`
    * :meth:`check_password <pyrogram.Client.check_password>`
    * :meth:`connect <pyrogram.Client.connect>`
    * :meth:`disconnect <pyrogram.Client.disconnect>`
    * :meth:`get_active_sessions <pyrogram.Client.get_active_sessions>`
    * :meth:`get_password_hint <pyrogram.Client.get_password_hint>`
    * :meth:`initialize <pyrogram.Client.initialize>`
    * :meth:`log_out <pyrogram.Client.log_out>`
    * :meth:`recover_password <pyrogram.Client.recover_password>`
    * :meth:`resend_code <pyrogram.Client.resend_code>`
    * :meth:`resend_phone_number_code <pyrogram.Client.resend_phone_number_code>`
    * :meth:`reset_session <pyrogram.Client.reset_session>`
    * :meth:`reset_sessions <pyrogram.Client.reset_sessions>`
    * :meth:`send_code <pyrogram.Client.send_code>`
    * :meth:`send_phone_number_code <pyrogram.Client.send_phone_number_code>`
    * :meth:`send_recovery_code <pyrogram.Client.send_recovery_code>`
    * :meth:`sign_in <pyrogram.Client.sign_in>`
    * :meth:`sign_in_bot <pyrogram.Client.sign_in_bot>`
    * :meth:`sign_in_qrcode <pyrogram.Client.sign_in_qrcode>`
    * :meth:`sign_up <pyrogram.Client.sign_up>`
    * :meth:`terminate <pyrogram.Client.terminate>`

.. toctree::
    :hidden:

    accept_terms_of_service <accept_terms_of_service>
    change_phone_number <change_phone_number>
    check_password <check_password>
    connect <connect>
    disconnect <disconnect>
    get_active_sessions <get_active_sessions>
    get_password_hint <get_password_hint>
    initialize <initialize>
    log_out <log_out>
    recover_password <recover_password>
    resend_code <resend_code>
    resend_phone_number_code <resend_phone_number_code>
    reset_session <reset_session>
    reset_sessions <reset_sessions>
    send_code <send_code>
    send_phone_number_code <send_phone_number_code>
    send_recovery_code <send_recovery_code>
    sign_in <sign_in>
    sign_in_bot <sign_in_bot>
    sign_in_qrcode <sign_in_qrcode>
    sign_up <sign_up>
    terminate <terminate>

Bots
----

.. hlist::
    :columns: 3

    * :meth:`answer_callback_query <pyrogram.Client.answer_callback_query>`
    * :meth:`answer_inline_query <pyrogram.Client.answer_inline_query>`
    * :meth:`answer_web_app_query <pyrogram.Client.answer_web_app_query>`
    * :meth:`check_bot_username <pyrogram.Client.check_bot_username>`
    * :meth:`create_bot <pyrogram.Client.create_bot>`
    * :meth:`create_managed_bot <pyrogram.Client.create_managed_bot>`
    * :meth:`delete_bot_commands <pyrogram.Client.delete_bot_commands>`
    * :meth:`get_bot_commands <pyrogram.Client.get_bot_commands>`
    * :meth:`get_bot_default_privileges <pyrogram.Client.get_bot_default_privileges>`
    * :meth:`get_bot_info <pyrogram.Client.get_bot_info>`
    * :meth:`get_bot_info_description <pyrogram.Client.get_bot_info_description>`
    * :meth:`get_bot_info_short_description <pyrogram.Client.get_bot_info_short_description>`
    * :meth:`get_bot_name <pyrogram.Client.get_bot_name>`
    * :meth:`get_chat_menu_button <pyrogram.Client.get_chat_menu_button>`
    * :meth:`get_collectible_item_info <pyrogram.Client.get_collectible_item_info>`
    * :meth:`get_game_high_scores <pyrogram.Client.get_game_high_scores>`
    * :meth:`get_inline_bot_results <pyrogram.Client.get_inline_bot_results>`
    * :meth:`get_managed_bot_token <pyrogram.Client.get_managed_bot_token>`
    * :meth:`get_owned_bots <pyrogram.Client.get_owned_bots>`
    * :meth:`get_similar_bots <pyrogram.Client.get_similar_bots>`
    * :meth:`list_managed_bots <pyrogram.Client.list_managed_bots>`
    * :meth:`refund_star_payment <pyrogram.Client.refund_star_payment>`
    * :meth:`remove_chat_verification <pyrogram.Client.remove_chat_verification>`
    * :meth:`remove_user_verification <pyrogram.Client.remove_user_verification>`
    * :meth:`replace_managed_bot_token <pyrogram.Client.replace_managed_bot_token>`
    * :meth:`request_callback_answer <pyrogram.Client.request_callback_answer>`
    * :meth:`save_prepared_inline_message <pyrogram.Client.save_prepared_inline_message>`
    * :meth:`send_game <pyrogram.Client.send_game>`
    * :meth:`send_inline_bot_result <pyrogram.Client.send_inline_bot_result>`
    * :meth:`set_bot_commands <pyrogram.Client.set_bot_commands>`
    * :meth:`set_bot_default_privileges <pyrogram.Client.set_bot_default_privileges>`
    * :meth:`set_bot_info <pyrogram.Client.set_bot_info>`
    * :meth:`set_bot_info_description <pyrogram.Client.set_bot_info_description>`
    * :meth:`set_bot_info_short_description <pyrogram.Client.set_bot_info_short_description>`
    * :meth:`set_bot_name <pyrogram.Client.set_bot_name>`
    * :meth:`set_chat_menu_button <pyrogram.Client.set_chat_menu_button>`
    * :meth:`set_game_score <pyrogram.Client.set_game_score>`
    * :meth:`set_user_emoji_status <pyrogram.Client.set_user_emoji_status>`
    * :meth:`verify_chat <pyrogram.Client.verify_chat>`
    * :meth:`verify_user <pyrogram.Client.verify_user>`

.. toctree::
    :hidden:

    answer_callback_query <answer_callback_query>
    answer_inline_query <answer_inline_query>
    answer_web_app_query <answer_web_app_query>
    check_bot_username <check_bot_username>
    create_bot <create_bot>
    create_managed_bot <create_managed_bot>
    delete_bot_commands <delete_bot_commands>
    get_bot_commands <get_bot_commands>
    get_bot_default_privileges <get_bot_default_privileges>
    get_bot_info <get_bot_info>
    get_bot_info_description <get_bot_info_description>
    get_bot_info_short_description <get_bot_info_short_description>
    get_bot_name <get_bot_name>
    get_chat_menu_button <get_chat_menu_button>
    get_collectible_item_info <get_collectible_item_info>
    get_game_high_scores <get_game_high_scores>
    get_inline_bot_results <get_inline_bot_results>
    get_managed_bot_token <get_managed_bot_token>
    get_owned_bots <get_owned_bots>
    get_similar_bots <get_similar_bots>
    list_managed_bots <list_managed_bots>
    refund_star_payment <refund_star_payment>
    remove_chat_verification <remove_chat_verification>
    remove_user_verification <remove_user_verification>
    replace_managed_bot_token <replace_managed_bot_token>
    request_callback_answer <request_callback_answer>
    save_prepared_inline_message <save_prepared_inline_message>
    send_game <send_game>
    send_inline_bot_result <send_inline_bot_result>
    set_bot_commands <set_bot_commands>
    set_bot_default_privileges <set_bot_default_privileges>
    set_bot_info <set_bot_info>
    set_bot_info_description <set_bot_info_description>
    set_bot_info_short_description <set_bot_info_short_description>
    set_bot_name <set_bot_name>
    set_chat_menu_button <set_chat_menu_button>
    set_game_score <set_game_score>
    set_user_emoji_status <set_user_emoji_status>
    verify_chat <verify_chat>
    verify_user <verify_user>

Business
--------

.. hlist::
    :columns: 3

    * :meth:`answer_pre_checkout_query <pyrogram.Client.answer_pre_checkout_query>`
    * :meth:`answer_shipping_query <pyrogram.Client.answer_shipping_query>`
    * :meth:`delete_business_messages <pyrogram.Client.delete_business_messages>`
    * :meth:`get_business_account_gifts <pyrogram.Client.get_business_account_gifts>`
    * :meth:`get_business_account_star_balance <pyrogram.Client.get_business_account_star_balance>`
    * :meth:`get_business_connection <pyrogram.Client.get_business_connection>`
    * :meth:`read_business_message <pyrogram.Client.read_business_message>`
    * :meth:`remove_business_account_profile_photo <pyrogram.Client.remove_business_account_profile_photo>`
    * :meth:`set_business_account_bio <pyrogram.Client.set_business_account_bio>`
    * :meth:`set_business_account_gift_settings <pyrogram.Client.set_business_account_gift_settings>`
    * :meth:`set_business_account_name <pyrogram.Client.set_business_account_name>`
    * :meth:`set_business_account_profile_photo <pyrogram.Client.set_business_account_profile_photo>`
    * :meth:`set_business_account_username <pyrogram.Client.set_business_account_username>`
    * :meth:`transfer_business_account_stars <pyrogram.Client.transfer_business_account_stars>`

.. toctree::
    :hidden:

    answer_pre_checkout_query <answer_pre_checkout_query>
    answer_shipping_query <answer_shipping_query>
    delete_business_messages <delete_business_messages>
    get_business_account_gifts <get_business_account_gifts>
    get_business_account_star_balance <get_business_account_star_balance>
    get_business_connection <get_business_connection>
    read_business_message <read_business_message>
    remove_business_account_profile_photo <remove_business_account_profile_photo>
    set_business_account_bio <set_business_account_bio>
    set_business_account_gift_settings <set_business_account_gift_settings>
    set_business_account_name <set_business_account_name>
    set_business_account_profile_photo <set_business_account_profile_photo>
    set_business_account_username <set_business_account_username>
    transfer_business_account_stars <transfer_business_account_stars>

Chats
-----

.. hlist::
    :columns: 3

    * :meth:`add_chat_members <pyrogram.Client.add_chat_members>`
    * :meth:`archive_chats <pyrogram.Client.archive_chats>`
    * :meth:`ban_chat_member <pyrogram.Client.ban_chat_member>`
    * :meth:`ban_chat_sender_chat <pyrogram.Client.ban_chat_sender_chat>`
    * :meth:`close_forum_topic <pyrogram.Client.close_forum_topic>`
    * :meth:`close_general_topic <pyrogram.Client.close_general_topic>`
    * :meth:`create_channel <pyrogram.Client.create_channel>`
    * :meth:`create_folder <pyrogram.Client.create_folder>`
    * :meth:`create_folder_invite_link <pyrogram.Client.create_folder_invite_link>`
    * :meth:`create_forum_topic <pyrogram.Client.create_forum_topic>`
    * :meth:`create_group <pyrogram.Client.create_group>`
    * :meth:`create_supergroup <pyrogram.Client.create_supergroup>`
    * :meth:`delete_channel <pyrogram.Client.delete_channel>`
    * :meth:`delete_chat_photo <pyrogram.Client.delete_chat_photo>`
    * :meth:`delete_folder <pyrogram.Client.delete_folder>`
    * :meth:`delete_folder_invite_link <pyrogram.Client.delete_folder_invite_link>`
    * :meth:`delete_forum_topic <pyrogram.Client.delete_forum_topic>`
    * :meth:`delete_supergroup <pyrogram.Client.delete_supergroup>`
    * :meth:`delete_user_history <pyrogram.Client.delete_user_history>`
    * :meth:`edit_folder <pyrogram.Client.edit_folder>`
    * :meth:`edit_folder_invite_link <pyrogram.Client.edit_folder_invite_link>`
    * :meth:`edit_forum_topic <pyrogram.Client.edit_forum_topic>`
    * :meth:`edit_general_topic <pyrogram.Client.edit_general_topic>`
    * :meth:`export_folder_link <pyrogram.Client.export_folder_link>`
    * :meth:`get_chat <pyrogram.Client.get_chat>`
    * :meth:`get_chat_event_log <pyrogram.Client.get_chat_event_log>`
    * :meth:`get_chat_member <pyrogram.Client.get_chat_member>`
    * :meth:`get_chat_members <pyrogram.Client.get_chat_members>`
    * :meth:`get_chat_members_count <pyrogram.Client.get_chat_members_count>`
    * :meth:`get_chat_online_count <pyrogram.Client.get_chat_online_count>`
    * :meth:`get_chat_settings <pyrogram.Client.get_chat_settings>`
    * :meth:`get_chats_for_folder_invite_link <pyrogram.Client.get_chats_for_folder_invite_link>`
    * :meth:`get_dialogs <pyrogram.Client.get_dialogs>`
    * :meth:`get_dialogs_count <pyrogram.Client.get_dialogs_count>`
    * :meth:`get_direct_messages_topics <pyrogram.Client.get_direct_messages_topics>`
    * :meth:`get_direct_messages_topics_by_id <pyrogram.Client.get_direct_messages_topics_by_id>`
    * :meth:`get_folder_invite_links <pyrogram.Client.get_folder_invite_links>`
    * :meth:`get_folders <pyrogram.Client.get_folders>`
    * :meth:`get_forum_topics <pyrogram.Client.get_forum_topics>`
    * :meth:`get_forum_topics_by_id <pyrogram.Client.get_forum_topics_by_id>`
    * :meth:`get_forum_topics_count <pyrogram.Client.get_forum_topics_count>`
    * :meth:`get_personal_channels <pyrogram.Client.get_personal_channels>`
    * :meth:`get_send_as_chats <pyrogram.Client.get_send_as_chats>`
    * :meth:`get_similar_channels <pyrogram.Client.get_similar_channels>`
    * :meth:`get_suitable_discussion_chats <pyrogram.Client.get_suitable_discussion_chats>`
    * :meth:`hide_general_topic <pyrogram.Client.hide_general_topic>`
    * :meth:`join_chat <pyrogram.Client.join_chat>`
    * :meth:`join_folder <pyrogram.Client.join_folder>`
    * :meth:`leave_chat <pyrogram.Client.leave_chat>`
    * :meth:`leave_folder <pyrogram.Client.leave_folder>`
    * :meth:`mark_chat_unread <pyrogram.Client.mark_chat_unread>`
    * :meth:`pin_chat_message <pyrogram.Client.pin_chat_message>`
    * :meth:`pin_forum_topic <pyrogram.Client.pin_forum_topic>`
    * :meth:`process_chat_has_protected_content_disable_request <pyrogram.Client.process_chat_has_protected_content_disable_request>`
    * :meth:`promote_chat_member <pyrogram.Client.promote_chat_member>`
    * :meth:`reopen_forum_topic <pyrogram.Client.reopen_forum_topic>`
    * :meth:`reopen_general_topic <pyrogram.Client.reopen_general_topic>`
    * :meth:`reorder_folders <pyrogram.Client.reorder_folders>`
    * :meth:`restrict_chat_member <pyrogram.Client.restrict_chat_member>`
    * :meth:`set_administrator_title <pyrogram.Client.set_administrator_title>`
    * :meth:`set_chat_description <pyrogram.Client.set_chat_description>`
    * :meth:`set_chat_direct_messages_group <pyrogram.Client.set_chat_direct_messages_group>`
    * :meth:`set_chat_discussion_group <pyrogram.Client.set_chat_discussion_group>`
    * :meth:`set_chat_member_tag <pyrogram.Client.set_chat_member_tag>`
    * :meth:`set_chat_permissions <pyrogram.Client.set_chat_permissions>`
    * :meth:`set_chat_photo <pyrogram.Client.set_chat_photo>`
    * :meth:`set_chat_protected_content <pyrogram.Client.set_chat_protected_content>`
    * :meth:`set_chat_title <pyrogram.Client.set_chat_title>`
    * :meth:`set_chat_ttl <pyrogram.Client.set_chat_ttl>`
    * :meth:`set_chat_username <pyrogram.Client.set_chat_username>`
    * :meth:`set_main_profile_tab <pyrogram.Client.set_main_profile_tab>`
    * :meth:`set_send_as_chat <pyrogram.Client.set_send_as_chat>`
    * :meth:`set_slow_mode <pyrogram.Client.set_slow_mode>`
    * :meth:`set_upgraded_gift_colors <pyrogram.Client.set_upgraded_gift_colors>`
    * :meth:`toggle_folder_tags <pyrogram.Client.toggle_folder_tags>`
    * :meth:`toggle_forum_topics <pyrogram.Client.toggle_forum_topics>`
    * :meth:`toggle_join_to_send <pyrogram.Client.toggle_join_to_send>`
    * :meth:`transfer_chat_ownership <pyrogram.Client.transfer_chat_ownership>`
    * :meth:`unarchive_chats <pyrogram.Client.unarchive_chats>`
    * :meth:`unban_chat_member <pyrogram.Client.unban_chat_member>`
    * :meth:`unban_chat_sender_chat <pyrogram.Client.unban_chat_sender_chat>`
    * :meth:`unhide_general_topic <pyrogram.Client.unhide_general_topic>`
    * :meth:`unpin_all_chat_messages <pyrogram.Client.unpin_all_chat_messages>`
    * :meth:`unpin_chat_message <pyrogram.Client.unpin_chat_message>`
    * :meth:`unpin_forum_topic <pyrogram.Client.unpin_forum_topic>`
    * :meth:`update_chat_notifications <pyrogram.Client.update_chat_notifications>`
    * :meth:`update_color <pyrogram.Client.update_color>`
    * :meth:`update_folder <pyrogram.Client.update_folder>`

.. toctree::
    :hidden:

    add_chat_members <add_chat_members>
    archive_chats <archive_chats>
    ban_chat_member <ban_chat_member>
    ban_chat_sender_chat <ban_chat_sender_chat>
    close_forum_topic <close_forum_topic>
    close_general_topic <close_general_topic>
    create_channel <create_channel>
    create_folder <create_folder>
    create_folder_invite_link <create_folder_invite_link>
    create_forum_topic <create_forum_topic>
    create_group <create_group>
    create_supergroup <create_supergroup>
    delete_channel <delete_channel>
    delete_chat_photo <delete_chat_photo>
    delete_folder <delete_folder>
    delete_folder_invite_link <delete_folder_invite_link>
    delete_forum_topic <delete_forum_topic>
    delete_supergroup <delete_supergroup>
    delete_user_history <delete_user_history>
    edit_folder <edit_folder>
    edit_folder_invite_link <edit_folder_invite_link>
    edit_forum_topic <edit_forum_topic>
    edit_general_topic <edit_general_topic>
    export_folder_link <export_folder_link>
    get_chat <get_chat>
    get_chat_event_log <get_chat_event_log>
    get_chat_member <get_chat_member>
    get_chat_members <get_chat_members>
    get_chat_members_count <get_chat_members_count>
    get_chat_online_count <get_chat_online_count>
    get_chat_settings <get_chat_settings>
    get_chats_for_folder_invite_link <get_chats_for_folder_invite_link>
    get_dialogs <get_dialogs>
    get_dialogs_count <get_dialogs_count>
    get_direct_messages_topics <get_direct_messages_topics>
    get_direct_messages_topics_by_id <get_direct_messages_topics_by_id>
    get_folder_invite_links <get_folder_invite_links>
    get_folders <get_folders>
    get_forum_topics <get_forum_topics>
    get_forum_topics_by_id <get_forum_topics_by_id>
    get_forum_topics_count <get_forum_topics_count>
    get_personal_channels <get_personal_channels>
    get_send_as_chats <get_send_as_chats>
    get_similar_channels <get_similar_channels>
    get_suitable_discussion_chats <get_suitable_discussion_chats>
    hide_general_topic <hide_general_topic>
    join_chat <join_chat>
    join_folder <join_folder>
    leave_chat <leave_chat>
    leave_folder <leave_folder>
    mark_chat_unread <mark_chat_unread>
    pin_chat_message <pin_chat_message>
    pin_forum_topic <pin_forum_topic>
    process_chat_has_protected_content_disable_request <process_chat_has_protected_content_disable_request>
    promote_chat_member <promote_chat_member>
    reopen_forum_topic <reopen_forum_topic>
    reopen_general_topic <reopen_general_topic>
    reorder_folders <reorder_folders>
    restrict_chat_member <restrict_chat_member>
    set_administrator_title <set_administrator_title>
    set_chat_description <set_chat_description>
    set_chat_direct_messages_group <set_chat_direct_messages_group>
    set_chat_discussion_group <set_chat_discussion_group>
    set_chat_member_tag <set_chat_member_tag>
    set_chat_permissions <set_chat_permissions>
    set_chat_photo <set_chat_photo>
    set_chat_protected_content <set_chat_protected_content>
    set_chat_title <set_chat_title>
    set_chat_ttl <set_chat_ttl>
    set_chat_username <set_chat_username>
    set_main_profile_tab <set_main_profile_tab>
    set_send_as_chat <set_send_as_chat>
    set_slow_mode <set_slow_mode>
    set_upgraded_gift_colors <set_upgraded_gift_colors>
    toggle_folder_tags <toggle_folder_tags>
    toggle_forum_topics <toggle_forum_topics>
    toggle_join_to_send <toggle_join_to_send>
    transfer_chat_ownership <transfer_chat_ownership>
    unarchive_chats <unarchive_chats>
    unban_chat_member <unban_chat_member>
    unban_chat_sender_chat <unban_chat_sender_chat>
    unhide_general_topic <unhide_general_topic>
    unpin_all_chat_messages <unpin_all_chat_messages>
    unpin_chat_message <unpin_chat_message>
    unpin_forum_topic <unpin_forum_topic>
    update_chat_notifications <update_chat_notifications>
    update_color <update_color>
    update_folder <update_folder>

Contacts
--------

.. hlist::
    :columns: 3

    * :meth:`add_contact <pyrogram.Client.add_contact>`
    * :meth:`delete_contacts <pyrogram.Client.delete_contacts>`
    * :meth:`get_blocked_message_senders <pyrogram.Client.get_blocked_message_senders>`
    * :meth:`get_contacts <pyrogram.Client.get_contacts>`
    * :meth:`get_contacts_count <pyrogram.Client.get_contacts_count>`
    * :meth:`import_contacts <pyrogram.Client.import_contacts>`
    * :meth:`search_contacts <pyrogram.Client.search_contacts>`
    * :meth:`set_contact_note <pyrogram.Client.set_contact_note>`

.. toctree::
    :hidden:

    add_contact <add_contact>
    delete_contacts <delete_contacts>
    get_blocked_message_senders <get_blocked_message_senders>
    get_contacts <get_contacts>
    get_contacts_count <get_contacts_count>
    import_contacts <import_contacts>
    search_contacts <search_contacts>
    set_contact_note <set_contact_note>

Invite Links
------------

.. hlist::
    :columns: 3

    * :meth:`approve_all_chat_join_requests <pyrogram.Client.approve_all_chat_join_requests>`
    * :meth:`approve_chat_join_request <pyrogram.Client.approve_chat_join_request>`
    * :meth:`create_chat_invite_link <pyrogram.Client.create_chat_invite_link>`
    * :meth:`decline_all_chat_join_requests <pyrogram.Client.decline_all_chat_join_requests>`
    * :meth:`decline_chat_join_request <pyrogram.Client.decline_chat_join_request>`
    * :meth:`delete_chat_admin_invite_links <pyrogram.Client.delete_chat_admin_invite_links>`
    * :meth:`delete_chat_invite_link <pyrogram.Client.delete_chat_invite_link>`
    * :meth:`edit_chat_invite_link <pyrogram.Client.edit_chat_invite_link>`
    * :meth:`export_chat_invite_link <pyrogram.Client.export_chat_invite_link>`
    * :meth:`get_chat_admin_invite_links <pyrogram.Client.get_chat_admin_invite_links>`
    * :meth:`get_chat_admin_invite_links_count <pyrogram.Client.get_chat_admin_invite_links_count>`
    * :meth:`get_chat_admins_with_invite_links <pyrogram.Client.get_chat_admins_with_invite_links>`
    * :meth:`get_chat_invite_link <pyrogram.Client.get_chat_invite_link>`
    * :meth:`get_chat_invite_link_joiners <pyrogram.Client.get_chat_invite_link_joiners>`
    * :meth:`get_chat_invite_link_joiners_count <pyrogram.Client.get_chat_invite_link_joiners_count>`
    * :meth:`get_chat_join_requests <pyrogram.Client.get_chat_join_requests>`
    * :meth:`revoke_chat_invite_link <pyrogram.Client.revoke_chat_invite_link>`

.. toctree::
    :hidden:

    approve_all_chat_join_requests <approve_all_chat_join_requests>
    approve_chat_join_request <approve_chat_join_request>
    create_chat_invite_link <create_chat_invite_link>
    decline_all_chat_join_requests <decline_all_chat_join_requests>
    decline_chat_join_request <decline_chat_join_request>
    delete_chat_admin_invite_links <delete_chat_admin_invite_links>
    delete_chat_invite_link <delete_chat_invite_link>
    edit_chat_invite_link <edit_chat_invite_link>
    export_chat_invite_link <export_chat_invite_link>
    get_chat_admin_invite_links <get_chat_admin_invite_links>
    get_chat_admin_invite_links_count <get_chat_admin_invite_links_count>
    get_chat_admins_with_invite_links <get_chat_admins_with_invite_links>
    get_chat_invite_link <get_chat_invite_link>
    get_chat_invite_link_joiners <get_chat_invite_link_joiners>
    get_chat_invite_link_joiners_count <get_chat_invite_link_joiners_count>
    get_chat_join_requests <get_chat_join_requests>
    revoke_chat_invite_link <revoke_chat_invite_link>

Messages
--------

.. hlist::
    :columns: 3

    * :meth:`add_checklist_tasks <pyrogram.Client.add_checklist_tasks>`
    * :meth:`add_poll_answer <pyrogram.Client.add_poll_answer>`
    * :meth:`add_poll_option <pyrogram.Client.add_poll_option>`
    * :meth:`add_task_to_todo <pyrogram.Client.add_task_to_todo>`
    * :meth:`add_to_gifs <pyrogram.Client.add_to_gifs>`
    * :meth:`append_todo_list <pyrogram.Client.append_todo_list>`
    * :meth:`approve_suggested_post <pyrogram.Client.approve_suggested_post>`
    * :meth:`compose_text_with_ai <pyrogram.Client.compose_text_with_ai>`
    * :meth:`copy_media_group <pyrogram.Client.copy_media_group>`
    * :meth:`copy_message <pyrogram.Client.copy_message>`
    * :meth:`decline_suggested_post <pyrogram.Client.decline_suggested_post>`
    * :meth:`delete_chat_history <pyrogram.Client.delete_chat_history>`
    * :meth:`delete_direct_messages_chat_topic_history <pyrogram.Client.delete_direct_messages_chat_topic_history>`
    * :meth:`delete_messages <pyrogram.Client.delete_messages>`
    * :meth:`delete_poll_answer <pyrogram.Client.delete_poll_answer>`
    * :meth:`delete_poll_option <pyrogram.Client.delete_poll_option>`
    * :meth:`delete_scheduled_messages <pyrogram.Client.delete_scheduled_messages>`
    * :meth:`download_media <pyrogram.Client.download_media>`
    * :meth:`edit_inline_caption <pyrogram.Client.edit_inline_caption>`
    * :meth:`edit_inline_media <pyrogram.Client.edit_inline_media>`
    * :meth:`edit_inline_reply_markup <pyrogram.Client.edit_inline_reply_markup>`
    * :meth:`edit_inline_text <pyrogram.Client.edit_inline_text>`
    * :meth:`edit_message_caption <pyrogram.Client.edit_message_caption>`
    * :meth:`edit_message_checklist <pyrogram.Client.edit_message_checklist>`
    * :meth:`edit_message_media <pyrogram.Client.edit_message_media>`
    * :meth:`edit_message_reply_markup <pyrogram.Client.edit_message_reply_markup>`
    * :meth:`edit_message_text <pyrogram.Client.edit_message_text>`
    * :meth:`fix_text_with_ai <pyrogram.Client.fix_text_with_ai>`
    * :meth:`forward_media_group <pyrogram.Client.forward_media_group>`
    * :meth:`forward_messages <pyrogram.Client.forward_messages>`
    * :meth:`get_available_effects <pyrogram.Client.get_available_effects>`
    * :meth:`get_chat_history <pyrogram.Client.get_chat_history>`
    * :meth:`get_chat_history_count <pyrogram.Client.get_chat_history_count>`
    * :meth:`get_custom_emoji_stickers <pyrogram.Client.get_custom_emoji_stickers>`
    * :meth:`get_direct_messages_chat_topic_history <pyrogram.Client.get_direct_messages_chat_topic_history>`
    * :meth:`get_discussion_message <pyrogram.Client.get_discussion_message>`
    * :meth:`get_discussion_replies <pyrogram.Client.get_discussion_replies>`
    * :meth:`get_discussion_replies_count <pyrogram.Client.get_discussion_replies_count>`
    * :meth:`get_main_web_app <pyrogram.Client.get_main_web_app>`
    * :meth:`get_media_group <pyrogram.Client.get_media_group>`
    * :meth:`get_message_read_participants <pyrogram.Client.get_message_read_participants>`
    * :meth:`get_messages <pyrogram.Client.get_messages>`
    * :meth:`get_scheduled_messages <pyrogram.Client.get_scheduled_messages>`
    * :meth:`get_stickers <pyrogram.Client.get_stickers>`
    * :meth:`get_web_app_link_url <pyrogram.Client.get_web_app_link_url>`
    * :meth:`get_web_app_url <pyrogram.Client.get_web_app_url>`
    * :meth:`mark_checklist_tasks_as_done <pyrogram.Client.mark_checklist_tasks_as_done>`
    * :meth:`open_web_app <pyrogram.Client.open_web_app>`
    * :meth:`read_chat_history <pyrogram.Client.read_chat_history>`
    * :meth:`read_mentions <pyrogram.Client.read_mentions>`
    * :meth:`read_reactions <pyrogram.Client.read_reactions>`
    * :meth:`retract_vote <pyrogram.Client.retract_vote>`
    * :meth:`search_channel_posts <pyrogram.Client.search_channel_posts>`
    * :meth:`search_global <pyrogram.Client.search_global>`
    * :meth:`search_global_count <pyrogram.Client.search_global_count>`
    * :meth:`search_global_hashtag_messages <pyrogram.Client.search_global_hashtag_messages>`
    * :meth:`search_global_hashtag_messages_count <pyrogram.Client.search_global_hashtag_messages_count>`
    * :meth:`search_messages <pyrogram.Client.search_messages>`
    * :meth:`search_messages_count <pyrogram.Client.search_messages_count>`
    * :meth:`search_posts <pyrogram.Client.search_posts>`
    * :meth:`search_posts_count <pyrogram.Client.search_posts_count>`
    * :meth:`send_animation <pyrogram.Client.send_animation>`
    * :meth:`send_audio <pyrogram.Client.send_audio>`
    * :meth:`send_cached_media <pyrogram.Client.send_cached_media>`
    * :meth:`send_chat_action <pyrogram.Client.send_chat_action>`
    * :meth:`send_checklist <pyrogram.Client.send_checklist>`
    * :meth:`send_contact <pyrogram.Client.send_contact>`
    * :meth:`send_dice <pyrogram.Client.send_dice>`
    * :meth:`send_document <pyrogram.Client.send_document>`
    * :meth:`send_location <pyrogram.Client.send_location>`
    * :meth:`send_media_group <pyrogram.Client.send_media_group>`
    * :meth:`send_message <pyrogram.Client.send_message>`
    * :meth:`send_message_draft <pyrogram.Client.send_message_draft>`
    * :meth:`send_photo <pyrogram.Client.send_photo>`
    * :meth:`send_poll <pyrogram.Client.send_poll>`
    * :meth:`send_reaction <pyrogram.Client.send_reaction>`
    * :meth:`send_screenshot_notification <pyrogram.Client.send_screenshot_notification>`
    * :meth:`send_sticker <pyrogram.Client.send_sticker>`
    * :meth:`send_todo <pyrogram.Client.send_todo>`
    * :meth:`send_venue <pyrogram.Client.send_venue>`
    * :meth:`send_video <pyrogram.Client.send_video>`
    * :meth:`send_video_note <pyrogram.Client.send_video_note>`
    * :meth:`send_voice <pyrogram.Client.send_voice>`
    * :meth:`send_web_page <pyrogram.Client.send_web_page>`
    * :meth:`set_direct_messages_chat_topic_is_marked_as_unread <pyrogram.Client.set_direct_messages_chat_topic_is_marked_as_unread>`
    * :meth:`set_todo_tasks_completion <pyrogram.Client.set_todo_tasks_completion>`
    * :meth:`start_bot <pyrogram.Client.start_bot>`
    * :meth:`stop_poll <pyrogram.Client.stop_poll>`
    * :meth:`stream_media <pyrogram.Client.stream_media>`
    * :meth:`summarize_message <pyrogram.Client.summarize_message>`
    * :meth:`transcribe_audio <pyrogram.Client.transcribe_audio>`
    * :meth:`translate_message_text <pyrogram.Client.translate_message_text>`
    * :meth:`translate_text <pyrogram.Client.translate_text>`
    * :meth:`view_messages <pyrogram.Client.view_messages>`
    * :meth:`vote_poll <pyrogram.Client.vote_poll>`

.. toctree::
    :hidden:

    add_checklist_tasks <add_checklist_tasks>
    add_poll_answer <add_poll_answer>
    add_poll_option <add_poll_option>
    add_task_to_todo <add_task_to_todo>
    add_to_gifs <add_to_gifs>
    append_todo_list <append_todo_list>
    approve_suggested_post <approve_suggested_post>
    compose_text_with_ai <compose_text_with_ai>
    copy_media_group <copy_media_group>
    copy_message <copy_message>
    decline_suggested_post <decline_suggested_post>
    delete_chat_history <delete_chat_history>
    delete_direct_messages_chat_topic_history <delete_direct_messages_chat_topic_history>
    delete_messages <delete_messages>
    delete_poll_answer <delete_poll_answer>
    delete_poll_option <delete_poll_option>
    delete_scheduled_messages <delete_scheduled_messages>
    download_media <download_media>
    edit_inline_caption <edit_inline_caption>
    edit_inline_media <edit_inline_media>
    edit_inline_reply_markup <edit_inline_reply_markup>
    edit_inline_text <edit_inline_text>
    edit_message_caption <edit_message_caption>
    edit_message_checklist <edit_message_checklist>
    edit_message_media <edit_message_media>
    edit_message_reply_markup <edit_message_reply_markup>
    edit_message_text <edit_message_text>
    fix_text_with_ai <fix_text_with_ai>
    forward_media_group <forward_media_group>
    forward_messages <forward_messages>
    get_available_effects <get_available_effects>
    get_chat_history <get_chat_history>
    get_chat_history_count <get_chat_history_count>
    get_custom_emoji_stickers <get_custom_emoji_stickers>
    get_direct_messages_chat_topic_history <get_direct_messages_chat_topic_history>
    get_discussion_message <get_discussion_message>
    get_discussion_replies <get_discussion_replies>
    get_discussion_replies_count <get_discussion_replies_count>
    get_main_web_app <get_main_web_app>
    get_media_group <get_media_group>
    get_message_read_participants <get_message_read_participants>
    get_messages <get_messages>
    get_scheduled_messages <get_scheduled_messages>
    get_stickers <get_stickers>
    get_web_app_link_url <get_web_app_link_url>
    get_web_app_url <get_web_app_url>
    mark_checklist_tasks_as_done <mark_checklist_tasks_as_done>
    open_web_app <open_web_app>
    read_chat_history <read_chat_history>
    read_mentions <read_mentions>
    read_reactions <read_reactions>
    retract_vote <retract_vote>
    search_channel_posts <search_channel_posts>
    search_global <search_global>
    search_global_count <search_global_count>
    search_global_hashtag_messages <search_global_hashtag_messages>
    search_global_hashtag_messages_count <search_global_hashtag_messages_count>
    search_messages <search_messages>
    search_messages_count <search_messages_count>
    search_posts <search_posts>
    search_posts_count <search_posts_count>
    send_animation <send_animation>
    send_audio <send_audio>
    send_cached_media <send_cached_media>
    send_chat_action <send_chat_action>
    send_checklist <send_checklist>
    send_contact <send_contact>
    send_dice <send_dice>
    send_document <send_document>
    send_location <send_location>
    send_media_group <send_media_group>
    send_message <send_message>
    send_message_draft <send_message_draft>
    send_photo <send_photo>
    send_poll <send_poll>
    send_reaction <send_reaction>
    send_screenshot_notification <send_screenshot_notification>
    send_sticker <send_sticker>
    send_todo <send_todo>
    send_venue <send_venue>
    send_video <send_video>
    send_video_note <send_video_note>
    send_voice <send_voice>
    send_web_page <send_web_page>
    set_direct_messages_chat_topic_is_marked_as_unread <set_direct_messages_chat_topic_is_marked_as_unread>
    set_todo_tasks_completion <set_todo_tasks_completion>
    start_bot <start_bot>
    stop_poll <stop_poll>
    stream_media <stream_media>
    summarize_message <summarize_message>
    transcribe_audio <transcribe_audio>
    translate_message_text <translate_message_text>
    translate_text <translate_text>
    view_messages <view_messages>
    vote_poll <vote_poll>

Password
--------

.. hlist::
    :columns: 3

    * :meth:`change_cloud_password <pyrogram.Client.change_cloud_password>`
    * :meth:`enable_cloud_password <pyrogram.Client.enable_cloud_password>`
    * :meth:`remove_cloud_password <pyrogram.Client.remove_cloud_password>`

.. toctree::
    :hidden:

    change_cloud_password <change_cloud_password>
    enable_cloud_password <enable_cloud_password>
    remove_cloud_password <remove_cloud_password>

Payments
--------

.. hlist::
    :columns: 3

    * :meth:`add_collection_gifts <pyrogram.Client.add_collection_gifts>`
    * :meth:`apply_gift_code <pyrogram.Client.apply_gift_code>`
    * :meth:`buy_gift_upgrade <pyrogram.Client.buy_gift_upgrade>`
    * :meth:`check_gift_code <pyrogram.Client.check_gift_code>`
    * :meth:`convert_gift <pyrogram.Client.convert_gift>`
    * :meth:`convert_gift_to_stars <pyrogram.Client.convert_gift_to_stars>`
    * :meth:`craft_gift <pyrogram.Client.craft_gift>`
    * :meth:`create_gift_collection <pyrogram.Client.create_gift_collection>`
    * :meth:`create_invoice_link <pyrogram.Client.create_invoice_link>`
    * :meth:`create_star_gift_collection <pyrogram.Client.create_star_gift_collection>`
    * :meth:`delete_gift_collection <pyrogram.Client.delete_gift_collection>`
    * :meth:`delete_passkey <pyrogram.Client.delete_passkey>`
    * :meth:`delete_star_gift_collection <pyrogram.Client.delete_star_gift_collection>`
    * :meth:`drop_gift_original_details <pyrogram.Client.drop_gift_original_details>`
    * :meth:`edit_star_subscription <pyrogram.Client.edit_star_subscription>`
    * :meth:`edit_user_star_subscription <pyrogram.Client.edit_user_star_subscription>`
    * :meth:`get_available_gifts <pyrogram.Client.get_available_gifts>`
    * :meth:`get_chat_gifts <pyrogram.Client.get_chat_gifts>`
    * :meth:`get_chat_gifts_count <pyrogram.Client.get_chat_gifts_count>`
    * :meth:`get_gift_auction_state <pyrogram.Client.get_gift_auction_state>`
    * :meth:`get_gift_collections <pyrogram.Client.get_gift_collections>`
    * :meth:`get_gift_upgrade_preview <pyrogram.Client.get_gift_upgrade_preview>`
    * :meth:`get_gift_upgrade_variants <pyrogram.Client.get_gift_upgrade_variants>`
    * :meth:`get_gifts_for_crafting <pyrogram.Client.get_gifts_for_crafting>`
    * :meth:`get_passkeys <pyrogram.Client.get_passkeys>`
    * :meth:`get_payment_form <pyrogram.Client.get_payment_form>`
    * :meth:`get_star_gift_auction_state <pyrogram.Client.get_star_gift_auction_state>`
    * :meth:`get_star_gift_collections <pyrogram.Client.get_star_gift_collections>`
    * :meth:`get_stars_balance <pyrogram.Client.get_stars_balance>`
    * :meth:`get_stars_transactions <pyrogram.Client.get_stars_transactions>`
    * :meth:`get_stars_transactions_by_id <pyrogram.Client.get_stars_transactions_by_id>`
    * :meth:`get_ton_balance <pyrogram.Client.get_ton_balance>`
    * :meth:`get_upgraded_gift <pyrogram.Client.get_upgraded_gift>`
    * :meth:`get_upgraded_gift_value_info <pyrogram.Client.get_upgraded_gift_value_info>`
    * :meth:`get_user_gifts <pyrogram.Client.get_user_gifts>`
    * :meth:`gift_premium_subscription <pyrogram.Client.gift_premium_subscription>`
    * :meth:`gift_premium_with_stars <pyrogram.Client.gift_premium_with_stars>`
    * :meth:`hide_gift <pyrogram.Client.hide_gift>`
    * :meth:`increase_gift_auction_bid <pyrogram.Client.increase_gift_auction_bid>`
    * :meth:`place_gift_auction_bid <pyrogram.Client.place_gift_auction_bid>`
    * :meth:`process_gift_purchase_offer <pyrogram.Client.process_gift_purchase_offer>`
    * :meth:`remove_collection_gifts <pyrogram.Client.remove_collection_gifts>`
    * :meth:`reorder_collection_gifts <pyrogram.Client.reorder_collection_gifts>`
    * :meth:`reorder_gift_collections <pyrogram.Client.reorder_gift_collections>`
    * :meth:`reorder_star_gift_collections <pyrogram.Client.reorder_star_gift_collections>`
    * :meth:`reuse_star_subscription <pyrogram.Client.reuse_star_subscription>`
    * :meth:`search_gifts_for_resale <pyrogram.Client.search_gifts_for_resale>`
    * :meth:`send_gift <pyrogram.Client.send_gift>`
    * :meth:`send_gift_purchase_offer <pyrogram.Client.send_gift_purchase_offer>`
    * :meth:`send_invoice <pyrogram.Client.send_invoice>`
    * :meth:`send_paid_media <pyrogram.Client.send_paid_media>`
    * :meth:`send_paid_reaction <pyrogram.Client.send_paid_reaction>`
    * :meth:`send_payment_form <pyrogram.Client.send_payment_form>`
    * :meth:`send_resold_gift <pyrogram.Client.send_resold_gift>`
    * :meth:`set_gift_collection_name <pyrogram.Client.set_gift_collection_name>`
    * :meth:`set_gift_resale_price <pyrogram.Client.set_gift_resale_price>`
    * :meth:`set_pinned_gifts <pyrogram.Client.set_pinned_gifts>`
    * :meth:`show_gift <pyrogram.Client.show_gift>`
    * :meth:`transfer_gift <pyrogram.Client.transfer_gift>`
    * :meth:`update_star_gift_collection <pyrogram.Client.update_star_gift_collection>`
    * :meth:`upgrade_gift <pyrogram.Client.upgrade_gift>`

.. toctree::
    :hidden:

    add_collection_gifts <add_collection_gifts>
    apply_gift_code <apply_gift_code>
    buy_gift_upgrade <buy_gift_upgrade>
    check_gift_code <check_gift_code>
    convert_gift <convert_gift>
    convert_gift_to_stars <convert_gift_to_stars>
    craft_gift <craft_gift>
    create_gift_collection <create_gift_collection>
    create_invoice_link <create_invoice_link>
    create_star_gift_collection <create_star_gift_collection>
    delete_gift_collection <delete_gift_collection>
    delete_passkey <delete_passkey>
    delete_star_gift_collection <delete_star_gift_collection>
    drop_gift_original_details <drop_gift_original_details>
    edit_star_subscription <edit_star_subscription>
    edit_user_star_subscription <edit_user_star_subscription>
    get_available_gifts <get_available_gifts>
    get_chat_gifts <get_chat_gifts>
    get_chat_gifts_count <get_chat_gifts_count>
    get_gift_auction_state <get_gift_auction_state>
    get_gift_collections <get_gift_collections>
    get_gift_upgrade_preview <get_gift_upgrade_preview>
    get_gift_upgrade_variants <get_gift_upgrade_variants>
    get_gifts_for_crafting <get_gifts_for_crafting>
    get_passkeys <get_passkeys>
    get_payment_form <get_payment_form>
    get_star_gift_auction_state <get_star_gift_auction_state>
    get_star_gift_collections <get_star_gift_collections>
    get_stars_balance <get_stars_balance>
    get_stars_transactions <get_stars_transactions>
    get_stars_transactions_by_id <get_stars_transactions_by_id>
    get_ton_balance <get_ton_balance>
    get_upgraded_gift <get_upgraded_gift>
    get_upgraded_gift_value_info <get_upgraded_gift_value_info>
    get_user_gifts <get_user_gifts>
    gift_premium_subscription <gift_premium_subscription>
    gift_premium_with_stars <gift_premium_with_stars>
    hide_gift <hide_gift>
    increase_gift_auction_bid <increase_gift_auction_bid>
    place_gift_auction_bid <place_gift_auction_bid>
    process_gift_purchase_offer <process_gift_purchase_offer>
    remove_collection_gifts <remove_collection_gifts>
    reorder_collection_gifts <reorder_collection_gifts>
    reorder_gift_collections <reorder_gift_collections>
    reorder_star_gift_collections <reorder_star_gift_collections>
    reuse_star_subscription <reuse_star_subscription>
    search_gifts_for_resale <search_gifts_for_resale>
    send_gift <send_gift>
    send_gift_purchase_offer <send_gift_purchase_offer>
    send_invoice <send_invoice>
    send_paid_media <send_paid_media>
    send_paid_reaction <send_paid_reaction>
    send_payment_form <send_payment_form>
    send_resold_gift <send_resold_gift>
    set_gift_collection_name <set_gift_collection_name>
    set_gift_resale_price <set_gift_resale_price>
    set_pinned_gifts <set_pinned_gifts>
    show_gift <show_gift>
    transfer_gift <transfer_gift>
    update_star_gift_collection <update_star_gift_collection>
    upgrade_gift <upgrade_gift>

Phone
-----

.. hlist::
    :columns: 3

    * :meth:`get_call_members <pyrogram.Client.get_call_members>`

.. toctree::
    :hidden:

    get_call_members <get_call_members>

Premium
-------

.. hlist::
    :columns: 3

    * :meth:`apply_boost <pyrogram.Client.apply_boost>`
    * :meth:`get_boosts <pyrogram.Client.get_boosts>`
    * :meth:`get_boosts_status <pyrogram.Client.get_boosts_status>`

.. toctree::
    :hidden:

    apply_boost <apply_boost>
    get_boosts <get_boosts>
    get_boosts_status <get_boosts_status>

Pyromod
-------

.. hlist::
    :columns: 3

    * :meth:`ask <pyrogram.Client.ask>`
    * :meth:`get_listener_matching_with_data <pyrogram.Client.get_listener_matching_with_data>`
    * :meth:`get_listener_matching_with_identifier_pattern <pyrogram.Client.get_listener_matching_with_identifier_pattern>`
    * :meth:`get_many_listeners_matching_with_data <pyrogram.Client.get_many_listeners_matching_with_data>`
    * :meth:`get_many_listeners_matching_with_identifier_pattern <pyrogram.Client.get_many_listeners_matching_with_identifier_pattern>`
    * :meth:`listen <pyrogram.Client.listen>`
    * :meth:`register_next_step_handler <pyrogram.Client.register_next_step_handler>`
    * :meth:`remove_listener <pyrogram.Client.remove_listener>`
    * :meth:`stop_listener <pyrogram.Client.stop_listener>`
    * :meth:`stop_listening <pyrogram.Client.stop_listening>`
    * :meth:`wait_for_callback_query <pyrogram.Client.wait_for_callback_query>`
    * :meth:`wait_for_message <pyrogram.Client.wait_for_message>`

.. toctree::
    :hidden:

    ask <ask>
    get_listener_matching_with_data <get_listener_matching_with_data>
    get_listener_matching_with_identifier_pattern <get_listener_matching_with_identifier_pattern>
    get_many_listeners_matching_with_data <get_many_listeners_matching_with_data>
    get_many_listeners_matching_with_identifier_pattern <get_many_listeners_matching_with_identifier_pattern>
    listen <listen>
    register_next_step_handler <register_next_step_handler>
    remove_listener <remove_listener>
    stop_listener <stop_listener>
    stop_listening <stop_listening>
    wait_for_callback_query <wait_for_callback_query>
    wait_for_message <wait_for_message>

Stickers
--------

.. hlist::
    :columns: 3

    * :meth:`add_sticker_to_set <pyrogram.Client.add_sticker_to_set>`
    * :meth:`create_sticker_set <pyrogram.Client.create_sticker_set>`
    * :meth:`get_sticker_set <pyrogram.Client.get_sticker_set>`

.. toctree::
    :hidden:

    add_sticker_to_set <add_sticker_to_set>
    create_sticker_set <create_sticker_set>
    get_sticker_set <get_sticker_set>

Stories
-------

.. hlist::
    :columns: 3

    * :meth:`can_post_stories <pyrogram.Client.can_post_stories>`
    * :meth:`copy_story <pyrogram.Client.copy_story>`
    * :meth:`delete_stories <pyrogram.Client.delete_stories>`
    * :meth:`edit_story_caption <pyrogram.Client.edit_story_caption>`
    * :meth:`edit_story_media <pyrogram.Client.edit_story_media>`
    * :meth:`edit_story_privacy <pyrogram.Client.edit_story_privacy>`
    * :meth:`enable_stealth_mode <pyrogram.Client.enable_stealth_mode>`
    * :meth:`forward_story <pyrogram.Client.forward_story>`
    * :meth:`get_all_stories <pyrogram.Client.get_all_stories>`
    * :meth:`get_archived_stories <pyrogram.Client.get_archived_stories>`
    * :meth:`get_chat_stories <pyrogram.Client.get_chat_stories>`
    * :meth:`get_pinned_stories <pyrogram.Client.get_pinned_stories>`
    * :meth:`get_stories <pyrogram.Client.get_stories>`
    * :meth:`get_story_views <pyrogram.Client.get_story_views>`
    * :meth:`hide_chat_stories <pyrogram.Client.hide_chat_stories>`
    * :meth:`pin_chat_stories <pyrogram.Client.pin_chat_stories>`
    * :meth:`read_chat_stories <pyrogram.Client.read_chat_stories>`
    * :meth:`send_story <pyrogram.Client.send_story>`
    * :meth:`show_chat_stories <pyrogram.Client.show_chat_stories>`
    * :meth:`unpin_chat_stories <pyrogram.Client.unpin_chat_stories>`
    * :meth:`view_stories <pyrogram.Client.view_stories>`

.. toctree::
    :hidden:

    can_post_stories <can_post_stories>
    copy_story <copy_story>
    delete_stories <delete_stories>
    edit_story_caption <edit_story_caption>
    edit_story_media <edit_story_media>
    edit_story_privacy <edit_story_privacy>
    enable_stealth_mode <enable_stealth_mode>
    forward_story <forward_story>
    get_all_stories <get_all_stories>
    get_archived_stories <get_archived_stories>
    get_chat_stories <get_chat_stories>
    get_pinned_stories <get_pinned_stories>
    get_stories <get_stories>
    get_story_views <get_story_views>
    hide_chat_stories <hide_chat_stories>
    pin_chat_stories <pin_chat_stories>
    read_chat_stories <read_chat_stories>
    send_story <send_story>
    show_chat_stories <show_chat_stories>
    unpin_chat_stories <unpin_chat_stories>
    view_stories <view_stories>

Users
-----

.. hlist::
    :columns: 3

    * :meth:`block_user <pyrogram.Client.block_user>`
    * :meth:`check_username <pyrogram.Client.check_username>`
    * :meth:`create_story_album <pyrogram.Client.create_story_album>`
    * :meth:`delete_profile_photos <pyrogram.Client.delete_profile_photos>`
    * :meth:`delete_story_album <pyrogram.Client.delete_story_album>`
    * :meth:`edit_story <pyrogram.Client.edit_story>`
    * :meth:`export_story_link <pyrogram.Client.export_story_link>`
    * :meth:`get_chat_audios <pyrogram.Client.get_chat_audios>`
    * :meth:`get_chat_audios_count <pyrogram.Client.get_chat_audios_count>`
    * :meth:`get_chat_photos <pyrogram.Client.get_chat_photos>`
    * :meth:`get_chat_photos_count <pyrogram.Client.get_chat_photos_count>`
    * :meth:`get_common_chats <pyrogram.Client.get_common_chats>`
    * :meth:`get_default_emoji_statuses <pyrogram.Client.get_default_emoji_statuses>`
    * :meth:`get_me <pyrogram.Client.get_me>`
    * :meth:`get_peer_stories <pyrogram.Client.get_peer_stories>`
    * :meth:`get_stories_history <pyrogram.Client.get_stories_history>`
    * :meth:`get_story_albums <pyrogram.Client.get_story_albums>`
    * :meth:`get_user_profile_audios <pyrogram.Client.get_user_profile_audios>`
    * :meth:`get_users <pyrogram.Client.get_users>`
    * :meth:`remove_my_profile_photo <pyrogram.Client.remove_my_profile_photo>`
    * :meth:`repost_story <pyrogram.Client.repost_story>`
    * :meth:`set_emoji_status <pyrogram.Client.set_emoji_status>`
    * :meth:`set_my_profile_photo <pyrogram.Client.set_my_profile_photo>`
    * :meth:`set_personal_channel <pyrogram.Client.set_personal_channel>`
    * :meth:`set_profile_photo <pyrogram.Client.set_profile_photo>`
    * :meth:`set_username <pyrogram.Client.set_username>`
    * :meth:`suggest_birthday <pyrogram.Client.suggest_birthday>`
    * :meth:`unblock_user <pyrogram.Client.unblock_user>`
    * :meth:`update_birthday <pyrogram.Client.update_birthday>`
    * :meth:`update_personal_chat <pyrogram.Client.update_personal_chat>`
    * :meth:`update_profile <pyrogram.Client.update_profile>`
    * :meth:`update_status <pyrogram.Client.update_status>`
    * :meth:`update_story_album <pyrogram.Client.update_story_album>`

.. toctree::
    :hidden:

    block_user <block_user>
    check_username <check_username>
    create_story_album <create_story_album>
    delete_profile_photos <delete_profile_photos>
    delete_story_album <delete_story_album>
    edit_story <edit_story>
    export_story_link <export_story_link>
    get_chat_audios <get_chat_audios>
    get_chat_audios_count <get_chat_audios_count>
    get_chat_photos <get_chat_photos>
    get_chat_photos_count <get_chat_photos_count>
    get_common_chats <get_common_chats>
    get_default_emoji_statuses <get_default_emoji_statuses>
    get_me <get_me>
    get_peer_stories <get_peer_stories>
    get_stories_history <get_stories_history>
    get_story_albums <get_story_albums>
    get_user_profile_audios <get_user_profile_audios>
    get_users <get_users>
    remove_my_profile_photo <remove_my_profile_photo>
    repost_story <repost_story>
    set_emoji_status <set_emoji_status>
    set_my_profile_photo <set_my_profile_photo>
    set_personal_channel <set_personal_channel>
    set_profile_photo <set_profile_photo>
    set_username <set_username>
    suggest_birthday <suggest_birthday>
    unblock_user <unblock_user>
    update_birthday <update_birthday>
    update_personal_chat <update_personal_chat>
    update_profile <update_profile>
    update_status <update_status>
    update_story_album <update_story_album>

Utilities
---------

.. hlist::
    :columns: 3

    * :meth:`add_handler <pyrogram.Client.add_handler>`
    * :func:`compose <pyrogram.compose>`
    * :meth:`export_session_string <pyrogram.Client.export_session_string>`
    * :func:`idle <pyrogram.idle>`
    * :meth:`ping <pyrogram.Client.ping>`
    * :meth:`remove_error_handler <pyrogram.Client.remove_error_handler>`
    * :meth:`remove_handler <pyrogram.Client.remove_handler>`
    * :meth:`restart <pyrogram.Client.restart>`
    * :meth:`run <pyrogram.Client.run>`
    * :meth:`run_sync <pyrogram.Client.run_sync>`
    * :meth:`start <pyrogram.Client.start>`
    * :meth:`stop <pyrogram.Client.stop>`
    * :meth:`stop_transmission <pyrogram.Client.stop_transmission>`

.. toctree::
    :hidden:

    add_handler <add_handler>
    compose <compose>
    export_session_string <export_session_string>
    idle <idle>
    ping <ping>
    remove_error_handler <remove_error_handler>
    remove_handler <remove_handler>
    restart <restart>
    run <run>
    run_sync <run_sync>
    start <start>
    stop <stop>
    stop_transmission <stop_transmission>
