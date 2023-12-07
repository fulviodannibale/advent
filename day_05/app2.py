import sys

file_path = 'input.txt'
min_location=sys.maxsize
maps={}
current_map = ""
with open(file_path, 'r') as file:

    seeds = next(file).split(":")[1].split()
    count = 0
    for line in file:
        if "map" in line:
            count += 1
            maps[str(count)] = {}
            maps[str(count)]["tuples"] = []
        elif line.strip():
            r = line.split()
            maps[str(count)]["tuples"].append((int(r[1]), int(r[0]), int(r[2])))


for k in range(0, len(seeds), 2):
    for j in range (int(seeds[k]), int(seeds[k]) + int(seeds[k+1]),1):
        next_compare = j
        for i in range(1, len(maps)+1):
            for t in maps[str(i)]["tuples"]:
                source = t[0]
                destination = t[1]
                interval = t[2]
                if source <= next_compare <= source + interval:
                    next_compare = next_compare + destination - source
                    break
        if(next_compare < min_location):
            min_location = next_compare
            print(min_location)

print(min_location)



