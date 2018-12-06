with open('input.txt') as file:
    frequency = 0
    seen = {frequency}
    found = False
    lines = file.read().splitlines()
    while (not found):
        for step in lines:
            print(step[0] + ' ' + step[1:])
            if (step[0] == '+'):
                frequency += int(step[1:])
            else:
                frequency -= int(step[1:])
            if (frequency in seen):
                print('Answer: {}'.format(frequency))
                found = True
                break
            seen.add(frequency)
