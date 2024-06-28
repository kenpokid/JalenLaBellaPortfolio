#!/user/bin/env python3

print("Pay Check Calculator\n")

Continue = "y"
while Continue.lower() == "y":
    worked = input("Hours Worked: ")
    pay_rate = input("Hourly Pay Rate: ")
    worked = float(worked)
    pay_rate = float(pay_rate)
    gross_pay = worked * pay_rate
    gross_pay = round(gross_pay, 2)
    print("\nGross Pay: " + str(gross_pay))
    tax_rate = 18
    print("Tax Rate: " + str(tax_rate) + "%")
    tax_rate = float(tax_rate)
    tax_amount = gross_pay * (tax_rate / 100)
    tax_amount = float(tax_amount)
    tax_amount = round(tax_amount, 2)
    print("Tax Amount: " + str(tax_amount))
    take_home_pay = gross_pay - tax_amount
    take_home_pay = round(take_home_pay, 2)
    print("Take Home Pay: " + str(take_home_pay))

    Continue = input("\ncontinue (y/n)?")
print("Goodbye")
