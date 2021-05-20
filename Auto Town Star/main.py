from screen_search import *
import pyautogui
import time

searchSellButton = Search("imgs/btnComprar.png")
searchSelectGrapes = Search("imgs/selectGrapesBlack.png")
searchSelectedGrapes = Search("imgs/selectedGrapesBlack.png")
searchSelectWine = Search("imgs/selectWineBlack.png")
searchSelectedWine = Search("imgs/selectedWineBlack.png")

ventaUvas = 0
ventaVino = 0

while True:
    try:
        print(f"Se ha vendido {ventaUvas} de veces.")
        pyautogui.click(x=371, y=839)
        time.sleep(0.5)
        pyautogui.click(x=957, y=1013)
        time.sleep(10)

        venta = False

        while not venta:
            continuar = False
            posSelectedWine = searchSelectedWine.imagesearch()
            if posSelectedWine[0] != -1:
                posSellBtn = searchSellButton.imagesearch()
                if posSellBtn[0] != -1:
                    pyautogui.click(x=(posSellBtn[0]+10), y=(posSellBtn[1]+10))
                    venta = True
                    ventaVino += 1
                    continuar = False
                else:
                    continuar = True
            else:
                continuar = True


            if continuar == True:
                continuar = False    
                posSelectWine = searchSelectWine.imagesearch()
                if posSelectWine[0] != -1:
                    pyautogui.click(x=(posSelectWine[0]+10), y=(posSelectWine[1]+10))
                    time.sleep(2)
                    posSellBtn = searchSellButton.imagesearch()
                    if posSellBtn[0] != -1:
                        pyautogui.click(x=(posSellBtn[0]+10), y=(posSellBtn[1]+10))
                        venta = True
                        ventaVino += 1
                        continuar = False
                    else:
                        continuar = True
                else:
                    continuar = True


            posSelectedGrapes = searchSelectedGrapes.imagesearch()
            if posSelectedGrapes[0] != -1:
                posSellBtn = searchSellButton.imagesearch()
                if posSellBtn[0] != -1:
                    pyautogui.click(x=(posSellBtn[0]+10), y=(posSellBtn[1]+10))
                    venta = True
                    ventaUvas += 1
                    continuar = False
                else:
                    continuar = True
            else:
                continuar = True


            if continuar == True:
                continuar = False    
                posSelectGrapes = searchSelectGrapes.imagesearch()
                if posSelectGrapes[0] != -1:
                    pyautogui.click(x=(posSelectGrapes[0]+10), y=(posSelectGrapes[1]+10))
                    time.sleep(2)
                    posSellBtn = searchSellButton.imagesearch()
                    if posSellBtn[0] != -1:
                        pyautogui.click(x=(posSellBtn[0]+10), y=(posSellBtn[1]+10))
                        venta = True
                        ventaUvas += 1
                        continuar = False
                    else:
                        continuar = True
                else:
                    continuar = True

            if continuar == True:
                time.sleep(5)

        time.sleep(210)
    except:
        print("Error")