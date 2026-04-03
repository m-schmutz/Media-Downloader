#!/usr/bin/bash

# exit on command fail
set -e

# absolute path of directory containing this script 
declare -r SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# absolute path of project directory
declare -r PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# absolute path of 'binaries' directory
declare -r BINARIES_DIR="$PROJECT_DIR/binaries"


# absolute path of dlp python environment
declare -r DLP_ENV="$PROJECT_DIR/dlp-env"

# absolute path of pip for the dlp environment
declare -r DLP_ENV_PIP="$DLP_ENV/bin/pip3"


# absolute path of web python environment
declare -r WEB_ENV="$PROJECT_DIR/web-env"

# absolute path of pip for the web environment
declare -r WEB_ENV_PIP="$WEB_ENV/bin/pip3"

# absolute path of pip requirements for the web environment
declare -r WEB_REQUIREMENTS="$PROJECT_DIR/requirements/web.txt"


# if yt-dlp binary is not downloaded, download it and set to be executable
if [[ ! -f "$BINARIES_DIR/yt-dlp" ]]; then
    curl -sSL "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp" -o "$BINARIES_DIR/yt-dlp"
    chmod +x "$BINARIES_DIR/yt-dlp"
fi

# if deno binary is not downloaded, download it 
if [[ ! -f "$BINARIES_DIR/deno" ]]; then
    curl -L "https://github.com/denoland/deno/releases/latest/download/deno-x86_64-unknown-linux-gnu.zip" -o "$BINARIES_DIR/deno-x86_64-unknown-linux-gnu.zip"
    unzip -q "$BINARIES_DIR/deno-x86_64-unknown-linux-gnu.zip" -d "$BINARIES_DIR"
    rm "$BINARIES_DIR/deno-x86_64-unknown-linux-gnu.zip"
fi


# if dlp python environment is not installed, install it with requirements
if [[ ! -d "$DLP_ENV"]]; then
    python3 -m venv "$DLP_ENV"
    "$DLP_ENV_PIP" install -U yt-dlp-ejs
fi

# if web python environment is not installed, install it with requirements
if [[ ! -d "$WEB_ENV"]]; then
    python3 -m venv "$WEB_ENV"
    "$WEB_ENV_PIP" install -r "$WEB_REQUIREMENTS"
fi
