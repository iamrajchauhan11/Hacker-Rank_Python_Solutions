#Problem 18 Hacker Rank Solution

#Find a String

def count_substring(string, sub_string):
    count = 0
    for i in range(len(string) - len(sub_string) + 1):
        if (string[i:i+len(sub_string)] == sub_string):
            count += 1
    return count

if __name__ == '__main__':
    string = raw_input().strip() #strip() method is used to remove character from both left and right based on the argument....
    sub_string = raw_input().strip()

    count = count_substring(string, sub_string)
    print (count)

#Copy or Write same code in Hacker Rank terminal
#Language used Python 3
#Thankyou !! I will see you in next video...
#KEEP CODE & KEEP LEARN.