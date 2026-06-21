from PIL import Image

from .base_driver import DisplayDriver
from waveshare_epd import epd10in85


class WaveshareDriver(DisplayDriver):

    def __init__(self):

        self.epd = epd10in85.EPD()
        self.initialized = False

    def startup(self):

        if not self.initialized:
            init_fn = getattr(self.epd, "init", None) or getattr(self.epd, "Init", None)
            if init_fn is None:
                raise AttributeError("EPD driver has no init/Init method")
            init_fn()
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