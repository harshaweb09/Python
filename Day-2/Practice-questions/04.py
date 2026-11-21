#A function that calculates the final price after a discount

def calc_final_price(price,discount_percentage):
  discount_amount = price * (discount_percentage/100)
  final_price = price - discount_amount
  return final_price

print(calc_final_price(250,15))
  