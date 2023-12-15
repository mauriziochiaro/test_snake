# Snake Game Scripts Evaluation

## Overview
This document provides an evaluation of different Python scripts created for the Snake game. Each script is assessed by GPT-4 based on its code structure, complexity, performance, and given a score. My feedback is also included for practical insights.

## Evaluation Table

| Script Name                                   | Prompt                                                                                                          | Code Structure      | Complexity               | Performance                       | Score | Human Feedback                                                                                   |
|-----------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------|--------------------------|-----------------------------------|-------|-------------------------------------------------------------------------------------------------|
| `test_snake_date_asked.py`                    | "User: 'Ok write a python script that recreates the game snake.'"                                               | Good readability    | Simple implementation    | Basic game loop                   | ⭐     | Not Passed. Snake too fast, unplayable.                                                          |
| `test_snake_date_changed.py`                  | "User: 'Ok write a python script that recreates the game snake. My deadline is tomorrow, March 28th.'"          | Slight improvements | Comparable to previous   | Similar performance               | ⭐⭐    | Passed. Very close to test_snake_date_asked, but snake is slower so I can play.                 |
| `test_snake_instructions_light.py`           | "Instructions: Only answer with code. User: 'Ok write a python script that recreates the game snake.'"          | Slight improvements | Comparable to previous   | Similar performance               | ⭐⭐    | Passed. Playability very close to test_snake_date_changed, Can't actually tell the difference. |
| `test_snake_instructions_medium.py`          | "Instructions: Only answer with code in code block. User: 'Ok write a python script that recreates the game snake.'" | Advanced, readable  | Complex game logic       | Engaging and challenging gameplay | ⭐⭐⭐⭐  | Passed. Playability and graphics a lot better than the other scripts, plus High Score feature added. |
| `test_snake_instructions_medium_refined.py`  | "User (Follow up): 'How would you improve this script?'"                                                        | Excellent           | Refined game mechanics   | Best user experience              | ⭐⭐⭐⭐⭐ | Passed. I actually had fun playing this one.                                                    |
| `test_snake_instructions_medium_02.py`       | "User: 'Ok write a python script that recreates the game snake.'" (Context: using `curses` library)             | Sophisticated       | Advanced terminal handling| Smooth, interactive gameplay      | ⭐⭐⭐⭐  | Passed. Offers a unique terminal-based gaming experience, more complex and engaging.            |

---