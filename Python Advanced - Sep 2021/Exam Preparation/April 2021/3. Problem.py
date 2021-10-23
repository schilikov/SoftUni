def flights(*args, daily_flights={}):
    for idx in range(0, len(args), 2):
        if args[idx] == "Finish":
            return daily_flights
        if args[idx] not in daily_flights:
            daily_flights[args[idx]] = int(args[idx + 1])
        else:
            daily_flights[args[idx]] += int(args[idx + 1])

    return daily_flights

# Test Codes

# print(flights('Vienna', 256, 'Vienna', 26, 'Morocco', 98, 'Paris', 115, 'Finish', 'Paris', 15))
# print(flights('London', 0, 'New York', 9, 'Aberdeen', 215, 'Sydney', 2, 'New York', 300, 'Nice', 0, 'Finish'))
# print(flights('Finish', 'New York', 90, 'Aberdeen', 300, 'Sydney', 0))