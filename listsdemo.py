"""
Data type to store more than one value in one variable name
List items are in brackets ,separated with "," [ 1,2,3,]
"""
cars = ["bmw", "honda","audi"]
empty_list =[]
print(cars)
print(empty_list)

print(cars[0])

print(cars[2])

num_list =[1, 2, 3]
sum_num = num_list[0] + num_list[1]

print(sum_num)

more_cars =["HellCat","Toyota","Kia"]

print(more_cars[1])

# Will change the value of Toyota to charger in the list
more_cars[1] = "Charger"
print(more_cars[1])
print(more_cars)