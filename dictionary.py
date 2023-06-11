contactList = {'Freida':'+91 22411 95075','Aliza':'+92 062 728 9441','Shopna':'+880 123 622','Pavitra':'+94 431 882'}
print(contactList['Freida'])
print(contactList.get('Pavitra'))
contactList['Roshni'] = '+91 45781 77814'
print(contactList['Roshni'])
countries = dict(ind = 'India',lk = 'Sri Lanka')
print(countries)
del contactList['Aliza']
print(contactList)
print(contactList.pop('Aliza','Contact not found'))
contactList.update({'Freida':'+91 55512 71632'})
print(contactList.get('Freida'))
print(contactList.values())
