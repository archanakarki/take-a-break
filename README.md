# Take a break

This program : 
- opens the an URL in the web brower 
- after every given duration. 

    This program uses a modules called webbrowser and time from Python Standard Library.
    For browser, default browser is opened whereas the times are given in seconds for 2 hours.

## My understanding and interpretation of Abstraction through this project.

    This programs highlights the use and idea of abstraction in simple form too. 

    When we download Python, we get acces to its huge set of code that can perform certain action. That is called the Python standard library. Such codes are seperated on different files also called modules based on the seperation of their work so functions that works on webbrowsers are on webbrowser module and those related to time are in time module. 

    In webbrowser, open function can open a web browser, whereas in time , ctime can find current time and sleep can suspend the function for some time. How? We donot know. Its hidden so we can only include these few line in our program and it can do the commom work. We brought codes to our file from Python standard library and solved our issue. 

    Abstraction in programming is about hiding real implementation of application from user and just focusing on it implementation. In this context, how the webbrowser.open() opened the url we gave to it and how is time.sleep() suspended the program after some time in Python is known to developers maintaining Python but it is hidden from us as users. But for our ease, we can use it and yippe we have our work done.

