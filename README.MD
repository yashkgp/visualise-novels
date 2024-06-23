# Mac Text to Image App

This macOS application monitors the clipboard for text selection and sends the selected text to a server, which returns an image. The app displays the received image with a loading screen while waiting for the server response.

## Installation

1. Ensure you have Python 3.7+ installed on your macOS system.

2. Clone this repository

3. Create and activate a virtual environment: 
    `python3 -m venv venv`
    `source venv/bin/activate`
4. Install the required dependencies:
    `pip install -r requirements.txt`
5. Install the application:
    `pip install -e .`


## Usage

1. Run the application
2. The app will start and minimize to the system tray.

3. Select any text on your macOS system. The app will automatically detect the selection, send it to the server, and display the received image in the app window.

4. A loading screen will appear while waiting for the server response.



## Development

To make changes to the app, modify the files in the `src/` directory. After making changes, reinstall the app using `pip install -e .` to update the installed version.