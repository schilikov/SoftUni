# Add/remove cars to/from the parking lot and then print them
num = int(input())

cars = set()

for _ in range(num):
    command, number = input().split(", ")
    if command == "IN":
        cars.add(number)
    else:
        cars.remove(number)

if cars:
    [print(car) for car in cars]
else:
    print("Parking Lot is Empty")