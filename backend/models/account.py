class Account:
    def __init__(
        self,
        id: int,
        account_type: str,
        balance: float,
        customer_id: int
    ):
        self.id = id
        self.account_type = account_type
        self.balance = balance
        self.customer_id = customer_id