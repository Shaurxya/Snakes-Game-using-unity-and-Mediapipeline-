# Testing Guide

## Manual Testing

Since this is a game with hardware dependencies (webcam) and graphical output, automated testing is limited. Here's how to test the game manually:

### Prerequisites
1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Ensure you have a working webcam

### Test Cases

#### Test 1: Game Launch
**Steps:**
1. Run `python snake_game.py`
2. Verify two windows open:
   - Game window (800x600)
   - Hand tracking window (webcam feed)

**Expected:** Both windows open successfully, snake appears in center, food spawns randomly

#### Test 2: Hand Control
**Steps:**
1. Position hand in front of camera
2. Move hand left - verify snake moves left
3. Move hand right - verify snake moves right
4. Move hand up - verify snake moves up
5. Move hand down - verify snake moves down

**Expected:** Snake follows hand movement direction with smooth control

#### Test 3: Keyboard Fallback
**Steps:**
1. Press arrow keys (up, down, left, right)
2. Verify snake responds to each key

**Expected:** Keyboard controls work as backup to hand gestures

#### Test 4: Food Collection
**Steps:**
1. Navigate snake to red food block
2. Collect the food

**Expected:** 
- Score increases by 1
- Snake grows by 1 segment
- New food spawns at random location

#### Test 5: Self-Collision
**Steps:**
1. Grow snake by collecting several food items
2. Navigate to collide with snake's own body

**Expected:** 
- Game over screen appears
- Final score displayed
- "Press SPACE to restart" message shown

#### Test 6: Game Restart
**Steps:**
1. After game over, press SPACE

**Expected:**
- Game resets to initial state
- Score resets to 0
- Snake back to starting position and length

#### Test 7: Exit Game
**Steps:**
1. Press ESC key

**Expected:** Both windows close, game exits cleanly

### Structure Tests

Run the automated structure test:
```bash
python3 -c "
import sys
with open('snake_game.py', 'r') as f:
    content = f.read()
checks = [
    ('class Snake:', 'Snake class'),
    ('class Food:', 'Food class'),
    ('class HandDetector:', 'HandDetector class'),
    ('class Game:', 'Game class'),
]
for check, desc in checks:
    assert check in content, f'{desc} not found'
print('All structure checks passed!')
"
```

### Performance Considerations

- Game should run at ~15 FPS
- Hand detection should have minimal lag
- No memory leaks during extended play

### Known Limitations

- Requires Python 3.8+
- Webcam must be available
- Lighting conditions affect hand detection accuracy
- Works best with single hand in frame
