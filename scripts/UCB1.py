import math
import random
import sys

SLOT_NUMBER : int = 7
TRIAL_NUMBER : int = 100000

def SelectSlot(ucb1 : float) -> int:
    return ucb1.index(max(ucb1))

def Gamble(successRate : float) -> int: 
    if random.random() < successRate / 100.0 :
        return 1
    else:
        return 0
    
def CalculateUCB1(trial : int, success : int , allTrial : int) -> float:
    if(trial == 0):
        return sys.float_info.max

    successRate : float = success / trial
    bias : float = math.sqrt(2.0 * math.log(allTrial) / trial)

    return successRate + bias

def StartUCB1():
    successRateOnlyGodKnows = [random.randint(0, 75) for _ in range(SLOT_NUMBER)]

    ucb1 = [0.0 for _ in range(SLOT_NUMBER)]
    trialCount = [0 for _ in range(SLOT_NUMBER)]
    successfulCount = [0 for _ in range(SLOT_NUMBER)]
    
    totalReward : int = 0

    for trial in range(TRIAL_NUMBER):
        
        # Calculate UCB1 of each slot
        for slotIndex in range(SLOT_NUMBER):
            ucb1[slotIndex] = CalculateUCB1(trialCount[slotIndex], successfulCount[slotIndex], sum(trialCount))
        
        # Select slot and Gamble with selected slot
        selectedSlotIndex : int = SelectSlot(ucb1)
        reward : int = Gamble(successRateOnlyGodKnows[selectedSlotIndex])
        totalReward += reward
        
        # Count Result
        trialCount[selectedSlotIndex] += 1
        successfulCount[selectedSlotIndex] += reward
            
        print("Trial : " + str(trial) + " | Selected : " + str(selectedSlotIndex) + " | IsSuccess : " + str(reward) + " | TotalReward : " + str(totalReward) + " | UCB1 : " + ", ".join(map(str, ucb1))) 
        
    print()
    print("------------------------ Summary ------------------------")
    print("Success Rate Truly : " + ", ".join(map(str, successRateOnlyGodKnows)))  
    print("Trial Count        : " + ", ".join(map(str, trialCount)))  
    print("Success Count      : " + ", ".join(map(str, successfulCount))) 
    print("Total Reward       : " + str(totalReward))
    print("Regret             : " + str(int(TRIAL_NUMBER * max(successRateOnlyGodKnows) / 100 - totalReward)))
    print("---------------------------------------------------------")
    print()
        
if __name__ == '__main__':
    StartUCB1()
