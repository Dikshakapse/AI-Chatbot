from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import mysql.connector
from transformers import pipeline
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

# Define the Pydantic model for the request payload
class QueryRequest(BaseModel):
    query: str
app = FastAPI()

# Database connection
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Diksha@404",  # Replace with your MySQL password
        database="supplier_chatbot"
    )

# LLM summarization pipeline
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods
    allow_headers=["*"],  # Allows all headers
)
# Custom workflow (replaces LangGraph)
def fetch_supplier_info(supplier_id: int):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM suppliers WHERE id = %s", (supplier_id,))
    result = cursor.fetchone()
    conn.close()
    return result

def summarize_supplier_info(supplier_info: dict):
    return f"Supplier {supplier_info['name']} provides {supplier_info['product_categories']}."
@app.post("/query")
async def query(request: QueryRequest):
    print("Received query:", request.query) 
    user_query = request.query  
    if "supplier" in user_query.lower():
        supplier_id = 1  
        supplier_info = fetch_supplier_info(supplier_id)
        print("Supplier info:", supplier_info)  
        summary = summarize_supplier_info(supplier_info)  
        return {"response": summary}
    elif "product" in user_query.lower():
        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products WHERE name LIKE %s", (f"%{user_query}%",)) 
        result = cursor.fetchall()
        conn.close()
        print("Product info:", result)  
        return {"response": result}
    else:
        return {"response": "Query not supported yet."}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)