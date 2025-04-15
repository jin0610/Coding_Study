dial = {
    2 : ['A', 'B', 'C'],
    3 : ['D', 'E', 'F'],
    4 : ['G', 'H', 'I'],
    5 : ['J', 'K', 'L'],
    6 : ['M', 'N', 'O'],
    7 : ['P', 'Q', 'R', 'S'],
    8 : ['T', 'U', 'V'],
    9 : ['W', 'X', 'Y', 'Z']
}

text = list(input())
time = 0

for t in text:
    for d in dial:
        if t in dial[d]:
            time += (d + 1)

print(time)