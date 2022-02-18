planetas = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Neptune']
user_planet = input('Please enter the name of the planet (with a capital letter to start)')
planeta_index = planetas.index(user_planet)
print('Here are the planets closer than ' + user_planet)
print(planetas[0:planeta_index])
print('Here are the planets further than ' + user_planet)
print(planetas[planeta_index + 1:])