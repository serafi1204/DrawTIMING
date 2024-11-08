from . import Module
from .visio import style, Shape, Visio, Page, Group, Line, makeGroup
from .Signal import Wave, Signal

def readData(source:str):
    waves = []
    
    for line in source.split('\n'):
        ss = line.split(':')
        if (len(ss) != 3): continue
        
        name = ss[0].strip()
        thickness = int(ss[1].strip())
        signals = ss[2].strip().split(',')
        
        wave = Wave(name, thickness)
        for signal in signals:
            if (signal.strip()==''): continue
            
            ss = signal.strip().split(' ')
            name = ss[0]
            beginCycle = int(ss[1].strip())
            endCycle = int(ss[2].strip())
            
            wave.addSignal(Signal(name, beginCycle, endCycle))
        
        waves.append(wave)
        
    return waves

def drawLabel(page, name:str, y:int, thickness:int):
    w = max(5, len(name)/5)
    h = style.fontSizeSub/10
    
    label = Shape(page,Visio.masterRect)
    label.onlyText()
    label.pos(-w/2, -(0.5*thickness+y))
    label.size(w, h)
    label.style(fontAlign=2, fontSize=style.fontSizeMain, colorFillClear=True, lineClear=True)
    label.visioObject.Characters.Text = name
    

def drawSignal(page, signal:Signal, thickness:int, y:int):
    h = signal.endCycle - signal.beginCycle + 1
    w = thickness
    
    label = Shape(page,Visio.masterRect)
    label.pos(signal.beginCycle+w/2, -(h/2+y))
    label.size(w, h)
    label.style(fontSize=style.fontSizeSub)
    label.visioObject.Characters.Text = signal.name

def drawTiming(page, waves:list, xOffset=0.5, yOffset=0.5):
    # Draw Backgroud
    W = max([wave.lastCycle for wave in waves])+1
    W = (int(W/5)+1)*5+1
    H = len(waves)
    
    # X axis
    xAxis = Line(page)
    xAxis.staightLine(-0.5, 0, W+xOffset, 0)
    # Y axis
    y = sum([wave.thickness for wave in waves[:H-1]])+yOffset*(H+1)
    yAxis = Line(page)
    yAxis.staightLine(0, 0.5, 0, -H-y)
    
    label = Shape(page,Visio.masterRect)
    label.onlyText()
    label.pos(0, 0.8)
    label.size(1, style.fontSizeSub/10)
    label.style(fontAlign=1, fontSize=style.fontSizeMain, colorFillClear=True, lineClear=True)
    label.visioObject.Characters.Text = f"{0}"
    
    axisGroup = [xAxis, yAxis, label]
    
    for i in range(1, W):
        yAxisSub = Line(page)
        yAxisSub.staightLine(i, 0.5, i, -H-y)
        
        color = "RGB(100, 100, 100)" if (i%5==0) else "RGB(200, 200, 200)"
        lineType = 1 if (i%5==0) else 16
        yAxisSub.style(color=color, lineType=lineType)
        
        label = Shape(page,Visio.masterRect)
        label.onlyText()
        label.pos(i, 0.8)
        label.size(2, style.fontSizeSub/10)
        label.style(fontAlign=1, fontSize=style.fontSizeMain, colorFillClear=True, lineClear=True)
        label.visioObject.Characters.Text = f"{i}"
        
        axisGroup.append(label)
        axisGroup.append(yAxisSub)
        
    Group(axisGroup)
    
    # Draw wave
    y = yOffset
    for i, wave in enumerate(waves):
        drawLabel(page, wave.name, y, wave.thickness)
        for signal in wave.signal:
            drawSignal(page, signal, wave.thickness, y)
            
        y += wave.thickness + yOffset
    y -= wave.thickness

    
            
        
        