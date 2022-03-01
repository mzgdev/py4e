#write a program that ask the user a score between 0.0 and 1.0, if the score is out the range, show a error message else show the next table:
'''
>= 0.9  "outstanding"
>=0.8   "remarkable"
>=0.7   "good"
>=0.6   "enough"
< 0.6   "insufficient"
'''

try:
    score = float(input("enter a score between 0.0 and 1.0:"))
except:
    print("error, enter a number between 0.0 and 1.0")
    exit()

if (0.0 < score < 1.0): 
    if score >= 0.9 :
        print("outstanding")
    elif score >= 0.8:
        print("remarkable")
    elif score >= 0.7 :
        print("good")
    elif score >= 0.6:
        print("enough")
    else:
        print("insufficient")
else:
    print("error, enter a number between 0.0 and 1.0")

        
