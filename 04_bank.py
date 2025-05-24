class BankName():
    bank_name = "Haseeb Bank"
    
    @classmethod
    def chnage_bank_name(cls, new_bank_name):
        cls.bank_name = new_bank_name


Bank1 = BankName()
print(Bank1.bank_name)
BankName.chnage_bank_name("new Bank")
print(Bank1.bank_name)