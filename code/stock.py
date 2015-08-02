# -*- coding: utf-8 -*-
# gusimiu@baidu.com
# 

import time

class DailyData:
    def __init__(self, 
            date,
            open,
            high,
            low,
            close,
            volume,
            adj_close):
        self.date = date
        self.open = float(open)
        self.close = float(close)
        self.high = float(high)
        self.low = float(low)
        self.volume = int(volume)
        self.adjust_close = float(adj_close)
        
        self.epoch_date = time.mktime(time.strptime(date, '%Y-%m-%d'))

if __name__ == '__main__':
    pass    
