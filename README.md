# Face_Detection_using_OpenCV
Face Detection using OpenCV: Detect faces in images and videos with real-time performance. Leverages Haar cascades for accurate results.

This Python script uses the OpenCV library to perform face detection in images and videos. It leverages the Haar cascade classifier, a popular technique for object detection, to achieve real-time face detection with high accuracy.

**Features**

Detects faces in both images and videos
Optimized performance for real-time face detection
Draws rectangles around the detected faces
Supports various image and video formats

**Requirements**

Python (version 3.11.3)
OpenCV library (version 4.7.0.72)
Haar cascade XML file for face detection (you can download from the following file) = https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml

**Usage**
- Install the required dependencies, including Python and OpenCV.
- Download the Haar cascade XML file for face detection and place it in the same directory as the script.
- Modify the image_path variable in the code to the path of the image you want to process.
- Uncomment the relevant lines and modify the video_path variable to the path of the video you want to process.
- Run the script and observe the output window, which displays the processed image or video with rectangles around the detected faces.
- Press the 'q' key to exit the video processing loop.
