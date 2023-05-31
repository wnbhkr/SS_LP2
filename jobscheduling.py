class job:
    def __init__(self,id,profit,deadline):
        self.id=id
        self.profit=profit
        self.deadline=deadline

def jobScheduling(arr,max_dead):
    n=len(arr)
    for i in range(n):
        for j in range(n-1-i):
            if arr[j].profit < arr[j+1].profit:
                arr[j],arr[j+1]=arr[j+1],arr[j]

    schedule=[False]*max_dead # schedule with size equal to max dead (all elements false)
    max_profit=0
    for i in range(len(arr)): #loop through each job
        for j in range(arr[i].deadline-1, -1, -1): #range(start, end, incremennt) - > deadline-1 to 0(-1 excluded)
            # loop from deadline - 1 to 0 for selected job (ith job)
            if schedule[j] is False: # check if the place is empty (in schedule)
                schedule[j]=arr[i].id # if empty put job (id) there
                max_profit += arr[i].profit
                break 
    print(schedule)
    print('Maxprofit ',max_profit)

arr = []
print('Enter space seperated job id, profit, deadline ')
while(True):
    ans=input().split()
    if(ans[0]=='-1'):
        break
    j=job(ans[0], int(ans[1]), int(ans[2]))
    arr.append(j)
max_dead = max([i.deadline for i in arr])
print(max_dead)
print('Following is max profit sequence of jobs')
jobScheduling(arr, max_dead)


# profit = [15,27,10,100, 150]
# jobs = ["j1", "j2", "j3", "j4", "j5"]
# deadline = [2,3,3,3,4] 
# profitNJobs = list(zip(profit,jobs,deadline))
# profitNJobs = sorted(profitNJobs, key = lambda x: x[0], reverse = True)
# slot = []
# for _ in range(len(jobs)):
#     slot.append(0)

# profit = 0
# ans = []

# for i in range(len(jobs)):
#     ans.append('null')

# for i in range(len(jobs)):
#         job = profitNJobs[i]
#         #check if slot is occupied
#         for j in range(job[2], 0, -1):
#             if slot[j] == 0:
#                 ans[j] = job[1]
#                 profit += job[0]
#                 slot[j] = 1
#                 break
        
# print("Jobs scheduled buddy:",ans[1:])
# print(profit)