# CodeAlpha Stock Portfolio Tracker

## Internship Task 2 — Python Programming

A console application that calculates the value of a stock portfolio using user-entered stock symbols and quantities. It uses a hardcoded dictionary of sample prices, displays each holding's value and the total, and saves a CSV summary.

**Important:** Prices are fixed sample values for this learning project, not live market prices or investment advice.

### Sample stock prices (USD)
| Symbol | Price |
|---|---:|
| AAPL | $180.00 |
| TSLA | $250.00 |
| GOOGL | $140.00 |
| MSFT | $420.00 |
| AMZN | $175.00 |

### Features
- User enters stock symbols and quantities.
- Validates symbols and positive whole-number quantities.
- Calculates per-stock investment and total investment.
- Saves results to `portfolio_summary.csv`.

### Concepts
Dictionaries, lists, loops, conditionals, functions, input validation, arithmetic, and CSV file handling.

### Requirements
Python 3.8 or later. No external packages required.

### Run
```bash
python stock_portfolio.py
```
Enter a supported symbol (for example, `AAPL`), enter its quantity, and repeat. Type `DONE` to finish.

### Example calculation
- AAPL: 2 × $180.00 = $360.00
- TSLA: 3 × $250.00 = $750.00
- Total: $1,110.00

The program creates `portfolio_summary.csv` in the folder from which it is run.

### Project structure
```text
CodeAlpha_StockPortfolioTracker/
├── stock_portfolio.py
├── README.md
├── VIDEO_SCRIPT.txt
├── LINKEDIN_POST.txt
└── SUBMISSION_CHECKLIST.txt
```

Author: Python Programming Intern — CodeAlpha
