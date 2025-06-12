# Sudoku Game with LLM Interaction Based on MCP Protocol

## 🧪 Experiment Overview

This project implements a simple command-line **Sudoku game** with simulated **large language model (LLM)** interaction, based on the **Model Context Protocol (MCP)**. Users can request the model to auto-complete a row (or column) to reduce puzzle-solving difficulty.

---

## 📋 Requirements

To run this project, you need:

- Python 3.6 or later
- Command Line (Terminal, PowerShell, etc.)

> No third-party libraries are required. All code uses Python Standard Library.

---

## 🗂 Project Structure

sudoku_mcp_experiment/
├── sudoku_game.py # Main game loop (UI and interaction)
├── llm_assist.py # Simulated LLM auto-fill logic
└── README.md # This documentation

![image](https://github.com/user-attachments/assets/bdcec77a-b734-4622-a2ee-7847efb9b84b)


## 🚀 How to Run

1. Clone or download this repository
2. Open a terminal and navigate to the project folder
3. Run the following command:
python sudoku_game.py
You will see the Sudoku board and an input prompt. To fill the first row using LLM assistance, enter:
fill row 1
💬 Example Interaction
Initial board:
. 1 . . 3 . 4 . .
. . . 7 4 5 . . .
. . 4 . 9 6 . 3 .
...
Command:
fill row 1
Result:![image](https://github.com/user-attachments/assets/f1719054-913e-4e25-8589-14b5db58a4e2)

