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


class Data(BaseModel):
    items: List[AttackData]

    @classmethod
    def from_file(cls, filepath: str):
        with open(filepath, 'r') as f:
            data = json.load(f)
            sorted_items = sorted(data['AttackData'], key=lambda x: x['country'])
            return cls(items=sorted_items)
