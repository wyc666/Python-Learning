import urllib
import urlparse

def print_list(list):
    for i in list:
        print i

def progress(blk, blk_size, total_size):
    print ('%d/%d - %0.2f%%' % (blk*blk_size, total_size, (float)(blk*blk_size)/total_size))

def demo():
    content = urllib.urlopen('http://blog.kamidox.com')
    http_message = content.info()
    print_list(http_message)
    content.readlines
    # for i in range(10):
    #     print content.readline

def url_parse(url):
    result = urlparse.urlparse(url)
    print result
    query = urlparse.parse_qs(result.query)
    print query

if __name__ == '__main__':
    # demo()
    url_parse('https://www.baidu.com/s?tn=80035161_2_dg&wd=%E9%9B%85%E8%99%8E%E8%B4%A2%E7%BB%8F%E7%9A%84api')