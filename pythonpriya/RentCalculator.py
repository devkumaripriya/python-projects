#inputs we need from the user
#Total rent
#Total Food ordered for sanacking
#Electricity units spend
#charge per unit
#Persons living in room/flat

##Output
#Total amount you've to pay is

Rent=int(input("Enter Your Flat Rent ="))
food=int(input("Enter the amount of food Ordered:"))
electricity_spend=int(input("Enter The Total Of Electricity Spend = "))
UnitOfCharge=int(input("Enter the charge per unit = "))
persons=int(input("Enter the no.of person living in room = "))
total_bill=electricity_spend*UnitOfCharge

output=(food+Rent+total_bill) // persons

print("Each person will pay =",output)