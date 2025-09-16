# 1. List of toppings
toppings = ["pepperoni", "pineapple", "cheese", "sausage", "olives", "anchovies", "mushrooms"]

# 2. List of prices
prices = [2, 6, 1, 3, 2, 7, 2]

# 3. Count number of $2 slices
num_two_dollar_slices = prices.count(2)
print("Number of $2 slices:", num_two_dollar_slices)

# 4. Find number of pizzas
num_pizzas = len(toppings)

# 5. Print number of pizzas
print(f"We sell {num_pizzas} different kinds of pizza!")

# 6. Create two-dimensional list [price, topping]
pizza_and_prices = [
    [2, "pepperoni"],
    [6, "pineapple"],
    [1, "cheese"],
    [3, "sausage"],
    [2, "olives"],
    [7, "anchovies"],
    [2, "mushrooms"]
]

# 7. Print pizza_and_prices
print("\nPizza and Prices (unsorted):")
print(pizza_and_prices)

# 8. Sort pizza_and_prices by price (ascending)
pizza_and_prices.sort()

# 9. Get cheapest pizza
cheapest_pizza = pizza_and_prices[0]

# 10. Get priciest pizza
priciest_pizza = pizza_and_prices[-1]

# 11. Remove most expensive pizza (anchovies)
pizza_and_prices.pop()

# 12. Add new topping "peppers" priced at 2.5
pizza_and_prices.append([2.5, "peppers"])

# Re-sort after adding new topping
pizza_and_prices.sort()

# 13. Slice the three cheapest pizzas
three_cheapest = pizza_and_prices[:3]

# 14. Print three cheapest pizzas
print("\nThree cheapest pizzas:")
print(three_cheapest)
