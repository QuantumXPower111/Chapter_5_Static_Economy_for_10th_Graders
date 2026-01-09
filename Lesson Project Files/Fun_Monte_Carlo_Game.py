import numpy as np

def monte_carlo_game(S=100, K=105, simulations=100):
    outcomes = S * np.exp(np.random.normal(0.05 - 0.5*0.2**2, 0.2, simulations))
    payoffs = np.maximum(outcomes - K, 0)
    price = np.mean(payoffs) * np.exp(-0.05)
    return price

print(monte_carlo_game())  # Varies, around 8