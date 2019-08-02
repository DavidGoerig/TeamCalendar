from .models import Devices

def handle_device_file(f):
    for chunk in f.chunks():
        splitted_file = chunk.splitlines()
        for line in splitted_file:
            splitted = line.decode().split(',')
            if len(splitted) is 6 and any(elem is None for elem in splitted):
                new = Devices(name=splitted[2],
                              serial_number=splitted[3],
                              sap_equipment_nbr=int(splitted[4]),
                              location=splitted[5],
                              ip_address=splitted[0]+splitted[1])
                new.save()

