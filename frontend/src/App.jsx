import { useState, useEffect } from "react";
import GroceryList from "./GroceryList";
import GroceryForm from "./GroceryForm";
import "./App.css";

function App() {
  const [groceries, setGroceries] = useState([]);
  const [isModalOpen, setIsModalOpen] = useState(false);
  const [currentGrocery, setCurrentGrocery] = useState({});
  useEffect(() => {
    fetchGroceries();
  }, []);

  const fetchGroceries = async () => {
    const response = await fetch("http://127.0.0.1:5000/groceries"); //sends request to backend
    const data = await response.json()  //waits for json data
    setGroceries(data.groceries)  //sets groceries in the state
  };

  const closeModal = () => {
    setIsModalOpen(false);
    setCurrentGrocery({})
  };

  const openCreateModal = () => {
    if (!isModalOpen) setIsModalOpen(true);
    setCurrentGrocery({})
  };

  const openEditModal = (grocery) => {
    if (isModalOpen) {
      return
    }
    setCurrentGrocery(grocery)
    setIsModalOpen(true)
  }

  const onUpdate = () => {
    closeModal()
    fetchGroceries()
  }
  return (
    <>
      <GroceryList groceries={groceries} updateGrocery = {openEditModal} updateCallback={onUpdate}/>
      <button onClick={openCreateModal}>Create New Item</button>
      {isModalOpen && (
        <div className="modal">
          <div className="modal-content">
            <span className="close" onClick={closeModal}>
              &times;
            </span>
            <GroceryForm existingGrocery={currentGrocery} updateCallback={onUpdate}/>
          </div>
        </div>
      )}
    </>
  );
}
export default App;
