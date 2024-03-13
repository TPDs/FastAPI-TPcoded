from classes.datatype import AttackData
from pydantic import BaseModel
from geoip2.database import Reader

geoip_database_path = 'datafiles/GeoLite2-Country.mmdb'

async def ip_parser(data: list[AttackData]) -> list[AttackData]:
    return_list = []        
    with Reader(geoip_database_path) as reader:
        for i in data:
            try:              
                response = reader.country(i.ip)                
                ip_data = AttackData(ip=i.ip, country=response.country.name, payload=i.payload,Timestamp=i.Timestamp)
                return_list.append(ip_data)
            except Exception as e:
                print(f"Error processing {i}: {e}")    
    return return_list