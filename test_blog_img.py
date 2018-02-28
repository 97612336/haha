import json
import urllib.request as ur
from urllib.request import Request
def upload_img(img_data):
    url=r'http://x.mouto.org/wb/x.php?up'
    #设置headers
    headers={
        "User-Agnet": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 "
                      "(KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36",
    }
    #小图
    little_img=r'https://ws1.sinaimg.cn/thumbnail/'
    #中图
    middle_img=r'https://ws1.sinaimg.cn/mw690/'
    #大图
    big_img=r'https://ws1.sinaimg.cn/large/'
    #创建request请求
    request=Request(url=url,data=img_data)
    #打开请求,获取响应
    response=ur.urlopen(request)
    #获取响应的数据
    json_data=response.read().decode('utf-8')
    #加载json数据,获取加载后的字典
    json_dict=json.loads(json_data)
    #获取后缀链接:
    img_url=json_dict['pid']+'.jpg'
    #获取图片
    big_img=big_img+img_url
    middle_img=middle_img+img_url
    little_img=little_img+img_url

    dict_url={
        'large_img':big_img,
        'middle_img':middle_img,
        'small_img':little_img
    }
    return dict_url