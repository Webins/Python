import requests
from bs4 import BeautifulSoup as Bs
from csv import writer

page_num = 1
mode = "w"
last_chance = False
while(True):
    if page_num == 1:
        url = "https://www.rithmschool.com/blog"
    else:
        url = f"https://www.rithmschool.com/blog?page={page_num}"
        mode = "a"

    response = requests.get(url)

    soup = Bs(response.text, "html.parser")

    articles = soup.find_all("article")

    with open("blog_data.csv", mode) as file:
        csv_writer = writer(file)
        if page_num == 1: csv_writer.writerow(["title", "link", "date"])
        for article in articles:
            title = article.select(".section-heading")[0].find("a").get_text()
            link = article.select(".card")[0].find_all("p")[1].find("a").attrs["href"]
            date = article.select(".card")[0].find("time").attrs["datetime"]
            csv_writer.writerow([title, link, date])

    print(f"Finished page: {page_num}")
    page_num += 1

    if last_chance:
        break

    if page_num == int(soup.select(".pagination")[0].select(".last")[0].find("a").attrs["href"].split("=")[1]):
        last_chance = True
