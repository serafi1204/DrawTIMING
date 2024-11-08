class Wave:
    def __init__(self, name, thickness=1):
        self.name = name 
        self.signal = []
        self.thickness = thickness
        self.lastCycle = 0
        
    def addSignal(self, signal):
        if (type(signal) is list):
            addSignal(signal)
        elif (type(signal) is Signal):
            self.lastCycle = max(self.lastCycle, signal.endCycle)
            self.signal.append(signal)
        else:
            raise TypeError
        
class Signal:
    def __init__(self, name, beginCycle, endCycle=-1):
        self.name = name
        self.beginCycle = beginCycle
        self.endCycle = endCycle if (beginCycle!=-1) else beginCycle