
# Snake 
## Introduction
This is a simple implementation of the classic Snake game using the Pygame library. The game involves controlling a snake to eat randomly placed food, grow longer, and avoid collisions with the game boundaries and itself.
## Installation
Ensure you have Python and Pygame installed on your system. You can install Pygame using the following command:

```
pip install pygame
```

## Usage
1. Run the script using Python:

```
python3 snake.py
```

2. Use the arrow keys (UP, DOWN, LEFT, RIGHT) to control the snake's direction.

3. The snake will grow in length each time it eats the food.

4. The game ends if the snake collides with the game boundaries or itself.
## Code Structure
### Constants
- WINDOW: The size of the game window.
- TILE_SIZE: The size of each tile in the game grid.
### Variables
- screen: Pygame display surface.
- clock: Pygame clock for controlling the game's frame rate.
- snake_head: Rectangular object representing the snake's head.
- snake_body: List containing rectangular objects representing the snake's body segments.
- snake_dir: Tuple representing the snake's current movement direction.
- dirs: Dictionary to track valid movement directions.
- food: Rectangular object representing the food's position.
### Functions
- get_random_position(): Returns a random position within the game grid for the snake head and food.
## Main Game Loop
The script enters an infinite loop where it continuously updates the game state, checks for user input, and redraws the screen.

1. User Input Handling:
    - Detects key presses to change the snake's direction.

2. Update Game State:

    - Moves the snake according to its current direction.

    - Handles collisions with food, updating the snake's length and spawning new food.

    - Checks for collisions with the game boundaries or itself, resetting the game if necessary.

3. Draw Game Elements:

    - Clears the screen and redraws the food and snake.

4. Display Update:

    - Updates the display and controls the frame rate using Pygame's clock.



