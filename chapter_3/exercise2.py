#write a program to ask the user a price per hour and hours of number for calculate the salary.
# use try and except to limit the data type introduced.

try:
    price = float(input("write your price per hour: "))
    hours = float(input("write the amount of hours worked:"))
    if hours > 40:
        salary = (40 * price) + ((hours - 40) * price * 1.5)
    else:
        salary = hours * price

    print(f"The final salary is: {salary}\n")

except:
    print("Error, you must enter a number please.")

