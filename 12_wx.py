import wx

app = wx.App()
win = wx.Frame(None, title="Simple Editor")

loadButton = wx.Button(win, label='Open', pos=(215,5), size=(80,25))

saveButton = wx.Button(win, label='Save', pos=(300,5), size=(80,25))

win.Show()

app.MainLoop()