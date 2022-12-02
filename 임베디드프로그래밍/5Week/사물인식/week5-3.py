# jetson.inference use object detect
import jetson.inference
import jetson.utils

cam = jetson.utils.gstCamera(640,480,'/dev/video0')
disp = jetson.utils.glDisplay()
font = jetson.utils.cudaFont() # cuda : compute device archtect
net=jetson.inference.imageNet('googlenet')

while disp.IsOpen():
    frame, width, height = cam.CaptureRGBA()
    classID, confidence = net.Classify(frame,width,height)
    item = net.GetClassDesc(classID)

    font .OverlayText(frame,width,height,item,5,5,font.Magenta,font.Black)
    disp.RenderOnce(frame,width,height)
