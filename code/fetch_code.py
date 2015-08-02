# -*- coding: utf-8 -*-
# gusimiu@baidu.com
# 

import urllib
import re
import sys

def fetch_all_chinese_code():
    f=urllib.urlopen('http://bbs.10jqka.com.cn/codelist.html')
    ret = []
    for line in f.readlines():
        if '<li><a href' in line:
            m = re.search('>([^>]*)</a', line)
            if m:
                info = m.groups()[0]
                arr = info.split(' ')
                if len(arr)<2:
                    print >> sys.stderr, 'Error line: %s (ignored)' % info.decode('gb18030').encode('utf-8')
                    continue
                elif len(arr)>2:
                    print >> sys.stderr, 'merge space: %s' % info.decode('gb18030').encode('utf-8')
                    name = ''.join(arr[:-2])
                    code = arr[-1]
                else:
                    name, code = arr
                ret.append( (name.decode('gb18030'), code) )
    return ret

if __name__ == '__main__':
    ret = fetch_all_chinese_code()
    for name, code in ret:
        print '%s\t%s' % (name.encode('utf-8'), code)
