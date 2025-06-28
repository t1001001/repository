from pydantic import BaseModel
from typing import Optional

# message model
class Message(BaseModel):
    msg_id: Optional[str] = None
    name: str
    message: str