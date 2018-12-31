import re
import sys
import collections

p = re.compile('Step (\w) must be finished before step (\w) can begin.')

word = 'Step W must be finished before step Y can begin.'

with open('input.txt') as file:
    lines = file.read().splitlines()
    tracker = {}
    for line in lines:
        matches = p.search(line)
        if matches:
            if matches.group(2) not in tracker:
                tracker[matches.group(2)] = [matches.group(1)]
            else:
                tracker[matches.group(2)].append(matches.group(1))
            if matches.group(1) not in tracker:
                tracker[matches.group(1)] = []
        else:
            print("There's something wrong with your input file.")
            sys.exit(1)
    sorted_tracker = collections.OrderedDict(sorted(tracker.items()))
    print(sorted_tracker)
    output = ''
    prev = len(sorted_tracker)
    while len(sorted_tracker) != 0:
        print("{}".format(sorted_tracker))
        for key in list(sorted_tracker.keys()):
            value = sorted_tracker[key]
            if len(value) == 0:
                for key2 in list(sorted_tracker.keys()):
                    value2 = sorted_tracker[key2]
                    if key in value2:
                        sorted_tracker[key2].remove(key)
                print("Picked {}".format(key))
                output += key
                del sorted_tracker[key]
                break
        if prev == len(sorted_tracker):
            break
        else:
            prev = len(sorted_tracker)
    print(output)

