path = 'memo.txt'

with open(path) as f:
    for line in f:
        if line.startswith('■'):
            print(line, end='')