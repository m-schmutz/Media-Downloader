#!/usr/bin/bash

# exit on command fail
set -e

# absolute path of directory containing this script 
declare -r SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# absolute path of project directory
declare -r PROJECT_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"

# absolute path of 'binaries' directory
declare -r BINARIES_DIR="$PROJECT_DIR/binaries"





# if yt-dlp binary is not downloaded, download it and set to be executable
if [[ ! -f "$BINARIES_DIR/yt-dlp" ]]; then
    curl -L "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp" -o "$BINARIES_DIR/yt-dlp"
    chmod +x "$BINARIES_DIR/yt-dlp"
fi


# if deno binary is not downloaded, download it 
if [[ ! -f "$BINARIES_DIR/yt-dlp" ]]; then
    curl -L "https://github.com/yt-dlp/yt-dlp/releases/latest/download/yt-dlp" -o "$BINARIES_DIR/yt-dlp"
    chmod +x "$BINARIES_DIR/yt-dlp"
fi


























