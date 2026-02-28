from robloxAPI import GroupData as GD
import time
import config

# Variables
newMembers = 0
members = GD.getGroupMembers(config.SEA_GROUP_ID) 
memberJoins = GD.getDailyMemberJoins(config.SEA_GROUP_ID, config.DAYS_OF_DATA) # This command may take a bit of time to return
milestoneAmount = config.MILESTONE_AMOUNT # Amount required for every election
target = 0

print("INFO (MAIN) - Processing data... \n")

# Algorithm
while target <= members:
    target = target + config.MILESTONE_AMOUNT

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

