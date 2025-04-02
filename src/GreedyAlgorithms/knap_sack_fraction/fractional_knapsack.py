import math

def fractional_knapsack(capacity, items):
    # Sort items by value/weight ratio in descending order
    items.sort(key=lambda x: x[1] / x[0], reverse=True)

    total_value = 0.0  # Total value of the knapsack
    for weight, value in items:
        if capacity >= weight:
            # Take the full item
            total_value += value
            capacity -= weight
        else:
            # Take the fractional part
            total_value += (capacity / weight) * value
            break  # Knapsack is full

    return math.ceil(total_value)

