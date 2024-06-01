from classes.datatype import AttackData 
from util.pocketbase import pb_db

pbb = pb_db.get_db()

async def optimzer(list) -> list[AttackData]: ## need tuning
    return_list = []
    for i in list:
        ilist = i[1].split('*-*')    
        ilist[0] = ilist[0].replace(']','')
        ilist[1] = ilist[1].replace('::ffff:','')
        ilist[0] = ilist[0][1:-1]         
        ilist.pop(2)
        ilist.pop(2)      
        ilist.pop(3)
        ilist[2] = ilist[2].replace(' ','')  
        ilist[1] = ilist[1].replace(' ','')         
        dataset = AttackData(ip=ilist[1], country='None', payload=ilist[2], Timestamp=ilist[0])
        return_list.append(dataset)           
    return return_list

async def updateattackdatatodb(attack_data: list[AttackData]):
    try:  
        pbbdata = pbb.collection('attack_data').get_full_list()     
        for x, y in zip(pbbdata, attack_data): ## need tuning
            pbb.collection('attack_data').update(x.id,y.dict()) 
        print("Failed to load data..")        
        return attack_data
    except Exception as e:
        print(f"Error in updateattackdata: {e}")
