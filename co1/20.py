#remove2evennumber
evenList=[22,34,77,88,4000]
print("evenList items=",evenList)
for ev in evenList:
    if(ev % 2 == 0):
        evenList.remove(ev)
print("list after removing even number",evenList)