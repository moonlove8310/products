products = []
while True:
    name = input('please input the thing you bought: ')
    if name == 'q':
        break
    price = input('please input the price of the thing: ')
    # i = []
    # i.append(name)
    # i.append(price)
    # i = [name, price]
    # products.append(i)
    products.append([name, price])
# print(products)

for p in products:
    # print(p)
    # print(p[0])
    print('the price of', p[0], 'is', p[1])