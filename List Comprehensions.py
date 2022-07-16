#Problem 8 Hacker Rank Solutions
#List Comprehensions

from typing import final


if __name__ == '__main__':
    x = int(input())
    y = int(input())
    z = int(input())
    n = int(input())

    final = []
    for i in range(x+1):
        for j in range(y+1):
            for k in range(z+1):
                l = [i,j,k]
                sum=0
                for m in l:
                    sum+=m
                if sum!=n:
                    final.append(l)
    print(final)