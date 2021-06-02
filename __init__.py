from mycroft import FallbackSkill
import datetime as dt

        startTime = datetime.datetime(11,45,0)
        currentTime = date.time.now().time()
        endTime = datetime.time(23,00,0)


class OnsmokeoFallback(FallbackSkill):
    """
     A skill to answer any question asked between
     11:45am and 12:00pm Monday - Friday
    """
    def __init__(self):
        super(OnsmokeoFallback, self).__init__(name='Smokeo Fallback Skill')
        #I want the fallback code to run only at particular times. Do I need to include this 
        # in the initialisation code here?

    def initialize(self):
    """
    Registers the fallback handler
    The fallback handler listents to determine if an Utterance can be handled.
    I don't want it to listen for utterances. I just want it to respond "I'm on  Smokeo
    if the user activates Mycroft in a particular time. Does this mean I don't want to use
    initialize? 
    """ 
        self.register_fallback(self.handle_fallback, 99) #Set to 99 so has high priority.

    def IsSmokeoTime():
    """
    Defines period when Smokeo happens    
    """
     if currentTime >=startTime and <=endTime
        IsSmokeoTime = True
        else IsSmokeoTime = False

    def handle_fallback(self, message):
    """
    Answers any utterance (or no utterance) made between 11:45am and 12:00pm Monday - Friday"
    """
    # utterance = message.data.get("utterance") 
    #have commented this out because don't want fallback to have to wait for utterance. 
 
    if IsSmokeoTime = True
       self.speak('Im on Smoke O. Do it yourself')
       return True
    else:
       return False 

   def shutdown(self):
       self.remove_fallback(self.handle_fallback)
       super(OnsmokeoFallback, self).shutdown()
   
   def create_skill():
       return OnsmokeoFallback() 
