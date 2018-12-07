import collections

two = 0
three = 0
with open('input.txt') as file:
    for line in file:
        tracker = collections.defaultdict(int)
        id = line.rstrip()
        for char in id:
            tracker[char] += 1
        look_for_two = True
        look_for_three = True
        for k, v in tracker.items():
            if v == 2 and look_for_two:
                two += 1
                look_for_two = False
            elif v == 3 and look_for_three:
                three += 1
                look_for_three = False
            if not look_for_two and not look_for_three:
                break
checksum = two * three
print("{}".format(checksum))
