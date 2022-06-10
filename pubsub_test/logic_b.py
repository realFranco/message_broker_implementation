from eventManager import event_manager


def drive_airplane(brand: str) -> None:
    print(f'I will drive a {brand} airplane')

event_manager.subscribe(caller=drive_airplane, topic='airplane')
