#If the bill was $150.0, split between 5 people, with 12% tip.
#Each person should pay (150.0 / 5) * 1.12 = 33.6
#Round the result to 2 decimal places = 33.60

#  12/100
# 0.12
#  150*0.12
# 18.0
#  150 + 18
# 168
#  150 * 1.12
# 168.00000000000003
#  168 / 5
# 33.6

# Welcom to the tip Calculator.
# What was the total bill? $124.56
# What percentage tip would you like to give? 10, 12 or 15? 12
# How many people to  split the bill? 7
# Each person should pay: $19.93

print('Welcom to the tip Calculator.')
# bill = input("What was the total bill? $")
# print(type(bill)) -> <class 'str'>
bill = float(input("What was the total bill? $"))
# print(type(bill)) -> <class 'float'>
tip = int(input("What percentage tip would you like to give? 10, 12 or 15? "))
people = int(input("How many people to split the bill? "))
bill_with_tip = tip / 100 * bill + bill
# bill_with_tip = bill * (1 + tip / 100)
# tip_as_percent = tip / 100
# total_tip_amount = bill * tip_as_percent
# total_bill = bill + total_tip_amount
bill_per_person = bill_with_tip / people
# print(bill_with_tip)
# print(bill_per_person)
# final_amount = round(bill_per_person, 2)
final_amount = "{:.2f}".format(bill_per_person)
print(f"Each person should pay: ${final_amount}")
