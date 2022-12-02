# 영상 저장하기
import cv2

display_W = 640
display_H = 480
fps = 20

video = cv2.VideoCapture(0,cv2.CAP_V4L)

video.set(cv2.CAP_PROP_FRAME_WIDTH, display_W)
video.set(cv2.CAP_PROP_FRAME_HEIGHT, display_H)
video.set(cv2.CAP_PROP_FPS,fps)

out = cv2.VideoWriter("/home/chaehanbin/다운로드/Chaehanbin_Jetson/video/me.avi",cv2.VideoWriter_fourcc(*"XVID"),20,(display_W,display_H))

while True:
    ret, frame = video.read()
    cv2.imshow("video",frame)
    cv2.moveWindow('video',0,0)
    out.write(frame)

    if cv2.waitKey(30) == ord('q'):
        break

video.release()
out.release()
cv2.destroyAllWindows()
