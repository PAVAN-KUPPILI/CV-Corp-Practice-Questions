def product(price):
    def discount():
        return price*(1-(10/100))
    return discount
result= product(150)
print(result())