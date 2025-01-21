from PIL import Image, ImageSequence

class ASCIIArtGenerator:
    ASCII_CHARS = "@%#*+=-:. "

    def __init__(self, width=80, height=40):
        self.width = width
        self.height = height

    def resize_image(self, image):
        """Resize the image for ASCII art."""
        return image.resize((self.width, self.height))

    def image_to_ascii(self, image):
        """Convert an image to an ASCII string."""
        image = image.convert('L')  # Convert to grayscale
        pixels = image.getdata()
        ascii_str = "".join(
            [self.ASCII_CHARS[min(len(self.ASCII_CHARS) - 1, pixel // (256 // len(self.ASCII_CHARS)))] for pixel in pixels]
        )
        return ascii_str

    def generate_ascii_frames(self, gif_path):
        """Generate ASCII frames from a GIF file."""
        try:
            with Image.open(gif_path) as im:
                frames = []
                for frame in ImageSequence.Iterator(im):
                    resized_frame = self.resize_image(frame)
                    ascii_frame = self.image_to_ascii(resized_frame)
                    frames.append(ascii_frame)
                return frames
        except FileNotFoundError:
            print(f"[ERROR] GIF file not found: {gif_path}")
            return []
