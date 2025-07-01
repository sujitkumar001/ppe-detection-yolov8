# 🦺 PPE Detection System using YOLOv8

This project is a real-time **PPE (Personal Protective Equipment) Detection System** built using **YOLOv8 and OpenCV** to enhance **safety operations in a steel plant environment**. It detects whether individuals are wearing essential safety gear like **hard hats, safety vests, gloves, and shoes**, and displays results on a dynamic dashboard.

## 🚀 Features

- Real-time detection via webcam
- Detects multiple PPE items per person:
  - Hard Hat
  - Safety Vest
  - Gloves
  - Shoes
- Safety status indicator (Safe / Unsafe)
- Logs violations with timestamp
- Live Stream Dashboard (Built using Streamlit)
- Saves images of violators
- Custom-trained YOLOv8 model

## 🏭 Use Case

Designed for **industrial environments** like steel plants, this system helps monitor safety compliance by automatically identifying workers who are missing required protective equipment.

## 📂 Project Structure

ppe_project_with_Dashboard/
│
├── best2.pt # Trained YOLOv8 model
├── safety_detect.py # Detection script
├── violation_log.csv # Violation logs
├── dashboard/
│ ├── app.py # Streamlit Dashboard
│ └── components/
│ ├── live_feed.py
│ ├── violation_log_view.py
│ └── person_module.py
└── README.md

## 🛠️ How to Run

1. Clone the repo:
   ```bash
   git clone https://github.com/sujitkumar001/ppe-detection-yolov8.git
   cd ppe-detection-yolov8
Install dependencies:

pip install -r requirements.txt
Run the dashboard:

streamlit run dashboard/app.py
Make sure your webcam is connected and accessible.

📷 Screenshot

📌 Requirements
Python 3.8+

OpenCV

Ultralytics (YOLOv8)

Streamlit

Pandas

📈 Future Enhancements
Add DeepSort for person tracking

Generate downloadable violation reports

Real-time alert system (audio/email)

Violation trend analytics (daily/hourly)

👨‍💻 Author
Sujit Kumar
📧 pulakalasujit001@gmail.com
🔗 https://www.linkedin.com/in/pulakala-sujit-kumar/

