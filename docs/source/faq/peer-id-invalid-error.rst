PEER_ID_INVALID error
---------------------

This error means Irenogram cannot resolve the peer (user, group, or channel) you specified. Common causes:

1. **You have never interacted with this peer** — Telegram only knows about peers that have appeared in your
   contact list, common chats, or message history. Try forwarding a message from the target user/chat first.
2. **Wrong ID format** — Channel and supergroup IDs should be prefixed with ``-100`` when used as integers.
   Irenogram handles this automatically when you pass a username or invite link.
3. **The peer does not exist** — The user/group/channel may have been deleted.
