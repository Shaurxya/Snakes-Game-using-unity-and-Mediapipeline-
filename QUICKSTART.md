# 🚀 Quick Start Guide

## Get Started in 3 Steps

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

This installs:
- **opencv-python** - Webcam processing
- **mediapipe** - Hand tracking
- **pygame** - Game rendering

### Step 2: Run the Game
```bash
python snake_game.py
```

### Step 3: Play!
1. **Position yourself** in front of the webcam
2. **Show your hand** to the camera
3. **Move your hand** to control the snake:
   - Left → Snake goes left
   - Right → Snake goes right
   - Up → Snake goes up
   - Down → Snake goes down

## What You'll See

### Game Window (800x600)
```
┌─────────────────────────────────────┐
│ Score: 0                            │
│                                     │
│         🟩 ← Snake Head             │
│         🟩                          │
│                                     │
│                  🟥 ← Food          │
│                                     │
│                                     │
│ Move hand to control | ESC to quit │
└─────────────────────────────────────┘
```

### Hand Tracking Window
Shows your webcam feed with hand landmarks drawn in real-time.

## Controls

### Primary: Hand Gestures
- **Move hand left/right/up/down** → Snake follows

### Backup: Keyboard
- **Arrow Keys** → Manual control
- **ESC** → Exit game
- **SPACE** → Restart after game over

## Tips for Best Experience

✅ **Good lighting** - Helps hand detection  
✅ **Clear background** - Reduces noise  
✅ **Single hand** - Works best with one hand  
✅ **Smooth movements** - More responsive control  

## Troubleshooting

**Camera not working?**
- Check camera permissions
- Close other apps using camera
- Try unplugging/replugging USB camera

**Hand not detected?**
- Move closer to camera
- Improve lighting
- Keep hand in frame
- Try using keyboard as fallback

**Game too fast/slow?**
Edit `snake_game.py` and change:
```python
FPS = 15  # Lower = slower, Higher = faster
```

---

**That's it! Have fun! 🎮🐍**
