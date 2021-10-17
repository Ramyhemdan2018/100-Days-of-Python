weight = float(input("What is your weight? "))
shbr = float(input("enter your hight with shbr: "))
shbr_to_meter = (shbr * 11.592) /100
print("your hight with metres is: ", shbr_to_meter)
height = float(input("What is your hight? "))


bmi = round(weight / height ** 2)
if bmi < 18.5:
  print(f"Your bmi is {bmi}, you are underweight.")
elif bmi > 18.5 and bmi < 25:
  print(f"Your bmi is {bmi}, you are normal weight.")
elif bmi < 30 and bmi > 25:
  print(f"our bmi is {bmi}, you are overweight.")
elif bmi < 35 and bmi > 30:
  print(f"Your bmi is {bmi}, you are obese")
else:
  print(f"Your bmi is {bmi}, you are clinically obese")

