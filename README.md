# Offline Gemma Describer

A small Python tool that describes images and summarizes text files,
running 100% on-device with Gemma 4 E2B via Ollama. No cloud, no API calls.

Tested on a MacBook Pro (16GB) with Wi-Fi turned off.

## Setup
1. Install Ollama and run: ollama pull gemma4:e2b
2. pip install ollama

## Usage
python3 describe.py path/to/image.png
python3 describe.py notes.txt# offline-gemma-describer
