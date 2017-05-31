#!/usr/bin/env python
import json
import re
import codecs

def write_file(url):
    # TODO: Doesn't work yet
    # This function will write to article.txt
    js = get_json_from_url(url)
    with open(article.txt,'w') as f:
        f.write(js)
    return


def main():
    # Open from file
    try:
        with open('article.txt','r',encoding='utf-8') as f:
            text = f.read()
    except:
        with open('article.txt','r') as f:
            text = f.read()

    # Read and parse json
    js = json.loads(text)
    title = js['result']['article']['title']
    content = js['result']['article']['translatedContent']
    content = re.sub(r'<.*?>','',content)

    # Save file
    with codecs.open(title,'w','utf-8') as f:
        f.write(content)


if __name__=="__main__":
    main()


# # Unclear how to automatically retrieve these things 
# import requests
# import json
# import lxml.html
# import ast

# main_url = 'http://newslibrary.naver.com/viewer/index.nhn?articleId=1990092500209221005&edtNo=2&printCount=1&publishDate=1990-09-25&officeId=00020&pageNo=21&printNo=21251&publishType=00020'
# main_text = requests.get(main_url).text
# # Interesting: the following are equivalent
# js = ' '.join(tree.xpath('//div[@id="viewer_wrap"]/script/text()')) 
# js = tree.find('.//div[@id="viewer_wrap"]/script').text
# start = js.find('aFlashVars')
# end = js[start:].find('];')
# temp = js[start:start+end+1].partition('=')[2].strip().replace('\r','').replace('\n','').replace('\t','')
# temp = temp.replace(' + nViewerSize','')
# paramlist = ast.literal_eval(temp)
# form_data2 = {i.split('=')[0]:i.split('=')[1] for i in paramlist if i.split('=')[1]!=''}

# article1 = requests.post('http://newslibrary.naver.com/api/article/list/json?urlKey=articleInfo&requestID=3&target=viewer&viewID=app_articleInfo',
#     data = {'includeEtcEntity':'true',
#             'detailCode':'1001100001000000110111100000001010000000001',
#             'publishType':'00020',
#             'detailYn':'false',
#             'startPageNo':'8',
#             'printNo':'18305',
#             'date':'1981-04-02',
#             'includeBlind':'true',
#             'officeId':'00020',
#             'pageCount':'2'})

# headers = {
#     'Host':'newslibrary.naver.com',
#     'Referer':'http://newslibrary.naver.com/swf/NewsTimeMachine.swf?20161130112608',
#     'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.11; rv:53.0) Gecko/20100101 Firefox/53.0'
# }

# form_data = {
#     'date':'1990-09-25',
#     'startPageNo':'20',
#     'printNo':'21251',
#     'pageCount':'2',
#     'publishType':'00020',
#     'includeBlind':'true',
#     'detailYn':'false',
#     'includeEtcEntity':'true',
#     'officeid':'00020',
#     'detailCode':'1001100001000000110111100000001010000000001'
#     }

# url1 = 'http://newslibrary.naver.com/api/article/list/json?urlKey=articleInfo&requestID=3&target=viewer&viewID=app_articleInfo'

# form_data.update(form_data2)
# article1 = requests.post(url1,
#     data = form_data)

# text1 = article1.text
# print(text1)