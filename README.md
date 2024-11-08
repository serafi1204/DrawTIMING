# DrawTIMING
This project generates a timing diagram based on the input string.

# DEMO VEIEO
[![Video Label](http://img.youtube.com/vi/EYCsdMdQp6E/0.jpg)](https://www.youtube.com/watch?v=EYCsdMdQp6E)

# HOW TO USE
### Preparation
    pip install pywin32

### Input rule
Fill in the item enclosed in {}.

    {wave0 name}:{thickness}:{signal0 txet} {start cycle} {end cycle}, {signal1 txet} {start cycle} {end cycle}, ...
    {wave1 name}:{thickness}:{signal0 txet} {start cycle} {end cycle}, {signal1 txet} {start cycle} {end cycle}, ...
    {wave2 name}:{thickness}:{signal0 txet} {start cycle} {end cycle}, {signal1 txet} {start cycle} {end cycle}, ...
    ...
    
### Basics
    # Essential part
    from lib.visio import Page
    from lib.drawing import drw

    page = addPage()

    # Drawing timing diagram
    waves = readData(input()) # Read input string
    drawTiming(page, wave) # Draw timing diagram
    page.CenterDrawing() # Move diagram to center of page

### main function
drawTiming(wavws:list(Wave), xOffet:int, yOffset:int)
![드로잉1](https://github.com/user-attachments/assets/872766b3-8f3e-47aa-a90e-07b7b19a710c)

# TODO
- Coloring
