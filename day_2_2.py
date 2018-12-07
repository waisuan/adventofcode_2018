with open('input.txt') as file:
    lines = file.read().splitlines()
    found = False
    for idx, val in enumerate(lines):
        for idx2, val2, in enumerate(lines):
            if idx2 == idx:
                continue
            count = sum(1 for a, b in zip(val, val2) if a != b)
            if count == 1:
                print("{} vs. {}".format(val, val2))
                common = ''
                for a, b in zip(val, val2):
                    if a == b:
                        common += a
                print("{}".format(common))
                found = True
                break
        if found:
            break
