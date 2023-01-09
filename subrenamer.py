#!/usr/bin/python
import os
import re

subfiles = []
videofiles = []

# get directory from user input as well as the file extension of the videos and the subs
folderpath = (
    input(
        "Enter the directory that contains both the subs and video files (default current directory):"
    )
    or "."
)
subext = input("Enter the extension for the subtitles (default srt):") or "srt"
videoext = input("Enter the extension for the video files (default mkv):") or "mkv"

# get a list of the paths we care about
for i in os.listdir(folderpath):
    if re.search(f"{subext}$", i) is not None:
        subfiles.append(i)
    if re.search(f"{videoext}$", i) is not None:
        videofiles.append(i)

# make sure we have a valid file list
assert len(subfiles) == len(videofiles), "Number of sub and video files do not match"
assert len(subfiles) != 0, "There are no files to move! Aborting"

# match up the files so we can loop through them in order.
subfiles = sorted(subfiles)
videofiles = sorted(videofiles)
for sub, vid in zip(subfiles, videofiles):
    destination = vid.rsplit(videoext, 1)[0] + subext
    print(f"current name: {sub}\t new name:{destination}")
    # using os.rename so it won't overwrite any files
    os.rename(os.path.join(folderpath, sub), os.path.join(folderpath, destination))
