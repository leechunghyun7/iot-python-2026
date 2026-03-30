## ex18_encapsule.py 캡슐화

class Accoutn:
    def __init__(self,money):
        self.balance =money

    def deposit(self,money): #입금
        self.balance += money

    def get_balance(self):
        return self.balance
    
if __name__ =='__main__':
    myacc = Account(1000000)
    print(f'계좌금액은{myacc.get_balance():,}원')
    #print(f'계좌금액:{myacc.balance:,}달러')
    
    myacc.deposit(100_000)
    print(f'계좌금액은 {myacc.get_balance():,}')

    print(f'계좌금액은 {myacc.get_balance():,}원')
