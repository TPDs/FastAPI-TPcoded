import whoisdomain as whois
from typing import Optional
from pydantic import BaseModel , validator


class attack_data(BaseModel):
    ip: str
    #city: Optional[str] 
    country: Optional[str]
    payload: str = 'null'  
    CVE: str = 'null'    
    Timestamp: str = 'null'
    attack_link: str = 'null'


async def ip_parser(data : list):
    return_list = []
    for ip in data:
        w = whois.query(ip)     
        print(w)      
        if w is not None:
            ip_data = attack_data(ip=ip, country=w.registrant_country)        
            return_list.append(ip_data)
    return return_list
 