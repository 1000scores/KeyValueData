import argparse
import os
import tempfile
import json




parser = argparse.ArgumentParser()

parser.add_argument("--key",
                    help = "this is key")
parser.add_argument("--value",
                    help = "this is value")

args = parser.parse_args()
k = args.key
v = args.value

storage_path = os.path.join(tempfile.gettempdir(), 'storage.data')


storage = None
with open(storage_path, 'a') as f:
    pass

with open(storage_path, 'r') as f:
    cur = f.readline()
    #print(cur)
    if cur == '':
        storage = {}
    else:
        storage = json.loads(cur)

#print(storage)
if v == None:
    if not(str(k) in storage):
        print(None)
    else:
        for index, i in enumerate(storage[str(k)]):
            if index + 1 == len(storage[str(k)]):
                print(i)
            else:
                print(i, end=", ")

else:
    if str(k) in storage:
        storage[str(k)].append(v)
    else:
        storage[str(k)] = [v]
    #print(storage)
    with open(storage_path, 'w') as f:
        f.write(json.dumps(storage))





