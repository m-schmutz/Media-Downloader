#################################################################
# Local Imports

from ..config import DLP_ENV_PIP, DLP_ENV_PY, YT_DLP_PATH


#################################################################
# Update Arguments

UPDATE_DLP_PIP = (
    DLP_ENV_PIP,
    'install',
    '-U',
    'pip'
)


UPDATE_DLP_EJS = (
    DLP_ENV_PIP,
    'install',
    '-U',
    'yt-dlp-ejs'
)


UPDATE_YT_DLP = (
    DLP_ENV_PY,
    YT_DLP_PATH,
    '-U'
)