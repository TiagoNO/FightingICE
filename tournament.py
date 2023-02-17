import sys
import os
#!/usr/bin/env python3
import subprocess
from subprocess import DEVNULL, STDOUT

def check_existing(p1_name, p2_name):
    files = os.listdir("log/point/")
    for f in files:
        if "{}_{}".format(p1_name, p2_name) in f or "{}_{}".format(p2_name, p1_name) in f:
            return True
    return False

ai_dir = "data/ai/"

ais = []
for f in os.listdir(ai_dir):
    if ".jar" in f:
        ais.append(f.replace(".jar", ""))

for i in range(len(ais)):
    for j in range(i+1, len(ais)):
        if check_existing(ais[i], ais[j]):
            print("{} vs {} already exist...".format(ais[i], ais[j]))
            continue
        else:
            print("{} vs {}!".format(ais[i], ais[j]))
            command = ["java", "-cp", "FightingICE.jar:lib/lwjgl/*:lib/natives/linux/*:lib/*:data/ai/*", "Main", "--a1", "{}".format(ais[i]), "--a2", "{}".format(ais[j]), "--fastmode", "--grey-bg", "--inverted-player", "1", "--limithp", "400", "400", "--n", "2", "--c1", "ZEN", "--c2", "ZEN", "--disable-window"]
            process = subprocess.Popen(command, stdout=DEVNULL, stderr=DEVNULL)
            process.wait()