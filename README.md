Essentially this script is targeted at both users and subtitle authors who need to take filenames that look like this:
```
Series_Title_EP_Number_Full_Episode_Title_[encoding options]_[CRC32].mkv
subs1.srt
```
and rename them to look like this:
```
Series_Title_EP_Number_Full_Episode_Title_[encoding options]_[CRC32].mkv
Series_Title_EP_Number_Full_Episode_Title_[encoding options]_[CRC32].srt
```

The requirements for this to work well are:
1. You have the same number of subtitle and video files
2. All files sort correctly, e.g., no roman numerals or episode numbers after the checksum
3. The only files in the directory with the chosen extensions are the ones you want to rename
