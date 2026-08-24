LOVERS = {1: 'Rahima', 2: 'Alishba', 3: 'Fizza'}
FRIENDS = {4: 'Bilal', 5: 'Arbab', 6: 'Shahzor'}
# method 1
new_dict = LOVERS | FRIENDS
print(new_dict)

#method 2
new_dict_v2 = {**LOVERS, **FRIENDS}
print(new_dict_v2)

#method 3
losers = LOVERS.copy()
enemies = FRIENDS.copy()
losers.update(enemies)
print(losers)

#method 4
losers_v2 = LOVERS.copy()
for key, value in enemies.items():
    losers_v2[key] = value

print(losers_v2)
