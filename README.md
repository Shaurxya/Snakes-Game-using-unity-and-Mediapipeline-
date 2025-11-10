# 🐍 Hand-Controlled Snake Game (MediaPipe + Python)

A fun interactive Snake game controlled entirely by hand gestures using Google MediaPipe for real-time hand tracking and Pygame for rendering. Move the snake by moving your hand — no keyboard required!

## 🎮 Controls

### 🖐️ Hand Detection
MediaPipe tracks your hand landmarks via webcam in real-time.

### 👆 Movement
Move your hand in front of the camera to control the snake's direction:
- **Move left** — snake moves left
- **Move right** — snake moves right  
- **Move up** — snake moves up
- **Move down** — snake moves down

### ⌨️ Keyboard (Fallback)
Arrow keys also work as alternative controls if needed.

### 🍎 Objective
Eat the red food to grow longer and increase your score!

## 🧠 Tech Stack

- **Python 3.11** — Core programming language
- **MediaPipe** — Hand-tracking and landmark detection
- **OpenCV** — Webcam feed processing
- **Pygame** — Game logic and rendering

## 🚀 Features

✅ **Real-time hand gesture control** — Move your hand, control the snake  
✅ **MediaPipe hand tracking** — Accurate hand landmark detection  
✅ **Smooth gameplay** — Optimized for responsive controls  
✅ **Score tracking** — Track your progress  
✅ **Collision detection** — Game over when snake hits itself  
✅ **Food spawning** — Random food placement  
✅ **Visual feedback** — See your hand tracking in real-time

## 📦 Installation

### Prerequisites
- Python 3.8 or higher
- Webcam (built-in or external)

### Setup

1. **Clone the repository:**
```bash
git clone https://github.com/Shaurxya/Snakes-Game-using-unity-and-Mediapipeline-.git
cd Snakes-Game-using-unity-and-Mediapipeline-
```

2. **Install dependencies:**
```bash
pip install -r requirements.txt
```

## 🎯 Usage

1. **Run the game:**
```bash
python snake_game.py
```

2. **Position yourself:**
   - Sit in front of your webcam
   - Ensure good lighting
   - Keep your hand visible in the camera frame

3. **Play:**
   - The game window and hand tracking window will open
   - Move your hand to control the snake direction
   - Eat the red food blocks to grow and score points
   - Avoid hitting your own tail!

4. **Controls:**
   - **ESC** — Quit game
   - **SPACE** — Restart after game over
   - **Arrow keys** — Fallback keyboard controls

## 🎨 Game Features

### Snake
- Green body segments
- Dark green head
- Grows when eating food
- Wraps around screen edges

### Food
- Red square blocks
- Randomly spawns after being eaten
- Each food increases score by 1

### Hand Tracking
- Real-time hand detection
- Visual landmarks displayed
- Movement threshold to prevent jitter
- Mirror mode for intuitive control

## 🛠️ Configuration

You can modify these settings in `snake_game.py`:

```python
SCREEN_WIDTH = 800      # Game window width
SCREEN_HEIGHT = 600     # Game window height
GRID_SIZE = 20          # Size of each grid cell
FPS = 15                # Game speed (frames per second)
```

## 🐛 Troubleshooting

### Camera not working
- Check if your webcam is connected
- Ensure no other application is using the webcam
- Grant camera permissions if prompted

### Hand not detected
- Improve lighting conditions
- Keep your hand within camera view
- Try moving your hand slower
- Adjust `min_detection_confidence` in the code

### Game too fast/slow
- Adjust the `FPS` variable in the code
- Higher FPS = faster game
- Lower FPS = slower game

## 🤝 Contributing

Contributions are welcome! Feel free to:
- Report bugs
- Suggest new features
- Submit pull requests

## 📄 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- Google MediaPipe team for the amazing hand tracking solution
- Pygame community for the game development framework
- OpenCV for computer vision capabilities

## 📧 Contact

For questions or feedback, please open an issue on GitHub.

---

**Enjoy the game! 🎮🐍**
