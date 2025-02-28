-- Use the database
USE supplier_chatbot;

-- Insert sample data into the 'suppliers' table
INSERT INTO suppliers (name, contact_info, product_categories) VALUES
('Supplier A', 'contact@supplierA.com', 'Electronics, Laptops'),
('Supplier B', 'contact@supplierB.com', 'Smartphones, Accessories');

-- Insert sample data into the 'products' table
INSERT INTO products (name, brand, price, category, description, supplier_id) VALUES
('Laptop X', 'Brand X', 1200.00, 'Laptops', 'High-performance laptop', 1),
('Smartphone Y', 'Brand Y', 800.00, 'Smartphones', 'Latest model smartphone', 2);