import cv2

# Read the captured video file
cap = cv2.VideoCapture(r"C:\Users\Madhu\OneDrive\문서\29_08_25[1]\29_08_25_194259.mp4")

print("Press:")
print("n - Normal speed")
print("s - Slow motion")
print("f - Fast motion")
print("q - Quit")

delay = 30   # default normal speed

while True:
    ret, frame = cap.read()
    if not ret:
        break

    cv2.imshow("Video Playback", frame)

    key = cv2.waitKey(delay) & 0xFF

    # Change playback speed based on key press
    if key == ord('n'):      # Normal speed
        delay = 30
    elif key == ord('s'):    # Slow motion
        delay = 100
    elif key == ord('f'):    # Fast motion
        delay = 5
    elif key == ord('q'):    # Quit
        break

cap.release()
cv2.destroyAllWindows()
