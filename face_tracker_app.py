from kivy.app import App
from kivy.uix.camera import Camera
from kivy.clock import Clock
from kivy.core.audio import SoundLoader
import cv2
import numpy as np

class FaceTrackerApp(App):
    def build(self):
        self.camera = Camera(resolution=(640, 480), play=True)
        self.sound = SoundLoader.load('beep.wav')
        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
        Clock.schedule_interval(self.update, 1.0 / 30.0)  # 30 FPS
        return self.camera

    def update(self, dt):
        if self.camera.texture:
            pixels = np.frombuffer(self.camera.texture.pixels, dtype=np.uint8)
            pixels = pixels.reshape((self.camera.texture.height, self.camera.texture.width, 4))
            frame = cv2.cvtColor(pixels, cv2.COLOR_RGBA2BGR)
            gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
            faces = self.face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
            if len(faces) == 0:
                if self.sound:
                    self.sound.play()

if __name__ == '__main__':
    FaceTrackerApp().run()
