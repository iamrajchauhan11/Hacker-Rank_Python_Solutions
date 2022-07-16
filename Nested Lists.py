#Problem 10 Hacker Rank Solution
#Nested Lists

score_list = [];
for _ in range(int(input())):
    name = input()
    score = float(input())
    score_list.append([name, score])
second_higest = sorted(set([score for name, score in score_list]))[1]

print('\n'.join(sorted([name for name, score in score_list if score == second_higest])))

#Paste or Write this code same as in Hacker rank Terminal....