import collections


dict1 = {'day1': 'Mon', 'day2': 'Tue'}
dict2 = {'day3': 'Wed', 'day1': 'Thu'}

chained = collections.ChainMap(dict1, dict2)

print(chained)
new_ = chained.maps
print(new_)

#get the keys
keys_ = list(chained.keys())
print(keys_)
values_ = list(chained.values())
print(values_)

items_ = list(chained.items())
print(items_)

for key, value in chained.items():
    print(key, value)

#check for an item in chained
print('day1' in chained.keys() )
print('Mon' in chained.values() )