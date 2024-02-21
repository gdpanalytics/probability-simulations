class Fivexfive:
    def __init__(self):

        self.lower_bound = 0
        self.bet_numbers = list(range(1, 31))

    def bets(self):
        bet = min(self.bet * 5, self.budget)
        self.budget -= bet
        self.budget_path.append(self.budget)
        return bet

    def cash_out(self, win):
        self.budget += win
        self.budget_path.append(self.budget)
        self.bet = self.starting_bet
        if self.budget >= self.upper_bound:
            self.in_game = False
            self.result = "Win"
            print("I won!")

    def pays(self):
        self.bet *= 5
        if self.budget == self.lower_bound:
            self.in_game = False
            self.result = "Loss"
            print("I lost!")

    def new_round(self, budget, starting_bet):
        self.budget = budget
        self.starting_bet = starting_bet
        self.bet = starting_bet
        self.upper_bound = 2 * budget
        self.in_game = True
        self.budget_path = list()


class Fibonacci:
    def __init__(self):

        self.lower_bound = 0
        self.bet_numbers = list(range(1, 13))

    def bets(self):
        bet = min(self.bet, self.budget)
        self.budget -= bet
        self.budget_path.append(self.budget)
        return bet

    def cash_out(self, win):
        self.budget += win
        self.budget_path.append(self.budget)
        self.bet = self.starting_bet
        self.fibonacci_series = [0, 1]
        if self.budget >= self.upper_bound:
            self.in_game = False
            self.result = "Win"
            print("I won!")

    def pays(self):
        self.fibonacci_series.append(
            self.fibonacci_series[-1] + self.fibonacci_series[-2]
        )
        self.bet = self.starting_bet * self.fibonacci_series[-1]
        if self.budget == self.lower_bound:
            self.in_game = False
            self.result = "Loss"
            print("I lost!")

    def new_round(self, budget, starting_bet):
        self.budget = budget
        self.starting_bet = starting_bet
        self.bet = starting_bet
        self.upper_bound = 2 * budget
        self.in_game = True
        self.budget_path = list()
        self.fibonacci_series = [0, 1]
