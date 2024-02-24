# yolov9-real-time-webcam
yolov9 real-time webcam


## Evaluation

[`yolov9-c.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-c.pt) [`yolov9-e.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/yolov9-e.pt) [`gelan-c.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-c.pt) [`gelan-e.pt`](https://github.com/WongKinYiu/yolov9/releases/download/v0.1/gelan-e.pt)

``` shell
# run yolov9 code for image 
python detect.py --weights gelan-c.pt --source "demo2.jpg" --view-img

# run yolov9 code for video
python detect.py --weights gelan-c.pt --source 0 --view-img
```


### Watch the Complete Step by Step Explanation

[![Watch the video](https://github.com/noorkhokhar99/yolov9-real-time-webcam/blob/main/Screenshot%202024-02-23%20at%204.53.26%20PM.png)](https://youtu.be/8jM1Pi4OxJo)
