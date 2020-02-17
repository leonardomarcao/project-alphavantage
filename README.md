## Project Alpha Vantage

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9579cdd2735c4941873f20e919e561a3)](https://app.codacy.com/manual/leonardomarcao/project-alphavantage?utm_source=github.com&utm_medium=referral&utm_content=leonardomarcao/project-alphavantage&utm_campaign=Badge_Grade_Dashboard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## About
Project aimed at importing and reconciling stock closing prices using the Alpha Vantage API
 

### Requirements
* Python 3.7+
* SQLite 3 ([How to Install](https://linuxhint.com/install_sqlite_browser_ubuntu_1804/))

### How to Install

1. Create virtual environment
```
    python3.x -m venv venv    
```
2. Activate created environment
```
    . venv/bin/activate
```
3. Install all requirements
```
    pip install -r requirements.txt
```
4. Create database using DDL on alphavantage.sql
```
sqlite3 alphavantage < alphavantage.sql
```
5. Create database using DDL on alphavantage.sql:
```
sqlite3 alphavantage < alphavantage.sql
```
6. Create .env file (**Env Example**):
```
alpha_vantage_api_url='https://www.alphavantage.co/'
database_name='alphavantage'
alpha_vantage_api_key='enter_your_api_key'
```
