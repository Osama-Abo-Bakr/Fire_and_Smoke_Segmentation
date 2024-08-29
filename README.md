# Fire_and_Smoke_Segmentation

## Overview
**Fire_and_Smoke_Segmentation** is an AI-driven project designed to detect and segment fire and smoke in real-time video footage. Utilizing the YOLOv8 model, this system offers high accuracy and quick detection, which can be crucial in preventing fire-related disasters. The integration of real-time alarms ensures immediate notification when a potential hazard is detected.

## Features
- **Real-time Fire and Smoke Detection:** Continuously analyzes video feeds to identify fire and smoke, ensuring timely alerts.
- **Automatic Alarm Trigger:** Integrates with an alarm system that is activated upon detection, enhancing safety measures.
- **Accurate Classification:** Differentiates between fire and smoke, providing clear and actionable information.

## Technology Stack
- **YOLOv8:** A state-of-the-art object detection framework used to identify fire and smoke.
- **OpenCV:** Provides functionalities for video capture, image processing, and real-time video display.
- **Pandas:** Used for managing and processing detection data.
- **Pygame:** Handles the real-time alarm functionality, ensuring immediate alerts when fire or smoke is detected.

## Installation
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Osama-Abo-Bakr/Fire_and_Smoke_Segmentation.git
   cd Fire_and_Smoke_Segmentation
   ```

2. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Download the Pre-trained YOLO Model:**
   - Download the `Fire_and_Smoke_Segmentation.pt` model and place it in the project directory.

## Usage
1. **Run the Detection Script:**
   ```bash
   python fire_and_smoke_segmentation.py
   ```

2. **Select Video Input:**
   - The script is set to process a predefined video file, but you can easily switch to a live webcam feed or another video source by modifying the `video = cv2.VideoCapture()` line in the code.

3. **Monitor Output:**
   - The video will display bounding boxes around detected fire and smoke, with labels indicating the type and the confidence level of the detection.
   - The alarm will sound automatically when fire or smoke is detected.

## Customization
- **Model Adjustment:** You can fine-tune the YOLO model to improve detection accuracy for specific environments or scenarios.
- **Alarm System Integration:** Customize the alarm settings to fit your specific needs, including different sounds or notification methods.

## Contributing
We welcome contributions! Please feel free to open issues or submit pull requests for enhancements, bug fixes, or additional features.

## License
This project is licensed under the MIT License, allowing you to freely use and modify the code for your applications.
