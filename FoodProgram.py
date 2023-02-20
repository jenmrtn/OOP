import FoodClass as fc

# this dictionary represents transactions. The key of the dictionary is the transaction identifier.
# The Value of the dictionary is a list. The elements in each list are -
# ['Date', 'Name of item', 'Cost', 'customerid' ]

dict = {'trans1':['2/15/2023','The Lone Patty',17,569],
                'trans2':['2/15/2023','The Octobreakfast',18,569],
                'trans3':['2/15/2023','The Octoveg',16,570],
                'trans4':['2/15/2023','The Octoburger',20,570],
}

discount=.2
#customer= fc.Customer(570, 'Danni Sellyar', '97 Mitchell Way Hewitt Texas 76712', 'dsellyarft@gmpg.org', '254-555-9362', False)
customer= fc.Customer(569, 'Aubree Himsworth', '1172 Moulton Hill Waco Texas Waco Texas 76710', 'ahimsworthfs@listmanage.com', '254-555-2273', True)
print('Customer Name:', customer.get_name())
print('Customer Phone:', customer.get_phone())
acc=0
for i in dict.values():
    if i[3]==customer.get_id():
        transaction=fc.Transaction(i[0],i[1],i[2],i[3])
        acc+= transaction.get_cost()
        print(f'Order Item: {transaction.get_item()} Price:' ' ${:.2f}'.format(transaction.get_cost()))
print('Total Cost:', '${:.2f}'.format(acc))
if customer.get_status()== True:
    discamnt=float(acc)*discount
    print('Member Discount:','${:.2f}'.format(discamnt))
    Tcost='${:.2f}'.format(acc-discamnt)
    discamnt='${:.2f}'.format(discamnt)
    print(f'Total Cost after discount: {Tcost}')
else:
    print('Total Cost:','${:.2f}'.format(acc))


