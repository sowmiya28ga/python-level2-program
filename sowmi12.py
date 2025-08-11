print("Government Of Tamilnadu")
print("Electicity Board")
print("-----------------------------")
print("Bill Reciept")
print("-----------------------------")
en=int(input("Enter The Eb No:"))
cn=input("Enter The Customer Name:")
pu=int(input("Enter The Previous Unit:"))
cu=int(input("Enter The Current Unit:"))
unit=pu+cu
print("Unit Consumed:",unit)
if unit >= 1000:
    amt= unit*10
    print("Amount To Be Pais:",amt)
elif unit >= 500:
    amt= unit*5
    print("Amount To Be Paid:",amt)
elif unit >= 100:
    amt= unit*2
    print("Amount To Be Paid:",amt)
else:
    print("Amount To Be Paid: Nill")
