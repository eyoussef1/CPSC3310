MONTHS_IN_YEAR = 12
PERCENT = 100

while (monthly_investment := float(input("Enter a monthly investment amount: "))) <= 0:
    print("Error: investment must be a positive number")

while (yearly_interest_rate := float(input("Enter a yearly interest rate: "))) <= 0:
    print("Error: yearly interest rate must be a positive number")

while (investment_years := int(input("Enter how many years to invest: "))) <= 0:
    print("Error: investment period must be a positive number of years")

investment = 0
months = investment_years * MONTHS_IN_YEAR
month = 1
monthly_interest_rate = yearly_interest_rate / MONTHS_IN_YEAR / PERCENT

while month <= months:
    investment = investment + monthly_investment
    monthly_revenue = investment * monthly_interest_rate
    investment = investment + monthly_revenue

    print(f"Month {month} revenue: {investment}")

    month += 1

print(f"After {investment_years} years, you will receive a total investment revenue of {investment:,.2f} at a yearly rate of {yearly_interest_rate}")
