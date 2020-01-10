class Bank:
    cash = 1000000

    @classmethod
    def available_cash(cls):
        print(cls.cash)

class AndhraBank(Bank):
    cash = 200000

    @classmethod
    def available_cash(cls):
        print("Bank Cash        = ",Bank.cash)
        print("Andhra Bank Cash = ",cls.cash)

class StateBank(Bank):
    cash = 500000

    @classmethod
    def available_cash(cls):
        print("Bank Cash        = ",Bank.cash)
        print("State Bank Cash  = ",cls.cash)
        print("Total Cash       = ",Bank.cash + cls.cash)

a = AndhraBank()
a.available_cash()

s = StateBank()
s.available_cash()
    
