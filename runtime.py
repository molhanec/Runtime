#!python3

from datetime import datetime
from subprocess import PIPE, run

def get_datetimes(type):
    datetime_strings = run(
        f'powershell {type}s.ps1', 
        check=True, 
        stdout=PIPE, 
        encoding="ASCII"
    ).stdout.split("\n")
    
    datetime_objects = []
    for datetime_string in datetime_strings:
        # skip non-dates
        if ":" not in datetime_string: continue
        datetime_object = datetime.strptime(
            datetime_string.strip(), 
            "%d.%m.%Y %H:%M:%S"
        )
        datetime_objects.append(datetime_object)
    
    return datetime_objects

boot_dts     = get_datetimes("boot")
shutdown_dts = get_datetimes("shutdown")
shutdown_dts.insert(0, "Running")

combined = zip(boot_dts, shutdown_dts)
first = True
for boot, shutdown in combined:
    print(boot, "==>", shutdown, end="")
    if first: 
        first = False
        print(f"  ({datetime.now().replace(microsecond=0) - boot})")
    else:
        print(f"  ({shutdown - boot})")