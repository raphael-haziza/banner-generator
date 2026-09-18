from .config import BannerConfig
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont

class BannerGenerator:
    def __init__(self, config):
        self.config = config

    def create_image(self):
        blank_image = Image.new("RGB", (self.config.width, self.config.height), (0, 0, 0)) # black background

        return blank_image

    def write_text(self, image):
        config_font = ImageFont.truetype(self.config.font_path, self.config.font_size)
        draw = ImageDraw.Draw(image)

        size_tuple = draw.textbbox((0,0), self.config.text, config_font)

        centered_width = (self.config.width - (size_tuple[2] - size_tuple[0])) // 2 # (image_width - (right - left)) // 2 to center it on the horizontal
        centered_height = (self.config.height - (size_tuple[3] - size_tuple[1])) // 2 # (image_height - (bottom - top)) // 2 to center it on the vertical

        draw.text((centered_width, centered_height), self.config.text, (255, 255, 255), config_font)

        return image

def main():
    config = BannerConfig("Raphaël Haziza", 1600, 400, 70, "assets/fonts/PressStart2P-Regular.ttf")
    generator = BannerGenerator(config)

    temp_image = generator.create_image()
    temp_image = generator.write_text(temp_image)

    current_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    temp_image.save("output/" + current_date + "_" + str(config.width) + "x" + str(config.height) + "_" + config.text + "." + config.format)

if __name__ == "__main__":
    main()