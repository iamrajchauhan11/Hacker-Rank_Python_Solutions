#Problem 19 Hacker Rank Solution
#String Validators

def fun1(s):    #This function is for isalnum()
    for i in range(len(s)):
        if (s[i].isalnum()):
            return True;
            break;
    return False;

def fun2(s):        #this function is for isalpha()
    for i in range(len(s)):
        if (s[i].isalpha()):
            return True;
            break;
    return False;

def fun3(s):        #this function is for isdigit()
    for i in range(len(s)):
        if (s[i].isdigit()):
            return True;
            break;
    return False;

def fun4(s):      #this function is for islower()
    for i in range(len(s)):
        if (s[i].islower()):
            return True;
            break;
    return False;

def fun5(s):         #this function is for isupper()
    for i in range(len(s)):
        if (s[i].isupper()):
            return True;
            break;
    return False;

#They all are builtin function in python...

if __name__ == '__main__':
    s = raw_input()

    flagalphanum = fun1(s)
    alphabetical = fun2(s)
    digit = fun3(s)
    lowercase = fun4(s)
    uppercase = fun5(s)

    print(flagalphanum)
    print(alphabetical)
    print(digit)
    print(lowercase)
    print(uppercase)

#This solution is too long so please download the code file from the description and then copy from there and paste in hacker Rank Terminal

#Lanuguage used Pyhton 3
#Thankyou! I will see you next time.......