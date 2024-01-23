# YouTube & Google Images Downloader

## Description

This command line application allows users to download images and videos based on a search query. 
Users can search for images via Google and videos on YouTube. The program offers flexibility in 
terms of the number of downloads, sorting criteria for videos, and directory selection for saving 
the downloaded content.

## Images



## Features

- Download images from Google based on a search query.
- Download videos from YouTube, with options to sort by relevance, upload date, or view count.
- Customizable download path for saving images and videos.
- Option to download either images, videos, or both.
- Restart and exit functionalities.

## Packages Used

- pytube: For downloading videos from YouTube.
- youtubesearchpython: To search for YouTube videos based on queries.
- pygoogle_image: To search and download images from Google.
- requests: For handling HTTP requests.
- os: For file and directory operations.
- time: To handle time-related tasks.
- sys: For system-specific parameters and functions.
- subprocess: To execute shell commands.
- pyfiglet: For ASCII art text.
- colorama: To add color to the console output.

## Installation

Before running the application, ensure you have Python installed on your system. Then, install the 
required packages using pip:

'''pip install pytube youtubesearchpython pygoogle_image requests pyfiglet colorama'''

## Usage (Windows OS Only).

- Open the script an run in a code interpreter (Pycharm, VsCode)
- Enter in command prompt (in directory of script): '''python download.py'''

Run the script in a Python environment. Follow the on-screen prompts to enter your search query,
choose the directory for downloads, select whether to download images, videos, or both, and specify
the number of items to download.

## Potential Issues

- API Changes: Changes in the YouTube API or Google Images API might cause the downloader functions to break.
- Network Issues: The program may encounter issues if there's an unstable internet connection.
- File Permissions: In certain environments, there might be issues with file permissions when trying to save downloads.
- Rate Limiting: Excessive use of APIs might trigger rate limiting.
- Compatibility: The script's compatibility with future versions of Python or its dependencies is not guaranteed.
- First three images downloaded may display unrelated icons. These can be saftely deleted.

## License

This project is distributed under the MIT License.

