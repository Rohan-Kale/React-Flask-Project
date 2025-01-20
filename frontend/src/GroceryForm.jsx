import { useState } from "react";

const GroceryForm = ({ existingGrocery = {}, updateCallback}) => {
  const [itemName, setItemName] = useState(existingGrocery.itemName || "") //state for each variable
  const [amountNeeded, setAmountNeeded] = useState(existingGrocery.amountNeeded || "")

  const updating = Object.entries(existingGrocery).length !== 0 //checks if object exists or not(for updating)

  const onSubmit = async (e) => {
    e.preventDefault() // do not refresh page automatically

    const data = {
      itemName,
      amountNeeded,
    }
    
    //if updating go to a different url
    const url = "http://127.0.0.1:5000/" + ( updating ? `update_grocery/${existingGrocery.id}`: "create_grocery")

    const options = {
      method: updating ? "PATCH": "POST",
      headers: {
        "Content-Type": "application/json", // specifying that we are submitting json data
      },
      body: JSON.stringify(data), //converts to JSON string
    };
    const response = await fetch(url, options);
    if (response.status != 201 && response.status != 200) {
      const data = await response.json();
      alert(data.message); //alerts user with error code data
    } else {
      updateCallback()
    }
  };

  return (
    <form onSubmit={onSubmit}>
      <div>
        <label htmlFor="itemName">Item Name:</label>
        <input
          type="text"
          id="itemName"
          value={itemName}
          onChange={(e) => setItemName(e.target.value)}
        />
      </div>
      <div>
        <label htmlFor="amountNeeded">Amount Needed:</label>
        <input
          type="text"
          id="amountNeeded"
          value={amountNeeded}
          onChange={(e) => setAmountNeeded(e.target.value)}
        />
      </div>
      <button type="submit">{updating ? `Update`: "Create"}</button>
    </form>
  );
};

export default GroceryForm;
