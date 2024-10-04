# ATM machine simulator

### Requirements:
1. The program should have a predefined dictionary of users with their account numbers and balances.
2. Users should be able to check their balance, deposit money, and withdraw money.
3. The program should ask for the user's account number and validate it.
4. If the account number is valid, the program should display a menu with options to check balance, deposit money, and withdraw money.
5. For the deposit and withdrawal options, the program should ask for the amount and update the balance accordingly.
6. The program should handle invalid inputs and display appropriate error messages.

### Example of the predefined dictionary:
```
accounts = {
    '123456': {'name': 'John Doe', 'balance': 1500},
    '789012': {'name': 'Jane Smith', 'balance': 2000},
    '345678': {'name': 'Alice Johnson', 'balance': 500}
}
```

### Proposed usage example:
```commandline
Please enter your account ID:
# 2233
This account ID is not valid. Please enter your account ID:
# 123456
Hi John, your account balance is 1500 coins. 
Use '+' to add coins, or '-' to withdraw coins. Use '?' to check your balance. Type 'exit' to quit.
> +300
Deposited: +300 coins. New balance: 1800 coins
> -5000
Error: Insufficient balance
> ?
Balance: 1800 coins
> -500
Withdrew: -500 coins. New balance: 1300 coins
> exit

Thank you for using the ATM. Goodbye!

```

### Use following template
```python

ACCOUNTS = {
    '123456': {'name': 'John Doe', 'balance': 1500},
    '789012': {'name': 'Jane Smith', 'balance': 2000},
    '345678': {'name': 'Alice Johnson', 'balance': 500}
}

class Authorization:
    def __init__(self, accounts):
        self.accounts = accounts

    def validate_account(self, account_number):
        """ Validate the account number """
        pass


class CoinOperations:
    def __init__(self, accounts):
        self.accounts = accounts

    def check_balance(self, account_number):
        """ Check the balance of the given account number """
        pass

    def deposit_coins(self, account_number, amount):
        """ Deposit coins to the given account number """
        pass

    def withdraw_coins(self, account_number, amount):
        """ Withdraw coins from the given account number """
        pass


class ATM:
    def __init__(self):
        # Predefined dictionary of accounts
        self.accounts = ACCOUNTS
        self.auth = Authorization(self.accounts)
        self.operations = CoinOperations(self.accounts)

    def run(self):
        """ Main method to run the ATM operations """
        pass

# Create an instance of the ATM and run it
atm_machine = ATM()
atm_machine.run()
```