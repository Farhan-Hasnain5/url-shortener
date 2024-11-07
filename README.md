# URL Shortener

This is a simple URL shortener application built using Python and Tkinter. It allows users to shorten long URLs and copy the shortened URL to the clipboard.

## Features

- Shorten long URLs using the TinyURL service.
- Copy the shortened URL to the clipboard with a single click.

## Requirements

- Python 3.x
- `tkinter` (usually included with Python)
- `pyshorteners` library
- `pyperclip` library

## Installation

1. Clone the repository:

   ```sh
   git clone https://github.com/Farhan-Hasnain5/url-shortener.git
   cd url-shortener
   ```

2. Install the required libraries:
   ```sh
   pip install pyshorteners pyperclip
   ```

## Usage

1. Run the application:

   ```sh
   python Gui_linkShortener.py
   ```

2. Enter the long URL in the input field and click the "Shorten URL" button.

3. The shortened URL will be displayed. Click the "Copy to Clipboard" button to copy the shortened URL.

## Code Overview

- The main application window is created using Tkinter.
- The `shorten_url` function retrieves the long URL, shortens it using the TinyURL service, and updates the result label.
- The `copy_to_clipboard` function copies the shortened URL to the clipboard.

