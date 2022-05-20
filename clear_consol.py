import os


def clear_consol():
    command = "clear"
    if os.name in ('nt', 'dos'):
        command = "cls"
    os.system(command)
