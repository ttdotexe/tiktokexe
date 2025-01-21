import os
import sys
import time


class ASCIIArtPlayer:
    def __init__(self, frames, width, height, speed=0.1):
        """Initialize the ASCII Art Player."""
        self.frames = frames
        self.width = width
        self.height = height
        self.speed = speed

    def _generate_ascii_title(self, dots):
        """Generate the ASCII art for the project title."""
        ascii_title = r"""
 /$$$$$$$$ /$$ /$$    /$$$$$$$$        /$$       /$$$$$$$$ /$$   /$$ /$$$$$$$$
|__  $$__/|__/| $$   |__  $$__/       | $$      | $$_____/| $$  / $$| $$_____/
   | $$    /$$| $$   /$$| $$  /$$$$$$ | $$   /$$| $$      |  $$/ $$/| $$      
   | $$   | $$| $$  /$$/| $$ /$$__  $$| $$  /$$/| $$$$$    \  $$$$/ | $$$$$   
   | $$   | $$| $$$$$$/ | $$| $$  \ $$| $$$$$$/ | $$__/     >$$  $$ | $$__/   
   | $$   | $$| $$_  $$ | $$| $$  | $$| $$_  $$ | $$       /$$/\  $$| $$      
   | $$   | $$| $$ \  $$| $$|  $$$$$$/| $$ \  $$| $$$$$$$$| $$  \ $$| $$$$$$$$
   |__/   |__/|__/  \__/|__/ \______/ |__/  \__/|________/|__/  |__/|________/                                             
        """
        return f"{ascii_title.strip()}{dots}"

    def play(self):
        """Play the ASCII animation with a fixed project title."""
        try:
            dots = ["●", "●●", "●●●"]  # Animation dots
            frame_index = 0
            dot_index = 0
            last_dot_update = time.time()

            # Clear the terminal and set up the layout
            os.system('cls' if os.name == 'nt' else 'clear')

            # Display the static ASCII title once
            sys.stdout.write("\033[{};0H".format(self.height + 1))  # Position cursor below GIF
            sys.stdout.write(self._generate_ascii_title("") + "\n")
            sys.stdout.flush()

            while True:
                # Move cursor to the top-left for GIF animation
                sys.stdout.write("\033[H")
                sys.stdout.flush()

                # Display the frame (GIF animation)
                for i in range(self.height):
                    print(self.frames[frame_index][i * self.width:(i + 1) * self.width])

                # Update the dots independently every 0.5 seconds
                if time.time() - last_dot_update >= 0.5:
                    sys.stdout.write("\033[{};80H".format(self.height + 8))  # Position cursor for dots
                    sys.stdout.write("   ")  # Clear old dots
                    sys.stdout.write("\033[{};80H".format(self.height + 8))
                    sys.stdout.write(dots[dot_index % len(dots)])  # Update dots only
                    sys.stdout.flush()
                    dot_index = (dot_index + 1) % len(dots)
                    last_dot_update = time.time()

                # Increment the frame index for the animation
                frame_index = (frame_index + 1) % len(self.frames)
                time.sleep(self.speed)

        except KeyboardInterrupt:
            print("\n[INFO] Playback interrupted by user.")
