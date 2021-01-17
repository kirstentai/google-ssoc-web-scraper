import requests
from bs4 import BeautifulSoup

url = "https://summerofcode.withgoogle.com/archive/2020/organizations/"
page = requests.get(url)

soup = BeautifulSoup(page.content, 'html.parser')
sec = soup.find("section")
divi = sec.find("div")
ull = divi.find("ul")
# list = ull.find_all("li")
# list = list2.find("aria-label")
# cont = list.find("ul")
# orgs=cont.find("li")

# results = divi.find_all(section, class="fixed-width")

# print(ull.prettify())
#job_elems = results.find_all('section', class_='card-content')

for tag in ull.find_all('li', class_="organization-card__container"):
    orgs = tag.find('a', class_="organization-card__link")
    title = orgs.find('div', class_="organization-card__footer md-padding")
    final = title.find('h4', class_="organization-card__name font-black-54")
    print(final.text.strip())
    # print("Results: ",final, '\n')

# soup.find_all('aria-label')
