from simulation import game_session, plot
from strategies import Fivexfive, Fibonacci


# parameters
budget = 100
starting_bet = 1
n_rounds = 1000

# simulation 5X5
simulation_5x5 = game_session(
    strategy=Fivexfive, budget=budget, starting_bet=starting_bet, n_rounds=n_rounds
)

plot(simulation_5x5, "5x5")

# simulation Fibonacci
simulation_fibonacci = game_session(
    strategy=Fibonacci, budget=budget, starting_bet=starting_bet, n_rounds=n_rounds
)

plot(simulation_fibonacci, "Fibonacci")
