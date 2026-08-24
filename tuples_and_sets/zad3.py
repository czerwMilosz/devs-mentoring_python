my_colors = "white blue red orange black purple"
user_colors = "blue orange red green yellow"

set_my_colors = set(my_colors.strip().split())
set_user_colors = set(user_colors.strip().split())

# czesc wspolna
print(set_my_colors & set_user_colors)
print(set_my_colors.intersection(set_user_colors))

# roznica zbiorow
print(set_my_colors - set_user_colors)
print(set_my_colors.difference(set_user_colors))

print(set_user_colors.difference(set_my_colors))