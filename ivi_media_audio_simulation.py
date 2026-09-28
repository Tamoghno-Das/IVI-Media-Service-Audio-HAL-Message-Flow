import time
from datetime import datetime


def log(component, message):
    timestamp = datetime.now().strftime("%H:%M:%S")
    print(f"{timestamp}  [{component}] {message}")


# -------------------------------------------------
# Audio HAL
# -------------------------------------------------

class AudioHAL:

    def set_volume(self, volume):
        log("AudioHAL", f"Received volume command: {volume}%")
        time.sleep(0.5)

        log("AudioHAL", f"Setting hardware volume to {volume}%")
        time.sleep(0.5)

        log("AudioHAL", "Volume successfully updated")

    def play_audio(self):
        log("AudioHAL", "Received PLAY command")
        time.sleep(0.5)

        log("AudioHAL", "Starting audio hardware")
        time.sleep(0.5)

        log("AudioHAL", "Audio playback started")

    def pause_audio(self):
        log("AudioHAL", "Received PAUSE command")
        time.sleep(0.5)

        log("AudioHAL", "Pausing audio hardware")
        time.sleep(0.5)

        log("AudioHAL", "Audio playback paused")

    def stop_audio(self):
        log("AudioHAL", "Received STOP command")
        time.sleep(0.5)

        log("AudioHAL", "Stopping audio hardware")
        time.sleep(0.5)

        log("AudioHAL", "Audio playback stopped")


# -------------------------------------------------
# Audio Manager
# -------------------------------------------------

class AudioManager:

    def __init__(self):
        self.audio_hal = AudioHAL()

    def play(self):
        log("AudioManager", "Forwarding PLAY request to Audio HAL")
        self.audio_hal.play_audio()

    def pause(self):
        log("AudioManager", "Forwarding PAUSE request to Audio HAL")
        self.audio_hal.pause_audio()

    def stop(self):
        log("AudioManager", "Forwarding STOP request to Audio HAL")
        self.audio_hal.stop_audio()

    def set_volume(self, volume):
        log("AudioManager", f"Forwarding volume request: {volume}%")
        self.audio_hal.set_volume(volume)


# -------------------------------------------------
# Media Service
# -------------------------------------------------

class MediaService:

    def __init__(self):
        self.audio_manager = AudioManager()

    def play_music(self):
        log("MediaService", "PLAY request received")
        time.sleep(0.5)

        log("MediaService", "Sending PLAY command to AudioManager")
        self.audio_manager.play()

    def pause_music(self):
        log("MediaService", "PAUSE request received")
        time.sleep(0.5)

        log("MediaService", "Sending PAUSE command to AudioManager")
        self.audio_manager.pause()

    def stop_music(self):
        log("MediaService", "STOP request received")
        time.sleep(0.5)

        log("MediaService", "Sending STOP command to AudioManager")
        self.audio_manager.stop()

    def change_volume(self, volume):
        log("MediaService", f"Volume request received: {volume}%")
        time.sleep(0.5)

        log("MediaService", "Sending volume command to AudioManager")
        self.audio_manager.set_volume(volume)


# -------------------------------------------------
# Media Controller
# -------------------------------------------------

class MediaController:

    def __init__(self):
        self.media_service = MediaService()

    def user_play(self):
        log("MediaController", "User pressed PLAY")
        self.media_service.play_music()

    def user_pause(self):
        log("MediaController", "User pressed PAUSE")
        self.media_service.pause_music()

    def user_stop(self):
        log("MediaController", "User pressed STOP")
        self.media_service.stop_music()

    def user_volume(self, volume):
        log("MediaController", f"User changed volume to {volume}%")
        self.media_service.change_volume(volume)


# -------------------------------------------------
# Main IVI Simulation
# -------------------------------------------------

def main():

    print("\n==========================================")
    print("      IVI MEDIA - AUDIO HAL SIMULATION")
    print("==========================================\n")

    controller = MediaController()

    # User presses Play
    controller.user_play()

    print("\n------------------------------------------\n")

    # User increases volume
    controller.user_volume(70)

    print("\n------------------------------------------\n")

    # User pauses music
    controller.user_pause()

    print("\n------------------------------------------\n")

    # User plays music again
    controller.user_play()

    print("\n------------------------------------------\n")

    # User stops music
    controller.user_stop()

    print("\n==========================================")
    print("           SIMULATION COMPLETED")
    print("==========================================\n")


if __name__ == "__main__":
    main()
    