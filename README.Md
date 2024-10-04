# Keylogger Project

## Overview
This project is a advance keylogger implemented in Python. It is designed for educational purposes only, to demonstrate how keylogging and data exfiltration techniques work. The keylogger captures keystrokes, takes screenshots, and captures webcam images, storing the collected data securely. The keylogger then sends the collected data via email using ProtonMail for secure communication.

## Features
- **Keystroke Logging**: Records all keystrokes made by the user.
- **Screenshot Capture**: Takes periodic screenshots of the user's screen.
- **Webcam Capture**: Captures images from the user's webcam (note that the webcam indicator light will turn on).
- **Data Exfiltration**: Sends the captured data via email using ProtonMail, ensuring secure transmission.
- **Data Encryption**: Encrypts captured screenshots and webcam images before sending them to maintain confidentiality.

## Requirements
- **Python 3.x**
- Required Python libraries:
  - `pynput`: For capturing keyboard input.
  - `opencv-python`: For webcam access and image capture.
  - `PIL (Pillow)`: For image processing.
  - `cryptography`: For encryption and decryption of captured files.
  - `smtplib`: For sending emails (with ProtonMail Bridge).

## Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/AH-bi/keylogger.git
    ```

2. Navigate to the project directory:
    ```bash
    cd <project_directory>
    ```

3. Install the required libraries:
    ```bash
    pip install pynput opencv-python Pillow cryptography
    ```

4. Set up ProtonMail Bridge:
   - Download and install ProtonMail Bridge from the ProtonMail website.
   - Log in and obtain SMTP/IMAP credentials.

## Usage
1. Modify the `keylogger.py` file to include your ProtonMail SMTP details.
2. Run the keylogger:
    ```bash
    python keylogger.py
    ```

The keylogger will start capturing keystrokes, screenshots, and webcam images. Captured data will be sent to your ProtonMail account at specified intervals.

## Important Note
- **Ethical Considerations**: This project is intended for educational purposes only. Use of keyloggers and similar software without the explicit consent of the user is illegal and unethical. Ensure you have permission to log activity on any device you use this software on.
- **Security**: Handle all captured data with care to maintain user privacy and comply with legal requirements.

## License
This project is licensed under the MIT License. See the LICENSE file for more details.

## Contributing
If you would like to contribute to this project, please open an issue or submit a pull request.
