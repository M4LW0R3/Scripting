my_foods = ['pizza', 'falafel', 'carrot cake']
friend_food = my_foods [:]

my_foods.append('cannoli')

print("My favourite foods are:")
print(my_foods)
friend_food.append('icecream')
print("\nMy friends favourite foods are:")
print(friend_food)

for food in my_foods:
    print(food)
for feed in friend_food:
    print(feed)