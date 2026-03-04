
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.db.base import Base
import uuid

class Lineage(Base):
    __tablename__ = "lineage"

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    upstream_fqn = Column(String(255), ForeignKey("datasets.fqn"))
    downstream_fqn = Column(String(255), ForeignKey("datasets.fqn"))

    upstream = relationship("Dataset", foreign_keys=[upstream_fqn])
    downstream = relationship("Dataset", foreign_keys=[downstream_fqn])
