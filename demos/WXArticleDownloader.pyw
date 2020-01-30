
import sys,os

sys.path.append(os.path.abspath("../"))
import html2text
import urllib.request as urllib

def fun():
    pass


if __name__ == '__main__':
    import PySimpleGUI as sg

    form = sg.FlexForm('Weixin Article Downloader')
    layout = [
    [sg.Text('Input Article URL')],
    [
    sg.Text('URL',auto_size_text=True), 
    sg.Input('https://mp.weixin.qq.com/s/SUj6Phar0oFs87hlS89V1A',size=(80,1), key='url')
    ],
    [sg.Checkbox('Images', key='img', default=True), sg.Checkbox('Ext-Links', key='link', default=True),],
    [sg.OK("Convert"), sg.Cancel()]
    ]

    button, val = form.Layout(layout).Read()

    if(button != "Convert"): 
        print("user quit")
        exit(0)


    baseurl = val.get("url")
    
    encoding = 'utf-8'
    j = urllib.urlopen(baseurl)
    data = j.read()
    data = data.decode(encoding)
    h = html2text.HTML2Text(baseurl=baseurl)
    h.ignore_links = not val.get("link")
    h.ignore_images = not val.get("img")
    h.body_width = 0

    with open("e:/Temp/wx.md", 'w', encoding=encoding) as f:
        f.write(h.handle(data))

    with open("e:/Temp/wx.html", 'w', encoding=encoding) as f:
        f.write(data)
