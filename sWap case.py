#Problem 14 hacker Rank Solution
#sWAP cAse

def swap_case(s):
    s = list(s)

    for i in range(0, len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90: #ASCII Code of UpperCase Alphabets are 65 to 90 
            s[i] = s[i].lower()

        elif ord(s[i]) >= 97 and ord(s[i]) <= 122: #ASCII Code of lowercase alphabets are from 97 to 122
            s[i] = s[i].upper()
    
    return "".join(s)

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)

#you cn se the ASCII code of the alphabets: http://sticksandstones.kstrom.com/appen.html
#Write or Paste this code in Hacker rank terminal 
#LAnguage used Python 3
#Thankyou! I will see you in next vediooo....