#Program with function
def getName(): 
    nameFunc = input ("Name: ")
    return nameFunc

def getAge():
    ageFunc = input("Age: ") 
    return ageFunc

def getAddress():
    addressFunc = input("Address: ")
    return addressFunc

def displayOutput (NameF, AgeF, AddressF):
      print(f"Hi my name is {NameF}.  I am {AgeF} and I live in {AddressF}.")


#Steps in making this program
# 1.step ask for name and save to variable
name = getName()
# 2.step ask for age and save to variable 
age = getAge()
# 3.step ask for address and save to variable 
address = getAddress()
# 4.step display name age and address
displayOutput(name, age, address)

