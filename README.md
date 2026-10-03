# PLP Python Week 8 - Final Capstone Toolkit

## Project Description
This project is a menu-driven terminal utility application that combines variables, loops, conditional routing, and structural list mutations. The program provides the user with three interactive tools: a Number Guessing Game with high/low dynamic feedback, a dynamic Task Tracker to add or clear to-do list items, and a Name Formatter Pro tool that sanitizes inputs and analyzes string character lengths.

## How to Run the Toolkit
1. Ensure you have Python installed on your system.
2. Open your terminal or command prompt.
3. Navigate to the project directory:
   ```bash
   cd plp-python-week7/plp-python-week8
   ```
4. Run the script using the following command:
   ```bash
   python toolkit.py
   ```
5. Follow the on-screen menu prompts by entering a number from 1 to 4.

## Project Reflection
Building the Task Tracker tool was the most challenging part of this assignment because managing an independent data collection loop inside the main program's menu framework required a careful approach to keep the states separate. The bug that took the longest to resolve was tracking down an accidental structural syntax error caused by misaligned spacing blocks, which Python flagged immediately with a runtime indentation failure. To fix it, I had to carefully map out the indentation spaces to align them with the main block requirements. If I were granted an additional week of development time, I would expand the system by incorporating file handling systems to automatically save the dynamic list data directly into a local backup text file before the program terminates.
