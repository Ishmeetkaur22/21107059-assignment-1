# question1
int_1 = float(input("first number "))

int_2 = float(input("second number "))

int_3 = float(input("third number "))

average = round ( int_1 + int_2 + int_3 / 3 , 2)

print (f"average of the numbers is {average}")

# question2
gross_income = float(input("Please enter your income$"))
dependent_no = float(input("Enter number of dependents"))
#standard deduction = $10,000
#dependent deduction = $3000
taxable_income = gross_income - 10000 - (dependent_no * 3000)
#Tax rate = 20%	
tax_payable = round( (20 / 100 * taxable_income), 2)
print("Your income tax is $",tax_payable)

# question3
seconds = int(input("Enter number of seconds. "))
minutes_displayed = seconds // 60
seconds_displayed = seconds % 60
print(seconds, "seconds is", minutes_displayed, "minutes and", seconds_displayed, "seconds.")

# question4
#String '25' is coverted to integer using int function for it to be added.
result = 25 + int('25') + 25.0
string_result = str(round(result))
print(string_result)

# question5
import math
#Loop is used since we need to perform an operation over and over again
for angle in range(0, 346, 15):
 radian_angle = math.radians(angle)
 sine_value = math.sin(radian_angle)
 cosine_value = math.cos(radian_angle)
 print (round(sine_value, 4), round(cosine_value, 4))
