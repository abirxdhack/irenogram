
import pyrogram

class Update:
    @staticmethod
    def stop_propagation():
        """Stop propagating this update to other handlers.

        Raises :class:`~pyrogram.StopPropagation` to prevent further handlers from receiving this update.
        """
        raise pyrogram.StopPropagation

    @staticmethod
    def continue_propagation():
        """Continue propagating this update to other handlers.

        Raises :class:`~pyrogram.ContinuePropagation` to pass this update on to the next matching handler.
        """
        raise pyrogram.ContinuePropagation
