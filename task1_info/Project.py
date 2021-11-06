import json
import numpy as np
import matplotlib.pyplot as plt
from metrics import eval_dist_metric

with open("intro_trajectory_1.json") as f:
    traj = json.load(f)
    

## Pre-calculate the pair indexes we are interested in
keys = []
for fp1 in traj['fps']:
    for fp2 in traj['fps']:
         # only calculate the upper triangle
        if fp1['step_index'] > fp2['step_index']:
            keys.append((fp1['step_index'], fp2['step_index']))
 
## Get the distances from PDR
true_d = {}
for step1 in traj['steps']:
    for step2 in traj['steps']:
        key = (step1['step_index'],step2['step_index'])
        if key in keys:
            true_d[key] = abs(step1['di'] - step2['di'])
            
    
euc_d = {}
man_d = {}
for fp1 in traj['fps']:
    for fp2 in traj['fps']:
        key = (fp1['step_index'],fp2['step_index'])
        if key in keys:
            euc_d[key] = euclidean(fp1['profile'],fp2['profile'])
            man_d[key] = manhattan(fp1['profile'],fp2['profile'])

print("Euclidean Average Error")
print(f'{eval_dist_metric(euc_d, true_d):.2f}')

print("Manhattan Average Error")
print(f'{eval_dist_metric(man_d, true_d):.2f}')