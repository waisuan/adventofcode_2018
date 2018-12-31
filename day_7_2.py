import re
import sys
import collections
import copy

class Worker:
    def __init__(self, id):
        self.id = id
        self.is_working = False
        self.working_seconds = 0
        self.working_on = ''

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

    workers = []
    for x in range(5):
        workers.append(Worker(x))

    seconds = 0
    working = True
    while working is True:
        seconds += 1
        print(sorted_tracker)

        updated_tracker = copy.deepcopy(sorted_tracker)

        for worker in workers:
            if worker.is_working is not True and len(sorted_tracker) != 0:
                worker.working_on = ''
                for key in list(sorted_tracker.keys()):
                    value = sorted_tracker[key]
                    if len(value) == 0:
                        worker.working_on = key
                        break
                if worker.working_on != '':
                    del sorted_tracker[worker.working_on]
                    del updated_tracker[worker.working_on]
                    worker.working_seconds = 60 + ord(worker.working_on) - 64
                    print("{}:: {} - {}".format(worker.id,
                                                worker.working_on, worker.working_seconds))
                    worker.is_working = True
                    # seconds += worker.working_seconds
                else:
                    print("{} is not working".format(worker.id))
            if worker.is_working is True:
                worker.working_seconds -= 1
                print("{}:: Tick ... {}".format(worker.id, worker.working_seconds))
                if worker.working_seconds == 0:
                    for key2 in list(updated_tracker.keys()):
                        value2 = updated_tracker[key2]
                        if worker.working_on in value2:
                            updated_tracker[key2].remove(worker.working_on)
                    worker.is_working = False
                    
        sorted_tracker = copy.deepcopy(updated_tracker)

        print("seconds:: {}".format(seconds))
        if len(sorted_tracker) == 0:
            working = False
            for worker in workers:
                if worker.is_working is True:
                    working = True

    print("{}".format(seconds))
