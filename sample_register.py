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
    def registerSample(register, sample):
        if register.sampleExists(sample.getID()):#if the sample exists tell the user u can't register it
            return 'This sample already exists'
        else:#saving the Sample object in the dictionary
            register.samples[sample.getID()] = sample
            return 'Sample registered successfully'
    def change_status(register, ID, newStatus):
        if not register.sampleExists(ID):
            return "Sample not found"
        sample=register.samples[ID]
        return sample.setStatus(newStatus)