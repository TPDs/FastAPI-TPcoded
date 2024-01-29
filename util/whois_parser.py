from typing import List, Optional
from pydantic import BaseModel
from geoip2.database import Reader

geoip_database_path = 'datafiles/GeoLite2-Country.mmdb'

class AttackData(BaseModel):
    ip: str
    country: Optional[str]
    payload: str = 'null'  
    CVE: str = 'null'    
    Timestamp: str = 'null'
    attack_link: str = 'null'

async def ip_parser(data: List[str]) -> List[AttackData]:
    return_list = []        
    with Reader(geoip_database_path) as reader:
        for ip in data:
            try:              
                response = reader.country(ip)
                print(response)
                ip_data = AttackData(ip=ip, country=response.country.name)
                return_list.append(ip_data)
            except Exception as e:
                print(f"Error processing {ip}: {e}")
    
    return return_list