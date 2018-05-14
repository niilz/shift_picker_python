import numpy as np


class Worker(object):
#creates a Worker with Array of blocked Days, and a starting workload of zero
    workerNames = []
    def __init__(self, name, blockedDays, workload):
        self.name = name
        self.blockedDays = blockedDays
        self.workload = workload
        self.workerNames.append(self)
    
    def year(self):
    #creates an array of weeks (range 1, 53 = one year), and inserts zeros for blocked days
        year = []
        for week in range(1, 53):
            if week not in self.blockedDays:
                year.append(week)
            else:
                year.append(0)
        return year

    def addWorkload(self):
    #when called workload increases by one
        self.workload += 1

#The worker instances, with Name, blocked_Days and a Workload of zero to start with
neil = Worker('Neil', [1,13,15,33,44,50,52], 0)
maik = Worker('Maik', [3,7,13,17,25,38,41,51], 0)
sarah = Worker('sarah', [5,6,11,14,17,22,30,45,52],0)
chris = Worker('Chris', [2,10,28,33,39,47,52],0)
susan = Worker('Susan', [1,9,10,23,35,45,52],0)

def createBinYear(individualYear):
#place 1 for blocked weekend and 0 for an available one    
    binYear = [x+1 if x == 0 else x*0 for x in individualYear]
    return binYear


def sumYears(workerClass):
#calls createBinYear on worker's weekendArray of years and returns their sum
    years = [createBinYear(w.year()) for w in workerClass.workerNames]
    summedYear = np.sum(years, axis=0)
    return list(summedYear)
#print(sumYears(Worker))

def prio(summed):
#list of tuples (index, amount of blocked weekends) sorted by blocked weekends
    idxPrioTuples = list(enumerate(summed))
    return sorted(idxPrioTuples, key=lambda x: x[1], reverse=True)
#print(prio(sumYears(Worker)))


prioliste = prio(sumYears(Worker))
#interim result: list of tuples(WEEK, SUM_unavailable_workers), sorted by unavailability, hence high priority 
#print(prioliste)

def leastLoaded(workerClass):
#returns list with workers sorted by least amount of added shifts (workload) at this time
    workerInstances = workerClass.workerNames
    sortedByWorkload = sorted(workerInstances, key=lambda x: x.workload)
    return sortedByWorkload

def dealShifts(prioliste):
#asigns a worker to a week
    shifts = []
    def addWorker(worker):
    #when called simply add (WEEK, NAME) to shifts. week[0]=number of week, +1 because list is yet zero based
        worker = leastLoaded(Worker)[count]
        shifts.append((week[0]+1, worker.name))
        worker.addWorkload()
    for week in prioliste:
    #loop through every week
        workers = leastLoaded(Worker)
        count = 0
        while week[0]+1 in workers[count].blockedDays:
        #if current worker is blocked for that date, take next worker
            count +=1
        if len(shifts) != 0 and (week[0], workers[count].name) in shifts:
        #if that worker has worked the week before take next worker
            count +=1
        addWorker(count)
        #add that worker to the shifts_list
    return sorted(shifts)

finalist = dealShifts(prioliste)
#the final List of all shifts

for x in finalist:
#print week and corresponding name line by line
    print(x)

for n in Worker.workerNames:
#show wrongly assigned weekends
    for x in finalist:
        if x[0] in n.blockedDays and x[1] == n.name:
            print(str(x[0]) + " should not be assigned to " + n.name)

amountOfShifts = {}
for num, name in sorted(finalist):
#finally print how many shifts each worker got assigned to
    if name not in amountOfShifts:
        amountOfShifts[name] = 1
    else:
        amountOfShifts[name] += 1

print(amountOfShifts)






