print("Good morning costumer price the of an apple is 20 pesos and the orange is 25 pesos each:")
apple = 20
orange = 25

def getApples():
    print(" How many apples you want to buy?: ")
    applesFunc = int(input())
    return applesFunc

def getOranges():
    print(" How many oranges you want to buy?: ")
    orangesFunc = int(input())
    return orangesFunc

def getAmount(): 
    amountFunc = float(apple*apples + orange*oranges)
    return amountFunc

def displayOutput (amount):
     print(f"The total amount need to pay is {amount} pesos")

#Steps in making this program
# 1. Show the price of the fruits in the market.
# 2.step ask for how many apples you want to buy.
apples = getApples()
# 3.step ask for how many oranges you want to buy.
oranges = getOranges()
# 4.step show the total amount that need to be paid.
amount = getAmount()
displayOutput (amount)
print("Thank you for shopping")   


