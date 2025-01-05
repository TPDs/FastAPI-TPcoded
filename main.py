import asyncio
from fastapi import FastAPI
from pathlib import Path
from dotenv import load_dotenv
import uvicorn
import os
from classes.datatype import AttackData
from util.pocketbase import pb_db
from util.lakefs import get_client, get_lakefs_logdata
from util.transformer import optimzer, updateattackdatatodb
from util.whois_parser import ip_parser
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger

data = {
    'ip': 'string',    
    'country': 'string',
    'payload': 'string' , 
    'CVE': 'string',     
    'Timestamp': 'string', 
    'attack_link':  'string',
}

load_dotenv() 
host = os.getenv('HOST')
app = FastAPI()
scheduler = BackgroundScheduler()
pbb = pb_db.get_db()
lake = get_client()

return_data = []

@app.get("/parse")
async def parser():
    return await get_lakefs_logdata()


@app.get("/data")
async def pb():
    result = pbb.collection('project').get_full_list()    
    return result


@app.get("/")
async def lakefs():    
    print('LakeFS')    
    return 'attack_data'


@app.get("/update")
async def updateattackdata():
    try:       
        w = await get_lakefs_logdata()
        ww = await optimzer(w)
        www = await ip_parser(ww)         
        return_data = await updateattackdatatodb(www)            
        return return_data
    except Exception as e:
        print(f"Error in updateattackdata: {e}")

def update_attack_data_job():
    asyncio.run(updateattackdata())

async def start_scheduler():
    scheduler.add_job(update_attack_data_job, 'cron', second='*/30')
    scheduler.start()
    print('Scheduler started')

async def main():       
    await start_scheduler()
    print('Server part 2')   
    uvicorn.run(f"{Path(__file__).stem}:app", port=5273, host=host, reload=False) # type: ignore

if __name__ == '__main__':
    print('Server part 1')
    asyncio.run(main())
   