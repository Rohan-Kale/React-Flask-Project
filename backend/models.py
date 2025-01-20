from config import db

class Grocery(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    item_name = db.Column(db.String(80), unique = False, nullable = False)
    amount_needed = db.Column(db.String(80), unique = False, nullable = False)

    def to_json(self):
        return {
            "id": self.id,
            "itemName": self.item_name, 
            "amountNeeded": self.amount_needed,
        }