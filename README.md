HOME SECURITY SERVICE
======================
Presentation video URL: <https://drive.google.com/drive/folders/1olCBgL0yhN92NcaZqWdjLsxqZ3L8HFYj?usp=sharing>

1.What does this project do?
-------------------------------
This is a program to check the sound level (amplitude, frequency, max peak) of the surrounding environment in real time.
If the decibel of the surrounding area is more than 40dB, the program will automatically send the email to warn the current situation.
It also displays the real time situation of the surrounding environment through the camera.
All the detailed data are shown in user customized dashboard in uBEAC website.

2.Why is this project useful?
---------------------------------
These days, security and privacy policy issues are rising. A lot of people are not guaranteed thier rights to be protected and kept anxious about it. People want to check what is going on near their places immediately and this program is best for them to remove unrest. Just by implementing this program, people can monitor what is happening in the surrounding environment in real time.

3.How do I get started?
-----------------------------
1. Download or clone the repository.
2. Download the LANmic and IP Webcam android mobile application.
3. Turn on the LANmic(set sample rate as 16,000) and IP Webcam mobile application, and note the IP addresses shown in two mobile applications.
4. Create an account for uBeac IoT Platform here: [uBeac](https://app.ubeac.io/ "uBeac link")
5. Create a gateway with UID, Name, and choose uBeac Multiple Devices as a firmware.
6. Move to the command prompt.
7. Install the following modules for python program in the command prompt.
   <pre><code>pip install scipy</code></pre>
   <pre><code>pip install numpy</code></pre>
8. Move to SoundDetection directory.
9. Update the file location, configuration section, and IP address from LANmic in main.py.
10. Update the email account information for the warning message in alarm.py.
11. Run main.py with python programming language version 3.
12. Go to Devices section in [uBeac](https://app.ubeac.io/ "uBeac link"), and can notice that live sensor requests for the device are kept updating.
13. Go to Dashboards section in [uBeac](https://app.ubeac.io/ "uBeac link"), and create a dashboard to lively check the detailed data.
14. Edit the dashboard. Drag widgets, choose a device for sound detection, and set the sensors.
15. Move to the command prompt.
16. Move to MotionCamera directory.
17. Update the IP address from IP Webcam mobile application and copy the entire html code.
18. Go to Dashboards section in [uBeac](https://app.ubeac.io/ "uBeac link").
19. In the dashboard, drag raw file for a widget and go to setting option.
20. In advanced setting, paste the copied html code.
21. Check the dashboard with data and test warning email with deliberate noise.

4.What is used in the project?
--------------------------------
1. Raspberry Pi 3 Model B
2. uBeac IoT Platform - [uBeac](https://app.ubeac.io/ "uBeac link")
3. Python programming language - version 3
4. SciPy - module for sound detection program
5. NumPy - module for sound detection program
6. Shell scripts
7. LANmic - android mobile application
8. IP Webcam - android mobile application

5.Contribution
----------------
* I additionally implemented an alarm system in the sound detector and live camera operation. 
I also modified few mathematical expressions/errors and added unit for each sensor in the sound detector program for the better performance and readability.

6.Where can I get more help?
------------------------------
* Use of uBEAC: <https://www.hackster.io/amir-pournasserian/how-to-monitor-your-computer-with-ubeac-b20fdb/>
* Use of HTML Language: <https://developer.mozilla.org/ko/docs/Web/HTML/>
* If you have any questions or find any errors of the program, please contact me at <21900421@handong.edu>

