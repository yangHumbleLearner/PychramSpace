# # user_name = 'hyw'
# # print(user_name.lower())
# # print(user_name.upper())
# # print(user_name.title())
# # var = 'hywzhengshuai'
# # print(var)
# # user_name1=' hyw '
# # print('\t'+ user_name1.lstrip() + '\n\n')
# # print('\t'+ user_name1.rstrip() + '\n\n')
# # print('\t'+ user_name1.strip() + '\n\n')
# # name_list=['彭于晏','华晨宇','李嘉诚']
# # name_list.insert(0,'hyw')
# # print(name_list)
# # name_list.insert(2,'料贵妃')
# # print(name_list)
# # for name in name_list:
# #     print('尊敬的：' + name + '（先生/女士），诚挚的邀请您参加今晚的宴会！')
#
# # print('抱歉只有两位可以共进晚餐')
# # n= int(len(name_list))
# # while n > 2 :
# #     lastname = name_list.pop()
# #     print(lastname + '别来了')
# # pizzas=['pizzA','pizzB','pizzC']
# # for temp in pizzas :
# #     print(temp)
#
# # temp = list(range(1,101))
# # print(min(temp))
# # print(max(temp))
# # print(sum(temp))
# #3的倍数 ：创建一个列表， 其中包含3~30内能被3整除的数字； 再使用一个for 循环将这个列表中的数字都打印出来。
#
# # temp = list(range(1,21,2))
# # for t in temp:
# #     print(t)
# # temp = list(range(3,31))
# # temp1=[]
# # for t in temp :
# #     if t % 3 ==0 :
# #         temp1.append(t)
# # print(temp1)
# # temp  = list(range(1,11,1))
# # temp2 = []
# # for t in temp :
# #     t = t ** 2
# #     temp2.append(t)
# # print(temp2)
# # for value in range(3,31,5):
# #     print(value)
# # lists = ['1','2','3','4','5','6','7']
# # print('The first three items in the list are:')
# # temp1 = lists[:3]
# # for t1 in temp1:
# #     print(t1)
# # print('Three items fromthe middle of the list are:' )
# # temp2 = lists[2:5]
# # for t2 in temp2:
# #     print(t2)
# # print('Three items fromthe middle of the list are:')
# # temp3 = lists[-3:]
# # for t3 in temp3:
# #     print(t3)
# # car = 'subaru'
# # print("Is car == 'subaru'? I predict True.")
# # print(car == 'subaru')
# # print("\nIs car == 'audi'? I predict False.")
# # print(car == 'audi')
# # car = 'bmw'
# # cars= ['bmw','audi']
# # print (car == cars[0])
# # mayun = {'first_name':'Ma','last_name':'Yun','age':'54','city':'HangZhou'}
# # # for key,value in mayun.items() :
# # #     print('key:' + key)
# # #     print('value:' + value)
# # dics = {'list':'列表','var':'变量','int':'整型','boolean':'布尔','str':'字符串'}
# # print('dics[\'list\']'+':' + dics['list'])
# # print('dics[\'var\']'+':' + dics['var'])
# # print('dics[\'int\']'+':' + dics['int'])
# # print('dics[\'boolean\']'+':' + dics['boolean'])
# # print('dics[\'str\']'+':' + dics['str'])
# # favorite_languages = {
# #     'amada':'C',
# #     'jacky':'java',
# #     'frank':'c++',
# #     'polly':'php',
# #     'maily':'.net'
# #     }
# # lists = ['amada','jacky','mayun','admin']
# # temp = []
# # for k in favorite_languages.keys():
# #     temp.append(k)
# #     print(temp)
# #     for s in lists :
# #         if s in temp:
# #             print('1')
# #         else:
# #             print('2')
# # coding:utf-8
# import urllib
#
# domain = 'http://www.liaoxuefeng.com'           #廖雪峰的域名
# path = r'C:\Users\cyhhao2013\Desktop\temp\\'    #html要保存的路径
#
# # 一个html的头文件
# input = open(r'C:\Users\cyhhao2013\Desktop\0.html', 'r')
# head = input.read()
#
# # 打开python教程主界面
# f = urllib.urlopen("http://www.liaoxuefeng.com/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000")
# home = f.read()
# f.close()
#
# # 替换所有空格回车（这样容易好获取url）
# geturl = home.replace("\n", "")
# geturl = geturl.replace(" ", "")
#
# # 得到包含url的字符串
# list = geturl.split(r'em;"><ahref="')[1:]
#
# # 强迫症犯了，一定要把第一个页面也加进去才完美
# list.insert(0, '/wiki/001374738125095c955c1e6d8bb493182103fac9270762a000">')
#
# # 开始遍历url List
# for li in list:
#     url = li.split(r'">')[0]
#     url = domain + url              #拼凑url
#     print (url)
#     f = urllib.urlopen(url)
#     html = f.read()
#
#     # 获得title为了写文件名
#     title = html.split("<title>")[1]
#     title = title.split(" - 廖雪峰的官方网站</title>")[0]
#
#     # 要转一下码，不然加到路径里就悲剧了
#     title = title.decode('utf-8').replace("/", " ")
#
#     # 截取正文
#     html = html.split(r'<!-- block main -->')[1]
#     html = html.split(r'<h4>您的支持是作者写作最大的动力！</h4>')[0]
#     html = html.replace(r'src="', 'src="' + domain)
#
#     # 加上头和尾组成完整的html
#     html = head + html+"</body></html>"
#
#     # 输出文件
#     output = open(path + "%d" % list.index(li) + title + '.html', 'w')
#     output.write(html)
#     output.close()
import bs4
print(bs4)
