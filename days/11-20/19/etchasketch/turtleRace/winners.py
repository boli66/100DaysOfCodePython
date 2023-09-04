import random
import turtleRaceModified as t
def selectionSort(nums: list[int], ddd):
    for i in range(len(nums)):
        for s in range(i,len(nums)):
            if(nums[s]<nums[i]):
                temp = nums[i]
                nums[i] = nums[s]
                nums[s] = temp

                temp = ddd[i]
                ddd[i] = ddd[s]
                ddd[s] = temp
    return [nums,ddd]
def reverse(l):
    newList = []
    for i in range(len(l)-1,-1,-1):
        newList.append(l[i])
    return newList



winners = {}

for i in t.colors:
    winners[i] = 0

for i in range(int(input("How many times should the game run: "))):
    winners[t.main()]+=1

ranks = []
names = []
for i in winners:
    ranks.append(winners[i])
    names.append(i)

out = selectionSort(ranks,names)
ranks = reverse(out[0])
names = reverse(out[1])
count = 1

for i in range(len(ranks)):
    print(f"{count}. {names[i]} won {ranks[i]} times.")
    count+=1
