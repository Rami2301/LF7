Individual Learning Goal
==========================

During the hackathon, I aim to develop the following competencies in smart home security and facial recognition:

- Technical: Computer vision and machine learning algorithms for facial recognition
- Problem-Solving: Analyzing and solving complex security problems
- Collaboration: Effective teamwork for system design and implementation
- Innovation: Creative solutions for secure and user-friendly smart homes

DIY Problem Definition – 5WH Method
=====================================

***What***

What is the problem? Security for smart homes, specifically controlling access with facial recognition.

***Why***

Why is it important? More and more people want to secure their homes, especially against break-ins. Facial recognition can make access control safer and automated.

***Who***

Who is affected? People who want more security at home, especially homeowners or renters in areas where security is a concern.

***Where***

Where does the problem occur? In homes, apartments, or offices that need extra security.

***When***

When does the problem occur? Particularly when the home is unoccupied or at night when access needs to be monitored.

***Security Features***
- Facial Recognition: Automatic recognition of authorized users and blocking of unauthorized access
- Emergency Alarm: Triggering of an alarm in case of unauthorized access or other security threats
- Notification: Notification of the homeowner in case of unauthorized access or other security threats
- secure: Not able to loose a Key or copy fingerprints like on a Keypad

***Comfort Features***
- Automatic Door Opening: Automatic opening of the door upon recognition of an authorized user
- Smart Home Integration: Integration with other smart home devices for comprehensive control of the house
- User-Friendly Interface: Simple and intuitive operation of the system
- Personalization: Possibility to adapt the system to the individual needs of the user


Blog Post
============

Title
“How Facial Recognition Can Make Your Home Safer”

Content
In a world where security is becoming increasingly important, our facial recognition technology offers an innovative solution for homeowners. With this smart solution, doors only open for authorized individuals. Security you can trust—without the need for keys.

Ideate
==========

***Dream***



- A facial recognition technology that automatically unlocks the door when an authorized user stands in front of it.
- An emergency alarm that is triggered when unauthorized access to the house occurs.
- A notification to the homeowner's smartphone with a picture of the visitor.
- An integration with other smart home devices to offer a comprehensive security solution.
- An option to lock or unlock specific areas of the house as needed.

***Reality***
How realistic is it to make the dream part true?

- Technical feasibility: 8/10 - Facial recognition technology is already available and can be integrated with smart home devices. However, there may be technical challenges in implementing the system, such as ensuring accurate recognition and avoiding false positives.
- Cost: 6/10 - The cost of implementing a facial recognition system can be high, especially if it requires specialized hardware and software. However, the cost can be reduced by using existing smart home devices and integrating them with the facial recognition system.
- User acceptance: 9/10 - Many users are already comfortable with using facial recognition technology, such as Apple's Face ID. However, there may be concerns about privacy and security, which need to be addressed.
- Regulatory compliance: 7/10 - There may be regulatory requirements that need to be met, such as ensuring that the system complies with data protection laws. However, these requirements can be addressed through careful planning and implementation.


***Critique***

- The facial recognition technology is an innovative solution, but it must also be secure and reliable.
- The emergency alarm is important, but it must also be designed to avoid frequent false triggers.
- The notification to the smartphone is a good idea, but it must also be designed to avoid sending unnecessary notifications.



### AEIOU Analysis

| **Category**    | **Description** |
|-----------------|-----------------|
| **A – Activities** | - Homeowners approach the door and interact with the smart security system for facial recognition. <br> - Users manage the system remotely via a smartphone app. <br> - Guests, such as family or delivery personnel, attempt entry, either triggering authorized access or being flagged as unauthorized. |
| **E – Environment** | - The system is placed at the main entrance of the home (front door, gate). <br> - Includes hardware (camera, sensors, Raspberry Pi) integrated into the environment. <br> - The environment’s lighting and outdoor conditions (weather, day/night) can affect the accuracy of facial recognition. |
| **I – Interactions** | - **Homeowner Interaction**: Regular interaction through facial recognition for seamless, hands-free entry. <br> - **Remote Monitoring**: Homeowners receive notifications and can manually grant access via their smartphones. <br> - **Unauthorized Attempt**: Triggers alarms or alerts, prompting the user to respond via the app. <br> - **Visitors**: Limited or temporary access can be granted remotely by the homeowner for guests or deliveries. |
| **O – Objects** | - **Camera**: Used to capture and identify faces. <br> - **Raspberry Pi**: Processes the facial recognition algorithm. <br> - **Smartphone**: Acts as the control hub for notifications, remote access, and system management. <br> - **Smart Lock**: Connected to the system to automatically unlock doors for recognized users. |
| **U – Users** | - **Primary Users**: Homeowners and regular residents who frequently use the system. <br> - **Secondary Users**: Guests, delivery personnel, and service providers who may use temporary access or require approval from the homeowner. <br> - **Extreme Users**: Users who have heightened security concerns (e.g., high-profile individuals or frequent travelers). |



### Activity Diagram

![diagram](https://github.com/user-attachments/assets/aed2b332-c566-49b8-8cf7-63f1220f7107)


### Problem Statement: Smart Home Security Using Facial Recognition
Homeowners and renters who prioritize safety often face the challenge of relying on traditional security systems that are prone to false alarms and unauthorized access. These systems often lack the ability to provide real-time, intelligent monitoring and don’t offer flexible control over who can enter the home.

This problem becomes more significant in households where multiple users (such as family members, visitors, or service providers) need secure access. Current solutions fail to address the need for both reliability and convenience.

To bridge this gap, we aim to develop a smart home security system that uses facial recognition to provide reliable, real-time access control. Our solution will reduce the risk of unauthorized entry, eliminate many false alarms, and offer users the ability to monitor and manage their home’s security remotely.


### Empathy Map

![Empathy Map fertig-1](https://github.com/user-attachments/assets/3ec85879-011f-4a4a-8375-95d9a2e806bd)


### Canvas Business Model 

![Canva Modell drawio](https://github.com/user-attachments/assets/84b0a2ac-e4f3-48c5-9d5c-479d2ddb0048)


### How does it work
Our system works by integrating a smart door lock that can recognize Bluetooth signals. On the Raspberry Pi, we use fswebcam and OpenCV to enable facial recognition. A camera is connected to the Pi and installed above the entrance door. The code is set up in such a way that there is a folder where known faces are stored. You can manually add pictures to this folder or create images through a command. For this, we need a button that can connect to the Raspberry Pi. This button is used to create new images for people who should be authorized. When the button is pressed, 15 pictures of the person in front of the camera are taken, and that person is then added to the list of authorized individuals. If the button is not pressed, nothing happens. If someone steps in front of the camera, the system checks whether the images match any of the authorized individuals. If a match is found, the door lock opens; if not, the door remains closed.
