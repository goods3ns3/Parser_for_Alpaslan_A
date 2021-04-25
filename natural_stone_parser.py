from requests_html import HTMLSession
import csv


def save_result(row):
    with open('result.csv', 'a', encoding='utf-8', newline='') as links_csv:
        writer = csv.writer(links_csv, delimiter=';')
        writer.writerow(row)


URL = 'https://www.stonecontact.com/natural-stone'
session = HTMLSession()
r = session.get(URL)

# r.html.render(sleep=1)

products = r.html.xpath('//*[@id="main"]/div[2]/div[3]', first=True)

for item in products.absolute_links:
    r = session.get(item)

    # get all descriptions
    title = r.html.find('div.NaturalStones-desc-title', first=True).text
    subtitle = r.html.find('div.BorderB', first=True).text
    color = r.html.xpath('//*[@id="MainContainer_Control_lblHtmlColor"]', first=True).text
    country = r.html.xpath('//*[@id="MainContainer_Control_lblHtmlCountry"]', first=True).text
    description = r.html.find('div.NaturalStones-desc-company-info', first=True).text

    # get images links
    img_link = r.html.find('#bigpicturepanel', first=True).attrs['src']

    # save images
    response = session.get(img_link)
    if response.status_code == 200:
        with open(f"{title}.jpg", 'wb') as f:
            f.write(response.content)



