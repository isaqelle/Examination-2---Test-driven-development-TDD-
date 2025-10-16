# 🐷 Pig Dice Game

A terminal-based implementation of the classic **Pig Dice Game**, built in Python.  
This project was developed as part of the *Methods for Sustainable Programming (DA214A)* course at Kristianstad University.  
The game allows a human player to compete against a computer opponent with adjustable difficulty levels (Easy or Hard).

---

## 🎲 About the Game

PIG is a simple dice game with two players.  
Each player repeatedly rolls a die until either a **1** is rolled or the player decides to **hold**.  
The player who first scores **100 or more points** wins.

### 📖 Game Rules

- The objective is to be the first player to reach **100 points**.  
- On each turn, the player rolls a six-sided die.  
- If the player rolls a **1**, their turn ends and they receive **no points**.  
- If the player rolls any other number, they can choose to **roll again** or **hold** to keep their current round score.  
- If the player chooses to hold, their round score is added to their total score.  

### 💻 Computer Difficulty

If playing against the computer:  
- The player can select a difficulty level that affects the computer’s decision-making.  
- **Easy mode:** The computer stops rolling when it reaches **15 points** in a round or rolls a **1**.  
- **Hard mode:** The computer stops rolling when it reaches **25 points** in a round or rolls a **1**.  

---

## About the Project

- **Course:** Methods for Sustainable Programming (DA115B)  
- **Institution:** Kristianstad University  
- **Assignment:** Examination 2 – Test-Driven Development (TDD)  
- **Developed by:** Jasmine Rezai and Isabelle Dahlström  
- **Programming Language:** Python  

---

## 🎮 Features

- Create a player
- Play against a computer-player  
- Adjustable difficulty levels (Easy or Hard)  
- High score tracking  
- Display of game rules in a formatted UI  
- Intelligent computer strategy based on difficulty  
- Fully text-based interface with clean ASCII layout  

---



---

## ⚙️ Installation

1. Clone the repository:
```bash
git clone https://github.com/jasminerezai/Examination-2---Test-driven-development-TDD-.git
```

2. Install dependencies using Make:
```bash
make install
```

3. Create and activate a virtual environment: (Optional)
```bash
python -m venv venv
source venv/bin/activate   # Mac/Linux
venv\Scripts\activate      # Windows
```


4. Run the game:
```bash
python -m src.main
```

## Testing
Start the Unittests:
```bash
make coverage 
```
