with open('input.txt') as file:
    frequency = 0
    for line in file:
        step = line.rstrip()
        print(step[0] + ' ' + step[1:])
        if (step[0] == '+'):
            frequency += int(step[1:])
        else:
            frequency -= int(step[1:])
    print('Answer: {}'.format(frequency))
