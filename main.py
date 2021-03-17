import os
import re

import requests
from fake_useragent import UserAgent
from lxml import etree


def get100samplesfromRunoob(url):
    ua = UserAgent()

    # headers伪装成一个浏览器进行的请求
    # 不加这个的话，网页会识别出请求来自一个python而不是浏览器的正常请求
    headers = {"User-Agent": ua.random}
    url1 = "https://www.runoob.com/python/python-exercise-example{}.html"
    url2 = "https://www.runoob.com/python/python-exercise-example%s.html"
    data = []
    response = requests.get(url=url, headers=headers)
    data.append(response.text)
    return data


def addTitle2Readme(url, datas):
    titles = ""
    for html_text in datas:
        # print(html_text)
        tree = etree.HTML(html_text)
        title = tree.xpath('//div[@class="article-intro"]/h1/text()')[0]
        titles += os.linesep + f"[{title}]({url})"
        titles.replace("'", "")

    print(titles)

    readme = open("README.md", "a")
    readme.write(titles)
    readme.close()


def saveData2File(url, datas):
    for html_text in datas:
        # print(html_text)
        tree = etree.HTML(html_text)
        title = tree.xpath('//div[@class="article-intro"]/h1/text()')

        if "44.html" not in url:
            example = tree.xpath('//div[@class="article-intro"]/p/strong/text()')
            desc = tree.xpath('//div[@class="article-intro"]/p/strong/../text()')
        else:
            print("44.html")
            example = tree.xpath('//div[@class="article-intro"]/p[2]/text()')
            desc = tree.xpath('//div[@class="article-intro"]/p[4]/text()')

        # print(title)
        # print(example)
        # print(desc)

        if desc and desc[0]:
            example.insert(1, desc[0])
        if len(desc) > 1 and desc[1]:
            example.append(desc[1])

        content = "#" + url + os.linesep
        print(content + os.linesep + str(example))

        def_fun = "def fun():\r  pass" + os.linesep
        main_fun = 'if __name__ == "__main__":' + os.linesep + "  print(fun())"

        for text in example:
            content += "#" + str(text).replace("\r\n", "") + os.linesep

        for t in title:
            num = re.search(r"\d+", t)
            filename = "sample" + num.group()
            # filename = re.sub(r"\D+", "sample", t)
            filename += ".py"
            print(filename)
            file = open("./samples/" + filename, "w")
            file.write(content + os.linesep * 10 + def_fun + main_fun)
            file.close()


if __name__ == '__main__':
    for num in range(1, 101):
        # print(url1.format(num)) #format
        # print(url2 % num)#
        url = f"https://www.runoob.com/python/python-exercise-example{num}.html"
        # saveData2File(url, get100samplesfromRunoob(url))
        addTitle2Readme(url, get100samplesfromRunoob(url))
