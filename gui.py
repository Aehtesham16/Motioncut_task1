import random
import tkinter as tk
from tkinter import messagebox

class GuessTheNumberGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Guess the Number")

        # Generate the random number
        self.number = random.randint(1, 100)
        self.attempts = 10

        # Create widgets
        self.label = tk.Label(root, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(root)
        self.entry.pack(pady=10)

        self.button = tk.Button(root, text="Submit Guess", command=self.check_guess)
        self.button.pack(pady=10)

        self.result_label = tk.Label(root, text=f"Attempts remaining: {self.attempts}")
        self.result_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
        except ValueError:
            messagebox.showerror("Invalid input", "Please enter a valid number.")
            return

        if guess < 1 or guess > 100:
            messagebox.showerror("Out of range", "Please guess a number between 1 and 100.")
            return

        self.attempts -= 1

        if guess < self.number:
            self.result_label.config(text="Too low! Attempts remaining: " + str(self.attempts))
        elif guess > self.number:
            self.result_label.config(text="Too high! Attempts remaining: " + str(self.attempts))
        else:
            messagebox.showinfo("Congratulations!", f"You guessed the number {self.number} correctly!")
            self.reset_game()
            return

        if self.attempts == 0:
            messagebox.showinfo("Game Over", f"You're out of attempts! The correct number was {self.number}.")
            self.reset_game()

    def reset_game(self):
        self.number = random.randint(1, 100)
        self.attempts = 10
        self.result_label.config(text=f"Attempts remaining: {self.attempts}")
        self.entry.delete(0, tk.END)

# Run the Tkinter GUI game
if __name__ == "__main__":
    root = tk.Tk()
    game = GuessTheNumberGame(root)
    root.mainloop()
