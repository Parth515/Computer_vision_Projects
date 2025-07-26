## Face_detection.ipynb script uses two of the most basic algorithms: 
###1. Haar Cascade Classifier
- Implemented using OpenCV's Cascade Classifier.
- Based on Haar-like features and the Viola-Jones algorithm.
- Detects faces by scanning the image at multiple scales using a cascade of simple classifiers.

Advantages:
- Fast on CPU.
- No deep learning required.

Limitations:
- Sensitive to lighting and pose variations.
- Not as accurate as CNN-based methods.

###2. HOG (Histogram of Oriented Gradients)
- Implemented using dlib's HOG-based face detector.
- Works by analyzing gradient orientation histograms in localized regions.
- Uses sliding window + SVM classifier to detect faces.

Advantages:
- No training required (pre-trained model included in dlib).
- Works reasonably well for frontal faces.

Limitations:
- Slower than Haar cascades.
- Struggles with non-frontal faces.




## facedetection_basics.py and facedetection_module.py scripts uses MediaPipe Face Detection, which is powered by the BlazeFace model:
- BlazeFace is a lightweight, real-time CNN (Convolutional Neural Network) optimized for mobile and edge devices.
- It performs single-shot detection (similar to SSD) to find faces in an image.

The model outputs:
- Relative bounding boxes around faces.
- Confidence score for each detection.

How It Works
1. Convert the frame to RGB.
2. Pass the image to MediaPipe FaceDetection.
3. The model returns detections (bounding boxes + scores).
4. Draw bounding boxes using cv2.rectangle and display FPS.

Why BlazeFace?
- Extremely fast (real-time even on CPU).
- Works well for videos and streams.
- Robust to different face sizes and orientations.


