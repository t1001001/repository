from typing import List, Optional, Final
from src.models.models import Message
from src.config import db

COLLECTION: Final = "messages"

# CREATE a message
async def create_message(message: Message) -> Message:
    data = message.model_dump()
    doc_ref = db.collection(COLLECTION).add(data)
    doc_id = doc_ref[1].id
    db.collection(COLLECTION).document(doc_id).update({"msg_id": doc_id})
    return Message(msg_id = doc_id, name = message.name, message = message.message)

# READ messages (limited to 5)
async def read_messages(limit: int = 5) -> List[Message]:
    docs = db.collection(COLLECTION).limit(limit).stream()
    messages = [Message(**doc.to_dict()) for doc in docs]
    return messages

# READ a individual message by its msg_id
async def read_message(msg_id: str) -> Optional[Message]:
    docs = db.collection(COLLECTION).where("msg_id", "==", msg_id).stream()
    for doc in docs:
        return Message(**doc.to_dict())
    return None