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

while True: #Loop to make the code run infinitely after choosing an option
    print("What Would you like to do?")
    print("-1: Quit")
    print("0: Properties")
    print("1: Live View Camera (Ctrl + C to end preview)")
    print("2: Take a video")
    print("3: Infinite Video")
    answer = input()
    if answer == "-1":
        quit()
    if answer == "0":
        print("Do you want to flip the camera?")
        print("0: No")
        print("1: Yes")
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
        vidName = input()
        if vlfip == True and hflip == True:
            os.system("sudo rpicam-vid --vflip --hflip -o "+vidName+".h264 --width 1280 --height 720 --framerate 30 -t "+duration+"s")
        elif vlfip == True:
            os.system("sudo rpicam-vid --vflip -o "+vidName+".h264 --width 1280 --height 720 --framerate 30 -t "+duration+"s")
        elif hflip == True:
            os.system("sudo rpicam-vid --hflip -o "+vidName+".h264 --width 1280 --height 720 --framerate 30 -t "+duration+"s")
        else:
            os.system("sudo rpicam-vid -o "+vidName+".h264 --width 1280 --height 720 --framerate 30 -t "+duration+"s")
        os.system("sudo mv "+vidName+".h264 /home/cam1/Desktop/'Test Videos'/")
    if answer == "3":
        print("What should the video name be?")
        vidName = input()
        if vflip == True and hflip == True:
            os.system("sudo rpicam-vid --vflip --hflip -o "+vidName+".h264 --width 1280 --height 720 --framerate 30 -t 0")
        elif vflip == True:
            os.system("sudo rpicam-vid --vflip -o "+vidName+".h264 --width 1280 --height 720 --framerate 30 -t 0")
        elif hflip == True:
            os.system("sudo rpicam-vid --hflip -o "+vidName+".h264 --width 1280 --height 720 --framerate 30 -t 0")
        else:
            os.system("sudo rpicam-vid  -o "+vidName+".h264 --width 1280 --height 720 --framerate 30 -t 0")
        os.system("sudo mv "+vidName+".h264 /home/cam1/Desktop/'Test Videos'/")
        
