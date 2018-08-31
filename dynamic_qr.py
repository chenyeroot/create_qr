from MyQR import myqr

urls = "https://m.weike.fm/liveroom/24130413"

#生成动图二维码
myqr.run(urls,  #需要转化成二维码的链接
         picture = '.../皮卡丘.gif', #作为背景的动态图
         colorized = True,
         save_name = '.../catfish.gif' #注意，后缀格式是gif
         )
