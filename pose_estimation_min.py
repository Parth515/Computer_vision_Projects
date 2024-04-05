import cv2
import mediapipe as mp
import time

mpDraw = mp.solutions.drawing_utils
mpPose = mp.solutions.pose
pose = mpPose.Pose()

cap = cv2.VideoCapture('pose_videos/pose2.mp4')  # to read the video
pTime = 0
while True:
    success, img = cap.read()   # to read the video

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGRA2RGB)
    results = pose.process(imgRGB)  # reduces the frame rate
    # print(results.pose_landmarks) # to get the landmark
    if results.pose_landmarks:
        mpDraw.draw_landmarks(img, results.pose_landmarks, mpPose.POSE_CONNECTIONS)
        for id, lm in enumerate(results.pose_landmarks.landmark):
            h, w, c = img.shape
            print(id, lm)

            cx, cy = int(lm.x * w), int(lm.y * h)  # to get the pixel value
            cv2.circle(img, (cx, cy), 5, (255, 0, 0), cv2.FILLED)

    cTime = time.time()                # to see the frame rate
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3,
                (255, 0, 0), 3)  # to show the frame rate in video

    cv2.imshow("Image", img)        # to show the video
    cv2.waitKey(1)
