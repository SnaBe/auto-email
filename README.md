# auto-mail setup guide
Automate mailing a large list of users in Python using selenium or smtplib


### 1. Clone this repository, download the needed modules & driver
```
$ pip install selenium
```
Linux/OSX/Windows Chromedriver: http://chromedriver.chromium.org/downloads

### 2. Edit the config.py to fit your needs

```
details = {
	'email_address': 'myfake.mail22@yahoo.com',
	'email_password': 'best/paSSword.2019',
	'subject': 'Python browser automation',
	'message': 'Looking to automate your own email list? Go download this coding example at - https://github.com/SnaBe/auto-mail',
	'users': ['example-mail@gmail.com', 'mail-example@gmail.com', 'myfake.mail22@yahoo.com']
}

```

### 3. Run it
```
$ py smtplib_email_a_list.py
$ py selenium_email_a_list.py

```
