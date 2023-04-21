#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = float(input('Enter the total bill: '))
number_of_people = int(input('Enter the totoal number of people to split this bill: '))
each_bill = bill / number_of_people
ten_percent_tip = each_bill * 0.1
twelve_percent_tip = each_bill * 0.12
fifteen_percent_tip = each_bill * 0.15
percentage = int(input('Enter a percentage between 10, 12 and 15: '))
if(percentage == 10):
    print(each_bill + ten_percent_tip)
elif(percentage == 12):
    print(each_bill + twelve_percent_tip)
elif(percentage == 15):
    print(each_bill + fifteen_percent_tip)
else:
    print('Please enter a number within range')