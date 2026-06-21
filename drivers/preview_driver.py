from pathlib import Path
from PIL import Image

from .base_driver import DisplayDriver


class PreviewDriver(DisplayDriver):

    def __init__(self):
        self.output_dir = Path("output")
        self.output_dir.mkdir(exist_ok=True)

    def show(self, image: Image.Image) -> None:

        image.save(
            self.output_dir / "dashboard.png"
        )

        image.show()