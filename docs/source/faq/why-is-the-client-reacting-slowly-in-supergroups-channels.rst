Why is the client reacting slowly in supergroups/channels?
----------------------------------------------------------

Telegram intentionally limits update delivery speed for clients that are members of many large supergroups
or channels. This is a server-side rate limit and cannot be bypassed.

To mitigate this:

- Reduce the number of large groups/channels the account is a member of.
- Use :doc:`/topics/smart-plugins` to ensure handlers are as fast as possible.
- Consider processing updates asynchronously so that slow handlers do not block incoming updates.
