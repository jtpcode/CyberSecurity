In this project we use OWASP Top Ten Web Application Security Risks -list from 2017 to demonstrate five different security risks and their fixes in a simple guestbook web application. The chosen risks are Cross site scripting (XSS), Broken access control, Sensitive data exposure, CSRF and Broken Authentication. The Django framework used in this example application automatically takes care of a lot of security issues, so some of the vulnerabilities are a bit forced, for example Flaw 1, where all the messages are deliberately marked as safe so we can demonstrate running a hostile jacascript in one of the messages. Same applies for CSRF vulnerability (Flaw 4) where we use the decorator @csrf_exempt to prevent checking for csrf token. For sensitive data we chose to show the email address of the message sender, since it is more natural and probable flaw in a simple guestbook website than for example social security number.

We have provided links to the repository itself with installation instructions below if needed. Also there are links to every flaw and its location in the code base. The fix for the flaw is located right after the flawed codeline(s). For your convenience there are also links for screen captures for all the vulnerabilities, before and after the fix. The application is tested to work in both Windows and Linux Cubbli environments.

LINK: https://github.com/jtpcode/CyberSecurity
Installation instructions:
- Follow the link to the repository and clone the repo into your own computer:
  - $ git clone git@github.com:jtpcode/CyberSecurity.git
- This project uses Django version 5.2.1. To install:
  - $ python -m pip install Django
- If you have to update Django and you installed Django with pip, you can use:
  - $ python -m pip install -U Django
- To run the application in the project root directory:
  - $ python manage.py runserver
- The application is located at http://127.0.0.1:8000/guestbook/

The Github repo already includes a db.sqlite3 database file for testing purposes with few messages included. There is a user (username/password) in the system you can use for testing:
- alice/in_wonderland

There is also an admin user (username/password), but that's not necessary for the assignment:
- admin/hellurei

Python version 3.13.1 was used in the project. 

Here are the flaws with descriptions, links and fixes:

FLAW 1: Cross site scripting (XSS)
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L20

Description of flaw 1:
For some reason the developer has created a for loop for marking all the messages as safe, so messages can include for example javascript which is executed when the guestbook main page is loaded. You can see a simple javascript example with unwanted pop up window in the picture following this link:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-1-before-1.png

How to fix it:
Remove the for-loop completely, so messages aren't marked as safe. In the picture (follow the link below) you can see the pop up doesn't appear and you can actually see the javascrip code in plain text in the message queue:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-1-after-1.png


FLAW 2: Broken access control
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L14

Description of flaw 2:
When fetching the messages, the developer has left out privacy filtering "filter(is_public=True)" in "views.py" method index(request), so also private messages are visible to everyone. You can see the message from "aapeli" which is marked as private in the database, see the picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-2-before-1.png

How to fix it:
Include "filter(is_public=True)" in the line of code, so messages are filtered according to privacy options. To see the effect, follow the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-2-after-1.png


FLAW 3: Sensitive Data Exposure
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/templates/guestbook/index.html#L12

Description of flaw 3:
When messages have been fetched from the database and passed on to "index.html", the message data is not properly handled since the current code shows the email address of the sender in the guestbook main view. You can see the result in the picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-3-before-1.png

How to fix it:
You must leave out the "msg.email" part from the code in order to not show the email address of the sender to everyone visiting the guestbook. You can see the result in the picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-3-after-1.png


FLAW 4: CSRF
LINKS:
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L29
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/templates/guestbook/submit.html#L4

Description of flaw 4:
A @csrf_exempt decorator is used in "views.py" for method submit_message(request). Also "csrf_token" has not been added to the related "submit.html" form. This allows an attacker to send a message from another page or location to the guestbook without problems. You can find the "attack page" used in this example here and also test it yourself by opening the file in another browser window:
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/attack_page/csrf_attack.html

See the attacker's message in the picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-4-before-1.png

How to fix it:
Remove the @csrf_exempt decorator from "views.py" AND ALSO add "{% csrf_token %}" in "submit.html" at the beginning of the form. By following the link below, you can see the result when "attack page" (see Description of flaw 4) is tried to execute again:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-4-after-1.png


FLAW 5: Injection
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L46

Description of flaw 5:
Developer has used 'subprocess.call' for debugging user input with direct shell access, which allows running any code in the command prompt. Follow the links below to see pictures of the situation, where 'testdir' is deleted via windows command prompt (for Linux the attacker could use for example 'John; rm -rf ./testdir'):

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-5-before-1.png
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-5-before-2.png
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-5-before-3.png

How to fix it:
Remove subprocess.call from the code and preferrably use for example 'print' for debugging inputs. The result can be seen in the picture following the links below, where only valid debug print is seen ("User input from: Mick & rmdir /s /q testdir") and 'testdir' stil exists:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-5-after-1.png
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-5-after-2.png
