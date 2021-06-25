import pyautogui as pt
import pyperclip

while True:
    try:
        position1 = pt.locateOnScreen("img_1.png", confidence=.70)
        x = position1[0]
        y = position1[1]
    except:
        print('wait')
        continue


    def getMessage():
        global x, y
        position = pt.locateOnScreen("img_1.png", confidence=.70)
        x = position[0]
        y = position[1]
        # print(x, y)
        pt.moveTo(x, y)
        pt.moveTo(x - 70, y)
        pt.click()
        position2 = pt.locateOnScreen("img.png", confidence=.60)
        x = position2[0]
        y = position2[1]
        pt.moveTo(x, y)
        pt.moveTo(x + 45, y - 45)
        pt.tripleClick()
        pt.rightClick()
        pt.moveRel(12, -120)
        pt.click()
        message = pyperclip.paste()
        # message = "p"
        print(message)
        return message


    def postResponse(message):
        global x, y
        position = pt.locateOnScreen("img.png", confidence=.60)
        x = position[0]
        y = position[1]

        # pt.moveTo(x + 200, y + 20, duration=0.5)
        # pt.click()
        # pt.typewrite(message, interval=0.01)
        # pt.typewrite("\n", interval=0.01)


    postResponse(getMessage())

# getMessage()
