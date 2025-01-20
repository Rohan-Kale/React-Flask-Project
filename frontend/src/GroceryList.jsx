import React from "react"

const GroceryList = ({groceries, updateGrocery, updateCallback}) => {
    const onDelete = async (id) => {
        try {
            const options = {
                method: "DELETE"
            }
            const response = await fetch(`http://127.0.0.1:5000/delete_grocery/${id}`, options)
            if (response.status == 200) {
                updateCallback()
            }
            else {
                console.error("FAILED TO DELETE")
            }
        }
        catch (error) {
            alert(error)
        }
    }
    return <div>
        <h2>Grocery List</h2>
        <table>
            <thead>
                <tr>
                    <th>Item Name</th>
                    <th>Amount Needed</th>
                    <th>Actions</th>
                </tr>
            </thead>
            <tbody>
                {groceries.map((grocery) => (
                    <tr key = {grocery.id}>
                        <td>{grocery.itemName}</td>
                        <td>{grocery.amountNeeded}</td>
                        <td>
                            <button onClick = {() => updateGrocery(grocery)}>Update</button>
                            <button onClick = {() => onDelete(grocery.id)}>Delete</button>
                        </td>
                    </tr>
                ))}
            </tbody>
        </table>
    </div>
}

export default GroceryList
