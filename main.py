import sqlite3
import lxml.html
import requests


def main():
    connection =sqlite3.connect('dtv_ebook.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS books (
            url TEXT PRIMARY KEY,
            title TEXT, series TEXT, authors TEXT, genres TEXT,
            status TEXT, formats TEXT, views INTEGER, tags TEXT,
            azw3 TEXT, epub TEXT, mobi TEXT, pdf TEXT
        )
    ''')

    cursor.execute('''SELECT url FROM books''')
    rows = cursor.fetchall()
    #urls = {row[0] for row in rows}

    for i in range(1219, 2000):
        url = f'https://dtv-ebook.com.vn/sach-truyen-ebook-313/{i}.html#gsc.tab=0'
        for detail_url in get_detail_urls(url):
            try:
                #if detail_url not in urls:
                    data = get_data(detail_url)
                    cursor.execute(
                        """INSERT INTO books (url, 
                        title, series, authors, genres, 
                        status, formats, views, tags, 
                        azw3, epub, mobi, pdf) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""",
                        data)
                    connection.commit()
                    print(i, data)
            except sqlite3.IntegrityError as e:
                print("Error:", i, e, detail_url)

    connection.close()


def get_detail_urls(list_url):
    response = requests.get(list_url)
    tree = lxml.html.fromstring(response.text)
    detail_urls = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div/div[2]/ul/li/div[1]/a/@href')
    return detail_urls


def get_data(detail_url):
    response = requests.get(detail_url)
    tree = lxml.html.fromstring(response.text)

    title = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tr[1]/td/h2/text()')
    series = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tr[3]/td[2]/a/text()')
    authors = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tr[2]/td[2]/a/text()')
    genres = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tr[4]/td[2]/a/text()')
    status = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tr[5]/td[2]/span/text()')
    formats = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tr[6]/td[2]/a/text()')
    views = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tr[7]/td[2]/span/text()')
    tags = tree.xpath('/html/body/section[2]/div[2]/div/div/div[1]/div[1]/div[1]/div[2]/table/tr[8]/td[2]/a/text()')
    azw3 = tree.xpath('//*[@id="download"]//a[contains(text(), "AZW3")]/@href')
    epub = tree.xpath('//*[@id="download"]//a[contains(text(), "EPUB")]/@href')
    mobi = tree.xpath('//*[@id="download"]//a[contains(text(), "MOBI")]/@href')
    pdf = tree.xpath('//*[@id="download"]//a[contains(text(), "PDF")]/@href')

    def f(text_list):
        return ', '.join([text.strip() for text in text_list])

    return (detail_url,
            f(title), f(series), f(authors), f(genres),
            f(status), f(formats), f(views), f(tags),
            f(azw3), f(epub), f(mobi), f(pdf))


if __name__ == '__main__':
    main()
