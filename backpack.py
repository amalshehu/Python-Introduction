backpack = {
    'money': 5000,
    'pouch': ['Chocolates', 'UNO cards', 'Bey Blade'],
    'instrument_box': ['Sharpener', 'Pen', 'Compass', 'Scale', 'Blade']
}
backpack['pouch'].sort()
backpack['pocket'] = ['Lolipop', 'Mini Boomerang', 'Sticky notes']
backpack['instrument_box'].append('Glue')
backpack['instrument_box'].remove('Blade')
backpack['money'] = 5500

print("########## My Backpack ##########")
print "Money:", backpack['money']
print "Items in my Pouch:", backpack['pouch']
print "Instrument box:", backpack['instrument_box']
print "My Pocket:", backpack['pocket']
