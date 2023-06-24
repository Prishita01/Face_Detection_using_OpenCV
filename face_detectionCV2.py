import cv2

# Load the Haar cascade XML file for face detection
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Function to detect faces in an image
def detect_faces(image):
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the grayscale image
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    
    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
    
    return image

# Function to process images
def process_image(image_path):
    # Load the image
    image = cv2.imread(image_path)
    
    # Perform face detection
    result_image = detect_faces(image)
    
    # Display the result
    cv2.imshow('Face Detection', result_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Function to process videos
def process_video(video_path):
    # Open the video file
    video_capture = cv2.VideoCapture(video_path)
    
    # Iterate over frames in the video
    while True:
        # Read the current frame
        ret, frame = video_capture.read()
        
        if not ret:
            break
        
        # Perform face detection on the frame
        result_frame = detect_faces(frame)
        
        # Display the result
        cv2.imshow('Face Detection', result_frame)
        
        # Check for the 'q' key to exit
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    
    # Release the video capture object
    video_capture.release()
    cv2.destroyAllWindows()

# Process an image
image_path = 'photo.jpeg'
process_image(image_path)

# Process a video
# video_path = 'video.mp4'
# process_video(video_path)
