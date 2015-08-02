# -*- coding: utf-8 -*-
# gusimiu@baidu.com
# 

import urllib
import sys
import stock

def yahoo_history_data(code, begin_ymd, end_ymd):
    url = ('http://table.finance.yahoo.com/table.csv?s=%s&d=%d&e=%d&f=%d&a=%d&b=%d&c=%d&ignore=.csv&g=d'
            % ( code, 
                end_ymd[1]-1, # end month.
                end_ymd[2], # end day.
                end_ymd[0], # end year.
                begin_ymd[1]-1, # begin month. 
                begin_ymd[2], # begin day.
                begin_ymd[0]  # begin year. 
            ))

    '''
    print >> sys.stderr,  url
    def hook(a,b,c): 
        print a,b,c
    f,d = urllib.urlretrieve(url, reporthook=hook)
    '''

    f,d = urllib.urlretrieve(url)
    ret = []
    for line in file(f).readlines():
        date, open, high, low, close, volume, adj_close = line.strip('\n').split(',')
        if date == 'Date':
            continue
        ret.append( stock.DailyData(date, open, high, low, close, volume, adj_close) )
    return ret

if __name__ == '__main__':
    pass 
