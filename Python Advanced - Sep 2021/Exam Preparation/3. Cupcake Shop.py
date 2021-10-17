def stock_availability(inventory, command, *args):
    if command == "delivery":
        return inventory + list(args)

    if not args:
        return inventory[1:]

    if isinstance(args[0], int):
        count = int(args[0])
        return inventory[count:]
    else:
        for x in args:
            while x in inventory:
                inventory.remove(x)
        return inventory

# Test Codes

# print(stock_availability(["choco", "vanilla", "banana"], "delivery", "caramel", "berry"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "delivery", "cookie","banana"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", 3))
# print(stock_availability(["chocolate", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["cookie", "chocolate", "banana"], "sell", "chocolate"))
# print(stock_availability(["chocolate", "vanilla", "banana"], "sell", "cookie"))