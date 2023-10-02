import cv2
import os
import numpy as np

# Create a directory to store cropped images
output_folder = "output_cropped"
os.makedirs(output_folder, exist_ok=True)

# Load the pre-trained SSD model for face detection
prototxt_path = "/home/aadhithbala/scripts/face-detection/models/deploy.prototxt"  # Path to the prototxt file
caffemodel_path = "/home/aadhithbala/scripts/face-detection/models/res10_300x300_ssd_iter_140000.caffemodel"  # Path to the model weights

net = cv2.dnn.readNetFromCaffe(prototxt_path, caffemodel_path)

# Load the pre-trained MTCNN model for face detection and landmarks
mtcnn = cv2.dnn.readNetFromTensorflow("/home/aadhithbala/scripts/face-detection/models/MTCNN/mtcnn.pb")

# Loop through each image in the folder
for filename in os.listdir("input_images"):
    if filename.endswith(".jpg"):
        # Read the image
        img = cv2.imread(os.path.join("input_images", filename))

        # Perform face detection using the SSD model
        blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104, 117, 123))
        net.setInput(blob)
        detections = net.forward()

        for i in range(detections.shape[2]):
            confidence = detections[0, 0, i, 2]

            # Filter out weak detections
            if confidence > 0.5:
                box = detections[0, 0, i, 3:7] * np.array([img.shape[1], img.shape[0], img.shape[1], img.shape[0]])
                (startX, startY, endX, endY) = box.astype("int")

                # Crop the face region
                face = img[startY:endY, startX:endX]

                # Save the cropped face with a unique filename
                cropped_filename = os.path.join(output_folder, f"{filename.split('.')[0]}_face_{i}.jpg")
                cv2.imwrite(cropped_filename, face)

# Release OpenCV resources
cv2.destroyAllWindows()
