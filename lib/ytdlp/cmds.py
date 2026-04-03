#################################################################
# Python Lib Imports

from subprocess import run


#################################################################
# Local Imports

from .args import UPDATE_DLP_PIP, UPDATE_DLP_EJS, UPDATE_YT_DLP


#################################################################
# Process Command Functions

def update_dlp_environment():
    for args in (UPDATE_DLP_PIP, UPDATE_DLP_EJS, UPDATE_YT_DLP):
        result = run(args, capture_output=True, text=True)

        if result.returncode:
            raise RuntimeError(result.stderr)

