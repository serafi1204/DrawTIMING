from lib.visio.Page import addPage
from lib.drawing import *
from lib.debug import *

with open("sample.txt", 'r') as f:
    ss = f.read()
    
page = addPage()
wave = readData(ss)
drawTiming(page, wave)
page.CenterDrawing()