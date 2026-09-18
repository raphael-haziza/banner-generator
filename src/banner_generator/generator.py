from .config import BannerConfig
from datetime import datetime
from PIL import Image

class BannerGenerator:
    def __init__(self, config):
        self.config = config

    def create_image(self):
        blank_image = Image.new("RGB", (self.config.width, self.config.height), (0, 0, 0)) # black background

        return blank_image

def main():
    config = BannerConfig("Raphaël Haziza", 1600, 400, 120, "assets/fonts/PressStart2P-Regular.ttf")
    generator = BannerGenerator(config)

    temp_image = generator.create_image()
    current_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    temp_image.save("output/" + current_date + "_" + str(config.width) + "x" + str(config.height) + "_" + config.text + "." + config.format)

if __name__ == "__main__":
    main()