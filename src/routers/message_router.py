from fastapi import APIRouter, Query, HTTPException
from typing import List, Optional
from src.models.models import Message
from src.services.message_service import create_message, read_messages, read_message

router = APIRouter()

# POST method for messages
@router.post("/messages", response_model = Message)
async def post_message(message: Message):
    return await create_message(message)

# POST method for all messages
@router.get("/messages", response_model = List[Message])
async def get_messages(limit: int = Query(default = 5, description = "limits the number of messages")):
    return await read_messages(limit)

# POST method for individual messages
@router.get("/messages/{msg_id}", response_model = Message)
async def get_message(msg_id: str):
    message = await read_message(msg_id)
    if not message:
        raise HTTPException(status_code = 404, detail = "message not found")
    return message

