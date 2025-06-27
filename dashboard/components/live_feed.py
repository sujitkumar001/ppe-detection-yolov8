import streamlit as st
import cv2
from ultralytics import YOLO
import datetime
import pandas as pd
from components.person_module import draw_person_info

model = YOLO("C:\\Users\\HP\\Desktop\\ppe_project\\best2.pt")
violation_classes = ['Hardhat', 'Safety vest', 'Shoes']

person_counter = 0

def run_live_feed():
    global person_counter
    stframe = st.empty()
    violation_log = []

    if "stop_detection" not in st.session_state:
        st.session_state.stop_detection = False

    if st.button("⏹ Stop Detection", key="stop_detection_btn"):
        st.session_state.stop_detection = True

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        st.error("Unable to access webcam.")
        return

    while not st.session_state.stop_detection:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.resize(frame, (800, 600))
        results = model.predict(frame, conf=0.5)
        current_violations = []
        person_modules = []

        for result in results:
            for box in result.boxes:
                cls_id = int(box.cls[0])
                class_name = result.names[cls_id]
                x1, y1, x2, y2 = map(int, box.xyxy[0])

                person_counter += 1
                person_id = f"Person {person_counter}"
                timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                is_violation = class_name in violation_classes

                status = "VIOLATION" if is_violation else "OK"
                color = (0, 0, 255) if is_violation else (0, 255, 0)
                label = f"{class_name}: {status}"
                
                cv2.rectangle(frame, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame, label, (x1, y1 - 10),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.6, color, 2)
                
                if is_violation:
                    current_violations.append([timestamp, person_id, class_name])
                
                person_modules.append((person_id, class_name, status, timestamp))

        draw_person_info(st, person_modules)

        if current_violations:
            df = pd.DataFrame(current_violations, columns=["timestamp", "person_id", "violation"])
            df.to_csv("violation_log.csv", mode='a', header=False, index=False)

        stframe.image(frame, channels="BGR")

    cap.release()
    cv2.destroyAllWindows()
