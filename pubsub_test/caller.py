from eventManager import event_manager
import logic_a
import logic_b


event_manager.send_message(topic='car', data={'brand': 'Honda', 'year': 2008})
event_manager.send_message('airplane', {'brand': 'Lotus'})
