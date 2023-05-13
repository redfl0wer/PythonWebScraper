from requests import get
from bs4 import BeautifulSoup

base_url = "https://weworkremotely.com/remote-jobs/search?term="
search_term = "php"

response = get(f"{base_url}{search_term}") 

if response.status_code != 200: 
  print("can't request website")
else:
    results = []
    soup = BeautifulSoup(response.text, "html.parser") #response.text는 웹사이트의 코드를 줌줌
    jobs = soup.find_all('section', class_="jobs")
    for job_section in jobs:
        job_posts = job_section.find_all('li')
        job_posts.pop(-1)
        for post in job_posts:
            anchors = post.find_all('a')
            anchor = anchors[1]
            link = anchor['href']
            try:
                company, kind, region = anchor.find_all('span', class_="company")
            except ValueError:
                company, kind = anchor.find_all('span', class_="company")
            title = anchor.find('span', class_='title')
            job_data = {
                'company' : company.string,
                'region' : region.string,
                'position' : title.string
                }
            results.append(job_data)
    for result in results:
        print(result)
        print("")
                
