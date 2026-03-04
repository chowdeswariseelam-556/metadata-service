
from pydantic import BaseModel
from typing import List

class DatasetCreate(BaseModel):
    fqn: str
    source_type: str

class LineageCreate(BaseModel):
    upstream_fqn: str
    downstream_fqn: str
