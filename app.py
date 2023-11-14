class Game:
    def __init__(self):
        self.player_score = 0
        self.opponent_score = 0
        self.player_move = ""
        self.opponent_move = ""
        self.moves = ["rock", "paper", "scissors"]

    def start(self):
        print("Welcome to Rock, Paper, Scissors!")
        self.player_move = input("What's your move? ").lower()
        self.opponent_move = self.moves[0]
        print(f"Opponent move: {self.opponent_move}")
        self.check_result()

    def check_result(self):
        if self.player_move == self.opponent_move:
            print("It's a tie!")
        elif self.player_move == "rock":
            if self.opponent_move == "scissors":
                print("You win!")
                self.player_score += 1
            else:
                print("You lose!")
                self.opponent_score += 1
        elif self.player_move == "paper":
            if self.opponent_move == "rock":
                print("You win!")
                self.player_score += 1
            else:
                print("You lose!")
                self.opponent_score += 1
        elif self.player_move == "scissors":
            if self.opponent_move == "paper":
                print("You win!")
                self.player_score += 1
            else:
                print("You lose!")
                self.opponent_score += 1
        else:
            print("Invalid move!")

        self.end()

    def end(self):
        print(f"Player score: {self.player_score}")
        print(f"Opponent score: {self.opponent_score}")

        play_again = input("Play again? (y/n) ").lower()

        if play_again == "y":
            self.start()
        else:
            print("Thanks for playing!")

game = Game()
game.start()