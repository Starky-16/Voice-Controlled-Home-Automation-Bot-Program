# Voice-Controlled-Home-Automation-Bot-Program
📌 Objective

A virtual robot that controls smart home devices (lights, fan, AC) using voice commands.

🛠 Tools & Technologies

Python

ROS (Robot Operating System)

Webots Simulator

SpeechRecognition API

🚀 Features

Listens to voice commands (e.g., "Turn on the light", "Switch off the fan").

Parses the command and identifies the target device.

Simulates smart home devices inside Webots.

Modular design:

Speech Module – captures & converts speech to text.

Command Parser – interprets commands.

Actuator Module – simulates device action in Webots.
How to Run

Clone the repository:

git clone https://github.com/Starky-16/Voice-Controlled-Home-Automation-Bot-Program.git
cd voice_home_bot


Install dependencies:

pip install SpeechRecognition pyttsx3
sudo apt install ros-noetic-desktop-full


Launch Webots and load the smart_home.wbt world.

Run the nodes:

rosrun voice_home_bot speech_recognition_node.py
rosrun voice_home_bot command_parser.py
rosrun voice_home_bot actuator_node.py

🎯 Example Commands

"Turn on the light"

"Switch off the fan"

"Start the AC"

📖 Future Improvements

Add support for more devices (TV, door, etc.)

Integrate with IoT hardware (ESP32, Raspberry Pi).

Enhance NLP for more natural commands.
