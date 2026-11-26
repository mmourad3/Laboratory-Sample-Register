class Sample:
    def __init__(sample,ID,Type,Status='Received' ,Readings=None):
        sample.__ID=ID
        sample.__Type=Type
        sample.__Status = Status
        sample.__Readings= Readings if Readings else []
        
    def getID(sample):
        return sample.__ID
    def getType(sample):
        return sample.__Type
    def getStatus(sample):
        return sample.__Status
    def getReadings(sample):
        return sample.__Readings
    
    def setStatus(sample, newStatus):
        if sample.__Status==newStatus:
            return f"Sample is already \'{newStatus}\'"
        if sample.__Status=="Received" and newStatus=="Processing":
            sample.__Status= "Processing"
            return "Status changed to Processing"
        if sample.__Status == "Processing" and newStatus == "Completed":
            if len(sample.__Readings)<3:#minimum of 3 readings is requried to complete the sample
                return "At least three readings are required"
            sample.__Status = "Completed"
            return "Status successfully changed to \'Completed\'"
        return "Invalid changing of status"
    def __str__(sample):
        return f"ID: {sample.__ID}, Type: {sample.__Type}, Status: {sample.__Status}, Readings: {sample.__Readings}"
    
    def addReading(sample, reading):
        if sample.__Status!= "Processing": #Sample status must be 'Processing' to be able to add reading
            return "Sample must be \'Processing\' to add readings"
        sample.__Readings.append(reading) #Add the reading to the sample's readings list
        return "Reading added successfully"
    def getStatistics(sample):
        if sample.__Status!="Completed": #Sample status must be 'Completed' to be able to get statistics
            return "Sample must be \'Completed\' to get statistics"
        mean=sum(sample.__Readings)/len(sample.__Readings) #Calculate the mean of the readings
        minimum=min(sample.__Readings) #Find the minimum
        maximum=max(sample.__Readings) #Find the maximum
        return f"Mean: {mean:.2f}, Min: {minimum}, Max: {maximum}"
    def countOutOfRange(sample,lower,upper):
        count=0
        for reading in sample.__Readings: #loop through the readings and count how many are out of range
            if reading<lower or reading>upper:
                count+=1
        return count
    def longestOutOfRange(sample, lower, upper):
        current=0 #current number of consecutve out of range readings
        longest=0 #longest run found so far
        for reading in sample.__Readings: 
            if reading<lower or reading>upper: 
                current+=1
            else: #we found a reading that is within the range
                if longest<=current:
                    longest=current #update the longest run if the current run is longer or equal to it
                current=0 #reset the current run when we find a reading within the range
        if longest<=current: #Checks the last run in case the last reading is out of the range
            longest=current
        return longest
    def validateLimits(sample,lower,upper): #Check if the lower and upper limits are valid
            if lower>upper:
                return "Lower limit cannot be greater than upper limit"
            return None #no error so the limits are valid
