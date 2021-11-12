class DataSet:
    liste_dataset = []

    def __init__(self, name, price, profit):
        self.name = name
        self.price = price
        self.profit = profit
        self.liste_dataset.append(self)

    def serialize_dataset(self):
        dataset = {
            "name": self.name,
            "price": float(self.price),
            "profit": float(self.profit),
        }
        return dataset

    def __repr__(self):
        """Return a string representation of this object.

        Returns:
            tuple : (name, price, profit)
        """
        return "{} {} {}".format(self.name, self.price, self.profit)  # O(1)
