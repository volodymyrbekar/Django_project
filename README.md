**Installation (MacOS)**
* git clone <inforse>
* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt



**# Workaround if an error occurs on MacBook M1**

export LDFLAGS="-L/opt/homebrew/Cellar/unixodbc/2.3.9_1/lib"
export CPPFLAGS="-I/opt/homebrew/Cellar/unixodbc/2.3.9_1/include"
pip install --upgrade pip
pip install -r requirements.txt
pip install --upgrade pip   

**Installation (Windows)**

* _Download python3 (3.8.5 preffered) and install it for all users by selecting appropriate checkbox during installatio_
* _* # Python https://www.python.org/downloads/windows/_
* _* # Git https://git-scm.com/download/win_

**# open terminal**

* git clone <inforse>
* python3 -m venv venv
* source venv/bin/activate
* pip install -r requirements.txt
