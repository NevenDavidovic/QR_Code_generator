import pyqrcode
import png
import time

choice=True
while choice:
    print("1 Payment Data")
    print("2 From a chunk of text to barcode")
    print("0 Exit")
    
    choice=input("Odaberi broj: ")  
    
    if choice=='1':
        # Ask for the person's name and last name, IBAN, and payment amount
        name = input("Enter your name: ")
        last_name = input("Enter your last name: ")
        iban = input("Enter your IBAN: ")
        amount = input("Enter payment amount: ")

        # Construct the payment data string
        payment_data = f"Name: {name}\nLast Name: {last_name}\nIBAN: {iban}\nAmount: {amount}"

        # Generate the QR code
        qr_code = pyqrcode.create(payment_data, error='H')

        # Save the QR code as a PNG image file
        filename = f"nfc_payment_{time.time()}.png"
        qr_code.png(filename, scale=10, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xff, 0xff])
        
    
    elif choice=='2':
        # Ask for the text to be encoded in QR code
        text = input("Enter the text to be encoded in QR code: ")

        # Generate the QR code
        qr_code = pyqrcode.create(text, error='H')

        # Save the QR code as a PNG image file
        filename = f"nfc_payment_{time.time()}.png"
        qr_code.png(filename, scale=10, module_color=[0, 0, 0, 255], background=[0xff, 0xff, 0xff, 0xff])
        
    elif choice=='0':
        # Exit the program
        choice=False
        
    else:
        # Invalid input, ask for input again
        print("Invalid input. Please enter a valid choice.\n")     
        
   






