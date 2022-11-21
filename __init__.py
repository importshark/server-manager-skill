from mycroft import MycroftSkill, intent_file_handler


class ServerManager(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('manager.server.intent')
    def handle_manager_server(self, message):
        self.speak_dialog('manager.server')


def create_skill():
    return ServerManager()

