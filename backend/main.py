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
from models import Contact

@app.route("/contacts", methods = ["GET"])  #Decorator specifies where to go to and valid methods
def get_contacts():
    contacts = Contact.query.all() #gets all contacts that exist in Contact database
    json_contacts = list(map(lambda x: x.to_json(), contacts)) #takes all elements in the list and applied lambda function that creates formatted list
    return jsonify({"contacts": json_contacts}) #jsonify converts into json data

@app.route("/create_contact", methods = ["POST"])
def create_contact():
    first_name = request.json.get("firstName")
    last_name = request.json.get("lastName")
    email = request.json.get("email")

    if not first_name or not last_name or not email:
        return jsonify({"message": "You must include a first name, last name, and email."}), 400    #error message, error code
    
    new_contact = Contact(first_name = first_name, last_name=last_name, email = email)
    try:
        db.session.add(new_contact) #adds new contact to database session(ready to commit like GitHub)
        db.session.commit() # permanently writes into the database
    except Exception as e:
        return jsonify({"message": str(e)}), 400
    
    return jsonify({"message": "User created!"}), 201

@app.route("/update_contact/<int:user_id>", methods = ["PATCH"])
def update_contact(user_id):
    contact = Contact.query.get(user_id)
    
    if not contact:
        return jsonify({"message": "User not found."}), 404
    
    data = request.json #request.json returns a dictionary
    contact.first_name = data.get("firstName", contact.first_name) # updates first name
    contact.last_name = data.get("lastName", contact.last_name)
    contact.email = data.get("email", contact.email)

    db.session.commit() # do not need to add since user is already committed

    return jsonify({"message": "User updated!"}), 200

@app.route("/delete_contact/<user_id>", methods = ["DELETE"])
def delete_contact(user_id):
    contact = Contact.query.get(user_id)

    if not contact:
        return jsonify({"message": "User not found."}), 404
    
    db.session.delete(contact)
    db.session.commit()

    return jsonify({"message": "User Deleted."}), 200

if __name__ == "__main__":
    #Creates a new database if does not exist
    with app.app_context():
        db.create_all()

    app.run(debug=True)
