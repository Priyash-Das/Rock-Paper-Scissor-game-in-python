# ✊🖐✌ Rock Paper Scissors Game (Python Console Version)

## 📌 About the Game

This is a simple **Rock, Paper, Scissors** game built in Python for the console. The player plays against the computer, which randomly selects one of the three choices. The first non-draw result (win or loss) ends the game and displays the outcome.

There are two versions of this game:
- `code1`: Uses a **mathematical approach** based on the difference `(computer - you)` to determine the winner.
- `code2`: Uses standard **`if-elif` conditions** to check all possible win/loss combinations directly.

This project is great for beginners who want to learn about:
- Basic Python syntax
- Dictionaries
- Random number generation
- User input handling
- Game logic using control flow

---

## ⚙️ How the Game Works (As Coded)

### Common Setup
- Inputs are accepted in many formats like `rock`, `ROCK`, `R`, `r`, etc.
- Internally:
  - `Rock` is represented as `1`
  - `Paper` as `-1`
  - `Scissors` as `0`
- A `youDict` converts user input to numbers.
- A `reverseDict` is used to convert numbers back to strings for printing.

🎮 Enjoy testing your logic and luck in this classic Python console challenge!
