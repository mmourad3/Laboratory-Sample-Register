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