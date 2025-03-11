import pandas as pd
import json
import csv
import re
# fname = '/Users/lucycai/Library/CloudStorage/OneDrive-TheSalvationArmy/Documents/TSA_Projects/D&I/ArchiveBox/data_clean/Grace_N1445 Holdings Summary Report - National holdings AS AT 16 August 2024 (1).xlsx'
# df = pd.read_excel(fname,sheet_name='CONTAINER', skiprows=3)
# df.to_csv('./backend/container.csv',index=False)


csv_file = './backend/container.csv'
json_file = './frontend/src/data.js'
# "Storage Branch": "Perth"
with open(json_file, 'r') as f:
    lines = f.read()
    lines = re.sub(r'\"([\w\s]+)\":\s\"([\w\s]*)\"',r"'\1': '\2'",lines)

with open('./frontend/src/data2.js','w') as f:
    f.write(lines)

exit(0)

with open(csv_file, 'r',encoding='utf-8') as file:
    csv_reader = csv.DictReader(file)
    data = list(csv_reader)
    #print(data)

with open(json_file,'w',encoding='utf-8') as file:
    json.dump(data,file, indent=2)

