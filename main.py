from requests import get
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

base_url = "https://kr.indeed.com/jobs?q="
search_term = "python"
response = get(f"{base_url}{search_term}")
if response.status_code != 200:
    print("Can't request website...")
else:
    soup = BeautifulSoup(response.text, "html.parser")
    job_list = soup.find("ul", class_="jobsearch-ResultsList")
    jobs = job_list.find_all('li')
    print(len(jobs))

