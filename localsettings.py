# Edit these variables to your liking, make sure to use \\ for backslash or / for forward slash 
undated_fs = "%t\\Season %s\\%t S%0s E%0e"
dated_fs   = "%t\\%t %sm %0d %y"
movie_fs   = "%t (%y)"

tvdest     = "D:\\Videos\\TV"
moviedest  = "D:\\Videos\\Movies"
sourcedir  = "D:\\Downloads\\Usenet" 
extensions = ["mkv", "avi", "mp4", "ts"]
SATELLITES = ["srt", "srr"]
min_size   = 100   # in MB / Megabytes (Default: 100MB)

overwrite  = True  # Overwrite files at destination?          (Default: True)
remove_CC  = True  # Remove country codes from filename?      (Default: True)
verbose    = True  # Show output in command line interface?   (Default: True)
truncate   = True  # Truncate the output to 80 characters?    (Default: True)
satellites = True  # Move related files such as subtitles?    (Default: True)
cleanup    = True  # Cleanup after moving files?              (Default: True)
clean_mode = 2     # Cleanup mode 1 or 2.                     (Default: 1)
                   # 1 is "safe cleanup" 2 removes the whole directory after something is moved. 
notify     = False # Show popup notifications instead of CLI? (Default: False)
stay_open  = False # Keep window open after execution?        (Default: False)
no_rename  = False # Prevent file operations for testing?     (Default: False)
remove_src = True  # Allow sourcedir to be removed during cleanup? (Default: False)
