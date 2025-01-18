import numpy as np
import random

# ---------------
# MAZE DEFINITION
# ---------------
#   0 => Wall
#   1 => Open path
#   9 => Goal

maze = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 0],
    [0, 1, 9, 1, 0],
    [0, 1, 1, 1, 0],
    [0, 0, 0, 0, 0]
]

# The agent will start here (row=1, col=1)
start_position = (1, 1)

# Define the actions our agent can take
actions = ["up", "down", "left", "right"]

# ------------------
# Q-LEARNING SETTINGS
# ------------------
alpha = 0.1    # Learning rate
gamma = 0.9    # Discount factor
epsilon = 0.1  # Exploration rate
episodes = 500 # Number of training episodes

# -------------
# Q-TABLE SETUP
# -------------
# We'll make a Q-table that's shaped like: [maze_height, maze_width, number_of_actions]
maze_height = len(maze)
maze_width = len(maze[0])
q_table = np.zeros((maze_height, maze_width, len(actions)))

# ------------------------
# HELPER FUNCTIONS / LOGIC
# ------------------------

def is_valid_position(x, y):
    """
    Checks if (x, y) is inside the maze and not a wall.
    """
    if x < 0 or x >= maze_height or y < 0 or y >= maze_width:
        return False  # Outside maze boundary
    if maze[x][y] == 0:
        return False  # It's a wall
    return True

def get_next_position(position, action):
    """
    Given a position (x, y) and an action (up, down, left, right),
    return the new position (x', y').
    """
    (x, y) = position
    if action == "up":
        x -= 1
    elif action == "down":
        x += 1
    elif action == "left":
        y -= 1
    elif action == "right":
        y += 1
    return (x, y)

def get_reward(new_position):
    """
    Returns the reward for moving to 'new_position'.
    - If goal (9), reward = +10
    - Otherwise just a small negative step cost: -0.1
    """
    x, y = new_position
    if maze[x][y] == 9:
        return 10.0
    else:
        return -0.1

def choose_action(position, epsilon):
    """
    Epsilon-greedy action choice:
    - With probability epsilon, pick a random action (exploration).
    - Otherwise, pick the action with the best Q-value (exploitation).
    """
    x, y = position
    if random.random() < epsilon:
        # Explore: pick a random action
        return random.choice(actions)
    else:
        # Exploit: pick the best action from Q-table
        action_index = np.argmax(q_table[x, y])
        return actions[action_index]

# --------------------
# Q-LEARNING TRAIN LOOP
# --------------------

def train_q_learning(episodes):
    """
    Run multiple episodes of Q-learning to train the Q-table.
    """
    for ep in range(episodes):
        # Reset to the start position every episode
        position = start_position

        done = False
        while not done:
            # 1. Choose an action
            action = choose_action(position, epsilon)

            # 2. Figure out next position
            next_pos = get_next_position(position, action)

            # 3. Check if it's valid or not
            if not is_valid_position(next_pos[0], next_pos[1]):
                # If not valid (wall or out of bounds), give a negative reward
                reward = -1.0
                # Don't move the agent
                next_pos = position
            else:
                # Valid move
                reward = get_reward(next_pos)

            # 4. Check if goal reached => done
            if maze[next_pos[0]][next_pos[1]] == 9:
                done = True

            # 5. Update Q-value with Q-learning formula
            (x, y) = position
            action_idx = actions.index(action)
            old_q = q_table[x, y, action_idx]
            next_max_q = np.max(q_table[next_pos[0], next_pos[1]])

            new_q = (1 - alpha) * old_q + alpha * (reward + gamma * next_max_q)
            q_table[x, y, action_idx] = new_q

            # 6. Move to next position
            position = next_pos

# -------------------------
# GET THE BEST PATH (GREEDY)
# -------------------------

def get_best_path():
    """
    Uses the learned Q-table to move greedily from the start to the goal.
    To avoid infinite loops, we limit the path length to 100 steps.
    """
    path = []
    position = start_position
    path.append(position)

    for step in range(100):
        # If we're at the goal, stop
        if maze[position[0]][position[1]] == 9:
            break

        # Pick the best action from Q-table
        (x, y) = position
        action_idx = np.argmax(q_table[x, y])
        best_action = actions[action_idx]

        # Compute next position
        next_pos = get_next_position(position, best_action)

        # If next position is invalid or doesn't move us anywhere, just stop
        # (to prevent infinite loops if Q-table is badly learned)
        if not is_valid_position(next_pos[0], next_pos[1]) or next_pos == position:
            break

        path.append(next_pos)
        position = next_pos

    return path

# ---------------
# MAIN EXECUTION
# ---------------
if __name__ == "__main__":
    print("Starting Q-learning training...")
    train_q_learning(episodes)
    print("Training completed.")

    print("\nFinding the best path from the start to the goal...")
    best_path = get_best_path()

    print("\nBest path (step by step):")
    for step in best_path:
        print(step)
