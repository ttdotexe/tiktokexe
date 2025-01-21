from src.ascii_generator import ASCIIArtGenerator
from src.ascii_player import ASCIIArtPlayer
from src.utils import get_user_speed

if __name__ == "__main__":
    input_gif = './assets/gif-to-ascii.gif'
    width, height = 90, 30

    print("[INFO] Generating ASCII frames...")
    generator = ASCIIArtGenerator(width=width, height=height)
    frames = generator.generate_ascii_frames(input_gif)

    if frames:
        user_speed = get_user_speed()
        print("[INFO] Starting ASCII animation...")
        player = ASCIIArtPlayer(frames, width=width, height=height, speed=user_speed)
        player.play()
    else:
        print("[ERROR] No frames to display.")
