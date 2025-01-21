# TTDOTEXE (TikTok.exe)

TTDOTEXE (TikTok.exe) is an innovative project that combines the charm of TikTok memes, with cutting-edge technology. Developed using Python and Microsoft Azure Quantum Framework, this project brings a playful yet technical approach to blockchain and ASCII art.

## Features

- **ASCII Art Animation**: Convert GIFs into stunning ASCII animations for terminal displays.
- **Quantum Computing Integration**: Leveraging Microsoft Azure Quantum Framework for enhanced cryptographic and computational efficiency.
- **Solana Blockchain**: Powered by Solana's high-speed, low-cost architecture, making blockchain interactions seamless.
- **Python-Based SPL Token**: First-of-its-kind Solana token coded entirely in Python.
- **Community-Focused**: Fully open-source to inspire collaboration and creativity.

## Visual Insights

### Understanding Color and ASCII Conversion

#### Color Conversion in ASCII Art
TTDOTEXE maps colors from GIF frames to ASCII characters with precision.

![8-bit Color Table](./images_rdm/8-bit_color_table.png)
*Example of 8-bit color mapping for ASCII art.*

#### Brightness and Pixel Analysis
Brightness and pixel saturation are key to selecting ASCII characters for animations.

![Brightness and Saturation Analysis](./images_rdm/imgBrightnes.png)
*Brightness and saturation levels affecting ASCII mapping.*

#### Frame-by-Frame Processing
Smooth animations are achieved through careful frame-by-frame analysis.

![Frame Processing](./images_rdm/imgVideoFrames.png)
*Frame-by-frame analysis for seamless animations.*

---

## Prerequisites

Before running the project, ensure you have the following installed:

- **Docker**
- **Python 3.8+**
- **pip**

## Installation

1. Clone the repository:

```bash
git clone https://github.com/ttdotexe/tiktokexe.git
cd tiktokexe
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. (Optional) Set up a virtual environment:

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

## Running the Project Locally

1. Run the ASCII art animation:

```bash
python TIKTOKEXE.py
```

2. Fetch token holders using the fetch_wallet script:

```bash
python fetch_wallet.py
```

## Running with Docker

1. Build the Docker image:

```bash
docker build -t tiktokexe .
```

2. Run the container:

```bash
docker run --rm -it tiktokexe
```

## Project Structure

```plaintext
.
├── assets                # GIFs and other assets
├── images_rdm            # Reference images
├── src                   # Source code
│   ├── ascii_generator.py
│   ├── ascii_player.py
│   ├── utils.py
├── translations          # Translation files
├── TIKTOKEXE.py          # Main entry point
├── fetch_wallet.py       # Script to fetch token holders
├── requirements.txt      # Python dependencies
├── Dockerfile            # Docker configuration
└── README.md             # Project documentation
```

## Why Microsoft Azure Quantum?

Azure Quantum provides state-of-the-art quantum-inspired algorithms that enhance cryptographic functions, optimize computational processes, and enable secure key exchanges. This integration ensures TTDOTEXE remains efficient, scalable, and secure.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contributing

Contributions are welcome! Feel free to open issues or submit pull requests.

## Contact

Follow the journey of TTDOTEXE on [GitHub](https://github.com/ttdotexe/tiktokexe). Share your feedback, and let’s make this project even better!