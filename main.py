import numpy as np
import pandas as pd

print('Welcome to the Five Crowns Score Keeper!')
print('How many people will be playing?')

num_people = int(input())

print('Please input each name IN ORDER! (Press ENTER after each name)')

names = []

for i in range(num_people):
    names.append(input())

scores = pd.DataFrame(columns = names)


for round in range(11):
    print(f'Who won round {round + 1}?')
    roundWinner = input()
    scores.loc[round, roundWinner] = 0
    winnerIndex = names.index(roundWinner)

    for person in names[winnerIndex + 1:]:
        print(f'Please enter the round {round + 1} score for {person}:')
        scores.loc[round, person] = int(input())

    for person in names[:winnerIndex]:
        print(f'Please enter the round {round + 1} score for {person}:')
        scores.loc[round, person] = int(input())

    Leaderboard = []

    for i in names:
        Leaderboard.append(scores[i].sum(axis = 0))
    
    Leaderboard.sort()
    print(f'Leaderboard:')

    count = 1
    for n in names:
        for x in names:
            if (Leaderboard[count -1] == scores[x].sum(axis = 0)):
                print(f'{count}. {x}: {Leaderboard[count -1]}')
        count += 1