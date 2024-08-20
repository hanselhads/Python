#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇
bill = float(input("Enter the bll amount\n"))

people = int(input("Enter the amount of people to split  the bill with\n"))

tip = float(input("Enter the amount of tip\n"))

bill_with_tip = bill + ((bill * tip) / 100)

bill_per_person = round(bill_with_tip / people ,3)

print(f"The amount to be paid by each person is {bill_per_person}")