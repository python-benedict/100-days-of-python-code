#Write a program that calculates the Body Mass Index (BMI) from a user's weight and height.

#The BMI is a measure of someone's weight taking into account their height. e.g. If a tall person and a short person both weigh the same amount, the short person is usually more overweight.

weight = input('Enter your weight: ')
height = input('Enter your height: ')
height_float = float(height)

BMI = float(weight) / height_float**2

print(int(BMI))