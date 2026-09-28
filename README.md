# IVI Media Service – Audio HAL Simulation

A simple Python-based simulation of an **In-Vehicle Infotainment (IVI)** audio system that demonstrates how user media commands propagate through different software layers, from the Media Controller to the Audio HAL and finally to the audio hardware.

## 📌 Project Overview

This project simulates the message flow inside an IVI system for common media operations such as:

* ▶️ Play music
* ⏸️ Pause music
* ⏹️ Stop music
* 🔊 Increase or change volume

The simulation demonstrates how a user's action travels through the following components:

```text
User
  ↓
Media Controller
  ↓
Media Service
  ↓
Audio Manager
  ↓
Audio HAL
  ↓
Audio Hardware
```

The project focuses on understanding the interaction between the **Media Service and Audio HAL** using a simple Python implementation and Android-style system logs.

## 🎯 Objectives

* Understand the basic architecture of an IVI audio system.
* Demonstrate message propagation between software components.
* Simulate communication between Media Service and Audio HAL.
* Generate logs showing how user commands move through the system.
* Understand the role of the Audio HAL in communicating with audio hardware.

## 🏗️ Architecture

```text
                 USER
                   │
                   │ Media Command
                   ▼
        ┌─────────────────────┐
        │  Media Controller   │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │    Media Service    │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │    Audio Manager    │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │      Audio HAL      │
        └──────────┬──────────┘
                   │
                   ▼
        ┌─────────────────────┐
        │   Audio Hardware    │
        └─────────────────────┘
```

## ⚙️ Technologies Used

* **Python 3**
* Object-Oriented Programming
* Console/System Logging
* IVI Architecture Concepts

## 📂 Project Structure

```text
IVI-Media-Audio-HAL/
│
├── ivi_media_audio_simulation.py
└── README.md
```

## 🚀 How to Run

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR-USERNAME/IVI-Media-Audio-HAL.git
```

### 2. Navigate to the Project

```bash
cd IVI-Media-Audio-HAL
```

### 3. Run the Simulation

```bash
python ivi_media_audio_simulation.py
```

## 🖥️ Sample Output

```text
==========================================
      IVI MEDIA - AUDIO HAL SIMULATION
==========================================

[MediaController] User pressed PLAY
[MediaService] PLAY request received
[MediaService] Sending PLAY command to AudioManager
[AudioManager] Forwarding PLAY request to Audio HAL
[AudioHAL] Received PLAY command
[AudioHAL] Starting audio hardware
[AudioHAL] Audio playback started

------------------------------------------

[MediaController] User changed volume to 70%
[MediaService] Volume request received: 70%
[MediaService] Sending volume command to AudioManager
[AudioManager] Forwarding volume request: 70%
[AudioHAL] Received volume command: 70%
[AudioHAL] Setting hardware volume to 70%
[AudioHAL] Volume successfully updated

------------------------------------------

[MediaController] User pressed PAUSE
[MediaService] PAUSE request received
[MediaService] Sending PAUSE command to AudioManager
[AudioManager] Forwarding PAUSE request to Audio HAL
[AudioHAL] Received PAUSE command
[AudioHAL] Pausing audio hardware
[AudioHAL] Audio playback paused
```

## 🔄 Message Flow

For example, when the user presses **PLAY**:

```text
User presses PLAY
       ↓
Media Controller receives input
       ↓
Media Service processes the request
       ↓
Audio Manager forwards the command
       ↓
Audio HAL receives PLAY command
       ↓
Audio Hardware starts playback
```

Similarly, commands such as **PAUSE**, **STOP**, and **VOLUME CHANGE** follow the same communication path.

## 📊 Supported Operations

| Operation | Description           |
| --------- | --------------------- |
| PLAY      | Starts audio playback |
| PAUSE     | Pauses audio playback |
| STOP      | Stops audio playback  |
| VOLUME    | Changes audio volume  |

## 💡 Key Learning

This project provides a simplified understanding of how different layers of an **In-Vehicle Infotainment system** communicate with each other.

It demonstrates that a user action does not directly control the hardware. Instead, the request passes through multiple software layers before reaching the **Audio HAL**, which represents the interface between higher-level software and the underlying audio hardware.

## 🔮 Future Improvements

The simulation can be extended with:

* Real Android Automotive APIs
* Android Logcat integration
* Navigation and media interaction
* Incoming-call audio interruption
* Automatic media resume
* Multiple audio sources
* Volume and audio-focus management
* Android Automotive Emulator integration

## 👨‍💻 Author

**Tamoghno Das**

Computer Science & Engineering Student

## 📄 Project Context

This project was developed as part of **Module 6 – IVI (In-Vehicle Infotainment) Systems** and demonstrates the message flow between a Media Service and Audio HAL through a simplified simulation.

