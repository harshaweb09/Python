#A function that performs a simple bank withdrawal with balance validation

def withdrawal(balance_amount,withdrawal_amount):
  if withdrawal_amount <= 0 :
    print("Invalid withdrawal amount")
  elif withdrawal_amount > balance_amount :
    print("Insuffient funds in your account")
  else : 
    balance_amount -= withdrawal_amount
    print("Withdrawal successful of amount ",withdrawal_amount , " and balance is " ,balance_amount)

withdrawal(10000,545466464)