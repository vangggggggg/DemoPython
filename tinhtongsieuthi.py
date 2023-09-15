name1 = 'orange'
price1 = 150
unit1 = 2

name2 = 'grape'
price2 = 130
unit2 = 23

tprice = price1 + price2
discount=15
fprice=tprice-discount

#quang trong
myformat = "{:<14}{:<25}{:<5}{}"
print(myformat.format('S.no', 'Product', 'Unit', 'Price'))
print(myformat.format('0', name1, unit1, price1))
print(myformat.format('1', name2, unit2, price2))
print(myformat.format('Discount: ', '', '', discount))
print(myformat.format('Total: ', '', '', fprice))