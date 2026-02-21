from robloxAPI import GroupData as GD
import time

# Variables
newMembers = 0
SEAGroupID = 2648601 # 2648601 is SEA's group ID
members = GD.getGroupMembers(SEAGroupID) 
memberJoins = GD.getDailyMemberJoins(SEAGroupID, 90) # This command may take a bit of time to return
milestoneAmount = 250000 # Amount required for every election
target = 0

print("INFO (MAIN) - Processing data... \n")

# Algorithm
while target <= members:
    target = target + milestoneAmount

membersRequired = target - members

days = len(memberJoins)

for i in range(days):
    Day = memberJoins[i]

    newMembers = newMembers + int(Day[0]) 

avgDailyJoins = round((newMembers / days))

daysToGo = round(membersRequired / avgDailyJoins)

# Date formatting
currentTime = time.time()
targetTime = currentTime + (daysToGo * 24 * 60 * 60) 
targetDate = time.strftime("%d-%m-%Y", time.localtime(targetTime))

#Results
print("INFO (MAIN) - Days to go: " + str(daysToGo))
print("INFO (MAIN) - Estimated date for Marshal Election(MM/DD/YYYY): " + targetDate + "\n")


if __name__ == "__main__":
    print("WARNING (SMED) - This program is still in development, expect bugs and errors. \n")

