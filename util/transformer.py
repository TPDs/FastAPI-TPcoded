
from classes.datatype import AttackData 

async def optimzer(list) -> list[AttackData]:
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


