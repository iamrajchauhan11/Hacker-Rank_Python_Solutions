#Problem 22 Hacker Rank Solution
#Designer Door Mat

R,C = map(int,input().split(' '))

for i in range(1,R,2):
    print((".|."*i).center(C,'-'))

print("WELCOME".center(C,'-'))

for i in range(R-2,-1,-2):
    print((".|."*i).center(C,'-'))

#Run this

#Write or Copy Paste this code in Hacker Rank Terminal...
#and, if any of my code is giving any kind of error so just change the lanugaue type in Hacker Rank terminal...

#Pypy 2 => Python 3
#Python 3 => Pypy 2

#Thankyou!!! I will see you next time.....