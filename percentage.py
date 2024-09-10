#take marks as input from user
print("Enter marks obtained in five subjects=")
maths = int(input("Maths="))
english = int(input("English="))
science = int(input("Science="))
islamiat = int(input("Islamiat="))
arts = int(input("Arts="))

#calculate percentage of marks
sum = maths+english+science+islamiat+arts
print("Total sum of all subjects=")
percentage = (sum/500)*100
print("Total percentage=", percentage)