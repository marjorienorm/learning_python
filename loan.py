# Get the loan details

money_owed = float( input ("How much do you owe, in dollars?\n"))   # $50,000

apr = float( input( "What is the annual percentage rate?\n"))      # 3%

payment = float( input( "What will your monthly payment be, in dollars?\n")) # $1,000

months = int( input( "How many months do you want to see results for?\n"))  # 24

# Divide apr by 100 to make it a percentage, then divide by 12 to make it monthly
monthly_rate = apr/100/12

for i in range( months):
    # Add in interest
    intrest_paid = money_owed * monthly_rate
    money_owed = money_owed + intrest_paid

    # Check if we have paid off the load and break out of the look of we have
    if( money_owed - payment < 0 ):
        print("The last payment is", money_owed, ".", end=' ')
        print("You paid off the loan in", i+1, "months.")
        break

    # Make payment
    money_owed = money_owed - payment

    # Print the results after this month
    print("Paid", payment, "of which", intrest_paid, "was interest.", end=' ' )
    print("Now I owe", money_owed)
