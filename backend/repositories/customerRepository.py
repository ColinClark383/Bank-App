from database import customer_collection
from models.customer import Customer

from bson import ObjectId


class CustomerRepository:

    def get_all(self):

        customers = []

        for customer in customer_collection.find():

            customers.append(
                Customer(
                    _id=str(customer["_id"]),
                    name=customer["name"],
                    email=customer["email"]
                )
            )

        return customers

    def get_by_id(self, customer_id):

        customer = customer_collection.find_one(
            {"_id": ObjectId(customer_id)}
        )

        if customer is None:
            return None

        return Customer(
            _id=customer["_id"],
            name=customer["name"],
            email=customer["email"]
        )

    def get_by_name(self, name):

        customers = []

        results = customer_collection.find(
            {
                "name": {
                    "$regex": f"^{name}$",
                    "$options": "i"
                }
            }
        )

        for customer in results:
            customers.append(
                Customer(
                    _id=customer["_id"],
                    name=customer["name"],
                    email=customer["email"]
                )
            )

        return customers

    def create(self, customer):

        customer_collection.insert_one(
            {
                "name": customer.name,
                "email": customer.email,
            }
        )

    def update(self, customer):

        customer_collection.update_one(
            {"_id": ObjectId(customer._id)},
            {
                "$set": {
                    "name": customer.name,
                    "email": customer.email
                }
            }
        )

    def delete(self, customer):

        customer_collection.delete_one(
            {"_id": ObjectId(customer._id)}
        )