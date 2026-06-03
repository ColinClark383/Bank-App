from bson import ObjectId

class Customer:

    def __init__(
        self,
        _id=None,
        name="",
        email=""
    ):
        self._id = str(_id) if _id else None
        self.name = name
        self.email = email