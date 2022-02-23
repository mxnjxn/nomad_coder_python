from pip._vendor import requests
indeed_result = requests.get(
    "https://ca.indeed.com/jobs?q=python&limit=50&radius=25&start=50&vjk=994857387fc3858b")
print(indeed_result)

# getting html
print(indeed_result.text)

# using request package enables to scrall html datas based on the url provided.
# However, only using html data wil be unnecessary and inefficient to get the intedend datas; therefore, we wil use BeautifulSoup4 to organize the desired data.
# method= function inside a object
# beautifulsoup is a wonderful package to extract information form html
