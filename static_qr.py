from MyQR import myqr

urls = "https://m.weike.fm/liveroom/24130413"

#带背景图的二维码
myqr.run(
    #先把这个网站转化成二维码
    urls,
    #背景图的路径
    picture = '.../logo.png',
    colorized = True,
    #输出的二维码成品
    save_name = 'logon_Python.png'
)
