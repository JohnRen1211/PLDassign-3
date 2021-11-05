print("The money inside the wallet.")
def getMoney():
    print("how much mney you have in wallet?")
    moneyFunc = int(input())
    return moneyFunc 

def getApple():
    print("How much is an apple? ")
    appleFunc = int(input()) 
    return appleFunc 

def maxApple (money,apple):
    print("How many apples I can buy?")
    return (money // apple)

def remainingMoney (money,maximumApple,apple):
    print("How much is the remaing money?")
    return float(money - (maximumApple * apple))

def displayOutput (maximumApple,remainCash):
     print(f"The amount of apples can buy are {maximumApple} and the remaining money is {remainCash} pesos")

#Steps in making this program
# 1. Check the amount of money in wallet.
# 2.step ask for how many money left in wallet.
money = getMoney()
# 3.step ask for how much is an apple.
apple = getApple()
# 4.step display the maximum apples that can be bought and the remaining money.
maximumApple = maxApple (money,apple)
print(maximumApple)
remainCash = remainingMoney(money,maximumApple,apple)
print(remainCash)
#5. step show the apples can buy and the remaing money.
displayOutput (maximumApple,remainCash)
print("Thank you for shopping")   
