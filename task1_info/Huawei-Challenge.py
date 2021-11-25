import csv
import json
import os
from tqdm import tqdm

path_to_data = "for_contestants"

with open("task1_data/task1_fingerprints.json") as f:
    fps = json.load(f)
    
with open("task1_data/task1_train.csv") as f:
    train_data = []
    train_h = csv.DictReader(f)
    for pair in tqdm(train_h):
        train_data.append([pair['id1'],pair['id2'],float(pair['displacement'])])
        
# with open("task1_data/task1_test.csv") as f:
#     test_h = csv.DictReader(f)
#     test_ids = []
#     for pair in tqdm(test_h):
#         test_ids.append([pair['id1'],pair['id2']])

def filter():
    newFps = {}
    for value in fps:
        newFps[value] = {}
        for value1 in fps[value]:          
            if fps[value][value1] > -70:
                newFps[value][value1] = fps[value][value1]

    return newFps
newFps = filter()

def filter2():
    newnewFps = []
    for value in newFps:
        for value1 in newFps[value]:
            newnewFps.append(value1)

    return list(sorted(set(newnewFps)))

newnewFps = filter2()
print(newnewFps)

def getEmitters():
    emitterDict = {}
    for emitter in tqdm(newnewFps):
        emitterDict[emitter] = {}
        for value in newFps:
            for value1 in newFps[value]:
                if value1 == emitter:
                    emitterDict[emitter][value1] = newFps[value][value1]
    return emitterDict

def getEmitters2():
    emitterDict = {}
    for value in tqdm(newFps):
        for value1 in newFps[value]:
            for emitter in newnewFps:
                if value1 == emitter:
                    if not (emitter in emitterDict):
                        emitterDict[emitter] = {}
                    emitterDict[emitter][value1] = newFps[value][value1]
    return emitterDict

test = getEmitters2()
print(test)
