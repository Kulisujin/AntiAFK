<h1>AntiAFK: Automatic Cursor Movement Script</h1>
    <h2>Description</h2>
    <p>AntiAFK is a Python script that simulates user activity by automatically moving the cursor after a period of inactivity. It's designed to prevent "Away From Keyboard" (AFK) status in applications or systems that may log out inactive users.</p>
    <h2>Versions</h2>
    <ul>
        <li><code>antiafk.py</code>: Full version with all features</li>
        <li><code>antiafk_slim.py</code>: Streamlined version with core functionality</li>
        <li><code>antiafk_cp</code>: Compact version for easy copying and pasting</li>
    </ul>
    <h2>Features</h2>
    <ul>
        <li>Monitors keyboard and mouse activity using low-level Windows hooks</li>
        <li>Automatically moves the cursor after a period of inactivity</li>
        <li>Uses both linear and Bezier curve movements for natural-looking cursor motion</li>
        <li>Keeps Microsoft Teams status as "Available" by simulating activity</li>
        <li>Customizable inactivity timeout</li>
        <li>Runs in the background with minimal CPU usage</li>
    </ul>
    <h2>Requirements</h2>
    <ul>
        <li>Windows operating system (tested on Windows 10)</li>
        <li>Python 3.6 or higher</li>
        <li>Administrative privileges (required for setting up low-level hooks)</li>
    </ul>
    <h2>Usage</h2>
    <h3>Full and Slim Versions</h3>
    <ol>
        <li>Open a command prompt with administrative privileges.</li>
        <li>Navigate to the directory containing the script.</li>
        <li>Run the script using Python:
            <pre><code>python antiafk.py</code></pre>
            or
            <pre><code>python antiafk_slim.py</code></pre>
        </li>
        <li>The script will run in the background. You will not see any output unless there's an error.</li>
        <li>To stop the script, press Ctrl+C in the command prompt window.</li>
    </ol>
    <h3>antiafk_cp Version</h3>
    <ol>
        <li>Open a Python interactive shell with administrative privileges.</li>
        <li>Copy and paste the one-liner version into the shell and press Enter.</li>
        <li>The script will run until you close the Python shell or interrupt it with Ctrl+C.</li>
    </ol>
    <h2>Customization</h2>
    <p>You can modify the following parameters in the script:</p>
    <ul>
        <li><code>self.timeout</code>: Adjust the inactivity period (in seconds) before the cursor starts moving.</li>
        <li><code>self.duration</code>: Modify the duration of cursor movements.</li>
        <li><code>self.next_move_time</code>: Change the interval between automatic movements.</li>
    </ul>
    <h2>Warning</h2>
    <div class="warning">
        <p>This script uses low-level system hooks and simulates user input. Use it responsibly and be aware of any policies or regulations in your environment regarding the use of such tools. While it can keep your Teams status as "Available", it's important to use this feature ethically and in compliance with your organization's policies.</p>
    </div>
    <h2>Troubleshooting</h2>
    <ul>
        <li>If you encounter a "Failed to set hooks" message, ensure you're running the script with administrative privileges.</li>
        <li>If the script doesn't seem to be working, check if your antivirus or security software is blocking it.</li>
    </ul>
    <h2>Disclaimer</h2>
    <p>This script is provided as-is, without any warranties. The authors are not responsible for any consequences resulting from the use of this script. Use at your own risk and in compliance with all applicable rules and regulations. Be aware that continuously appearing as "Available" on Teams when you're not actually available may have professional implications.</p>
