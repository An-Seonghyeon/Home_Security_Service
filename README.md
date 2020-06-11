HOME SECURITY SERVICE
======================
Presentation video URL:

1.What does this project do?
-------------------------------
This is a program to check the sound level (amplitude, frequency, max peak) of the surrounding environment in real time.
It also displays the real time situation of the surrounding environment through the camera.
All the detailed data are shown in user customized dashboard in uBEAC website.

2.Why is this project useful?
---------------------------------
These days, security and privacy policy issues are rising. A lot of people are not guaranteed thier rights to be protected and kept anxious about it. People want to check what is going on near their places immediately and this program is best for them to remove unrest. Just by implementing this program, people can monitor what is happening in the surrounding environment in real time.

3.How do I get started?
-----------------------------
1. Download or clone the repository
2. Download the LANmic and IP Webcam android mobile application
3. Note the IP addresses shown in LANmic and IP Webcam mobile application
4. Create an account for uBeac IoT Platform here: [uBeac](https://app.ubeac.io/ "uBeac link")
5. Create a gateway with UID, Name, and choose uBeac Multiple Devices as a firmware
6. Move to the command prompt
7. Install modules for python program in the command prompt
   <pre><code>{pip install scipy}</code></pre>
   <pre><code>{pip install numpy}</code></pre>
8. Move to SoundDetection directory
9. Update the file location, configuration section, and IP address from LANmic in main.py
10. Go to move 

4.What is used in the project?
----------------------------------
1. Raspberry Pi 3 Model B
2. uBeac IoT Platform - [uBeac](https://app.ubeac.io/ "uBeac link")
3. Python programming language - version 3
4. SciPy - module for sound detection program
5. NumPy - module for sound detection program
6. Shell scripts
7. LANmic - android mobile application
8. IP Webcam - android mobile application

5.Where can I get more help?
----------------------------------
* Use of uBEAC: <https://www.hackster.io/amir-pournasserian/how-to-monitor-your-computer-with-ubeac-b20fdb/>
* Use of HTML Language: <https://developer.mozilla.org/ko/docs/Web/HTML/>
* If you have any questions or find any errors of the program, please contact me at <21900421@handong.edu>

