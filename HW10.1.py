goods = {'Apple':[4.5,10],
         'Orange':[6.2,5],
         'Pinapple':[10.0,1],
         'Mango':[7.5,2],
         'Banana': [3.8,10]}

for key, value in goods.items():
    print(key, '-', value[0], '-',value[1])
cost = 0
while True:
    good = input('What? ')
    if good == 'n' or good not in goods.keys():
        break
    qty = int(input('How many? '))
    if qty > goods[good][1]:
        print('We dont have so much')
        continue
    cost += goods[good][0]*qty
    goods[good][1] -= qty
print('Price:', cost)
print('__________________________________________')
for key, value in goods.items():
    print(key, '-', value[0], '-', value[1])
