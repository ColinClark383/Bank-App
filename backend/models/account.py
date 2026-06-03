class Account:

    def __init__(
        self,
        _id,
        customer_id,
        account_type,
        balance
    ):
        self._id = _id
        self.customer_id = customer_id
        self.account_type = account_type
        self.balance = balance