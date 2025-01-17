print(bool('Kodnest')) #True
# print(int('Kod')) #error
print(int('12')) # 12 ---> IMP Str(int) ---> Int
# print(float('Stri')) #error
print(float('12.33')) # 12.33
print(bool('')) #false
print(bool(0)) #false
print(bool('str')) # True
# print(int('12.66')) # error
print(int(12.33)) # 12

# Taking float value from user and converting it into int
value = int(float(input('Enter the float Value')))
print(value, type(value)) # int 

original_price = float(input().strip())
discount_percentage = float(input().strip())

discount_amount = (original_price * discount_percentage) / 100
final_price = original_price - discount_amount

print(f"The final price of 
      the item after a {int(discount_percentage)}% discount is: {final_price}")