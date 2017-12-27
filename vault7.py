# -*- coding:utf-8 -*-
#__author__='Kakarotto'

import os
import requests
import re
from urllib import unquote
import time



url='https://wikileaks.org/vault7/document/'

proxies={
    "http":"http://127.0.0.1:1080",
    "https":"https://127.0.0.1:1080",
}

try:
    response=requests.get(url,proxies=proxies)
    content=response.content
    m=re.compile('a href=\"(.*?)\"')
    items=re.findall(m,content)

    for item in items:
        if '../' in item:
            ls=['../releases/','../document/']
            if item not in ls:
                item=item[3:-1]
                item1='https://wikileaks.org/vault7/'+item+'/'
                response = requests.get(item1, proxies=proxies)
                content = response.content
                m = re.compile('a href=\"(.*?)\"')
                downs = re.findall(m, content)
                for down in downs:
                    lss=['../../releases/','../../document/']
                    if '../../' in down and '#' not in down and down not in lss:
                        down=down[6:]
                        down='https://wikileaks.org/vault7/'+down
                        print down

except Exception,e:
    print e