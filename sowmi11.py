print("Takshashila University")
print("ongur,tindivanam")
print("---------------------")
print("Student Mark List")
print("---------------------")
pymark=int(input("Enter The Python Mark:"))
dbmark=int(input("Enter The Dbms Mark: "))
inmark=int(input("Enter The Industry Mark:"))
total=pymark+dbmark+inmark
print("Total Mark:",total)
avg=total/3
print("Average Mark:",avg)
if pymark >= 40 and dbmark >= 40 and inmark >= 40:
    print("Result: pass")
    if total >= 250:
        print("Grade: O Grade*")
    elif total >= 200:
        print("Grade: A+ Grade*")
    elif total >= 150:
        print("Grade: A Grade*")
    else:
        print("Grade: B Grade*")
else:
    print("Result: Fail")
    print("Grade: no Grade (Failed)")
