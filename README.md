# Overview

In baseball, a team can provide a departing free agent player with a qualifying offer: a one-year contract whose monetary value is the average of the 125 highest salaries from the past season. The player is free to reject it and sign with any other team, but his new team will have to forfeit a draft pick.

This is a django project that parses financial data from https://questionnaire-148920.appspot.com/swe/data.html using BeautifulSoup4. Using this data, I calculated the average salary of the 125 highest listed salaries to find the qualifying offer amount. This data is then presented to the user so they may make a final decision and present their decision to their supervisor.

# Instructions
## Initial Step
1. Download and Open the "MLB-QO-Calculator.zip" file.

## Steps – QUESTION A
1. Open file on local device
2. Click "QUESTION_A" folder
3. Click "Phillies Baseball R&D Questionnaire (Answers).pdf" file

## Steps – QUESTION B
1. Open up Terminal (mac) or Shell (window)
2. Navigate to "MLB-QO-Calculator", then into "QUESTION_B" directory
    ```terminal
    user$ cd MLB-QO-Calculator
    user$ cd QUESTION_B
    ```
3. Activate "MLB_VENV" virtual environment
    ```terminal
    user$ source MLB_VENV/bin/activate
    ```
4. If not already, download python through https://www.python.org/downloads/
5. Ensure following are installed: django, requests, and beautifulsoup4
    ```terminal
    (MLV_VENV) user$ pip3 install django
    (MLV_VENV) user$ pip3 install requests
    (MLV_VENV) user$ pip3 install beautifulsoup4
    ```
6. cd into MLB-QO-Calculator
    ```terminal
    (MLV_VENV) user$ cd MLB-QO-Calculator
    ```
7. run manage.py on local server
    ```terminal
    (MLV_VENV) user$ python3 manage.py runserver 127.0.0.1:8002
    ```
8. Open http://127.0.0.1:8002/ on local browser
9. Click "Qualifying Offer" button

# Sources
- https://www.crummy.com/software/BeautifulSoup/bs4/doc/
- https://docs.djangoproject.com/en/4.1/
- https://stackoverflow.com/questions/40529848/how-to-write-the-output-to-html-file-with-python-beautifulsoup
- https://www.youtube.com/watch?v=e_o1nacGQiw


