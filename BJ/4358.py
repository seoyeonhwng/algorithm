from collections import defaultdict
import sys

def get_ratio(count):
    return round(count * 100 / total, 4)

infos, total = defaultdict(int), 0
for line in sys.stdin:
    if line == '\n':
        break

    tree = line.rstrip()
    infos[tree] += 1
    total += 1

infos = sorted(infos.items(), key=lambda x:x[0])
for name, count in infos:
    ratio = get_ratio(count)
    print(name, '%.4f' %ratio)