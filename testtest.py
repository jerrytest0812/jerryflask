import json
with open ('jerryflask\static\data\message.json','r') as f :
            data = json.load(f)
            print('text:',data)
f.close