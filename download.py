from pytube import YouTube
from youtubesearchpython import *
import os
import time
from pygoogle_image import image as pi
import requests
import sys
import subprocess
import pyfiglet as Figlet
from colorama import Fore

appName = "Youtube & Google Images Downloader." 

def restart_program():
    subprocess.call(sys.executable + ' "' + os.path.realpath(__file__) + '"')

def check_exit(input_str):
    if input_str == 'x':
        print(f"\nThanks for using {appName}")
        time.sleep(3)
        sys.exit()

def download_image(image, limit, path):
    pi.download(keywords=image, limit=limit, directory=path)
    print(f"Downloaded {limit} images on {image} to {path}")

def download_video(video, path):
    yt = YouTube(video['link'])
    stream = yt.streams.get_highest_resolution()

    # Get the video URL and file size
    url = stream.url
    video_size = stream.filesize
    downloaded = 0  # Variable to track the amount downloaded
    chunk_size = 1024 * 1024  # 1 MB chunks

    # Ensure target directory exists
    os.makedirs(path, exist_ok=True)

    # Start the download
    file_path = os.path.join(path, stream.default_filename)
    with requests.get(url, stream=True) as r, open(file_path, 'wb') as f:
        for chunk in r.iter_content(chunk_size=chunk_size):
            if chunk:  # filter out keep-alive new chunks
                f.write(chunk)
                downloaded += len(chunk)
                progress = int((downloaded / video_size) * 100)
                sys.stdout.write(f"\rDownloading {video['title']} [{'#' * (progress // 5)}{'.' * (20 - progress // 5)}] {progress}%")
                sys.stdout.flush()
    print()  # Move to the next line after download completes

def download_videos(videos):
    print("Downloading videos...")
    for video in videos:
        download_video(video, path)
    print("\nAll videos downloaded successfully!\n")

def deleteExtra(directory, query):

    query = query.replace(" ", "_")
    finalPath = path + "/" + query
    png_files = [file for file in os.listdir(finalPath) if file.endswith('.png')]
    png_files.sort()  # Optional: sort the files if you want to delete the first three alphabetically

    for png_file in png_files[:3]:  # Get the first three files
        file_path = os.path.join(finalPath, png_file)
        os.remove(file_path)

def rename(path, query):

    query = query.replace(" ","_")
    path = path + "/"+ query
    num = 1

    for file in os.listdir(path):

        name, extension = file.rsplit('.', 1)
        name = query + str(num) + "." + str(extension)
        old = os.path.join(path,file)
        new = os.path.join(path,name)
        os.rename(old, new)
        num += 1

#------------------------------------------------------------------------------------------------------------------------------------------

title = Figlet.figlet_format(appName, width=100)
print(Fore.GREEN + title)
print(Fore.GREEN + "Enter (x) anytime to exit.\n")

query = input("Enter a search query: ")
check_exit(query)

while True:
    directory_path = input("\nEnter the directory to save your images/videos (or 'x' to exit): ")
    check_exit(directory_path)

    if "/" in directory_path or "\\" in directory_path:
        break
    else:
        print("\nInvalid directory path. Please enter a valid path.\n")

path = str(directory_path.replace("\\","/") + "/")

print(f"\nDirectory selected: {path}")

print(" ")

while True:
    choice = input("Download images(i), videos(v) or both(b)?: ")
    check_exit(choice)

    if "i" in choice or "v" in choice or "b" in choice:
        break
    else:
        print("\nInvalid choice. Acceptable options: 'i', 'v', 'b'.\n")

#-----Both------
        
#------Images------------------------------------------------------

if choice == "b":
    print(Figlet.figlet_format("Images.", width=100))

    while True:
        user_input = input("\nHow many images would you like to download (or 'x' to exit): ")
        check_exit(user_input)

        try:
            photoLimit = int(user_input)
            break  # Exit the loop since a valid integer was entered
        except ValueError:
            print("That's not a valid number. Please enter an integer.")
    

    photoLimit = photoLimit + 3
    download_image(query, photoLimit, path)

#------Videos---------------------------------------------------------

    print(Figlet.figlet_format("Videos.", width=100))

    while True:
            videoLimit = int(input("\nEnter the amount of results for videos: \n"))
            check_exit(videoLimit)

            try:
                videoLimit = int(videoLimit)
                break  # Exit the loop since a valid integer was entered
            except ValueError:
                print("That's not a valid number. Please enter an integer.")
            
    while True:
        print("Sort by: \n 1. Relevance. \n 2. Upload Date (Most recent.) \n 3. View Count\n")
        try:
            sortBy = int(input("Enter integer (1,2,3): "))
            check_exit(sortBy)

            if sortBy == 1:
                search = VideosSearch(query, limit=videoLimit)
                searchResult = search.result()
                break

            elif sortBy == 2:
                search = CustomSearch(query, VideoSortOrder.uploadDate, limit=videoLimit)
                searchResult = search.result()
                break

            elif sortBy == 3:
                search = CustomSearch(query, VideoSortOrder.viewCount, limit=videoLimit)
                searchResult = search.result()
                break

            else:
                print("Invalid input. Please enter 1, 2, or 3.")
                
        except ValueError:
            print("Invalid input. Please enter an integer.")

    print("\n")
    print("-" * 50)

    for video in searchResult['result']:
        print(f"Title: {video['title']}")
        print(f"Link: {video['link']}")
        print(f"Channel: {video['channel']['name']}")
        print(f"View Count: {video['viewCount']['short']}")
        print(f"Published: {video['publishedTime']}")
        print("-" * 30)

    decision = input("Would you like to download these videos? (y/n): ")
    check_exit(decision)

    if decision == "n":
        final = input("Would you like to quit(y) or start a new search(n)?: ")
        check_exit(final)

        if final == "y":
            print(f"\nThanks for using {appName}")
            time.sleep(3)

        elif final == "n":
            restart_program()

    elif decision == "y":
        download_videos(searchResult['result'])

#-----Images------

if choice == "i":

    while True:
        user_input = input("\nHow many images would you like to download (or 'x' to exit): ")
        print(" ")
        check_exit(user_input)

        try:
            photoLimit = int(user_input)
            break  # Exit the loop since a valid integer was entered
        except ValueError:
            print("\nThat's not a valid number. Please enter an integer.\n")
    

    photoLimit = photoLimit + 3

    download_image(query, photoLimit, path)

    deleteExtra(path, query)

    rename(path, query)

    startAgain = input("Start a new video/image search (y/n): ")
    check_exit(startAgain)

    if startAgain == "n":
        print(f"Thanks for using {appName}")
        time.sleep(3)

    if startAgain == "y":
        restart_program()



#-----Videos------

if choice == "v":

  while True:
    videoLimit = int(input("\nEnter the amount of results for videos: "))
    print(" ")
    check_exit(videoLimit)

    try:
        videoLimit = int(videoLimit)
        break  # Exit the loop since a valid integer was entered
    except ValueError:
        print("That's not a valid number. Please enter an integer.")
            
  while True:
    print("Sort by: \n 1. Relevance. \n 2. Upload Date (Most recent.) \n 3. View Count\n")
    try:
        sortBy = int(input("Enter integer (1,2,3): "))
        check_exit(sortBy)

        if sortBy == 1:
            search = VideosSearch(query, limit=videoLimit)
            searchResult = search.result()
            break

        elif sortBy == 2:
            search = CustomSearch(query, VideoSortOrder.uploadDate, limit=videoLimit)
            searchResult = search.result()
            break

        elif sortBy == 3:
            search = CustomSearch(query, VideoSortOrder.viewCount, limit=videoLimit)
            searchResult = search.result()
            break

        else:
            print("Invalid input. Please enter 1, 2, or 3.")
            
    except ValueError:
        print("Invalid input. Please enter an integer.")

print("\n")
print("-" * 50)

for video in searchResult['result']:
    print(f"Title: {video['title']}")
    print(f"Link: {video['link']}")
    print(f"Channel: {video['channel']['name']}")
    print(f"View Count: {video['viewCount']['short']}")
    print(f"Published: {video['publishedTime']}")
    print("-" * 30)

decision = input("Would you like to download these videos? (y/n): ")
check_exit(decision)
print(" ")

if decision == "n":
    final = input("Would you like to quit(y) or start a new search(n)?: ")
    check_exit(final)

    if final == "y":
        print(f"\nThanks for using {appName}")
        time.sleep(3)

    elif final == "n":
        restart_program()

elif decision == "y":
    download_videos(searchResult['result'])
    final = input("Would you like to quit(y) or start a new search(n)?: ")
    check_exit(final)

    if final == "y":
        print(f"\nThanks for using {appName}")
        time.sleep(3)

    elif final == "n":
        restart_program()
