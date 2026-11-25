import json
from sample import Sample

class SampleRegister:
    def __init__(register):
        register.FileName ='samples.json'
        register.samples={}
        register.loadSamples()
    def loadSamples(register):
        try:
            with open(register.FileName, "r") as suzieq:#suzieq is the file object used to read the saved samples
                content= suzieq.read().strip()
                saved= json.loads(content) if content else {}
        except FileNotFoundError:
            saved={}
        for ID, attr in saved.items():#convert the saved data back to Sample objects
            sample = Sample(attr['ID'],\
                            attr['Type'],\
                            attr['Status'],\
                            attr['Readings'])
            register.samples[ID]= sample
    def sampleExists(register,ID):
        return ID in register.samples
    def validateID(register,ID,mustExist=True): #'mustExist' specifies whether the ID should already exist or not
        if ID=="":
            return "ID cannot be empty"
        if mustExist and not register.sampleExists(ID): #returns error message if the sample doesn't exist when it should
            return "Sample not found"
        if not mustExist and register.sampleExists(ID):#returns error message if the sample exists when it shouldn't
            return "This sample already exists"
        return None #No error. The ID is valid
    def registerSample(register, sample):
        error=register.validateID(sample.getID(),False) #the sample shouldn't exist but if it does then an error message will be returned
        if error:
            return error
        register.samples[sample.getID()]=sample #saving the Sample object in the dictionary if there is no error
        return 'Sample registered successfully'
    def change_status(register, ID, newStatus):
        error=register.validateID(ID) #the sample should exist but if it doesn't then an error message will be returned
        if error:
            return error
        sample=register.samples[ID]
        return sample.setStatus(newStatus)
    
    def add_Reading(register,ID,reading):
        error=register.validateID(ID)
        if error:
            return error
        sample=register.samples[ID] #Gets the Sample object from the dictionary using its ID which is also the key
        return sample.addReading(reading) #Calls the 'addReading' method in the Sample class and returns the message received from that method        
    
    def get_Statistics(register, ID):
        error=register.validateID(ID)
        if error:
            return error
        sample=register.samples[ID] #Gets the Sample object using its ID
        return sample.getStatistics()
    def count_out_of_range(register, ID, lower, upper):
        error=register.validateID(ID)
        if error:
            return error
        sample=register.samples[ID]
        return sample.countOutOfRange(lower, upper)
    def longest_out_of_range(register, ID, lower, upper):
        error=register.validateID(ID)
        if error:
            return error
        sample=register.samples[ID]
        return sample.longestOutOfRange(lower, upper)