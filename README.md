# Python-Calculator

A simple desktop calculator app built with [Kivy](https://kivy.org/), supporting basic arithmetic (addition, subtraction, multiplication, division) and parentheses.

## Features

- On-screen numeric keypad (0–9) with decimal point
- Basic operators: addition (`+`), subtraction (`-`), multiplication (`×`), division (`÷`)
- Parentheses support for grouped expressions
- Clear (`C`) and evaluate (`=`) buttons
- Read-only display field showing the current expression/result

## Tech Stack

- **Python 3**
- [`Kivy`](https://kivy.org/) `2.3.0` — UI framework
- [`requests`](https://pypi.org/project/requests/) `2.32.3`

## Prerequisites

- Python 3
- pip

## Installation

Clone the repository:

```bash
git clone https://github.com/paoradox/Python-Calculator.git
cd Python-Calculator
```

Install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the app:

```bash
python main.py
```

This opens the calculator window. Tap the on-screen buttons to build an expression, then press `=` to evaluate it, or `C` to clear the display.

## Project Structure

```
Python-Calculator/
├── main.py           # App entry point and calculator logic
├── calculator.kv      # Kivy layout/UI definition (keypad, display)
├── requirements.txt
└── ico.ico            # App icon
```

## License

Not specified.
