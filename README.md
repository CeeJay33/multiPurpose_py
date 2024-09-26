# For the insta.py it is an  Instagram Brute Force Login Script

This script uses `Selenium` and `Requests` libraries to automate logging into Instagram using multiple passwords from a provided password list. It will attempt to log in with different passwords until a successful login is detected or all passwords are exhausted. If a password results in a successful login, it will be saved to a log file.

**Note**: This script is for educational purposes only. Unauthorized access to accounts is illegal. Please use this responsibly and with permission from the account holder.

## Requirements

- **Python 3.x**
- **Google Chrome Browser**
- **ChromeDriver** (Ensure that the version matches your installed version of Chrome)
- **Selenium WebDriver**
- **Requests library**

## Installation and Setup

### 1. Install Python 3.x

Make sure you have Python 3 installed. You can download it from the [official Python website](https://www.python.org/downloads/).

### 2. Install Required Libraries

Use `pip` to install the necessary Python packages. Open your terminal and run:

```bash
pip install selenium requests
