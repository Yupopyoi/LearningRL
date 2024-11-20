import numpy as np
from maze import Maze
import random

class QLearning:
    def __init__(self, maze):
        self.maze = maze
        self.q_table = np.zeros((maze.mase_size(), maze.mase_size(), 4))
        self.actions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # Right, Down, Left, Up

    def choose_action(self, state, epsilon : float):
        """Choose Action based on ε-greedy"""
        if random.uniform(0, 1) < epsilon:
            return random.randint(0, 3) 
        else:
            return np.argmax(self.q_table[state[0], state[1]])

    def update_qvalue(self, state, action, reward, next_state, alpha, gamma):
        """
        state      : Current state (Position)
        action     : Selected Action (Right, Down, Left, Up)
        reward     : Rewards obtained from this action
        next_state : Next state (Position)
        """
        # Get max Q value at next state (position) 
        max_next_q = np.max(self.q_table[next_state[0], next_state[1]])
        
        # Get Q value of the action to be taken this time
        current_q = self.q_table[state[0], state[1], action]
        
        # Set Q value
        self.q_table[state[0], state[1], action] = current_q + alpha * (reward + gamma * max_next_q - current_q)

    def train(self, episodes : int, alpha : float = 0.1, gamma : float = 0.9, epsilon : float = 0.1):
        for episode in range(episodes):
            state = self.maze.get_start_position()
            total_reward = 0

            while not self.maze.is_goal(state):
                # Choose Action based on ε-greedy
                action = self.choose_action(state, epsilon)
                
                # Temporarily determine the next position
                next_state = (state[0] + self.actions[action][0], state[1] + self.actions[action][1])

                # Check if the position is mobile
                if self.maze.is_valid_move(next_state):
                    if self.maze.is_goal(next_state):
                        reward = 10 
                    else:
                        reward = -1
                else:
                    next_state = state  # Status unchanged if movement is invaild
                    reward = -10

                # Update Q Value
                self.update_qvalue(state, action, reward, next_state, alpha, gamma)
                
                # Update state and reward
                state = next_state
                total_reward += reward

            print(f"Episode {episode + 1}: Total Reward = {total_reward}")
            
    def print_policy(self):
        """Output the direction of the maximum Q value in each state"""
        directions = ["→", "↓", "←", "↑"]  # Right, Down, Left, Up
        policy_grid = []

        print("------------------------------")

        for i in range(len(self.q_table)):
            row = []
            for j in range(len(self.q_table[0])):
                if self.maze.grid[i][j] == 1:  # wall
                    row.append("■")
                elif self.maze.grid[i][j] == 2:  # goal
                    row.append("G")
                else:
                    max_action = np.argmax(self.q_table[i, j])
                    row.append(directions[max_action])
            policy_grid.append(row)

        for row in policy_grid:
            print(" ".join(row))
        
        print("------------------------------")

    def solve(self):
        """Solve maze after learning"""
        
        self.print_policy()
        
        state = self.maze.get_start_position()
        path = [state]

        while not self.maze.is_goal(state):
            
            action = np.argmax(self.q_table[state[0], state[1]])
            next_state = (state[0] + self.actions[action][0], state[1] + self.actions[action][1])

            if not self.maze.is_valid_move(next_state):
                break
            
            path.append(next_state)
            state = next_state

        return path


if __name__ == "__main__":
    maze = Maze()
    q_learning = QLearning(maze)

    print("Training...")
    q_learning.train(episodes=1000)

    print("\nSolving...")
    path = q_learning.solve()
    print("Path to goal:", path)
    