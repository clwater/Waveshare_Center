from abc import ABC, abstractmethod
from PIL import Image


class DisplayDriver(ABC):

    @abstractmethod
    def show(self, image: Image.Image) -> None:
        """
        显示图像
        """
        pass

    def startup(self) -> None:
        """
        初始化设备（可选）
        """
        pass

    def clear(self) -> None:
        """
        清屏（可选）
        """
        pass

    def sleep(self) -> None:
        """
        进入低功耗模式（可选）
        """
        pass

    def shutdown(self) -> None:
        """
        关闭设备（可选）
        """
        pass