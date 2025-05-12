### 4. **Class Variables and Class Methods**  
#Create a class `Bank` with a class variable `bank_name`. Add a class method `change_bank_name(cls, name)` that allows changing the bank name. Show that it affects all instances.

class Bank:
    bank_name = "Habib Bank"

    @classmethod
    def Change_name(cls, name):
        cls.bank_name = name

    def Show(self):
        print(f"Bank Name: {self.bank_name} has been updated")

# Create first bank object
bank1 = Bank()
bank1.Change_name("Metropolitan Bank")
bank1.Show()

# Create second bank object
bank2 = Bank()
bank2.Change_name("Allied Bank")
bank2.Show()
