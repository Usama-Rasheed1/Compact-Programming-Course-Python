cars = [
    {'make': 'Samsung', 'model': 7, 'color': 'Blue'},
    {'make': ' Google ', 'model': 216, 'color': 'Black'},
    {'make': 'Mi Max', 'model': 2, 'color': 'Gold'}
]

sorted_cars = sorted(cars, key=lambda x: str(x['make']).strip().lower())

print("Original list of dictionaries:")
print(cars)

print("\nSorted list of dictionaries:")
print(sorted_cars)