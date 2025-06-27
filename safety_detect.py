import cv2
import pandas as pd
import datetime
from ultralytics import YOLO

# Load YOLOv8 model
model = YOLO('best2.pt')

# Start webcam
cap = cv2.VideoCapture(0)  # change to 1 or 2 if external webcam

# Define violation categories based on your model's training
violation_classes = ['Hardhat', 'Safety vest', 'Shoes']

# For logging
violation_log = []

print("🟢 Running detection. Press ESC to quit.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Resize for consistency
    frame = cv2.resize(frame, (1024, 768))

    # Predict
    results = model.predict(frame)

    alert_flag = False
    current_violations = []

    for result in results:
        for box in result.boxes:
            cls_id = int(box.cls[0])
            class_name = result.names[cls_id]

            x1, y1, x2, y2 = map(int, box.xyxy[0])

            # Draw bounding box
            color = (0, 255, 0)  # green
            if class_name in violation_classes:
                color = (0, 0, 255)  # red
                alert_flag = True
                current_violations.append(class_name)

            label = f"{class_name}"
            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
            cv2.putText(frame, label, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)

    # Log if there was a violation
    if alert_flag:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        for vtype in current_violations:
            violation_log.append([timestamp, vtype])

    # Show the output
    cv2.imshow("PPE Detection - Press ESC to Exit", frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break

# Cleanup
cap.release()
cv2.destroyAllWindows()

# Save log to CSV only if there are violations
if violation_log:
    df = pd.DataFrame(violation_log, columns=["timestamp", "violation"])
    df.to_csv("violation_log.csv", index=True)
    print("📝 Violation log saved to violation_log.csv")
else:
    print("ℹ️ No violations detected. Log file not created.")

print("🔴 Detection stopped. Exiting...")
# End of script
