import os
from MyQR import myqr

def create_img(url_words,img_size,save_name=None,photo_path=None,has_color=False,save_path=os.getcwd()):
    myqr.run(
        #跳转到的网页链接
        words=url_words,
        #生成的二维码的大小
        version=img_size,
        #二维码的图片
        picture=photo_path,
        #图片是否是彩色
        colorized=has_color,
        #图片的色度
        # contrast=color_size,
        #图片亮度
        # brightness=light_size,
        #图片保存的文件名
        save_name=save_name,
        #图片保存到的目录
        save_dir=save_path
    )

create_img(url_words='http://www.wzdh113.com',img_size=3)