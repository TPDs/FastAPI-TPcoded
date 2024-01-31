import json
from typing import List, Optional
import json
from typing import List
from pydantic import BaseModel

class AttackData(BaseModel):
    ip: str
    country: Optional[str]
    payload: str = 'null'  
    CVE: str = 'null'    
    Timestamp: str = 'null'
    attack_link: str = 'null'



class Item(BaseModel):
    name: str
    price: float

class Data(BaseModel):
    items: List[Item]

    @classmethod
    def from_file(cls, filepath: str):
        with open(filepath, 'r') as f:
            data = json.load(f)
            sorted_items = sorted(data['items'], key=lambda x: x['price'])
            return cls(items=sorted_items)
