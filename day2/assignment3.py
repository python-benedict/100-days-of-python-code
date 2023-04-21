#I was reading this article by Tim Urban - Your Life in Weeks and realised just how little time we actually have.
#Create a program using maths and f-Strings that tells us how many days, weeks, months we have left if we live until 90 years old.

user_age = int(input('Enter your age: '))
years_remaining = 90 - user_age
days_remaining = years_remaining * 365
weeks_remaining = years_remaining * 52
months_remaining = years_remaining * 12

message = f"you have {days_remaining} days remaining, {weeks_remaining} weeks remaining and {months_remaining} months remaining"
print(message)