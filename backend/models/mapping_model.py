from pydantic import BaseModel
from typing import Dict, List

class MappingItem(BaseModel):
    data: Dict

class SavePayload(BaseModel):
    items: List[Dict]