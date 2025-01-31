class InsufficientFundsException(Exception):
    def __init__(
        self,
        required_amount,
        current_balance,
        currency="UAH",
        transaction_type="withdrawal",
    ):
        self.required_amount = required_amount
        self.current_balance = current_balance
        self.currency = currency
        self.transaction_type = transaction_type
        super().__init__(
            f"Insufficient funds for {self.transaction_type} of {self.required_amount} {self.currency}. Current balance: {self.current_balance} {self.currency}."
        )


class Account:
    def __init__(self, account_number, balance=0, currency="UAH"):
        self.account_number = account_number
        self.balance = balance
        self.currency = currency

    def purchase(self, amount):
        if amount > self.balance:
            raise InsufficientFundsException(
                amount, self.balance, self.currency, "purchase"
            )
        self.balance -= amount
        print(
            f"A purchase was made in the {amount} of {self.currency}. Your balance {self.balance} {self.currency}"
        )


personal_account = Account("2203", 10)
try:
    personal_account.purchase(8)
    personal_account.purchase(20)
except InsufficientFundsException as e:
    print(e)
