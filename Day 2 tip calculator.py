print("Welcome to the bit calculator")

bill = float(input("What was the total bill? $"))

tip = int(input("What tip you want to give? 10, 12 or 15\n"))

people = int(input("How many people to split the bill?"))

bill_with_tip = tip / 100 * bill
bill_final = people/bill_with_tip
print ("Each person will pay ", bill_final+ "  $" )