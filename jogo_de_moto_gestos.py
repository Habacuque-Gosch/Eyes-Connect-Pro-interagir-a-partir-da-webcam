import cv2
from cvzone.HandTrackingModule import HandDetector
from pynput.keyboard import Key, Controller



video = cv2.VideoCapture(0)

video.set(3,1280)
video.set(4,720)

kb = Controller()

detector = HandDetector(detectionCon=0.8)
estadoAtual = [0,0,0,0,0]

setaDir = cv2.imread('seta esq.PNG')
setaEsq = cv2.imread('seta esq.PNG')

while True:
    sucesso, img = video.read()
    hands,img = detector.findHands(img)
        # ESQUERDA
    tecla = cv2.waitKey(1)
    if  tecla == ord('q'):
        break

    if hands:
        estado = detector.fingersUp(hands[0])
        if estado!=estadoAtual and estado == [1,1,0,0,0]:
            print('ESQUERDA')
            kb.release(Key.space)
            kb.release(Key.right)
            kb.press(Key.left)
        
            if estado == [0,0,0,0,0]:
                kb.release(Key.up)
                kb.release(Key.left)

        # DIREITA
        if estado!=estadoAtual and estado == [0,1,1,0,0]:
            print('DIREITA')
            kb.release(Key.space)
            kb.release(Key.left)
            kb.press(Key.right)

            if estado == [0,0,0,0,0]:
                kb.release(Key.up)
                kb.release(Key.right)

        # ACELERAR
        if estado!=estadoAtual and estado == [0,1,0,0,0]:
            print('Acelerar')
            kb.release(Key.space)
            kb.release(Key.space)
            kb.release(Key.down)
            kb.release(Key.right)
            kb.release(Key.left) 
            kb.press(Key.up)
            if estado == [0,0,0,0,0]:
                kb.press(Key.up)

        # ACELERAR
        if estado!=estadoAtual and estado == [0,0,0,0,1]:
            print('Acelerar')
            kb.release(Key.space)
            kb.release(Key.space)
            kb.release(Key.down)
            kb.release(Key.right)
            kb.release(Key.left)  
            kb.press(Key.down)
            if estado == [0,0,0,0,0]:
                kb.press(Key.up)
    
        # Ré
        if estado!=estadoAtual and estado == [0,0,0,0,0]:
            print('para trás')
            kb.release(Key.space)
            kb.release(Key.up)
            kb.release(Key.right)
            kb.release(Key.left)
            kb.press(Key.down)
            if estado == [0,0,0,0,0]:
                kb.release(Key.down)
    
        if estado!=estadoAtual and estado == [1,1,1,1,1]:
            print('Play')
            kb.release(Key.space)
            kb.release(Key.up)
            kb.release(Key.right)
            kb.release(Key.left)
            kb.press(Key.space)



        # if estado == estadoAtual and estado == [1, 0, 0, 0, 0]:
        #     img[50:216, 984:1230] = setaDir
        # if estado == estadoAtual and estado == [0, 1, 0, 0, 0]:
        #     img[50:216, 50:296] = setaEsq

        estadoAtual = estado

    cv2.imshow('gestos',cv2.resize(img,(640,420)))
    cv2.waitKey(1)