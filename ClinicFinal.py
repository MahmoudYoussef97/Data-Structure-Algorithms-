
import random

class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def enqueue(self, item):
        self.items.insert(0,item)

    def dequeue(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Doctor:
    def __init__(self,yRate, oRate):
        self.PatYoungRate = yRate
        self.PatOldRate = oRate
        self.currentPatient = None
        self.TimeRemaining = 0

    def tick(self):
        if self.currentPatient != None:
            self.TimeRemaining = self.TimeRemaining - 1
            if self.TimeRemaining <= 0:
                self.currentPatient = None

    def busy(self):
        return self.currentPatient != None

    def startNext(self, nextPat):
        self.currentPatient = nextPat

        if nextPat.getPatientsAge() in range(20,41):
            self.TimeRemaining = nextPat.getPatientsAge()/self.PatYoungRate
        if nextPat.getPatientsAge() in range(41,61):
            self.TimeRemaining = nextPat.getPatientsAge()/self.PatOldRate

class Patient:

    def __init__(self,time):
        self.timeStamp = time
        self.patientsAge = random.randrange(20,61)

    def getPatientsAge(self):
        return self.patientsAge

    def getTimeStamp(self):
        return self.timeStamp

    def waitTime(self, currentTime):
        return currentTime - self.timeStamp


def simulation(simulationTime, YoungRate, OldRate, breakTime):

    myClinic = Doctor( YoungRate, OldRate)
    myClinicQueue = Queue()
    waitingTimes = []

    for currentMin in range(simulationTime):

        if random.randrange(0, 6) == 4:             # A patient every 6 Minutes

            currentPatient = Patient(currentMin)

            if clinictype in "CDFGHcdfgh":          #to Minimize the probability of the younger patients in case of clinics A&B&H&I&J&K

                if currentPatient.getPatientsAge() in range(20, 41):
                    if random.randrange(1, 3) == 1:
                        myClinicQueue.enqueue(currentPatient)
                else:
                    myClinicQueue.enqueue(currentPatient)

            else:
                myClinicQueue.enqueue(currentPatient)

        halfTime = simulationTime // 2
        if currentMin >= halfTime  and currentMin <= halfTime + breakTime:
            continue


        if (not myClinic.busy()) and (not myClinicQueue.isEmpty()):

            nextPatient = myClinicQueue.dequeue()
            waitingTimes.append(nextPatient.waitTime(currentMin))
            myClinic.startNext(nextPatient)

        myClinic.tick()

    avg = sum(waitingTimes)/len(waitingTimes)
    print("Average WaitTime is ", avg ,"minutes", myClinicQueue.size(), "Patients Remaining")


while True :

    clinictype = input("please choose the type of your clinic\n"
                   "press 'A' for belly clinic\n"
                   "press 'B' for Ophthalmology\n"
                   "press 'C' for Orthopedic\n"
                   "press 'D' for surgery\n"
                   "press 'E' for dental\n"
                   "press 'F' for Dermatology\n"
                   "press 'G' for Brain and Neurology\n"
                   "press 'H' for Heart\n"
                   "press 'I' for Nose, ear and throat\n"
                   "press 'J' for Psychiatric\n"
                   "press 'K' for Oncology : \n")

    if not(clinictype in "ABCDEFGHIJKabcdefghijk") or len(clinictype) != 1:
        print("Please Enter A VALID Character\n")
        continue

    time_arrival = int(input("Arrival hour of the doctor is (in 24-hour Format): "))
    time_leaving = int(input("Leaving hour of the doctor will be (in 24-hour Format): "))
    numMins = (time_leaving - time_arrival)*60

    if(numMins <= 0):
        print("Please enter a valid format")
        continue

    youngRateWithDoctor = int(input("Younger patients rate: "))
    oldRateWithDoctor = int(input("OLDER patients rate: "))

    Break = int(input("input time you like to take as a break in minutes : "))

    for i in range(10):
        simulation(numMins,youngRateWithDoctor,oldRateWithDoctor,Break)
    print("\nSimulate Again\n")

