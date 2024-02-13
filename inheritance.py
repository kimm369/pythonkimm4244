class Mpesa:
    def __init__(self,account_balance,phone_number):
        self.account_balance = account_balance
        self.phone_number = phone_number
    def send_money(self,amount,recipient):
        if self.account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES Sent to {recipient} successful")
        else:
            print("Insufficient balance")
class Personal_Mpesa(Mpesa):
    def __init__(self,account_balance,phone_number,id_number):
        super(). __init__(account_balance,phone_number)
        self.id_number = id_number
    def buyairtime(self,amount):
        if self. account_balance >= amount:
            self.account_balance -= amount
            print(f"{amount} KES airtime bought successfull")
class Business_Mpesa(Mpesa):
    def __init__(self,account_balance,phone_number,business_number,business_name):
        super(). __init__(account_balance,phone_number)
        self.business_number = business_number
        self.business_name = business_name
    def receive_money(self,amount):
        self.account_balance += amount
        print(f"{amount} Kes received successfully")
personal=Personal_Mpesa(500,176426743,126787)
personal.send_money(550,89735783)
personal.buyairtime(20)

business=Business_Mpesa(886,176426743,3694244,"fazah")
business.receive_money(5641)