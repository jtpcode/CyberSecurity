In this project we used OWASP Top Ten Web Application Security Risks in 2017 to demonstrate five different security risks and their fixes in simple guestbook web application. The chosen risks are Cross site scripting (XSS), SQL-injection, Broken access control, Sensitive data exposure and CSRF.

LINK: https://github.com/jtpcode/CyberSecurity
Installation instructions:
- Follow the link to the repository and clone the repo into your own computer:
  - $ git clone git@github.com:jtpcode/CyberSecurity.git
- This project uses Django version 5.2.1. To install:
  - $ python -m pip install Django
- If you have to update Django and you installed Django with pip, you can use:
  - $ python -m pip install -U Django
- To run the application in project root directory:
  - $ python manage.py runserver
- The application is located at http://127.0.0.1:8000/guestbook/

Python version used in the project is 3.13.1

Here are the flaws with descriptions, links and fixes:

FLAW 1:
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L20

Description of flaw 1:
For some reason the developer has created a for loop for marking all the messages as safe, so messages can include for example javascript which is executed when the guestbook main page is loaded. You can see a simple javascript example with unwanted pop up window in the picture following this link:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-1-before-1.png


How to fix it:
Remove the for-loop completely, so messages aren't marked as safe. In the picture (follow the link below) you can see the pop up doesn't appear and you can actually see the javascrip code in plain text:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-1-after-1.png

FLAW 2:
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L14

Description of flaw 2:
When fetching the messages, the developer has left out privacy filtering "filter(is_public=True)", so also private messages are visible to everyone. You can see the message from "aapeli" which is marked as private in the database, see the picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-2-before-1.png

How to fix it:
include "filter(is_public=True)" in the code line, so messages are filtered according to privacy options. To see the effect, follow the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-2-after-1.png

FLAW 3:
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/templates/guestbook/index.html#L12

Description of flaw 3:
When messages have been fetched from the database and passed on to "index.html", the message data is not properly handled since the current code shows the email address of the sender in the guestbook main view. You can see the result in the picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-3-before-1.png

How to fix it:
You must leave out the "msg.email" part from the code in order to not show the email address of the sender to everyone visiting the guestbook. You can see the result in the picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-3-after-1.png

FLAW 4:
LINKS:
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L29
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/templates/guestbook/submit.html#L4

Description of flaw 4:
A @csrf_exempt decorator is used in "views.py" for method submit_message(request). Also "csrf_token" has not been added to the related "submit.html" page. This allows an attacker to send a message from another page/location to the guestbook without problems. You can find the "attack page" used in this example here:
https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/attack_page/csrf_attack.html

See the attacker's message in the picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-4-before-1.png

How to fix it:
Remove the @csrf_exempt decorator from "views.py" AND ALSO add "{% csrf_token %}" in "submit.html" file, at the beginning of the form. By following the link below, you can see the result when "attack page" (see Description of flaw 4) is tried to access again:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-4-after-1.png

FLAW 5:
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L34

Description of flaw 5:
A @login_required decorator has been left out from method submit_message(request) in "views.py". This allows anyone to access /guestbook/submit/submit.html to send messages without having to login to the site. Follow the link below to see a picture of the situation:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-5-before-1.png

How to fix it:
Add/uncomment @login_required decorator in the method submit_message(request) in "views.py". This way you have to login to the site before you can send messages. The result can be seen in a picture following the link below:

https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/screenshots/flaw-5-after-1.png
