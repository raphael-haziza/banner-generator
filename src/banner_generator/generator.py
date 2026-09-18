from .config import BannerConfig
from datetime import datetime
from PIL import Image, ImageDraw, ImageFont, ImageFilter

class BannerGenerator:
    def __init__(self, config):
        self.config = config

    def create_image(self, mode, color):
        blank_image = Image.new(mode, (self.config.width, self.config.height), color) # black transparant background

        return blank_image

    def write_text(self, image, color):
        config_font = ImageFont.truetype(self.config.font_path, self.config.font_size)
        draw = ImageDraw.Draw(image)

        size_tuple = draw.textbbox((0,0), self.config.text, config_font)

        centered_width = (self.config.width - (size_tuple[2] - size_tuple[0])) // 2 # (image_width - (right - left)) // 2 to center it on the horizontal
        centered_height = (self.config.height - (size_tuple[3] - size_tuple[1])) // 2 # (image_height - (bottom - top)) // 2 to center it on the vertical

        draw.text((centered_width, centered_height), self.config.text, color, config_font)

        return image

    def apply_glow(self, image, opacity_glow, glow_size):
        glow_image = self.create_image("RGBA", (0, 0, 0, 0))
        glow_image = self.write_text(glow_image, (255, 255, 255, opacity_glow))
        glow_filter = ImageFilter.GaussianBlur(glow_size) # glow effect using gaussian blur
        glow_image = glow_image.filter(glow_filter)

        return Image.alpha_composite(image, glow_image)


def main():
    config = BannerConfig("Raphaël Haziza", 1600, 400, 70, "assets/fonts/PressStart2P-Regular.ttf")
    generator = BannerGenerator(config)

    temp_image = generator.create_image("RGBA", (0, 0, 0, 255))
    temp_image = generator.apply_glow(temp_image, 255, 5)
    temp_image = generator.apply_glow(temp_image, 235, 10)
    temp_image = generator.apply_glow(temp_image, 195, 25)
    temp_image = generator.apply_glow(temp_image, 165, 35)
    temp_image = generator.write_text(temp_image, (255, 255, 255))

    current_date = datetime.now().strftime("%Y-%m-%d-%H-%M-%S")
    temp_image.save("output/" + current_date + "_" + str(config.width) + "x" + str(config.height) + "_" + config.text + "." + config.format)

if __name__ == "__main__":
    main()