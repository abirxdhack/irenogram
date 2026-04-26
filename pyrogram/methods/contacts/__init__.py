
from .add_contact import AddContact
from .delete_contacts import DeleteContacts
from .get_contacts import GetContacts
from .get_contacts_count import GetContactsCount
from .import_contacts import ImportContacts

from .get_blocked_message_senders import GetBlockedMessageSenders
from .search_contacts import SearchContacts
from .set_contact_note import SetContactNote
class Contacts(
    SetContactNote,
    SearchContacts,
    GetBlockedMessageSenders,
    GetContacts,
    DeleteContacts,
    ImportContacts,
    GetContactsCount,
    AddContact
):
    pass
