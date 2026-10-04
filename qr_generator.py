import qrcode
upi_id = input("enter your upi id: ")
#upi:\\pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=MESSAGE

#defining the UPI URLs for different payment apps
phonepe_url = f"upi:\\pay?pa={upi_id}&pn=YourName&am=0&cu=INR&tn=Payment"
paytm_url = f"upi:\\pay?pa={upi_id}&pn=YourName&am=0&cu=INR&tn=Payment"
googlepay = f"upi:\\pay?pa={upi_id}&pn=YourName&am=0&cu=INR&tn=Payment"

#create qr code
phonepe_url = qrcode.make(phonepe_url)
paytm_url = qrcode.make(paytm_url)
googlepay = qrcode.make(googlepay)

#save qr code
phonepe_url.save("phonepe_qr.png")
paytm_url.save("paytm_qr.png")  
googlepay.save("googlepay_qr.png")
import os
os.startfile("phonepe_qr.png")
#display qr code
phonepe_url.show()
paytm_url.show()
googlepay.show()
