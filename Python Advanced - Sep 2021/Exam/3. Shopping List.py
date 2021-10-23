def shopping_list(budget, **kwargs):
    if budget < 100:
        return "You do not have enough budget."

    bought_products = {}
    for key, value in kwargs.items():
        kwargs[key] = float(kwargs[key][0] * kwargs[key][1])

    for key, value in kwargs.items():
        if len(bought_products) == 5:
            break
        if budget >= value:
            if key not in bought_products.keys():
                bought_products[key] = value
            else:
                bought_products[key] += value
            budget -= value

    for k, v in bought_products.items():
        result = [f"You bought {k} for {v:.2f} leva." for k, v in bought_products.items()]
        return '\n'.join([x for x in result])

# Test Inputs

# print(shopping_list(100, microwave=(70, 2), skirts=(15, 4), coffee=(1.50, 10), ))
# print(shopping_list(20, jeans=(19.99, 1), ))
# print(shopping_list(104,
#                     cola=(1.20, 2),
#                     candies=(0.25, 15),
#                     bread=(1.80, 1),
#                     pie=(10.50, 5),
#                     tomatoes=(4.20, 1),
#                     milk=(2.50, 2),
#                     juice=(2, 3),
#                     eggs=(3, 1),
#                     ))
