import random
import datetime
 
def generate_transaction_id():
    return "TXN" + str(random.randint(100000, 999999))

def mask_card_number(card_number):
    return "****-****-****-" + card_number[-4:]

def print_receipt(name,card,amount):
    txn_id=generate_transaction_id()
    date_time=datetime.datetime.now()
    
    print("\n"+"="*40)
    print("Payment Receipt")
    print("="*40)
    print(f"Customer Name:{name}")
    print(f"Card Number:{mask_card_number(card)}")
    print(f"Amount Paid: {amount}")
    print(f"Transaction ID: {txn_id}")
    print(f"Date & Time: {date_time.strftime('%Y-%m-%d %H:%M:%S')}") 
    print("="*40)
    print("Thank you for your payment!")
    print("="*40)
    
name=input("Enter your name: ")
card_number=input("Enter your card number: ")
amount=float(input("Enter the amount to be paid: "))
    
    
print_receipt(name,card_number,amount)
