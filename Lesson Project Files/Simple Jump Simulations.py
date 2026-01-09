import numpy as np
import matplotlib.pyplot as plt

def simulate_stock_with_jump(start=100, days=20, jump_chance=0.2):
    prices = [start]
    for _ in range(days):
        change = np.random.normal(0, 5)  # Normal change
        if np.random.random() < jump_chance:  # Possible jump
            change -= 10  # Big drop
        prices.append(prices[-1] + change)
    plt.plot(prices)
    plt.title('Stock with Jumps')
    plt.show()

simulate_stock_with_jump()