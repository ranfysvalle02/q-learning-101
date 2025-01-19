# qloq

---
*Breaking free from life’s “river of thinking” by exploring new paths.*

# Learning to Navigate: A Q-Learning Adventure

When you think of “learning” in our everyday world, you might picture a child learning to ride a bike. They hop on, wobble around, possibly crash (a.k.a. **negative reward**), then get back up and try again. After enough **episodes** (attempts), they finally figure out how to balance and move forward smoothly. This process is not so different from the way **Q-learning** works in **Reinforcement Learning (RL)**. 

In Q-learning, the child riding the bike is your **agent**. The bike, helmet, maybe even the training wheels are the **tools** the agent has. The neighborhood—or the bike park they practice in—is the **environment**. Each time the child gets on the bike is like starting a new **episode**. Over time, the child develops a “mental map” of what actions lead to success and which lead to face-planting in the bushes. That mental map is analogous to our **Q-table**.

---

## Introduction: Caught in the Same Old Routine?

Have you ever felt stuck in a routine—like you’re floating along in the same “river of thinking,” doing the same things over and over just because they *work*? It’s comfortable to do what you already know—go to the same coffee shop, cook the same meals, watch the same shows. But imagine if you never tried a new restaurant, never tested a different route to work, never explored a new hobby. You’d miss out on so many possibilities!

This is where **epsilon** (in Q-learning) comes in. Think of it as the little voice nudging you to step out of your comfort zone every once in a while. You might discover a fantastic café on the next block—or you might find out it’s closed. Either way, you learn something new.

**Reinforcement Learning (RL)**, and specifically **Q-learning**, mimics this balancing act between “sticking to what we know” (exploitation) and “trying out fresh ideas” (exploration). In the story below, we’ll see how ducklings, children on bikes, and a simple coding agent in a maze all share this pattern of learning: exploring the world, dealing with rewards or penalties, and gradually building a mental map of what works.

---

## The Agent (Our Curious Duckling)

In Q-learning, the **agent** is the decision-maker or learner.  

- **Duckling Version**: A freshly hatched duckling that follows its mother, learns to avoid predators, and searches for food.  
- **Child-on-a-Bike Version**: A child who’s wobbling around, sometimes falling, sometimes zooming happily forward.  
- **In Our Code**: A small program figuring out how to move **up**, **down**, **left**, or **right** in a grid in order to achieve a goal.

All these “agents” have one key thing in common: they learn through trial and error, storing knowledge in a **Q-table** (or “mental map”) that tells them which actions are good and which to avoid.

---

## The Tools (Resources, Knowledge & Parameters)

Just like we have instincts and advice from friends or family, an RL agent has **hyperparameters** that shape how it learns:

1. **Alpha (\(\alpha\)) – Learning Rate**  
   Think of it as how fast you absorb new information. Too high, and you overreact to every outcome; too low, and you might ignore valuable lessons.

2. **Gamma (\(\gamma\)) – Discount Factor**  
   This decides whether you’re focused on the short term or the long haul. A high \(\gamma\) values future rewards (like the duckling learning to find a big pond later), while a low \(\gamma\) chases tiny, quick wins.

3. **Epsilon (\(\epsilon\)) – Exploration Rate**  
   This is your willingness to break out of your “river of thinking” and try something new. Maybe you try a different coffee shop or a new route home. Sure, it might not always work out—but sometimes, it leads to something amazing.

---

## The Environment (The World Around You)

The **environment** is everything that’s not the agent—basically the setting where you learn:

- **In the Duckling’s World**: A pond filled with lily pads, reeds, and the occasional predator.  
- **For the Child on a Bike**: Sidewalks, roads, or a bike park with smooth paths (positive experiences) and potholes (negative rewards).  
- **In Our Q-Learning Code**: A simple grid with walls (`0`), open paths (`1`), and a goal (`9`).

Just as a duckling learns which parts of the pond are safe, our agent learns which parts of the grid to avoid.

---

## Q-Learning (How It All Comes Together)

**Q-Learning** is an iterative process:

1. **Observe**: The agent sees what’s around (like a duckling spotting food or danger).  
2. **Decide**: Based on its Q-table and \(\epsilon\)-greedy strategy, it chooses to either exploit what it knows or explore something new.  
3. **Experience**: It gets a **reward** (or penalty) for what just happened.  
4. **Update**: The agent revises its Q-table—akin to the duckling updating its “mental map”: “this area is safe,” or “that direction leads to trouble.”  
5. **Repeat**: Over many tries (episodes), the agent’s decisions get better and more informed.

Ultimately, the agent learns to identify what’s **similar** in different scenarios (e.g., all these open paths with no walls around might be good) and what’s **dissimilar** (e.g., that corner with a predator or a dead-end is definitely not the same).

---

## Episodes (A Series of Repetitions)

An **episode** is one full run—start at some position, act until you reach the goal or get stuck, then reset.

- **Duckling**: Each day, waking up, searching for food, encountering obstacles, returning to safety. Next day, same process but a little wiser.  
- **Child on a Bike**: Each attempt at riding is an episode—some successes, some wipeouts, but lessons get learned each time.  
- **Maze Agent**: We place our agent at `(1,1)`, let it navigate until it finds `9` or gets trapped. Then we reset and try again.

This repetition refines the knowledge stored in the Q-table (or the duckling’s instincts, or the biker’s balance).

---

## An Ultra-Simple Q-Learning Maze Example

In a minimal coding setup:

1. We define a **maze** (the environment).  
2. We initialize a **Q-table** (the agent’s memory).  
3. We set our **hyperparameters** (\(\alpha, \gamma, \epsilon\)).  
4. Through **episodes**, the agent explores, collects rewards, and updates its Q-table.  
5. After many trials, it reliably finds the goal.

Just as the duckling grows from clumsy waddles to smooth swimming, the Q-learning agent evolves from random moves to a purposeful strategy.

---

### The Code Walkthrough

If you’ve ever watched a duckling swim across a pond, you know how quick they are to learn what works and what doesn’t. One day, they might discover where the tasty treats lie, the next they’re charting new courses to get there faster. In **Reinforcement Learning (RL)**, we strive to replicate this kind of trial-and-error learning in a computational way.

Below is a high-level view of the main components in `demo.py`:

1. **Environment Setup**  
   - A NumPy array `POND` specifies the layout (rocks, water, and treat).
   - A starting position `START_POS` is defined.

2. **Possible Actions**  
   - We encode the actions as numeric keys (0=up, 1=right, 2=down, 3=left).
   - We map each action to row/column changes like `(-1, 0)` for up or `(0, 1)` for right.

3. **Helper Functions**  
   - `is_valid_position(pos)`: Checks if the new position is within the grid and not a rock.  
   - `get_next_position(current_pos, action)`: Calculates the duckling’s next position. If invalid, it stays put.  
   - `get_reward(pos)`: Returns +10 if the duckling reaches the treat, otherwise -0.1.  
   - `is_goal(pos)`: Checks if the duckling is on the cell with the tasty treat.

4. **Q-Table Initialization**  
   - We maintain a dictionary `Q_table` keyed by `(row, col)`, where each value is a list of Q-values for each action.  
   - If a state doesn’t exist in `Q_table` yet, we initialize it with `[0.0, 0.0, 0.0, 0.0]`.

5. **Training Loop**  
   - We run the Q-learning for `NUM_EPISODES` episodes, each with a maximum number of steps.  
   - For each step:
     1. **Epsilon-Greedy Action Selection**:  
        - With probability `EPSILON`, choose a random action.  
        - Otherwise, choose the action with the highest Q-value.
     2. **State Transition**:  
        - Calculate `next_pos` and determine `reward`.
     3. **Q-value Update**:  
        - Update the Q-values using the Q-learning rule.
     4. **Check Goal**:  
        - If the duckling reaches the treat, end the episode.

6. **Epsilon Decay (Optional)**  
   - After each episode, `EPSILON` is slightly reduced so that the duckling explores less over time.

7. **Demonstration**  
   - Finally, the script shows a “greedy” run, where the duckling always picks the best-known action from the learned Q-table.  
   - It prints the path taken in this demonstration.

### The Pond Environment

The environment is a 2D grid where each cell represents one part of the pond:

```
  Row\Col   0    1    2    3    4
      0    [0,   1,   1,   1,   1]
      1    [1,   1,   0,   1,   9]
      2    [1,   0,   1,   1,   1]
      3    [1,   1,   1,   1,   1]
```

In this grid:
- `0` represents a **rock** (impassable; the duckling cannot swim there).
- `1` represents **water** (the duckling can swim freely).
- `9` represents the **tasty treat** (the goal).

Our duckling starts at position `(0,1)`—it’s in water, so it’s safe. The duckling can move **up, right, down**, or **left**, and we use an **epsilon-greedy** strategy to decide whether to explore or exploit.

---

### Observing the Duckling’s Learning
During training, you’ll see console output indicating whether the duckling is *exploring* or *exploiting*, which action it takes, and eventually celebrating when it finds the treat. Over multiple episodes, the duckling refines its internal Q-values, leading to a more direct route to the treat.

---

### Why This Matters
This little example—though simplistic—beautifully illustrates how **trial-and-error** plus **incremental updates** help an agent learn an optimal or near-optimal strategy. Many real-world problems, from robot navigation to game-playing AI, can be tackled with the same underlying Q-learning concepts.

---

## Final Thoughts: Break Free From Your River of Thinking

If you ever feel stuck in life, doing everything the same way simply because it’s comfortable, remember **epsilon**—that little spark of curiosity prompting you to see what else is out there. Learning happens when we challenge our biases and update our internal “map” of the world.

1. **Imprinting & Bias**: We tend to latch onto the first lesson or experience we have. Be mindful of that initial “imprint,” because it can skew how you see future opportunities.  
2. **Similar vs. Dissimilar**: By exploring, you discover which situations really do mirror past ones—and which are unique enough to justify a new approach.  
3. **Exploration vs. Exploitation**: Balancing the comfort of what you know with the thrill of the unknown is how you grow—whether you’re a duckling, a coder, or a café-hopper.  
4. **Rewards**: Be clear about what “success” looks like. In coding, it’s reaching a goal in a maze. In life, maybe it’s finding happiness, health, or a sense of adventure.

So go ahead, **dip your webbed feet into new waters**—step out of your routine, explore, learn from it, and watch your internal Q-table become richer and wiser. After all, life’s greatest discoveries often happen when you steer away from your usual path, letting a bit of “epsilon” guide you toward something new.

---

# FULL CODE

```python
#!/usr/bin/env python3
"""
demo.py

A fun Q-learning demo featuring our curious "duckling" navigating a simple pond
environment. The duckling learns through trial and error, balancing exploration
and exploitation to find a 'tasty treat' in the grid.

"""

import numpy as np
import random

# -----------------------------------------------------------------------------
# POND DEFINITION
# -----------------------------------------------------------------------------
# We'll represent the pond as a 2D grid:
#   0 = Rock (impassable; can't swim through)
#   1 = Water (free to swim)
#   9 = Tasty treat (goal)
#
# The duckling starts at (0,1) and tries to reach the cell with '9'.
#
#   Row\Col  0   1   2   3   4
#       0   [0,  1,  1,  1,  1]
#       1   [1,  1,  0,  1,  9]
#       2   [1,  0,  1,  1,  1]
#       3   [1,  1,  1,  1,  1]
#
# The duckling can't move into '0' cells. The '9' cell is the special goal.
# -----------------------------------------------------------------------------

POND = np.array([
    [0, 1, 1, 1, 1],
    [1, 1, 0, 1, 9],
    [1, 0, 1, 1, 1],
    [1, 1, 1, 1, 1]
])

# Starting position for our duckling (row, col).
START_POS = (0, 1)  # This is water, so the duckling can start here safely.

# Define possible actions: up, right, down, left.
# We'll map each action to a delta (row_change, col_change).
ACTIONS = {
    0: (-1, 0),  # Up
    1: (0, +1),  # Right
    2: (+1, 0),  # Down
    3: (0, -1)   # Left
}

# -----------------------------------------------------------------------------
# HYPERPARAMETERS (Learn Rate, Discount Factor, Exploration Rate)
# -----------------------------------------------------------------------------
ALPHA = 0.1       # Learning rate (0 < ALPHA <= 1)
GAMMA = 0.9       # Discount factor (0 <= GAMMA <= 1)
EPSILON = 0.3     # Initial exploration rate (0 <= EPSILON <= 1)

NUM_EPISODES = 50           # How many times the duckling tries (episodes)
MAX_STEPS_PER_EPISODE = 50  # Max steps per episode to prevent endless loops

# -----------------------------------------------------------------------------
# UTILITY FUNCTIONS
# -----------------------------------------------------------------------------
def is_valid_position(pos):
    """
    Check if a position in the pond is valid for swimming (not out of bounds
    and not a rock).
    """
    r, c = pos
    # Check if (r, c) is inside the pond array.
    if (0 <= r < POND.shape[0]) and (0 <= c < POND.shape[1]):
        # Ensure it's not a rock (0).
        return POND[r, c] != 0
    return False

def get_next_position(current_pos, action):
    """
    Given the current position (row, col) and an action (0,1,2,3),
    compute the next position. If it's invalid or blocked, stay put.
    """
    dr, dc = ACTIONS[action]
    new_pos = (current_pos[0] + dr, current_pos[1] + dc)
    
    # If the new position is invalid, we don't move.
    if not is_valid_position(new_pos):
        return current_pos
    return new_pos

def get_reward(pos):
    """
    Define the reward for swimming into a particular position.
    - If position has '9' (tasty treat), +10
    - Otherwise, small negative reward (-0.1) to encourage efficient paths
    """
    r, c = pos
    if POND[r, c] == 9:
        return 10.0
    else:
        return -0.1

def is_goal(pos):
    """
    Check if the current position is the 'tasty treat' goal.
    """
    r, c = pos
    return POND[r, c] == 9

# -----------------------------------------------------------------------------
# MAIN Q-LEARNING LOGIC
# -----------------------------------------------------------------------------
def main():
    # We'll store the duckling's Q-values in a dictionary:
    #   Q_table[(row, col)] = [Q_up, Q_right, Q_down, Q_left]
    # If a position hasn't been encountered yet, it will be initialized later.
    Q_table = {}

    def get_Q_values(state):
        """
        Retrieve Q-values for all actions from 'Q_table'. If the state (row,col)
        isn't in the table, initialize it with 0.0 for each possible action.
        """
        if state not in Q_table:
            Q_table[state] = [0.0, 0.0, 0.0, 0.0]  # Up, Right, Down, Left
        return Q_table[state]

    global EPSILON  # We'll modify EPSILON over time (optional decay).

    # -------------------------------
    # TRAINING LOOP
    # -------------------------------
    for episode in range(NUM_EPISODES):
        # Start each episode at the initial position (our duckling's start).
        current_pos = START_POS

        print(f"\n=== EPISODE {episode+1}/{NUM_EPISODES} ===")
        print("Duckling wakes up, stretches its wings, and prepares to explore...")

        for step in range(MAX_STEPS_PER_EPISODE):
            # 1. Observe the current state (position).
            state = current_pos

            # 2. Choose an action using epsilon-greedy strategy.
            if random.random() < EPSILON:
                # Explore (pick a random action).
                action = random.choice(list(ACTIONS.keys()))
                print(f"[Exploring] Duckling tries action {action}")
            else:
                # Exploit (pick best known action from Q-table).
                q_values = get_Q_values(state)
                action = int(np.argmax(q_values))
                print(f"[Exploiting] Duckling chooses action {action} with Q-values {q_values}")

            # 3. Perform the action to get the next position.
            next_pos = get_next_position(current_pos, action)

            # 4. Get a reward for moving into 'next_pos'.
            reward = get_reward(next_pos)

            # 5. Update Q-values (Q-learning update).
            old_q_values = get_Q_values(state)      # Q-values for the current state
            old_q = old_q_values[action]            # Q-value for the chosen action
            next_q_values = get_Q_values(next_pos)  # Q-values for the next state
            max_next_q = max(next_q_values)         # Best future Q-value

            # Q-learning formula:
            # Q_new = Q_old + ALPHA * (reward + GAMMA * max_next_q - Q_old)
            new_q = old_q + ALPHA * (reward + GAMMA * max_next_q - old_q)
            old_q_values[action] = new_q  # Update the Q-table

            # 6. Move the duckling to the next position.
            current_pos = next_pos

            # Check if we've reached the goal (the tasty treat).
            if is_goal(current_pos):
                print(">>> Hooray! The duckling found the TASTY TREAT!")
                break  # End this episode early if goal is reached.

        # (Optional) Decay epsilon so that the duckling explores less over time.
        EPSILON_decay = 0.99
        EPSILON *= EPSILON_decay

    # -------------------------------
    # DEMONSTRATION
    # -------------------------------
    print("\n=== DEMONSTRATION: Duckling uses its learned Q-table to find the treat! ===")

    # We'll do one final run in "greedy" mode (no random exploration).
    demo_pos = START_POS
    path_taken = [demo_pos]
    steps = 0

    while not is_goal(demo_pos) and steps < MAX_STEPS_PER_EPISODE:
        q_vals = get_Q_values(demo_pos)
        best_action = int(np.argmax(q_vals))  # Choose the best action from Q-table
        demo_pos = get_next_position(demo_pos, best_action)
        path_taken.append(demo_pos)
        steps += 1

    # Print out the final path our duckling takes.
    if is_goal(demo_pos):
        print("Quack! The duckling successfully reached the TASTY TREAT.")
        print("Path taken (row, col):")
        for p in path_taken:
            print(p)
    else:
        print("The duckling couldn't reach the goal in the demonstration.")
        print("Path taken (row, col):")
        for p in path_taken:
            print(p)

# -----------------------------------------------------------------------------
# Run the script
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    main()

```
