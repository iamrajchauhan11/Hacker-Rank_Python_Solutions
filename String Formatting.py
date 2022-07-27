#Problem 23 Hacker Rank Soltuion
#String Formatting

def print_formatted(number):
    l1 = len(bin(number)[2:])
    for i in range(l,number+1):
        print(str(i).rjust(l1,' '),end=" ")
        print(oct(i)[2:].rjust(l1," "),end=" ")
        print(((hex(i)[2:]).upper()).rjust(l1,' '),end=" ")
        print(bin(i)[2:].rjust(l1,' '),end=" ")
        print("")

if __name__ == '__main__':
    n = int(input())
    print_formatted(n)

#Lanuguage used Python 3
#Write or Copy Paste this code in Hacker Rank Terminal
#Thankyou!! I will see you in next videoo.....