from pathlib import Path

from PIL import Image

from drivers.factory import create_driver
from renderer import Renderer
from widgets.clock_widget import ClockWidget


OUTPUT_PATH = Path("output") / "self_test_dashboard.png"


def main() -> int:
    clock = ClockWidget()
    clock_data = clock.render()

    if not isinstance(clock_data, dict):
        raise TypeError(f"ClockWidget.render() must return dict, got {type(clock_data)!r}")
    for key in ("time", "date"):
        if key not in clock_data:
            raise KeyError(f"ClockWidget.render() missing key: {key}")

    renderer = Renderer()
    image = renderer.render()

    if not isinstance(image, Image.Image):
        raise TypeError(f"Renderer.render() must return PIL.Image.Image, got {type(image)!r}")

    expected_size = (1360, 480)
    if image.size != expected_size:
        raise ValueError(f"Unexpected image size: {image.size}, expected {expected_size}")

    OUTPUT_PATH.parent.mkdir(exist_ok=True)
    image.save(OUTPUT_PATH)

    driver = create_driver()
    print(f"ClockWidget: ok -> {clock_data['time']} {clock_data['date']}")
    print(f"Renderer: ok -> {image.mode} {image.size}")
    print(f"Saved: {OUTPUT_PATH}")
    print(f"Driver selected: {driver.__class__.__name__}")
    print("Self-test completed successfully.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

