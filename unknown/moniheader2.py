# coding=utf-8
import urllib.request  # 3.x 版本的库
import http.cookiejar


def makeMyOpener(head=None):
    if head is None:
        head = {
            'Connection': 'Keep-Alive',
            'Accept': 'text/html, application/xhtml+xml, */*',
            'Accept-Language': 'en-US,en;q=0.8,zh-Hans-CN;q=0.5,zh-Hans;q=0.3',
            'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64; Trident/7.0; rv:11.0) like Gecko'
        }
    cj = http.cookiejar.CookieJar()
    opener = urllib.request.build_opener(urllib.request.HTTPCookieProcessor(cj))
    header = []
    for key, value in head.items():
        elem = (key, value)
        header.append(elem)
    opener.addheaders = header
    return opener


def save_file(data):
    save_path = 'D:\\sbuu\\temp.out'
    f_obj = open(save_path, 'wb')  # wb 表示打开方式
    f_obj.write(data)
    f_obj.close()


oper = makeMyOpener()
uop = oper.open('http://www.baidu.com/', timeout=1000)
data = uop.read()
print(data.decode())

save_file(data)
