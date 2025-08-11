print("Sowmi Computer")
print("Nehru Street,Puducherry")
print("------------------------------")
print("Bill Reciept")
print("------------------------------")
IN=int(input("Enter The Item No:"))
par=input("Enter The Particular:")
rate=int(input("Enter The rate:"))
qua=int(input("Enter the Quantity:"))
total=rate*qua
print("Total Amount In Rs :",total)
if total >= 100000:
    gst = total*10/100
elif total >= 50000:
        gst = total*5/100
elif total >= 20000:
            gst = total*3/100
elif total >= 10000:
                gst = total*2/100
else:
        gst = total*1/100
print("Gst(good&service tax):",gst)
amt=total+gst
print("Amount To Be Paid:",amt)
