from requests import get
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from extractors.wwr import extract_wwr_jobs

options = Options()
options.add_argument("--no-sandbox")
options.add_argument("--disable-dev-shm-usage")

browser = webdriver.Chrome(options=options)

browser.get("https://kr.indeed.com/jobs?q=python&limit=50")
soup = BeautifulSoup(browser.page_source, "html.parser")
job_list = soup.find("ul", class_="jobsearch-ResultsList")
jobs = job_list.find_all("li", recursive = False) #자식요소만 검색하고 자손 요소는 검색하지 않는다
for job in jobs:
  zone = job.find("div", class_="mosaic-zone")
  if zone == None: #None means absence of something
    # h2 = job.find("h2", class_="jobTitle")
    # a = h2.find("a")
    anchor = job.select_one("h2 a")
    title = anchor['aria-label']
    link = anchor['href']
    print(title, link)
    print("\n")