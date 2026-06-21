from datetime import datetime


class ClockWidget:

    def render(self):

        now = datetime.now()

        return {
            "time": now.strftime("%H:%M"),
            "date": now.strftime("%Y-%m-%d")
        }