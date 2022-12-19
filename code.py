"""CircuitPython Essentials Internal RGB LED red, green, blue example"""
"""Código para mostrar un color RGB en el dotstar del microcontrolador dependiendo de la letra en el mensaje que el usuario escriba"""

import time
import board
import adafruit_dotstar
import neopixel

led = adafruit_dotstar.DotStar(board.APA102_SCK, board.APA102_MOSI, 1)
led.brightness = 0.3
letters = []

def switch(letter):
    if letter == "a" or letter == "A":
        led[0] = (255, 0, 0) # color: red
        time.sleep(1)
    elif letter == "b" or letter == "B":
        led[0] = (255, 124, 0) # color: orange
        time.sleep(1)
    elif letter == "c" or letter == "C":
        led[0] = (255, 220, 0) # color: yellow
        time.sleep(1)
    elif letter == "d" or letter == "D":
        led[0] = (85, 255, 0) # color: green
        time.sleep(1)
    elif letter == "e" or letter == "E":
        led[0] = (0, 255, 212) # color: cyan
        time.sleep(1)
    elif letter == "f" or letter == "F":
        led[0] = (0, 77, 255) # color: blue
        time.sleep(1)
    elif letter == "g" or letter == "G":
        led[0] = (97, 0, 255) # color: purple
        time.sleep(1)
    elif letter == "h" or letter == "H":
        led[0] = (182, 0, 255) # color: light purple
        time.sleep(1)
    elif letter == "i" or letter == "I":
        led[0] = (255, 0, 166) # color: pink
        time.sleep(1)
    elif letter == "j" or letter == "J":
        led[0] = (175, 68, 35) # color: terracota
        time.sleep(1)
    elif letter == "k" or letter == "K":
        led[0] = (199, 199, 191) # color: silver
        time.sleep(1)
    elif letter == "l" or letter == "L":
        led[0] = (20, 49, 23) # color: dark green
        time.sleep(1)
    elif letter == "m" or letter == "M":
        led[0] = (74, 37, 2) # color: brown
        time.sleep(1)
    elif letter == "n" or letter == "N":
        led[0] = (255, 196, 196) # color: light pink
        time.sleep(1)
    elif letter == "ñ" or letter == "Ñ":
        led[0] = (0, 0, 0) # color: black
        time.sleep(1)
    elif letter == "o" or letter == "O":
        led[0] = (255, 255, 177) # color: lemon
        time.sleep(1)
    elif letter == "p" or letter == "P":
        led[0] = (255, 131, 131) # color: coral
        time.sleep(1)
    elif letter == "q" or letter == "Q":
        led[0] = (172, 111, 53) # color: copper
        time.sleep(1)
    elif letter == "r" or letter == "R":
        led[0] = (147, 122, 32) # color: gold
        time.sleep(1)
    elif letter == "s" or letter == "S":
        led[0] = (108, 3, 3) # color: maroon
        time.sleep(1)
    elif letter == "t" or letter == "T":
        led[0] = (61, 61, 27) # color: olive
        time.sleep(1)
    elif letter == "u" or letter == "U":
        led[0] = (68, 95, 111) # color: dark blue
        time.sleep(1)
    elif letter == "v" or letter == "V":
        led[0] = (181, 222, 230) # color: pastel blue
        time.sleep(1)
    elif letter == "w" or letter == "W":
        led[0] = (197, 197, 231) # color: lavender
        time.sleep(1)
    elif letter == "x" or letter == "X":
        led[0] = (211, 243, 186) # color: light green

    elif letter == "y" or letter == "Y":
        led[0] = (243, 199, 128) # color: light orange

    elif letter == "z" or letter == "Z":
        led[0] = (232, 222, 209) # color: beige

    elif letter == " ":
        led[0] = (255, 255, 255) # color: white


while True:
    print('Escribe tu mensaje:')
    x = input()
    for i in range(0, len(x)):
        letters.append(ord(x[i]))
    
    if all(65 <= elem <= 90 or 97 <= elem <= 122 or elem == 241 or elem ==209 or elem == 32 for elem in letters):
        for j in range(0, len(x)):
            switch(x[j])
            time.sleep(4)
    else:
        print("No se aceptan caracteres especiales")
