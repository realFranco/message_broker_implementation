from pubsub import pub


class EventManager():

    def __init__(self):
        self.publisher = pub

    def subscribe(self, caller, topic: str) -> None:
        self.publisher.subscribe(caller, topic)

    # TODO: unsubscribe

    def send_message(self, topic, data) -> None:
        self.publisher.sendMessage(topic, **data)

event_manager = EventManager()
