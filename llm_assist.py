import openai
from config import OPENAI_API_KEY

openai.api_key = OPENAI_API_KEY

def fill_row(row_index, current_row):
    prompt = f"""You are a Sudoku expert. Please fill in the missing numbers (0 represents blanks) in this Sudoku row:
{current_row}
Return the completed row as a Python list of 9 integers only. No explanation."""

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=0
        )
        content = response.choices[0].message["content"].strip()
        result = eval(content)
        if isinstance(result, list) and len(result) == 9:
            return result
        else:
            raise ValueError("Invalid result format")
    except Exception as e:
        print("LLM Error:", e)
        return current_row
