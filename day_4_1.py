import re
import collections

pattern1 = re.compile('\[(.+)\]')
pattern2 = re.compile('#(\d+)')

with open('input.txt') as file:
    tracker = {}
    guard_ids = {}
    lines = file.read().splitlines()
    for line in lines:
        matches = pattern1.search(line)
        if matches:
            # print("{}".format(matches.group(1)))
            tracker[matches.group(1)] = line
        matches = pattern2.search(line)
        if matches:
            # print("{}".format(matches.group(1)))
            guard_ids[matches.group(1)] = 1
    sorted_tracker = collections.OrderedDict(sorted(tracker.items()))
    for k, v in sorted_tracker.items():
        print("{}".format(v))
        # matches = pattern2.search(v)
        # if matches:
        #     # print("{}".format(matches.group(1)))
        #     guard_id = matches.group(1)
        #     guard_ids[guard_id] = []
        #     # print("{} {}".format(k, guard_id))
        # else:
        #     #
