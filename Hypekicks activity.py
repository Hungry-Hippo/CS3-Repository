cart_total = float(input("Enter your cart total: "))
shipping_speed = input("Enter shipping speed (express/standard/overnight): ")
def calculate_checkout(cart_total, shipping_speed):
    if shipping_speed == "express":
        shipping = 20
    elif shipping_speed == "standard":
        shipping = 10
    elif shipping_speed == "overnight":
        shipping = 35
    elif shipping_speed == "free":
        shipping = 0
    else:
        shipping = 0
    return cart_total + shipping

if cart_total >= 100:
    shipping_speed = "free"
total = calculate_checkout(cart_total, shipping_speed)
print(total)