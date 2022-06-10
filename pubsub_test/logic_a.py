from eventManager import event_manager


def drive_car(brand: str, year: int) -> None:
    print(f'I will drive a {brand} car from {year}')

event_manager.subscribe(caller=drive_car, topic='car')
