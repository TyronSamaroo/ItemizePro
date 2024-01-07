const BASE_URL = 'http://localhost:8000'; // Your FastAPI server URL

export const fetchItem = async (itemId) => {
  try {
    const response = await fetch(`${BASE_URL}/items/${itemId}`);
    return await response.json();
  } catch (error) {
    console.error("Error fetching item:", error);
  }
};
