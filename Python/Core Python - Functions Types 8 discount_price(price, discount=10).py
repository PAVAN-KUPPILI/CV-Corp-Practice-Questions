def discount_price(price,discount=10):
    return price*(1-(discount/100))
print(discount_price(100))
print(discount_price(120,55))