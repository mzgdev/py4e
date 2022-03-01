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
def calification_calculator(score):

    if (0.0 < score < 1.0): 
        if score >= 0.9 :
            request = "outstanding"
        elif score >= 0.8:
            request = "remarkable"
        elif score >= 0.7 :
            request = "good"
        elif score >= 0.6:
            request = "enough"
        else:
            request = "insufficient"
    else:
        request = "error, enter a number between 0.0 and 1.0"
    return request

print(calification_calculator(score))        
