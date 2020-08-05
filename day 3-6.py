# -*- coding: utf-8 -*-
"""
Created on Wed Aug  5 15:16:45 2020

@author: user
"""
a=0
d={}

while a==0:
    print('1. 建立詞彙')
    print('2. 列出所有單字')
    print('3. 中翻英')
    print('4. 英翻中')
    print('5. 測驗學習結果')
    print('6. 離開系統')
    b=int(input('選擇一項服務'))
    if b==1:
        x=0
        while x==0:
            c=input('請輸入中文')
            e=input('請輸入他的英文單字')
            d[c]=e
            r=int(input('如果要退出請按0,繼續按1'))
            if r==0:
                x=x+1
    elif b==2:
        print(d)
    elif b==3:
        x=0
        while x==0:
            c=input('請輸入中文單字')
            for key in d.keys():
                if key==c:
                    e=d[c]
                    print(e)
                    break
                    
                if key not in d:
                    print('查無此單字')
            r=int(input('如果要退出請按0,繼續按1'))
            if r==0:
                x=x+1
    elif b==4:
        x=0
        while x==0:
            e=input('請輸入英文單字')
            for key,value in d.items():
               if value==e:
                   e=d[c]
                   print(c)
                   break
               if value not in d:
                   print('查無此單字')
               
            r=int(input('如果要退出請按0,繼續按1'))
            if r==0:
                x=x+1
    
    elif b==5:
        for key,value in d.items():
           print(key)
           f=input('這個的英文是甚麼?')
           if f==value:
               print('good job')
           if f!=value:
               print('try again')
            
    
    elif b==6:
        break