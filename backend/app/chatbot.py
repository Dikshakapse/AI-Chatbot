from langgraph import LangGraph
from transformers import pipeline

summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

graph = LangGraph()

@graph.node
def fetch_supplier_info(supplier_id: int):
    from .database import get_db_connection
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM suppliers WHERE id = %s", (supplier_id,))
    result = cursor.fetchone()
    conn.close()
    return result

@graph.node
def summarize_supplier_info(supplier_info: dict):
    summary = summarizer(supplier_info["product_categories"], max_length=50, min_length=25, do_sample=False)
    return summary[0]["summary_text"]