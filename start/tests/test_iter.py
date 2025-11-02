from itertools import chain

data=['SINCE 6-Oct-2025', 'BEFORE 7-Oct-2025']
res=chain(['()'],data)
for i in res:
    print(i)