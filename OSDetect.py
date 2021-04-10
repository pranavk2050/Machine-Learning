import tkinter
import os
import sys
import subprocess
import signal

#fov = 41.10          # Field of view of the camera
#camera_angle = 60    # Angle of the camera with respect to the bar on which it has mounted
#camera_height = 7.6  # Height of the camera from the ground in meters



top = tkinter.Tk()


top.minsize(500,200)
top.maxsize(500,200)
top.title("Vehicle Speed Detector") 
id=[]



def detector():
	#os.system("python object_tracker.py --video ./data/video/cars.mp4 --output ./outputs/cars.avi --model yolov4 --info --dont_show ")
	inputvideo=InputFile.get()
	outvideo=OutputFile.get()
	FOV=fov.get()
	Camera_Angle=camera_angle.get()
	Camera_Height=camera_height.get()
	
	
	process = subprocess.Popen("python ./object_tracker.py --video ./data/video/"+inputvideo+" --output ./outputs/"+outvideo+" --dont_show --model yolov4 --info --fov "+FOV+" --camera_angle "+Camera_Angle+" --camera_height "+Camera_Height)
	#process=subprocess.Popen(['python','OSDetect.py'])


def exit():
	os.system("Taskkill /IM python.exe /F" )

Detect = tkinter.Button(top, text =" Process Video",pady='5',command=detector)
InputFile=tkinter.Entry(top,width="20")


SaveAs = tkinter.Button(top, text =" Save As ",pady='5')
OutputFile=tkinter.Entry(top,width="20")
StopDetection = tkinter.Button(top, text =" Stop ",pady='5',command=exit)

fov = tkinter.Entry(top,width="10")
camera_angle = tkinter.Entry(top,width="10")
camera_height = tkinter.Entry(top,width="10")


Detect.place(x=30,y=30)
InputFile.place(x=125,y=30)
SaveAs.place(x=287,y=30)
OutputFile.place(x=350,y=30)



T = tkinter.Text(top,height = 1,width = 30)
l = tkinter.Label(T, text = "Insert FOV  Camera Angle  Camera Height")
l.config(font =("Courier", 10))
l.pack()
T.pack()

fov.place(x=30,y=120)
camera_angle.place(x=130,y=120)
camera_height.place(x=240,y=120)
T.place(x=30,y=90)



StopDetection.place(x=30,y=150)



top.mainloop()