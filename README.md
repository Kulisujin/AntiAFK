AntiAFK: Automatic Cursor Movement Script
Description
AntiAFK is a Python script that simulates user activity by automatically moving the cursor after a period of inactivity. It's designed to prevent "Away From Keyboard" (AFK) status in applications or systems that may log out inactive users.
A key feature of AntiAFK is its ability to keep Microsoft Teams from marking the user as "Away". Teams typically changes a user's status to "Away" after a period of inactivity. By simulating mouse movement at regular intervals, AntiAFK tricks Teams into thinking the user is still active, maintaining the "Available" status indefinitely.
Versions

antiafk.py: Full version with all features
antiafk_slim.py: Streamlined version with core functionality
antiafk_cp: Compact version for easy copying and pasting

Features

Monitors keyboard and mouse activity using low-level Windows hooks
Automatically moves the cursor after a period of inactivity
Uses both linear and Bezier curve movements for natural-looking cursor motion
Keeps Microsoft Teams status as "Available" by simulating activity
Customizable inactivity timeout
Runs in the background with minimal CPU usage

Requirements

Windows operating system (tested on Windows 10)
Python 3.6 or higher
Administrative privileges (required for setting up low-level hooks)

Usage
Full and Slim Versions

Open a command prompt with administrative privileges.
Navigate to the directory containing the script.
Run the script using Python:
Copypython antiafk.py
or
Copypython antiafk_slim.py

The script will run in the background. You will not see any output unless there's an error.
To stop the script, press Ctrl+C in the command prompt window.

antiafk_cp Version

Open a Python interactive shell with administrative privileges.
Copy and paste the one-liner version into the shell and press Enter.
The script will run until you close the Python shell or interrupt it with Ctrl+C.

Customization
You can modify the following parameters in the script:

self.timeout: Adjust the inactivity period (in seconds) before the cursor starts moving.
self.duration: Modify the duration of cursor movements.
self.next_move_time: Change the interval between automatic movements.

Warning
This script uses low-level system hooks and simulates user input. Use it responsibly and be aware of any policies or regulations in your environment regarding the use of such tools. While it can keep your Teams status as "Available", it's important to use this feature ethically and in compliance with your organization's policies.
Troubleshooting

If you encounter a "Failed to set hooks" message, ensure you're running the script with administrative privileges.
If the script doesn't seem to be working, check if your antivirus or security software is blocking it.
For Microsoft Teams, ensure that the script is running before you start Teams for best results.

Disclaimer
This script is provided as-is, without any warranties. The authors are not responsible for any consequences resulting from the use of this script. Use at your own risk and in compliance with all applicable rules and regulations. Be aware that continuously appearing as "Available" on Teams when you're not actually available may have professional implications.
