


#################################################################
# Constants

HEX_DIGITS = {'0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'a', 'b', 'c', 'd', 'e', 'f'}


UUID_LENGTH = 32


#################################################################
# String Utility functions

def check_valid_uuid(uuid: str) -> None:
    if len(uuid) != UUID_LENGTH:
        raise ValueError('uuid is not valid length')
    
    for digit in uuid:
        if digit not in HEX_DIGITS:
            raise ValueError(f'{digit} is not a valid uuid character')
