#Write a program that ask the user a temperature in celsius degrees, make the convertion to fahrenheit degrees and print the result.

temperature = input("enter a temperature in ºC:") 

temp_fahrenheit = (float(temperature) * 9/5) + 32

print(f"\nThe temperature is {temp_fahrenheit} ºF\n")
