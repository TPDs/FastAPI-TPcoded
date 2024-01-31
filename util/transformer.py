from classes.datatype import AttackData 


async def optimzer(list : list[str] ) -> list[AttackData]:
    return_list = []
    for i in list:
        ilist = i[1].split('*-*')       
        print(ilist)       
        return_list.append(i)
    return return_list