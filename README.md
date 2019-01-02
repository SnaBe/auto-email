# auto-mail setup guide
Automate mailing a large list of users in Python using selenium or smtplib


### 1. Clone this repository, download the needed modules & driver
```
$ pip install selenium
```
To use Selenium you'll need a Linux/OSX/Windows Chromedriver: http://chromedriver.chromium.org/downloads

### 2. Edit the config.py to fit your needs

#### Here's an example

```
details = {
	'email_address': 'myfake.mail22@yahoo.com',
	'email_password': 'best/paSSword.2019',
	'subject': 'Python browser automation',
	'message': 'Looking to automate your own email list?',
	'users': ['example-mail@gmail.com', 'mail-example@gmail.com', 'myfake.mail22@yahoo.com']
}

```

### 3. Run it
```
$ py smtplib_email_a_list.py
```
or
```
$ py selenium_email_a_list.py
```
