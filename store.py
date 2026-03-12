customer_name = input("Enter customer name: ")

product_name = input("Enter product name: ")

product_price = float(input("Enter product price: "))

product_quantity = int(input("Enter the amount: "))


subtotal = product_price * product_quantity

discount = product_price * (product_quantity * 0.10)

total = subtotal - discount


print(f"Your purchase subtotal is: {subtotal}")
print(f"Your discount is: {discount}")
print(f"Your total is: {total}")

