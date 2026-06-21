from PIL import Image

from .base_driver import DisplayDriver
from waveshare_epd import epd10in85g


class WaveshareDriver(DisplayDriver):

    def __init__(self):

        self.epd = epd10in85.EPD()
        self.initialized = False

    def startup(self):

        if not self.initialized:
            self.epd.init()
            self.initialized = True

    def show(self, image: Image.Image):

        self.startup()

        self.epd.display(
            self.epd.getbuffer(image)
        )

    def clear(self):

        self.startup()

        self.epd.Clear()

    def sleep(self):

        self.epd.sleep()

    def shutdown(self):

        self.sleep()