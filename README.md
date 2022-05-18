# ErgonomicChair
### Early stages of the project

This project consists of a "Smart Chair", with 8 sensors to monitor the user's posture.  
The chair connects to the desktop app via MQTT mainly, but can be connected via USB for troubleshooting.  
After the MQTT communication, the local server stores the data on the database using SQLite3.  
The UI was made using QT Designer and PyQt6:  

https://user-images.githubusercontent.com/94933775/168953086-38d64c5d-5acf-4c5d-a7ed-fe69eedfc2d0.mp4

# TODO
- Refine the UI
- Integrate the UI with the database using the Interface class from the local server
- Display visualy the data on the app
- Add a way to communicate with the chair via USB for configuration purposes
