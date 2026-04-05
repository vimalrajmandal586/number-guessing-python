# 🎯 Number Guessing Game

A fun command-line game where the **computer picks a secret number** and you have to guess it.  
The game gives you hints after every guess — telling you if the answer is higher or lower.  
This is my **second Python project** built while self-learning Python.

---

## 🎮 How to Play

1. The computer secretly picks a random number between **1 and 100**
2. You type your guess
3. The game tells you: **Too High ↑** or **Too Low ↓**
4. Keep guessing until you find the correct number
5. Your **total number of attempts** is shown at the end
6. Try to beat your own record — the fewer guesses, the better!

---

## ▶️ How to Run

1. Make sure Python is installed on your computer
2. Download or clone this repository
3. Open terminal / command prompt
4. Run the file:

```bash
python "NUMBER GUESSING.py"
```

---

## 💡 What I Learned Building This

- Using the **`random` module** to generate random numbers
- **While loops** — keeping the game running until the player wins
- **Comparison operators** — checking if guess is higher or lower
- **Counting attempts** — tracking how many guesses the player took
- Giving the user **feedback** after every action — a key UX concept

---

## 🔧 What I Plan to Improve Next

- Add **difficulty levels** — Easy (1-50), Medium (1-100), Hard (1-500)
- Add a **maximum attempts limit** — game over if you exceed it
- Show a **hint** if the player is stuck after 5 wrong guesses
- Keep a **leaderboard** of best scores saved to a file
- Add a **play again** option after each round

---

## 🧠 Interesting Fact About This Game

The most efficient strategy to win this game is called **Binary Search** —  
always guess the middle of the remaining range.  
For 1–100, that means starting at 50 — then 25 or 75 depending on the hint.  
This guarantees winning in **at most 7 guesses** for any number from 1 to 100.  
That's the same logic computers use to search through sorted data!

---

## 🛠️ Built With

- Python 3
- `random` module (built into Python — no installation needed)

---

## 👨‍💻 About Me

I am a student from **Mumbai, India** — self-learning Python while preparing for the Scholarship 2027.  
This project is part of my journey to build real coding skills from scratch.
