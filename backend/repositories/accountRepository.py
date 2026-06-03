from bson import ObjectId

from database import account_collection
from models.account import Account


class AccountRepository:

    def get_all(self):

        accounts = []

        for account in account_collection.find():

            accounts.append(
                Account(
                    _id=str(account["_id"]),
                    customer_id=str(account["customer_id"]),
                    account_type=account["account_type"],
                    balance=account["balance"]
                )
            )

        return accounts

    def get_by_id(self, account_id):

        account = account_collection.find_one(
            {"_id": ObjectId(account_id)}
        )

        if account is None:
            return None

        return Account(
            _id=str(account["_id"]),
            customer_id=str(account["customer_id"]),
            account_type=account["account_type"],
            balance=account["balance"]
        )

    def get_by_customer_id(self, customer_id):

        accounts = []

        for account in account_collection.find({
            "customer_id": ObjectId(customer_id)
        }):

            accounts.append(
                Account(
                    _id=str(account["_id"]),
                    customer_id=str(account["customer_id"]),
                    account_type=account["account_type"],
                    balance=account["balance"]
                )
            )

        return accounts

    def create(self, account):

        result = account_collection.insert_one({
            "customer_id": ObjectId(account.customer_id),
            "account_type": account.account_type,
            "balance": account.balance
        })

        account._id = str(result.inserted_id)

        return account

    def update(self, account):

        account_collection.update_one(
            {"_id": ObjectId(account._id)},
            {
                "$set": {
                    "account_type": account.account_type,
                    "balance": account.balance
                }
            }
        )

        return account

    def delete(self, account):

        account_collection.delete_one(
            {"_id": ObjectId(account._id)}
        )