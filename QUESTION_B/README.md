## Initial Step
1. Click "Code" at top right of screen and click "Download ZIP."

## Steps (QUESTION A)
1. Open file on local device
2. Click "QUESTION_A" folder
3. Click "Phillies Baseball R&D Questionnaire (Answers).pdf" file

## Steps (QUESTION B)
1. Open file on local device, open Terminal (mac) or PowerShell (window)
2. cd into the "QUESTION_B" directory
    ```terminal
    user $ source cd QUESTION_B
    ```
3. Activate "MLB_VENV" virtual environment
    ```terminal
    user $ source MLB_VENV/bin/activate
    (MLV_VENV) user $ 
    ```
4. If not already download python through https://www.python.org/downloads/
5. Ensure following are installed: django, requests
    ```terminal
    (MLV_VENV) user $ pip3 install django
    (MLV_VENV) user $ pip3 install requests
    ```
6. cd into MLB-QO-Calculator
    ```terminal
    (MLV_VENV) user $ cd MLB-QO-Calculator
    ```
7. run manage.py on local server
    ```terminal
    (MLV_VENV) user $ python3 manage.py runserver 127.0.0.1:8002
    ```
8. Open http://127.0.0.1:8002/ on local browser
9. Click "Qualifying Offer" button


## Contributing
