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
mouse_x = 0
mouse_y = 0

# Goal position
goal_x = 6
goal_y = 6

# Direction variables
direc_x = 0
direc_y = 0

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
        matrix.text("You Win!", (255, 255, 255))  # Display "You Win!" message in white
        matrix.show()
        
        # Turn matrix green
        for i in range(maze_width * maze_height):
            matrix.setPixel(i, (0, 255, 0))  # Green
        
        matrix.show()
        
        time.sleep(5)  # Display for 5 seconds before exiting
        
        # Reset game
        mouse_x = 0
        mouse_y = 0
        direc_x = 0
        direc_y = 0
        
        continue
    
    # Example joystick control (adapt to your input method)
    # Read joystick input or use ADC values to control mouse movement
    # Example movement logic (adjust as needed)
    value_x, value_y = adc.read_value(0), adc.read_value(1)
    
    # Print debug statements for troubleshooting
    print(f"Joystick/ADC values: X={value_x}, Y={value_y}")
    
    # Adjust joystick/ADC thresholds and direction control
    if value_x < 1800:
        direc_x = -1
        direc_y = 0
    elif value_x > 2350:
        direc_x = 1
        direc_y = 0
    elif value_y > 2350:
        direc_x = 0
        direc_y = -1
    elif value_y < 1800:
        direc_x = 0
        direc_y = 1
    
    # Check if next move hits a wall or stays within maze boundaries
    if (0 <= mouse_x + direc_x < maze_width) and (0 <= mouse_y + direc_y < maze_height):
        if maze[mouse_y + direc_y][mouse_x + direc_x] == 0:
            # Update mouse position
            mouse_x += direc_x
            mouse_y += direc_y
    else:
        # Print debug statement for boundary check or invalid move
        print("Boundary reached or invalid move")
    
    # Optional: Add delays to control game speed
    time.sleep(0.2)

# Game over or victory handling
# Display victory animation or end game logic here
