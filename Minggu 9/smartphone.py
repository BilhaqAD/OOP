from abc import ABC, abstractmethod

class VoiceAssistance(ABC):

    def __init__(self):
        self.status = False

    @abstractmethod
    def aktifkan_asisten():
        pass

    @abstractmethod
    def matikan_asisten():
        pass
    
    @abstractmethod
    def greetings():
        pass

class Smartphone(VoiceAssistance):

    def aktifkan_asisten(self):
        self.status = True
        print("voice asisten ON")

    def matikan_asisten(self):
        self.status = False
        print("voice asisten OFF")

    def greetings(self):
        if self.status == True:
            print("Hallo, apa kabar, Bagaimana harimu?")
        else:
            print("Nyalakan terlebih dahulu fitur voice asisten")

s = Smartphone()
s.greetings()
s.aktifkan_asisten()
s.greetings()
s.matikan_asisten()
s.greetings()