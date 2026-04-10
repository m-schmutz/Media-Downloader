


#################################################################
# Constants

HEX_DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}


UUID_LENGTH = 32


#################################################################
# String Utility functions

def check_valid_uuid(uuid: str) -> None|str:
    if len(uuid) != UUID_LENGTH:
        return 'uuid is not valid length'
    
    for digit in uuid:
        if digit not in HEX_DIGITS:
            return f'{digit} is not a valid uuid character'
        
    return None
