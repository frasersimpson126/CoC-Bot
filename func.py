import os
import time as t
from PIL import Image, ImageEnhance
import easyocr
import random as r

reader = easyocr.Reader(['en'])

def tap(x, y, port):
    os.system(f'"C:\Windows\platform-tools\\adb.exe" -s emulator-{str(port)} shell input tap {str(x)} {str(y)}')


def swipe(port): 
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' shell  input touchscreen swipe 1450 150 900 650 500 ')

def swipe2(port): 
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' shell  input touchscreen swipe 1900 850 100 850 500 ')

def find(port): 
  tap(100, 1000, port)
  t.sleep(0.3)
  tap(1375, 650, port)

def next(port):
  tap(1750, 800, port)


def checkloot(port):
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' shell screencap -p /sdcard/Pictures/' + port + 'val.png ')
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' pull sdcard/Pictures/ ')
  print("captured")
  t.sleep(2)

  with Image.open("Pictures/"+port+'val.png') as photo:


    (left, upper, right, lower) = (97, 155, 285, 295)
    loot = photo.crop((left, upper, right, lower))

     # Convert to grayscale
    loot = loot.convert('L')
    # Increase contrast
    loot = ImageEnhance.Contrast(loot).enhance(2.0)
    # Binarize (convert to black and white)
    loot = loot.point(lambda x: 0 if x < 250 else 255)

    loot = loot.save("Pictures/"+ port +"val.png")

    checkloot.result = reader.readtext(("Pictures/"+ port +"val.png"), allowlist='0123456789', detail = 0)
    if len(checkloot.result) < 3:
      checkloot.result = ["0", "0", "0"]  # Default values if OCR fails


def checktrophies(port):
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' shell screencap -p /sdcard/Pictures/' + port + 'trophies.png ')
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' pull sdcard/Pictures/ ')
  print("captured")
  t.sleep(2)

  with Image.open("Pictures/"+port+'trophies.png') as photo:


    (left, upper, right, lower) = (130, 160, 255, 210)
    trophies = photo.crop((left, upper, right, lower))

     # Convert to grayscale
    trophies = trophies.convert('L')
    # Increase contrast
    trophies = ImageEnhance.Contrast(trophies).enhance(2.0)
    # Binarize (convert to black and white)
    trophies = trophies.point(lambda x: 0 if x < 240 else 255)

    trophies = trophies.save("Pictures/"+ port +"trophies.png")

    checktrophies.result = reader.readtext(("Pictures/"+ port +"trophies.png"), allowlist='0123456789', detail = 0)



def checkpixel(port):
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' shell screencap -p /sdcard/Pictures/' + port + 'return.png ')
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' pull sdcard/Pictures/ ')

  checkp = Image.open("Pictures/"+ port +'return.png')
  if checkp.getpixel((898, 909)) == checkp.getpixel((969, 938)):
    return(True)
  else:
    return(False)


def checkpixelBB(port,x,y):

  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' shell screencap -p /sdcard/Pictures/' + port + 'bb.png ')
  os.system('"C:\Windows\platform-tools\\adb.exe" -s emulator-' + port + ' pull sdcard/Pictures/')

  checkp = Image.open("Pictures/"+ port +'bb.png')
  return(str(checkp.getpixel((x, y))))

