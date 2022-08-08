# the file where all the django files reside
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# render index.html when the button is not clicked
def button(request):
    url = "https://questionnaire-148920.appspot.com/swe/data.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.content, 'html.parser')
    
    data = soup.find('table', class_ = "table")
    return render(request, 'index.html', {'tableData' : data})

# re-render index.html with output
def output(request):
    # extract url of site to be parsed
    url = "https://questionnaire-148920.appspot.com/swe/data.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    # search site html for table
    MLB_table = soup.find('table', class_ = "table")
    arr = []
    total = 0
    count = 0
    data = 0
    
    # iterate through individual players and store salary in "arr"
    for player in MLB_table.find_all("tbody"):
        rows = player.find_all("tr")
        for row in rows:
            salary = row.find('td', class_ = "player-salary").text
            salary = salary.strip('$').replace(',', '')
            if salary != '' and salary.isdigit():
                arr.append(int(salary))
    
    # sort array in reverse order by salary amount
    arr = sorted(arr, reverse=True)
    
    # iterate array again get highest 125 salaries
    for a in arr:
        total+=a
        count+=1

        if count == 125:
            data = total // 125
            data = "{:,}".format(data)
            data = '$' + data
            return render(request, 'index.html', {'data' : data, 'img' : "https://imgur.com/LmekkPz"})

    # will render 0 as the data if arr is empty
    return render(request, 'index.html', {'data' : data})
