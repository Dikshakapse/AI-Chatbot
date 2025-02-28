# AI-Powered Chatbot for Supplier and Product Information

## 📝 Description
This project is an AI-powered chatbot that allows users to query a product and supplier database using natural language. The chatbot interacts with an open-source LLM and utilizes the LangGraph framework for agent workflows to fetch relevant information from a MySQL database and summarize the data using an LLM.

## 🚀 Features
- **Natural Language Queries**: Users can ask questions like:
  - "Show me all products under Brand X."
  - "Which suppliers provide laptops?"
  - "Give me details of product ABC."
- **Database Integration**: Fetches data from a MySQL database.
- **LLM Summarization**: Uses Hugging Face's BART model for summarization.
- **Responsive UI**: Built with React and Material-UI.

## 🛠️ Technologies Used
- **Frontend**: React, Material-UI, Axios
- **Backend**: Python, FastAPI, LangGraph, Hugging Face Transformers
- **Database**: MySQL
- ## 🚀 Getting Started

### Prerequisites
- Node.js (for frontend)
- Python 3.8+ (for backend)
- MySQL

### Installation
1. Clone the repository:
   git clone https://github.com/your-username/ai-chatbot-project.git
   cd ai-chatbot-project
Set up the backend:

cd backend
pip install -r requirements.txt
Set up the frontend:

cd ../frontend
npm install
Set up the database:

Import the SQL scripts (init.sql and sample_data.sql) into your MySQL database.

Running the Project
Start the backend:
cd backend
uvicorn app.main:app --reload
Start the frontend:
cd frontend
npm start
Open your browser and go to:
http://localhost:3000
