import urllib2
from HTMLParser import HTMLParser
import sys
reload(sys)
sys.setdefaultencoding('utf8')

class MovieParser(HTMLParser):
    def __init__(self):
        HTMLParser.__init__(self)
        self.movies = []

    def handle_starttag(self, tag, attrs):
        def _attr(attr_list, attr_name):
            for attr in attr_list:
                if attr[0] == attr_name:
                    return attr[1]
            return None

        if tag == 'li' and _attr(attrs, 'data-category') == 'nowplaying':
            movie = {}
            movie['title'] = _attr(attrs, 'data-title')
            movie['director'] = _attr(attrs, 'data-director')
            movie['score'] = _attr(attrs, 'data-score')
            movie['actors'] = _attr(attrs, 'data-actors')
            self.movies.append(movie)
            print '%(title)s|%(director)s|%(score)s|%(actors)s' % movie

def get_now_playing_movies(url):
    headers = {"User-Agent": "Mozilla/5.0"}
    request = urllib2.Request(url, headers=headers)
    content = urllib2.urlopen(request)
    parser = MovieParser()
    parser.feed(content.read())
    content.close()

if __name__ == "__main__":
    url = "https://movie.douban.com/nowplaying/nanjing/"
    get_now_playing_movies(url)