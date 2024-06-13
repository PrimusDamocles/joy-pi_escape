import time
from JoyPiAdvanced import LEDMatrix, adc
from numpy.random import randint

# Initialize LED Matrix
matrix = LEDMatrix()

# Initialize ADC
adc = adc()

# Maze (example representation, customize as needed)
maze_width = 8
maze_height = 8
maze = [
    [0, 0, 1, 1, 1, 1, 1, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 1, 1, 0, 1],
    [1, 0, 1, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 1, 1, 0, 1],
    [1, 1, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 1, 0, 0, 1],
    [1, 1, 1, 1, 1, 1, 1, 1]
]

# Mouse initial position
mouse_x = 1
mouse_y = 1

# Goal position
goal_x = 6
goal_y = 6

# Game loop
while True:
    # Update LED matrix display
    matrix.clean()
    
    # Draw maze walls and hide blue lights
    for y in range(maze_height):
        for x in range(maze_width):
            if maze[y][x] == 1:
                matrix.setPixel(y * maze_width + x, (0, 0, 0))  # Hide blue lights (set to black)
    
    # Draw mouse
    matrix.setPixel(mouse_y * maze_width + mouse_x, (255, 0, 0))  # Red for mouse
    
    # Draw goal
    matrix.setPixel(goal_y * maze_width + goal_x, (0, 255, 0))  # Green for goal
    
    # Show updated matrix
    matrix.show()
    
    # Check win condition
    if mouse_x == goal_x and mouse_y == goal_y:
        # Display win message on LED matrix
        matrix.clean()
        matrix.show()
        time.sleep(5)  # Display for 5 seconds before exiting
        break
    
    # Example joystick control (adapt to your input method)
    # Read joystick input or use ADC values to control mouse movement
    # Example movement logic (adjust as needed)
    value_x, value_y = adc.read_value(0), adc.read_value(1)
    
    if value_x < 1800:
        # Move left
        if maze[mouse_y][mouse_x - 1] != 1:
            mouse_x -= 1
    elif value_x > 2350:
        # Move right
        if maze[mouse_y][mouse_x + 1] != 1:
            mouse_x += 1
    elif value_y > 2350:
        # Move up
        if maze[mouse_y - 1][mouse_x] != 1:
            mouse_y -= 1
    elif value_y < 1800:
        # Move down
        if maze[mouse_y + 1][mouse_x] != 1:
            mouse_y += 1
    
    # Optional: Add delays to control game speed
    time.sleep(0.2)

# Game over or victory handling
# Display victory animation or end game logic here
