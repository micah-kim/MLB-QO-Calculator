# the file where all the django files reside
from django.shortcuts import render
import requests
from bs4 import BeautifulSoup

# render index.html when the button is not clicked
def button(request):
    return render(request, 'index.html')

def output(request):
    url = "https://questionnaire-148920.appspot.com/swe/data.html"
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    
    MLB_table = soup.find('table', class_ = "table")
    arr = []
    total = 0
    count = 0
    data = 0
    for player in MLB_table.find_all("tbody"):
        rows = player.find_all("tr")
        for row in rows:
            salary = row.find('td', class_ = "player-salary").text
            salary = salary.strip('$').replace(',', '')
            if salary != '' and salary.isdigit():
                arr.append(int(salary))
    
    arr = sorted(arr, reverse=True)
    
    for a in arr:
        total+=a
        count+=1

        if count == 125:
            data = total // 125
            data = "{:,}".format(data)
            data = '$' + data
            return render(request, 'index.html', {'data' : data})

    return render(request, 'index.html', {'data' : data})
