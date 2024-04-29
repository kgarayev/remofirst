from sqlalchemy import Column, Integer, String, UUID, TIMESTAMP, ForeignKey, DateTime
from sqlalchemy.orm import declarative_base
from sqlalchemy.sql import func
import sqlalchemy.dialects.postgresql as postgresql
import uuid
from sqlalchemy.sql import func


class MessageModel(declarative_base()):
    
    __tablename__ = "chat_message"
    
    id = Column(postgresql.UUID(as_uuid=True), primary_key=True, default=uuid.uuid4, unique=True)


    created_at = Column(DateTime(timezone=True), nullable=False, default=func.now())
    updated_at = Column(DateTime(timezone=True), nullable=True)
    
    
    message = Column(String, nullable=False)
    sender_id = Column(UUID, nullable=False)
    session_id_id = Column(UUID, nullable=False)

    
    