from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup

def get_page_count(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  browser = webdriver.Chrome(options=options)
  base_url = "https://kr.indeed.com/jobs?q="
  browser.get(f"{base_url}{keyword}")
  soup = BeautifulSoup(browser.page_source, "html.parser")
  pagination = soup.find("nav", role="navigation")
  pages = pagination.find_all("div", recursive=False)
  if len(pages) == 0:
    return 1
  print(len(pages))

get_page_count("python")

def extract_indeed_jobs(keyword):
  options = Options()
  options.add_argument("--no-sandbox")
  options.add_argument("--disable-dev-shm-usage")
  
  browser = webdriver.Chrome(options=options)
  
  base_url = "https://kr.indeed.com/jobs?q="
  browser.get(f"{base_url}{keyword}")
  results = []
  soup = BeautifulSoup(browser.page_source, "html.parser")
  job_list = soup.find("ul", class_="jobsearch-ResultsList")
  jobs = job_list.find_all("li", recursive=False)  #자식요소만 검색하고 자손 요소는 검색하지 않는다
  for job in jobs:
    zone = job.find("div", class_="mosaic-zone")
    if zone == None:  #None means absence of something
      # h2 = job.find("h2", class_="jobTitle")
      # a = h2.find("a")
      anchor = job.select_one("h2 a")
      title = anchor['aria-label']
      link = anchor['href']
      company = job.find("span", class_="companyName")
      location = job.find("div", class_="companyLocation")
      job_data = {
        'link': f"https://kr.indeed.com{link}",
        'company': company.string,
        'location': location.string,
        'position': title
      }
      results.append(job_data)
  
  for result in results:
    print(result, "\n\n")