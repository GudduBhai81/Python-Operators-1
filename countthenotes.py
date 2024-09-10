amount = int(input("Please enter amount for widthrawl="))

#calculating number of nots of different denominations
note1 = amount//100
note2 = (amount % 100)//50
note3 = ((amount % 100)% 50)//10

print("Notes of hundred", note1)
print("Notes of fifty", note2)
print("Notes of ten", note3)
