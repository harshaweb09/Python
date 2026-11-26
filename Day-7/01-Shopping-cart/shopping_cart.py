#Build a command-line Shopping Cart application using Python.

product_catalogue = [
  {"product_id":"P101","product_name":"Keyboard","price":800},
  {"product_id":"P102","product_name":"Mouse","price":500},
  {"product_id":"P103","product_name":"Monitor","price":8000},
  {"product_id":"P104","product_name":"Headphones","price":1200},
  {"product_id":"P105","product_name":"USB Cable","price":200}
  ] 

cart = {}

def view_products():
  print("======== AVAILABLE PRODUCTS ========")
  print(f"\n{'Product Id':<12} {'Product Name':<16} {'Price':>6}\n")
  for product in product_catalogue:
    print(f"{product['product_id']:<12} {product['product_name']:<16} {product['price']:>6}")

def display_main_menu():
  print("\n========== SHOPPING CART ==========\n")
  print("1. View Products")
  print("2. Add Product to Cart")
  print("3. View Cart")
  print("4. Update Product Quantity")
  print("5. Remove Product from Cart")
  print("6. Checkout")
  print("7. Exit\n")

def get_menu_choice():
  while True:
    try:
      choice = int(input("Choose an option : "))
      if 1 <= choice <= 7 :
        return choice
      else:
        print("\nInvalid choice! Please select an option from 1 to 7.\n")
    except ValueError:
      print("\nInvalid input! Please enter a number from 1 to 7.\n" )

def check_product_availability(product_id):
  for product in product_catalogue:
    if product['product_id'] == product_id:
      return True
  return False

def add_to_cart():
  product_id = input("Enter Product ID: ")
  if check_product_availability(product_id):
    while True:
      try:
        quantity = int(input("Enter Quantity: "))
        if quantity > 0:
          if product_id in cart:
            cart[product_id] += quantity
          else:
            cart[product_id] = quantity
          print("\nGreat choice! Item added to your cart.\n\nReady to checkout or keep shopping?")
          break
        else:
          print("Enter quantity greater than 0")
      except ValueError:
        print("Enter a positive valid quantity ")
  else:
    print("\nProduct not found! ,for knowing avaliable products choose option 1\n")

def view_cart():
  if not cart:
    print("\nYour cart is empty! let’s find something great or useful to put in it!\n")
  else:
    print("\n========== YOUR CART ==========\n")
    print(
      f"{'Product ID':<12} "
      f"{'Product Name':<14} "
      f"{'Price':>8} "
      f"{'Quantity':>10} "
      f"{'Subtotal':>12} "
      "\n")
    total = 0
    for product_id in cart:
      for product in product_catalogue:
        if product_id == product['product_id']:
          print(
            f"{product_id:<12} "
            f"{product['product_name']:<14} "
            f"{product['price']:>8} "
            f"{cart[product_id]:^10} "
            f"{product['price']*cart[product_id]:>12} "
            "\n")
          total += product['price']*cart[product_id]
    print('-'*50)
    print(f"\nTotal : {total}\n")

while True:
  display_main_menu()
  choice = get_menu_choice()
  if choice == 1:
    view_products()
  elif choice == 2:
    add_to_cart()
  elif choice == 3:
    view_cart()
  elif choice == 4:
    print("\nFeature coming soon!\n")
  elif choice == 5:
    print("\nFeature coming soon!\n")
  elif choice == 6:
    print("\nFeature coming soon!\n")
  elif choice == 7:
    print("\nThanks for shopping!\n")
    break

