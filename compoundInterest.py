def calculateCompoundInterest():
# This first 3 lines are provided for yougetACompoundIntrest()
# This first 3 lines are provided for you
    client_one_principal = float(input("Principle (amount): "))
    client_one_time =      float(input("Time:               "))
    client_one_rate =      float(input("Rate:               "))
 #print("Compound Interest: "+str(intrest))
    amount = client_one_principal * (1 + client_one_rate / 100)**client_one_time
    CI = amount - client_one_principal
    print('Compound Interest: ', round(CI,2))
    # end assignment



## if you want to test locally before you try to sync
## uncomment calculateCompoundInterest() and run > python monkeyCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
#calculateCompoundInterest()
#print('---')
#calculateCompoundInterest()
#print('---')
#calculateCompoundInterest()
