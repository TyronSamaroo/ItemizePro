import React, { useState, useEffect } from 'react';

function ItemList() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    const fetchItems = async () => {
      try {
        const response = await fetch('http://localhost:8000/items/');
        const data = await response.json();
        if (Array.isArray(data)) {
          setItems(data);
        } else {
          console.error('Data fetched is not an array:', data);
        }
      } catch (error) {
        console.error('Error fetching items:', error);
      }
    };

    fetchItems();
  }, []);

  return (
    <div>
      <h1>Item List</h1>
      {items.map(item => (
        <div key={item.id}>{item.name}</div>  // Adjust according to your data structure
      ))}
    </div>
  );
}

export default ItemList;