import requests
from bs4 import BeautifulSoup

def crawl_baidu_zhidao(query):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    search_url = "http://zhidao.baidu.com/search"
    params = {
        "word":query,
        "ie": "utf-8",
    }

    response = requests.get(search_url, params=params, headers=headers)
    #指定相应内容的编码为utf-8
    response.encoding = "utf-8"

    if response.status_code !=200:
        print("Failed to retrieve the web page.")
        return
    soup = BeautifulSoup(response.text, "html.parser")
    results = soup.find_all("dl", class_="dl")

    for result in results:
        # 提取标题和描述
        title = result.find("dt").get_text(strip=True)
        description = result.find("dd", class_="dd answer").get_text(strip=True)
        print(f"标题：{title}")
        print(f"内容摘要：{description}")
        print("-"*100)
if __name__ == "__main__":
    search_query = "能装5个24寸行李箱饿的是货拉拉的什么车型"
    crawl_baidu_zhidao(search_query)
    # import requests
    # from bs4 import BeautifulSoup
    #
    # search_word = 'Python'  # 搜索关键词
    # url = f"https://zhidao.baidu.com/search?word={search_word}"
    #
    # headers = {
    #     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3'}
    #
    # response = requests.get(url, headers=headers)
    # soup = BeautifulSoup(response.text, "html.parser")
    #
    # # 获取问题列表。注意，此处的CSS选择器可能会因为百度知道的页面结构变动而失效
    # questions = soup.select('.dt a')
    #
    # for question in questions:
    #     title = question.get_text()
    #     question_url = question.get('href')
    #     print(f"问题标题: {title}\n问题链接: {question_url}\n---")