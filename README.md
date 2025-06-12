# Sudoku Game with Real OpenAI LLM Interaction

## Overview

This project integrates OpenAI GPT to solve Sudoku rows via the command line, using real-time LLM interaction to simulate intelligent assistance in puzzle solving.

## Requirements

- Python 3.6+
- `openai` package (`pip install openai`)
- OpenAI API Key

## Setup

1. Paste your API key into `config.py`:
```python
OPENAI_API_KEY = "sk-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
```

2. Run the game:
```bash
python sudoku_game.py
```

3. At the prompt, enter:
```
fill row 1
```

The model will complete the first row using actual reasoning.
![image](https://github.com/user-attachments/assets/d93ff66b-fe20-492a-b11c-32f45d027b91)

## Files

- `sudoku_game.py`: main interface
- `llm_assist.py`: OpenAI integration logic
- `config.py`: API key configuration
