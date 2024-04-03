import csv
import os

directory = 'log/point/'

data = {}
players = set()

data_files = os.listdir(directory)
for f in data_files:
    file = f

    if 'CYR_AI' in f:
        f = f.replace('CYR_AI', 'CYRAI')

    if 'LGIST_Bot' in f:
        f = f.replace('LGIST_Bot', 'LGISTBot')

    if 'Fuzzy_ZYQAI' in f:
        f = f.replace('Fuzzy_ZYQAI', 'FuzzyZYQAI')

    if 'IBM_AI' in f:
        f = f.replace('IBM_AI', 'IBMAI')

    if 'JayBot_GM' in f:
        f = f.replace('JayBot_GM', 'JayBotGM')

    if 'Jitwisut_Zen' in f:
        f = f.replace('Jitwisut_Zen', 'JitwisutZen')

    if 'MonkeyLink_TriplePM' in f:
        f = f.replace('MonkeyLink_TriplePM', 'MonkeyLinkTriplePM')

    formatted = f.split("_")
    p1_name, p2_name = formatted[1], formatted[2]
    print(p1_name, p2_name)
    players.add(p1_name)
    players.add(p2_name)

    with open(directory + file, newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
        for game, p1HP, p2HP, frames in spamreader:
            if not p1_name in data:
                data[p1_name] = {}

            if not p2_name in data:
                data[p2_name] = {}

            if not p2_name in data[p1_name]:
                data[p1_name][p2_name] = []

            if not p1_name in data[p2_name]:
                data[p2_name][p1_name] = []

            data[p1_name][p2_name].append([int(game), int(p1HP), int(p2HP)])
            data[p2_name][p1_name].append([int(game), int(p2HP), int(p1HP)])

winrates = {}
matches_won = {}
for p1 in players:
    if not p1 in winrates:
        winrates[p1] = {}

    if not p1 in matches_won:
        matches_won[p1] = 0

    for p2 in players:
        if not p2 in winrates[p1]:
            winrates[p1][p2] = 0
        
        if p1 == p2:
            continue

        wins, losses, ties = 0, 0, 0
        try:
            for game, p1HP, p2HP in data[p1][p2]:
                if p1HP > p2HP:
                    wins += 1

                elif p1HP < p2HP:
                    losses += 1

                if p1HP == p2HP:
                    ties += 1

            winrates[p1][p2] = (wins + (0.5 * ties)) / (wins + losses + ties)
            if(winrates[p1][p2] > 1):
                print(p1, p2, wins, losses, ties)
                input()
            matches_won[p1] += wins             
        except:
            winrates[p1][p2] = -1

print(winrates['YIYAI'])



wr_file = open('winrates.txt', 'w')
wr_file.write("-;")
for p1 in players:
    wr_file.write("{};".format(p1))
wr_file.write("\n")

for p1 in winrates.keys():
    wr_file.write("{};".format(p1))
    for p2 in winrates[p1].keys():
        wr_file.write("{};".format(winrates[p1][p2]))
    wr_file.write("\n")
wr_file.close()

mt_file = open("ranking.txt", 'w')
for p1 in matches_won.keys():
    mt_file.write("{};{};\n".format(p1, matches_won[p1]))
mt_file.close()