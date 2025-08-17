import io
import time
from PIL import ImageChops, Image


def is_video_playing(driver, duration=10, interval=1):
    """
    duration: total time to monitor in seconds
    interval: time between screenshots
    """
    previous_frame = None
    frames_changed = 0
    checks = int(duration / interval)

    for _ in range(checks):
        screenshot = driver.get_screenshot_as_png()
        frame = Image.open(io.BytesIO(screenshot))

        if previous_frame:
            diff = ImageChops.difference(previous_frame, frame)
            if diff.getbbox():  # Non-zero diff means video has changed
                frames_changed += 1
        previous_frame = frame
        time.sleep(interval)

    if frames_changed >= 1:
        return True
    else:
        return False
