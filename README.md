## TESTING 
TESTING AN UPDATE TO A FILE
# ItemizePro

## Overview

This project consists of a frontend and a backend. The frontend is built with React and the backend is built with Python using the FastAPI framework.

## Frontend

The frontend of this application is located in the frontend directory. It is a React application created with Create React App.

To get started with the frontend, navigate to the frontend directory and install the dependencies:

```
cd frontend npm install
```
Then, you can start the development server with:
```
npm start
```

More details can be found in the [frontend README](frontend/README.md).

## Backend

The backend of this application is located in the backend directory. It is a Python application built with FastAPI.

To get started with the backend, navigate to the backend directory and install the dependencies:
```
cd backend pip install -r requirements.txt
```

Then, you can start the development server with:
```
uvicorn main:app --reload
```

More details can be found in the [backend README](backend/README.md).

## Testing

Tests for the frontend can be run with:
```
cd frontend npm test
```
