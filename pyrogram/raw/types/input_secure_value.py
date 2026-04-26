
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any


class InputSecureValue(TLObject):
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputSecureValue`.

    Details:
        - Layer: ``224``
        - ID: ``DB21D0A7``

    Parameters:
        type (:obj:`SecureValueType <pyrogram.raw.base.SecureValueType>`):
            N/A

        data (:obj:`SecureData <pyrogram.raw.base.SecureData>`, *optional*):
            N/A

        front_side (:obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`, *optional*):
            N/A

        reverse_side (:obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`, *optional*):
            N/A

        selfie (:obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`, *optional*):
            N/A

        translation (List of :obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`, *optional*):
            N/A

        files (List of :obj:`InputSecureFile <pyrogram.raw.base.InputSecureFile>`, *optional*):
            N/A

        plain_data (:obj:`SecurePlainData <pyrogram.raw.base.SecurePlainData>`, *optional*):
            N/A

    """

    __slots__: List[str] = ["type", "data", "front_side", "reverse_side", "selfie", "translation", "files", "plain_data"]

    ID = 0xdb21d0a7
    QUALNAME = "types.InputSecureValue"

    def __init__(self, *, type: "raw.base.SecureValueType", data: "raw.base.SecureData" = None, front_side: "raw.base.InputSecureFile" = None, reverse_side: "raw.base.InputSecureFile" = None, selfie: "raw.base.InputSecureFile" = None, translation: Optional[List["raw.base.InputSecureFile"]] = None, files: Optional[List["raw.base.InputSecureFile"]] = None, plain_data: "raw.base.SecurePlainData" = None) -> None:
        self.type = type
        self.data = data
        self.front_side = front_side
        self.reverse_side = reverse_side
        self.selfie = selfie
        self.translation = translation
        self.files = files
        self.plain_data = plain_data

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputSecureValue":
        
        flags = Int.read(b)
        
        type = TLObject.read(b)
        
        data = TLObject.read(b) if flags & (1 << 0) else None
        
        front_side = TLObject.read(b) if flags & (1 << 1) else None
        
        reverse_side = TLObject.read(b) if flags & (1 << 2) else None
        
        selfie = TLObject.read(b) if flags & (1 << 3) else None
        
        translation = TLObject.read(b) if flags & (1 << 6) else []
        
        files = TLObject.read(b) if flags & (1 << 4) else []
        
        plain_data = TLObject.read(b) if flags & (1 << 5) else None
        
        return InputSecureValue(type=type, data=data, front_side=front_side, reverse_side=reverse_side, selfie=selfie, translation=translation, files=files, plain_data=plain_data)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.data is not None else 0
        flags |= (1 << 1) if self.front_side is not None else 0
        flags |= (1 << 2) if self.reverse_side is not None else 0
        flags |= (1 << 3) if self.selfie is not None else 0
        flags |= (1 << 6) if self.translation else 0
        flags |= (1 << 4) if self.files else 0
        flags |= (1 << 5) if self.plain_data is not None else 0
        b.write(Int(flags))
        
        b.write(self.type.write())
        
        if self.data is not None:
            b.write(self.data.write())
        
        if self.front_side is not None:
            b.write(self.front_side.write())
        
        if self.reverse_side is not None:
            b.write(self.reverse_side.write())
        
        if self.selfie is not None:
            b.write(self.selfie.write())
        
        if self.translation is not None:
            b.write(Vector(self.translation))
        
        if self.files is not None:
            b.write(Vector(self.files))
        
        if self.plain_data is not None:
            b.write(self.plain_data.write())
        
        return b.getvalue()
