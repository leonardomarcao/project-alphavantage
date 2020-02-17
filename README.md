## Project Alpha Vantage

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/9579cdd2735c4941873f20e919e561a3)](https://app.codacy.com/manual/leonardomarcao/project-alphavantage?utm_source=github.com&utm_medium=referral&utm_content=leonardomarcao/project-alphavantage&utm_campaign=Badge_Grade_Dashboard)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
## About

Project aimed at importing and reconciling stock closing prices using the Alpha Vantage API and SQLite3
 

### Requirements
* Python 3.8
* SQLite 3 ([How to Install](https://linuxhint.com/install_sqlite_browser_ubuntu_1804/))

### How to Install

1. Create virtual environment
```
    python3.8 -m venv venv    
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
6. Create .env file (**Env Example**):
```
alpha_vantage_api_url='https://www.alphavantage.co/'
database_name='alphavantage'
alpha_vantage_api_key='enter_your_api_key'
```
7. Execute to import
```
python3.8 project-alphavantage/
```
Output example:

Stock Table

![image](https://i.ibb.co/4sYJ8Tm/Selection-125.png)

Stock Imports

![image](https://i.ibb.co/j4knGy5/Selection-124.png)

### License

MIT License

Copyright (c) 2020 Leonardo Marcão

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.