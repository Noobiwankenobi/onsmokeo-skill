from mycroft import MycroftSkill, intent_file_handler


class Onsmokeo(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('onsmokeo.intent')
    def handle_onsmokeo(self, message):
        self.speak_dialog('onsmokeo')


def create_skill():
    return Onsmokeo()

