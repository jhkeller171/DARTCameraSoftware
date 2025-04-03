import os
import time

print("      /`·.¸")
print("     /¸...¸`:·")
print(" ¸.·´  ¸   `·.¸.·´)")
print(": © ):´;      ¸  {")
print(" `·.¸ `·  ¸.·´\`·¸)")
print("     `\\´´\¸.·´")
print("DART Lab Camera Software")
print()
vflip = False
hflip = False
width = "1280"
height = "720"
framerate = "30"
ext = ".h264"
vidname = "noNameSet"

while True: #Loop to make the code run infinitely after choosing an option
    print("What Would you like to do?")
    print("-1: Quit")
    print("0: Properties")
    print("1: Live View Camera (Ctrl + C to end preview)")
    print("2: Take a video")
    print("3: Infinite Video")
    print("4: Export Videos")
    answer = input()
    if answer == "-1":
        quit()
    if answer == "0":
        print("What would you like to do?")
        print("0: Quit")
        print("1: Flip the Camera")
        print("2: Change the resolution")
        print("3: Change the framerate")
        print("4: Change the video format")
        answerZero = input()
        if answerZero == "1":
            print("Vertical flip or Horizontal Flip?")
            print("1: Vertical")
            print("2: Horizontal")
            answerZeroOne = input()
            if answerZeroOne == "1":
                if vflip == True:
                    vflip = False
                else:
                    vflip = True
            if answerZeroOne == "2":
                if hflip == True:
                    hflip = False
                else:
                    hflip = True
        if answerZero == "2":
            print("What Resolution would you like?")
            print("0: Back")
            print("1: 1920 x 1080")
            print("2: 1280 x 720 (Default)")
            print("3: 640 x 480")
            resAns = input()
            if resAns == "1":
                width = "1920"
                height = "1080"
            if resAns == "2":
                width = "1280"
                height = "720"
            if resAns == "3":
                width = "640"
                height = "480"
        if answerZero == "3":
            print("What would you like the framerate to be?")
            print("0: Back")
            print("1: 30 FPS (Default)")
            print("2: 60 FPS")
            print("3: 90 FPS")
            fpsAns = input()
            if fpsAns == "1":
                framerate = "30"
            if fpsAns == "2":
                framerate = "60"
            if fpsAns == "3":
                framerate = "90"
        if answerZero == "4":
            print("What would you like the video format to be?")
            print("0: Back")
            print("1: .h264 (Default)")
            print("2: .mp4")
            extAns = input()
            if extAns == "1":
                ext = ".h264 (Default)"
            if extAns == "2":
                ext = ".mp4 --codec libav"
    if answer == "1":
        if vflip == True and hflip == True:
            os.system("rpicam-hello -t  0 --hflip --vflip")
        elif vflip == True:
            os.system("rpicam-hello -t  0 --vflip")
        elif hflip == True:
            os.system("rpicam-hello -t  0 --hflip")
        else:
            os.system("rpicam-hello -t 0")
    if answer == "2":
        print("How long would you like the video to be in seconds?")
        duration = input()
        print("What should the video name be?")
        vidname = input()
        if vflip == True and hflip == True:
            os.system("sudo rpicam-vid --vflip --hflip -o "+vidname+ext+" --width "+width+" --height "+height+" --framerate "+framerate+" -t "+duration+"s")
        elif vflip == True:
            os.system("sudo rpicam-vid --vflip -o "+vidname+ext+" --width "+width+" --height "+height+" --framerate "+framerate+" -t "+duration+"s")
        elif hflip == True:
            os.system("sudo rpicam-vid --hflip -o "+vidname+ext+" --width "+width+" --height "+height+" --framerate "+framerate+" -t "+duration+"s")
        else:
            os.system("sudo rpicam-vid -o "+vidname+ext+" --width "+width+" --height "+height+" --framerate "+framerate+" -t "+duration+"s")
        os.system("sudo mv "+vidname+".* /home/*/Desktop/'Test Videos'/")
    if answer == "3":
        print("What should the video name be?")
        vidname = input()
        if vflip == True and hflip == True:
            os.system("sudo rpicam-vid --vflip --hflip -o "+vidname+ext+" --width "+width+" --height "+height+" --framerate "+framerate+" -t 0")
        elif vflip == True:
            os.system("sudo rpicam-vid --vflip -o "+vidname+ext+" --width "+width+" --height "+height+" --framerate "+framerate+" -t 0")
        elif hflip == True:
            os.system("sudo rpicam-vid --hflip -o "+vidname+ext+" --width "+width+" --height "+height+" --framerate "+framerate+" -t 0")
        else:
            os.system("sudo rpicam-vid  -o "+vidname+ext+" --width "+width+" --height "+height+" --framerate "+framerate+" -t 0")
        os.system("sudo mv "+vidname+".* /home/*/Desktop/'Test Videos'/")
    if answer == "4":
       os.system("sudo cp -r /home/*/Desktop/'Test Videos'/* /media/*/*/")