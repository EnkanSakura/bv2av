# coding=UTF-8

import sys
import win32api
import wx

APP_TITLE = u'AV<—>BV'
APP_ICON = './icon.ico'

table = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
tr = {}
for i in range(58):
    tr[table[i]] = i
s = [11, 10, 3, 8, 4, 6]
xor = 177451812
add = 8728348608


def dec(x):
    r = 0
    for i in range(6):
        r += tr[x[s[i]]] * 58 ** i
    return (r - add) ^ xor


def enc(x):
    x = (x ^ xor) + add
    r = list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]] = table[x // 58 ** i % 58]
    return ''.join(r)

# 上述源码来自于知乎回答
# 如何看待 2020 年 3 月 23 日哔哩哔哩将稿件的「av 号」变更为「BV 号」？ - mcfx的回答 - 知乎
# https://www.zhihu.com/question/381784377/answer/1099438784


class mainFrame(wx.Frame):
    '''程序主窗口类，继承自wx.Frame'''

    def __init__(self, parent):
        '''构造函数'''

        wx.Frame.__init__(self, parent, -1, APP_TITLE, style=wx.DEFAULT_FRAME_STYLE ^ wx.MAXIMIZE_BOX)
        self.SetBackgroundColour(wx.Colour(224, 224, 224))
        self.SetSize((280, 155))
        self.SetMaxSize((280, 155))
        self.SetMinSize((280, 155))
        self.Center()

        if hasattr(sys, "frozen") and getattr(sys, "frozen") == "windows_exe":
            exeName = win32api.GetModuleFileName(win32api.GetModuleHandle(None))
            icon = wx.Icon(exeName, wx.BITMAP_TYPE_ICO)
        else:
            icon = wx.Icon(APP_ICON, wx.BITMAP_TYPE_ICO)
        self.SetIcon(icon)

        wx.StaticText(self, -1, u'AV：', pos=(-40, 25), size=(100, -1), style=wx.ALIGN_RIGHT)
        wx.StaticText(self, -1, u'BV：', pos=(-40, 65), size=(100, -1), style=wx.ALIGN_RIGHT)

        self.tc1 = wx.TextCtrl(self, -1, '', pos=(60, 25), size=(150, -1), name='TC01', style=wx.TE_CENTER)
        self.tc2 = wx.TextCtrl(self, -1, '', pos=(60, 65), size=(150, -1), name='TC02', style=wx.TE_CENTER)

        # 控件事件
        self.tc1.Bind(wx.EVT_TEXT, self.EvtText)
        self.tc2.Bind(wx.EVT_TEXT, self.EvtText)


        # 系统事件
        self.Bind(wx.EVT_CLOSE, self.OnClose)
        self.Bind(wx.EVT_SIZE, self.On_size)

    def EvtText(self, evt):
        '''输入框事件函数'''

        obj = evt.GetEventObject()
        objName = obj.GetName()
        text = evt.GetString()

        if objName == 'TC01':
            self.tc2.SetValue(enc(int(text)))
        elif objName == 'TC02':
            self.tc1.SetValue(str(dec(text)))

    def On_size(self, evt):
        '''改变窗口大小事件函数'''

        self.Refresh()
        evt.Skip()  # 体会作用

    def OnClose(self, evt):
        '''关闭窗口事件函数'''

        dlg = wx.MessageDialog(None, u'确定要关闭本窗口？', u'操作提示', wx.YES_NO | wx.ICON_QUESTION)
        if dlg.ShowModal() == wx.ID_YES:
            self.Destroy()


class mainApp(wx.App):
    def OnInit(self):
        self.SetAppName(APP_TITLE)
        self.Frame = mainFrame(None)
        self.Frame.Show()
        return True


if __name__ == "__main__":
    app = mainApp()
    app.MainLoop()
