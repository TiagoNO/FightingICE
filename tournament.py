import sys
import os
#!/usr/bin/env python3
from subprocess import DEVNULL, STDOUT, check_call


ai_dir = "data/ai/"

ais = []
for f in os.listdir(ai_dir):
    if ".jar" in f:
        ais.append(f.replace(".jar", ""))

for i in range(len(ais)):
    for j in range(i+1, len(ais)):
        print("{} vs {}!".format(ais[i], ais[j]))
        command = ["java", "-cp", "FightingICE.jar:lib/lwjgl/*:lib/natives/linux/*:lib/*:data/ai/*", "Main", "--a1", "{}".format(ais[i]), "--a2", "{}".format(ais[j]), "--fastmode", "--grey-bg", "--inverted-player", "1", "--limithp", "400", "400", "--n", "2", "--c1", "ZEN", "--c2", "ZEN", "--disable-window"]
        check_call(command, stdout=DEVNULL, stderr=STDOUT)