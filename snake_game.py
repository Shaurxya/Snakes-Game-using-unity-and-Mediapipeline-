"""
Hand-Controlled Snake Game using MediaPipe and Pygame
Controls the snake direction based on hand position detected via webcam
"""

import cv2
import mediapipe as mp
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 20

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 100, 255)
DARK_GREEN = (0, 180, 0)

# Game settings
FPS = 15


class Snake:
    """Snake class to handle snake movement and growth"""
    
    def __init__(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (0, -GRID_SIZE)  # Start moving up
        self.color = GREEN
        self.head_color = DARK_GREEN
        
    def get_head_position(self):
        return self.positions[0]
    
    def update(self):
        cur = self.get_head_position()
        x, y = self.direction
        new = ((cur[0] + x) % SCREEN_WIDTH, (cur[1] + y) % SCREEN_HEIGHT)
        
        if len(self.positions) > 2 and new in self.positions[2:]:
            return False  # Collision with self
        else:
            self.positions.insert(0, new)
            if len(self.positions) > self.length:
                self.positions.pop()
        return True
    
    def reset(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2)]
        self.direction = (0, -GRID_SIZE)
    
    def render(self, surface):
        for i, p in enumerate(self.positions):
            rect = pygame.Rect(p[0], p[1], GRID_SIZE, GRID_SIZE)
            if i == 0:  # Head
                pygame.draw.rect(surface, self.head_color, rect)
                pygame.draw.rect(surface, WHITE, rect, 1)
            else:  # Body
                pygame.draw.rect(surface, self.color, rect)
                pygame.draw.rect(surface, WHITE, rect, 1)
    
    def set_direction(self, direction):
        # Prevent moving in opposite direction
        if (direction[0] * -1, direction[1] * -1) != self.direction:
            self.direction = direction


class Food:
    """Food class to handle food spawning"""
    
    def __init__(self):
        self.position = (0, 0)
        self.color = RED
        self.randomize_position()
    
    def randomize_position(self):
        self.position = (
            random.randint(0, (SCREEN_WIDTH // GRID_SIZE) - 1) * GRID_SIZE,
            random.randint(0, (SCREEN_HEIGHT // GRID_SIZE) - 1) * GRID_SIZE
        )
    
    def render(self, surface):
        rect = pygame.Rect(self.position[0], self.position[1], GRID_SIZE, GRID_SIZE)
        pygame.draw.rect(surface, self.color, rect)
        pygame.draw.rect(surface, WHITE, rect, 1)


class HandDetector:
    """Hand detector using MediaPipe"""
    
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=1,
            min_detection_confidence=0.5,
            min_tracking_confidence=0.5
        )
        self.mp_draw = mp.solutions.drawing_utils
        
    def find_hands(self, frame):
        """Process frame and detect hands"""
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        return results
    
    def get_hand_center(self, hand_landmarks, frame_width, frame_height):
        """Calculate center position of hand"""
        if hand_landmarks:
            # Use wrist landmark as reference
            wrist = hand_landmarks.landmark[0]
            x = int(wrist.x * frame_width)
            y = int(wrist.y * frame_height)
            return x, y
        return None
    
    def draw_landmarks(self, frame, hand_landmarks):
        """Draw hand landmarks on frame"""
        if hand_landmarks:
            self.mp_draw.draw_landmarks(
                frame,
                hand_landmarks,
                self.mp_hands.HAND_CONNECTIONS
            )


class Game:
    """Main game class"""
    
    def __init__(self):
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Hand-Controlled Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.small_font = pygame.font.Font(None, 24)
        
        self.snake = Snake()
        self.food = Food()
        self.score = 0
        self.running = True
        self.game_over = False
        
        # Hand detection
        self.hand_detector = HandDetector()
        self.cap = cv2.VideoCapture(0)
        self.previous_hand_pos = None
        
        # Dead zone threshold
        self.dead_zone = 50
        
    def handle_hand_input(self):
        """Process webcam feed and detect hand gestures"""
        ret, frame = self.cap.read()
        if not ret:
            return None
        
        frame = cv2.flip(frame, 1)  # Mirror the frame
        results = self.hand_detector.find_hands(frame)
        
        if results.multi_hand_landmarks:
            hand_landmarks = results.multi_hand_landmarks[0]
            self.hand_detector.draw_landmarks(frame, hand_landmarks)
            
            frame_height, frame_width, _ = frame.shape
            hand_pos = self.hand_detector.get_hand_center(
                hand_landmarks, frame_width, frame_height
            )
            
            if hand_pos and self.previous_hand_pos:
                dx = hand_pos[0] - self.previous_hand_pos[0]
                dy = hand_pos[1] - self.previous_hand_pos[1]
                
                # Determine direction based on hand movement
                if abs(dx) > abs(dy) and abs(dx) > self.dead_zone:
                    if dx > 0:
                        self.snake.set_direction((GRID_SIZE, 0))  # Right
                    else:
                        self.snake.set_direction((-GRID_SIZE, 0))  # Left
                elif abs(dy) > abs(dx) and abs(dy) > self.dead_zone:
                    if dy > 0:
                        self.snake.set_direction((0, GRID_SIZE))  # Down
                    else:
                        self.snake.set_direction((0, -GRID_SIZE))  # Up
            
            self.previous_hand_pos = hand_pos
        
        # Display webcam feed
        cv2.imshow("Hand Tracking", frame)
        cv2.waitKey(1)
        
        return frame
    
    def handle_keyboard_input(self):
        """Fallback keyboard controls"""
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.snake.set_direction((0, -GRID_SIZE))
        elif keys[pygame.K_DOWN]:
            self.snake.set_direction((0, GRID_SIZE))
        elif keys[pygame.K_LEFT]:
            self.snake.set_direction((-GRID_SIZE, 0))
        elif keys[pygame.K_RIGHT]:
            self.snake.set_direction((GRID_SIZE, 0))
    
    def run(self):
        """Main game loop"""
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                    elif event.key == pygame.K_SPACE and self.game_over:
                        self.reset_game()
            
            if not self.game_over:
                # Handle hand input
                self.handle_hand_input()
                
                # Handle keyboard input (fallback)
                self.handle_keyboard_input()
                
                # Update snake
                if not self.snake.update():
                    self.game_over = True
                
                # Check if snake ate food
                if self.snake.get_head_position() == self.food.position:
                    self.snake.length += 1
                    self.score += 1
                    self.food.randomize_position()
            
            # Render
            self.render()
            self.clock.tick(FPS)
        
        self.cleanup()
    
    def render(self):
        """Render game elements"""
        self.screen.fill(BLACK)
        
        if not self.game_over:
            self.snake.render(self.screen)
            self.food.render(self.screen)
            
            # Draw score
            score_text = self.font.render(f"Score: {self.score}", True, WHITE)
            self.screen.blit(score_text, (10, 10))
            
            # Draw instructions
            inst_text = self.small_font.render(
                "Move hand to control | ESC to quit",
                True, WHITE
            )
            self.screen.blit(inst_text, (10, SCREEN_HEIGHT - 30))
        else:
            # Game over screen
            game_over_text = self.font.render("GAME OVER", True, RED)
            score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
            restart_text = self.small_font.render(
                "Press SPACE to restart or ESC to quit",
                True, WHITE
            )
            
            self.screen.blit(
                game_over_text,
                (SCREEN_WIDTH // 2 - game_over_text.get_width() // 2, SCREEN_HEIGHT // 2 - 50)
            )
            self.screen.blit(
                score_text,
                (SCREEN_WIDTH // 2 - score_text.get_width() // 2, SCREEN_HEIGHT // 2)
            )
            self.screen.blit(
                restart_text,
                (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, SCREEN_HEIGHT // 2 + 50)
            )
        
        pygame.display.flip()
    
    def reset_game(self):
        """Reset game state"""
        self.snake.reset()
        self.food.randomize_position()
        self.score = 0
        self.game_over = False
        self.previous_hand_pos = None
    
    def cleanup(self):
        """Clean up resources"""
        self.cap.release()
        cv2.destroyAllWindows()
        pygame.quit()
        sys.exit()


def main():
    """Main entry point"""
    print("Starting Hand-Controlled Snake Game...")
    print("Move your hand in front of the camera to control the snake!")
    print("Arrow keys also work as fallback controls.")
    
    game = Game()
    game.run()


if __name__ == "__main__":
    main()
