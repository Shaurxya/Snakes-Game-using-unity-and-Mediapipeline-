# Game Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────┐
│                    Snake Game System                     │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│   Webcam     │    │  Game Logic  │    │   Display    │
│   Input      │    │              │    │   Output     │
└──────────────┘    └──────────────┘    └──────────────┘
        │                   │                   │
        │                   │                   │
        ▼                   ▼                   ▼
┌──────────────┐    ┌──────────────┐    ┌──────────────┐
│  MediaPipe   │    │    Snake     │    │   Pygame     │
│  HandDetector│───▶│    Game      │───▶│   Renderer   │
└──────────────┘    └──────────────┘    └──────────────┘
        │                   │
        │                   │
        ▼                   ▼
┌──────────────┐    ┌──────────────┐
│  OpenCV      │    │  Collision   │
│  Processing  │    │  Detection   │
└──────────────┘    └──────────────┘
```

## Component Details

### 1. HandDetector Class
- **Purpose:** Detect and track hand landmarks
- **Dependencies:** MediaPipe, OpenCV
- **Key Methods:**
  - `find_hands()`: Process frame and detect hands
  - `get_hand_center()`: Calculate hand center position
  - `draw_landmarks()`: Draw hand landmarks on frame

### 2. Snake Class
- **Purpose:** Manage snake state and behavior
- **Key Attributes:**
  - `positions`: List of (x, y) coordinates
  - `direction`: Current movement direction
  - `length`: Current snake length
- **Key Methods:**
  - `update()`: Move snake and check collisions
  - `render()`: Draw snake on screen
  - `set_direction()`: Change snake direction

### 3. Food Class
- **Purpose:** Manage food spawning
- **Key Attributes:**
  - `position`: Food location (x, y)
- **Key Methods:**
  - `randomize_position()`: Spawn food at random location
  - `render()`: Draw food on screen

### 4. Game Class
- **Purpose:** Main game controller
- **Dependencies:** All other classes
- **Key Methods:**
  - `run()`: Main game loop
  - `handle_hand_input()`: Process hand gestures
  - `handle_keyboard_input()`: Process keyboard input
  - `render()`: Draw all game elements

## Data Flow

```
Webcam → OpenCV → MediaPipe → Hand Landmarks → Direction
                                                     ↓
Snake Position ← Game Logic ← Direction Calculation ┘
       ↓
Collision Check → Game Over / Food Collection
       ↓
Pygame Render → Display
```

## Control Flow

1. **Initialization**
   - Create game window
   - Initialize snake at center
   - Spawn initial food
   - Start webcam capture

2. **Main Loop** (15 FPS)
   - Capture webcam frame
   - Detect hand landmarks
   - Calculate hand movement
   - Update snake direction
   - Move snake
   - Check collisions
   - Check food collection
   - Render frame

3. **Event Handling**
   - Process keyboard input
   - Handle window events
   - Manage game state

4. **Cleanup**
   - Release webcam
   - Close windows
   - Exit gracefully

## Key Features

### Hand Tracking
- Uses MediaPipe Hands solution
- Tracks wrist position as reference point
- Calculates movement delta between frames
- Applies dead zone threshold to prevent jitter

### Game Mechanics
- Grid-based movement (20x20 pixel cells)
- Snake wraps around screen edges
- Self-collision detection
- Random food spawning
- Score tracking

### Visual Feedback
- Real-time hand landmark display
- Score overlay
- Game over screen
- Control instructions
