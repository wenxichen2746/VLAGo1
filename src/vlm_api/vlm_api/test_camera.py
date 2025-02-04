import cv2
import time
import os

def capture_and_save_image(save_path="captured_image.jpg"):
    """Captures a frame from the Jetson Nano camera and saves it locally with adjusted exposure."""
    cap = cv2.VideoCapture(0)

    # Set exposure (0 is auto, -1 is manual mode, and positive values lower exposure)
    cap.set(cv2.CAP_PROP_AUTO_EXPOSURE, 0.1)  # Manual mode
    cap.set(cv2.CAP_PROP_EXPOSURE, -50)  # Adjust this based on lighting conditions

    time.sleep(2)  # Allow camera to adjust settings
    ret, frame = cap.read()
    cap.release()

    if not ret:
        print("Failed to capture image.")
        return

    os.makedirs(os.path.dirname(save_path), exist_ok=True)
    cv2.imwrite(save_path, frame)
    print(f"Image saved as {save_path}")

# Example usage
timestamp = time.strftime("%Y%m%d-%H%M%S")
capture_and_save_image(f"captured_images/image_{timestamp}.jpg")
