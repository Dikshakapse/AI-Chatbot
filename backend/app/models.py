from pydantic import BaseModel

class Supplier(BaseModel):
    id: int
    name: str
    contact_info: str
    product_categories: str

class Product(BaseModel):
    id: int
    name: str
    brand: str
    price: float
    category: str
    description: str
    supplier_id: int