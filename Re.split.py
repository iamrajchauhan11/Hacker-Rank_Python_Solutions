#Problem 24 Hacker Rank Solution

#Re.split()

#In this problem you just need one thing I'll show you...

regex_pattern = r"[, .]" #<= here	 # Do not delete 'r'.

#In Hacker Rank Terminal you will show this type of Code in Pyhton 3 Language...
#You just need to write 4 letters [, .] in between double quots""

import re
print("\n".join(re.split(regex_pattern, input())))

#Thankyou !! I will see you next time....