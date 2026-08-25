from datetime import datetime

from sqlalchemy import Column
from sqlalchemy import DateTime
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Text

from app.database import Base


class Call(Base):

    __tablename__ = "calls"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    calle_call_id = Column(
        String,
        nullable=True,
        index=True
    )

    created_at = Column(
        DateTime,
        default=datetime.utcnow
    )

    phone_number = Column(
        String,
        nullable=False
    )

    target = Column(
        String,
        nullable=False
    )

    purpose = Column(
        Text,
        nullable=False
    )

    status = Column(
        String,
        default="PENDING"
    )

    call_duration = Column(
        Integer,
        nullable=True
    )

    summary = Column(
        Text,
        nullable=True
    )

    transcript = Column(
        Text,
        nullable=True
    )

    structured_result = Column(
        Text,
        nullable=True
    )