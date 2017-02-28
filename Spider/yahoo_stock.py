import urllib
import datetime

def download_stock_data(stock_list):
    for stock_id in stock_list:
        url = 'http://ichart.yahoo.com/table.csv=?s=' + stock_id
        file_name = stock_id + '.csv'
        urllib.urlretrieve(url, file_name)

def download_stock_data_in_period(stock_list, start_date, end_date):
    for stock_id in stock_list:
        params = {'a': start_date.month - 1, 'b': start_date.day, 'c': start_date.year,
                  'd': end_date.month - 1, 'e': end_date.day, 'f': end_date.year, 's': stock_id}
        url = 'http://ichart.yahoo.com/table.csv?'
        qs = urllib.urlencode(params)
        url = url + qs
        file_name = '%s_%d%d%d_%d%d%d.csv' % (stock_id, start_date.year, start_date.month, start_date.day,
                                                        end_date.year, end_date.month, end_date.day)
        urllib.urlretrieve(url, file_name)


if __name__ == '__main__':
    stock_list = ['300001.sz', '300002.sz']
    start_date = datetime.date(year=2015, month=11, day=25)
    end_date = datetime.date(year=2015, month=12, day=17)
    # download_stock_data(stock_list)
    download_stock_data_in_period(stock_list, start_date, end_date)