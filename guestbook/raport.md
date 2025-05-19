**KORJAA LINKIT OIKEILLE RIVEILLE LOPUKSI**
**OTA KUVAKAAPPAUKSET**

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
Link: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L16

Description of flaw 1:
For some reason the developer has created a for loop for marking all the messages as safe, so messages can include for example javascript which is executed when the guestbook main page is loaded. You can see a simple javascript example with unwanted pop up window in the picture following this link:

![Flaw 1 before](.\screenshots\flaw-1-before-1.png)


How to fix it:
Remove the for-loop completely, so messages aren't marked as safe. In the picture (follow the link below) you can see the pop up doesn't appear and you can actually see the javascrip code in plain text:

![Flaw 1 before](.\screenshots\flaw-1-after-1.png)

FLAW 2:
LINK: https://github.com/jtpcode/CyberSecurity/blob/main/guestbook/views.py#L10

Description of flaw 2:
Developer has left "filter(is_public=True)" out, so also private messages are visible to everyone.

How to fix it: include "filter(is_public=True)", so messages are filtered according to privacy.

...

FLAW 5:
exact source link pinpointing flaw 5...
description of flaw 5...
how to fix it...