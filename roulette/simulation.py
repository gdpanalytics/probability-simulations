import random
from copy import deepcopy
import pandas as pd


def game_session(strategy, budget: int, starting_bet: int, n_rounds: int) -> list:
    player = strategy()
    game_session_history = list()
    wins = 0
    losses = 0

    game = 0
    while game < n_rounds:

        # round starts
        game += 1
        player.new_round(budget, starting_bet)
        print(f"Round number {game}")

        while player.in_game:

            # bet
            bet = player.bets()
            print(f"Player bets {bet}")

            # estrazione
            extraction = random.choice(list(range(37)))
            print(f"Extracted: {extraction}")

            # vincita o perdita
            if extraction in player.bet_numbers:
                print(f"Player cash out {bet*(36/len(player.bet_numbers))}")
                player.cash_out(bet * (36 / len(player.bet_numbers)))

            else:
                print("Player pays")
                player.pays()

            print()

        # round ends: update history
        game_session_history.append(deepcopy(player.budget_path))
        if player.result == "Win":
            wins += 1
        if player.result == "Loss":
            losses += 1

    print(f"Wins: {wins}")
    print(f"Losses: {losses}")

    return game_session_history


def plot(series, legend):

    # max series length
    max_len_serie = max([len(serie) for serie in series])

    # other series adapting
    game_stats = [
        serie + [serie[-1]] * (max_len_serie - len(serie)) for serie in series
    ]

    # plot
    df = pd.DataFrame(game_stats)
    df_mean = df.mean().to_frame()
    df_mean.columns = [legend]
    df_mean.plot(xlabel="Bets", ylabel="Budget", title="Plot", legend=True)

    return
