n = int(input())
seats = [input() for _ in range(n)]
k = int(input())
pass_list = [list(input().split()) for _ in range(k)]
for i in range(k):
    num = int(pass_list[i][0])
    side = pass_list[i][1]
    prefer = pass_list[i][2]
    isSetled = False
    for j in range(n):
        table = seats.copy()
        place = []
        if side == "left":
            letters = "ABC"
            if prefer == "aisle":
                isBooked = False
                for p in range(num):
                    if seats[j][2-p] == '#':
                        isBooked = True
                    table[j] = table[j][:2-p] + 'X' + table[j][2-p+1:]
                    place.insert(0, f"{j+1}{letters[2-p]}")
                if isBooked:
                    continue
                else:
                    print("Passengers can take seats:", ' '.join(place))
                    print('\n'.join(table))
                    seats[j] = table[j].replace('X', '#')
                    isSetled = True
                    break
            else:
                isBooked = False
                for p in range(num):
                    if seats[j][p] == '#':
                        isBooked = True
                    table[j] = table[j][:p] + 'X' + table[j][p+1:]
                    place.append(f"{j + 1}{letters[p]}")
                if isBooked:
                    continue
                else:
                    print("Passengers can take seats:", ' '.join(place))
                    print('\n'.join(table))
                    seats[j] = table[j].replace('X', '#')
                    isSetled = True
                    break
        else:
            letters = "DEF"
            if prefer == "aisle":
                isBooked = False
                for p in range(num):
                    if seats[j][4+p] == '#':
                        isBooked = True
                    table[j] = table[j][:4+p] + 'X' + table[j][4+p+1:]
                    place.append(f"{j + 1}{letters[p]}")
                if isBooked:
                    continue
                else:
                    print("Passengers can take seats:", ' '.join(place))
                    print('\n'.join(table))
                    seats[j] = table[j].replace('X', '#')
                    isSetled = True
                    break
            else:
                isBooked = False
                for p in range(num):
                    if seats[j][6-p] == '#':
                        isBooked = True
                    table[j] = table[j][:6-p] + 'X' + table[j][6-p+1:]
                    place.insert(0, f"{j + 1}{letters[2 - p]}")
                if isBooked:
                    continue
                else:
                    print("Passengers can take seats:", ' '.join(place))
                    print('\n'.join(table))
                    seats[j] = table[j].replace('X', '#')
                    isSetled = True
                    break
    if isSetled:
        continue
    else:
        print("Cannot fulfill passengers requirements")