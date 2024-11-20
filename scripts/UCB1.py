import math
import random
import sys

SLOT_NUMBER : int = 7
TRIAL_NUMBER : int = 100000

def select_slot(ucb1 : float) -> int:
    return ucb1.index(max(ucb1))

def gamble(success_rate : float) -> int: 
    if random.random() < success_rate / 100.0 :
        return 1
    else:
        return 0
    
def calculate_ucb1(trial : int, success : int , all_trial : int) -> float:
    if(trial == 0):
        return sys.float_info.max

    success_rate : float = success / trial
    bias : float = math.sqrt(2.0 * math.log(all_trial) / trial)

    return success_rate + bias

def start_ucb1():
    success_rate_only_god_knows = [random.randint(0, 75) for _ in range(SLOT_NUMBER)]

    ucb1 = [0.0 for _ in range(SLOT_NUMBER)]
    trial_count = [0 for _ in range(SLOT_NUMBER)]
    successful_count = [0 for _ in range(SLOT_NUMBER)]
    
    total_reward : int = 0

    for trial in range(TRIAL_NUMBER):
        
        # Calculate UCB1 of each slot
        for slot_index in range(SLOT_NUMBER):
            ucb1[slot_index] = calculate_ucb1(trial_count[slot_index], successful_count[slot_index], sum(trial_count))
        
        # Select slot and Gamble with selected slot
        selected_slot_index : int = select_slot(ucb1)
        reward : int = gamble(success_rate_only_god_knows[selected_slot_index])
        total_reward += reward
        
        # Count Result
        trial_count[selected_slot_index] += 1
        successful_count[selected_slot_index] += reward
            
        print(f"Trial : {str(trial)}  | Selected :  {str(selected_slot_index)} | IsSuccess :  {str(reward)} | TotalReward :  {str(total_reward)}  | UCB1 : {", ".join(map(str, ucb1))}") 
        
    print()
    print("------------------------ Summary ------------------------")
    print(f"Success Rate Truly : {", ".join(map(str, success_rate_only_god_knows))}")  
    print(f"Trial Count        : {", ".join(map(str, trial_count))}")  
    print(f"Success Count      : {", ".join(map(str, successful_count))}") 
    print(f"Total Reward       : {str(total_reward)}")
    print(f"Regret             : {str(int(TRIAL_NUMBER * max(success_rate_only_god_knows) / 100 - total_reward))}")
    print("---------------------------------------------------------")
    print()
        
if __name__ == '__main__':
    start_ucb1()
