
from sqlalchemy import Column, String, Enum
from sqlalchemy.orm import relationship
from app.db.base import Base
import enum

class SourceType(str, enum.Enum):
    mysql = "MySQL"
    mssql = "MSSQL"
    postgres = "PostgreSQL"

class Dataset(Base):
    __tablename__ = "datasets"

    fqn = Column(String(255), primary_key=True)
    source_type = Column(Enum(SourceType), nullable=False)

    upstream = relationship(
        "Lineage",
        foreign_keys="Lineage.downstream_fqn",
        back_populates="downstream",
    )

    downstream = relationship(
        "Lineage",
        foreign_keys="Lineage.upstream_fqn",
        back_populates="upstream",
    )
