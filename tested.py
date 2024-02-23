import cv2
import yolov9

# Load pretrained or custom model
model = yolov9.load("yolov9-c.pt", device="cpu")

# Set model parameters
model.conf = 0.25  # NMS confidence threshold
model.iou = 0.45  # NMS IoU threshold
model.classes = None  # (optional list) filter by class

# Open a connection to the webcam (you may need to adjust the index)
cap = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Perform inference on the frame
    results = model(frame)

    # Parse results
    predictions = results.pred[0]
    boxes = predictions[:, :4]  # x1, y1, x2, y2
    scores = predictions[:, 4]
    categories = predictions[:, 5]

    # Draw bounding boxes on the frame
    for box, score, category in zip(boxes, scores, categories):
        x1, y1, x2, y2 = map(int, box)
        label = f"{model.names[int(category)]}: {score:.2f}"
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('YOLOv9 Object Detection', frame)

    # Break the loop if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
