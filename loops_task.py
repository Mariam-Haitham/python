items = []

while(True):
    
    item = input('item (enter "done" when finished): ')
    
    if item.lower() == 'done':
        break
    
    price = float(input("price: "))
    quantity = int(input("quantity: "))
    
    items.append({item : [price, quantity]})
    
print("\n-------------------\nreceipt\n-------------------")

total = 0.0

for item in items:
    for key, value in item.items():
        print(value[1], key, "%.3f" %(value[0]*value[1]), "KD")
        total += (value[0]*value[1])
        
print("-------------------")
print("total: %.3f" %total, "KD")