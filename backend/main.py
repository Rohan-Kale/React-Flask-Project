# CRUD app(Create, Read, Update, Delete)

# Create, localhost:5000/create_contact--> server with endpoint create_contact
"""
Request -> Sends to Server(API)
type: GET
    Access a resource
type: POST
    Create something new
type: PATCH
    Update something
type: DELETE
    Delete something

json: {

}

Front End Sends Request, BackEnd returns a response
Response:
status: 404
json: {

}
"""
from flask import request, jsonify
from config import app, db
from models import Grocery

@app.route("/groceries", methods = ["GET"])  #Decorator specifies where to go to and valid methods
def get_groceries():
    groceries = Grocery.query.all() #gets all contacts that exist in Contact database as python object
    json_groceries = list(map(lambda x: x.to_json(), groceries)) #converts python list to json objects
    return jsonify({"groceries": json_groceries}) #converts groceries into json data

@app.route("/create_grocery", methods = ["POST"])
def create_grocery():
    item_name = request.json.get("itemName")
    amount_needed = request.json.get("amountNeeded")

    if not item_name or not amount_needed:
        return jsonify({"message": "You must include an item name and amount."}), 400    #error message, error code
    
    new_grocery = Grocery(item_name = item_name, amount_needed=amount_needed)
    try:
        db.session.add(new_grocery) #adds new contact to database session(ready to commit like GitHub)
        db.session.commit() # permanently writes into the database
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "Grocery created!"}), 201

@app.route("/update_grocery/<int:item_id>", methods = ["PATCH"])
def update_grocery(item_id):
    grocery = Grocery.query.get(item_id)
    
    if not grocery:
        return jsonify({"message": "Item not found."}), 404
    
    data = request.json #request.json returns a dictionary
    grocery.item_name = data.get("itemName", grocery.item_name) # updates item name
    grocery.amount_needed = data.get("amountNeeded", grocery.amount_needed)

    db.session.commit() # do not need to add anything since item is already committed

    return jsonify({"message": "Item updated!"}), 200

@app.route("/delete_grocery/<int:item_id>", methods = ["DELETE"])
def delete_grocery(item_id):
    grocery = Grocery.query.get(item_id)

    if not grocery:
        return jsonify({"message": "Item not found."}), 404
    
    db.session.delete(grocery)  #deletes the grocery
    db.session.commit()     #commits the changes

    return jsonify({"message": "Item Deleted."}), 200

if __name__ == "__main__":
    #Creates a new database if does not exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
