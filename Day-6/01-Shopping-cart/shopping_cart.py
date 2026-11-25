#Build a command-line Shopping Cart application using Python.

product_catalogue = [
  {"product_id":"P101","product_name":"Keyboard","price":800},
  {"product_id":"P102","product_name":"Mouse","price":500},
  {"product_id":"P103","product_name":"Monitor","price":8000},
  {"product_id":"P104","product_name":"Headphones","price":1200},
  {"product_id":"P105","product_name":"USB Cable","price":200}
  ] 

def view_products():
  print("======== AVAILABLE PRODUCTS ========")
  print(f"\n{'Product Id':<12} {'Product Name':<16} {'Price':>6}\n")
  for product in product_catalogue:
    print(f"{product['product_id']:<12} {product['product_name']:<16} {product['price']:>6}")