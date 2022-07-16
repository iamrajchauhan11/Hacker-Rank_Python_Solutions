#Problem 9 Hacker Rank Solution
#Find the Runner-Up Score!

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    print(sorted(list(set(arr)))[-2])
#Write or Paste this code same in Hacker Rank Terminal
#In All Program I used Python 3 as Lanugage...