import string
import random

alphabet = list(string.ascii_uppercase)
alphabet.append("Blank")

points = [1, 3, 3, 2, 1, 4, 2, 4, 1, 8, 5, 1, 3, 1, 1, 3, 10, 1, 1, 1, 1, 4, 4, 8, 4, 10, 0]
letterfreq = [9, 2, 2, 4, 12, 2, 3, 2, 9, 1, 1, 4, 2, 6, 8, 2, 1, 6, 4, 6, 4, 2, 2, 1, 2, 1, 2]
tiles = []

for number in range(27):
    for freq in range(letterfreq[number]):
        tiles.append(alphabet[number])

random.shuffle(tiles)

print(tiles)

Playerfreq = int(input("How many players?"))

hands = list()
for x in range(Playerfreq):
    hands.append([])
    for i in range(7):
        hands[x].append(tiles[-1])
        tiles.pop()

    print(hands[x])

print(tiles)
