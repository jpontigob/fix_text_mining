import pandas as pd
import json

df = pd.read_csv('/Users/jorgepontigo/Downloads/tsk_processed_message_pit_stop.csv', header=0, sep=',',parse_dates = ['create_dt'], usecols=[0,1,2,13,16,23], dayfirst = True)

id_lista = []
tail = []
type_ = []
alert = []
flight = []
source = []
notification_dt = []
_tail = []
mssg = df['message']
id_ = df['seq']
created_dt = df['notification_dt']
tail = df['fleet']



tail = df['fleet']

print(tail)

_tail = tail.str.split('-')
__tail = []
___tail = []

print(_tail[1][0])

for i in range(len(_tail)):
    if _tail[i][0] == 'B787':
        __tail.append(_tail[i][0])
        ___tail.append(0)
    else:
        __tail.append(_tail[i][0])
        ___tail.append(_tail[i][1])
        

dict = {"fleet": __tail, "sub_fleet": ___tail}

df2 = pd.DataFrame(dict)

print(df2) #test