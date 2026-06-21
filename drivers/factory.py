from pathlib import Path

from drivers.preview_driver import PreviewDriver


def create_driver():

    if Path("/dev/spidev0.0").exists():
        from drivers.waveshare_driver import WaveshareDriver
        return WaveshareDriver()

    return PreviewDriver()