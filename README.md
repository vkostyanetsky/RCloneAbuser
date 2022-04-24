# RCloneAbuser

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

It is a simple Python script, intended to execute [rclone](https://rclone.org) on a list of folders in one call. I use it to back up data from my PC to home NAS: it's a bit more convenient than make a bunch of cmd files, similar to each other.

## Well, how to use it?

There are two required parameters: `--config` and `--rclone`. First one is a path to the rclone binary file on your computer. Second one is a path to a YAML config file like [this one](config.yaml). For instance:

```
py abuser.py --config="D:\Apps\RCloneAbuser\config.yaml" --rclone="D:\Apps\RCloneAbuser\rclone.exe"
```

## How I have to write the config file?

There is a pair of paths per line, separated by colon. First one is a folder whose content must be synced. The second is the folder the first one needs to be synced with.  

## How does it work with rclone?

The script will execute the following command for an every pair of folders:

```
rclone sync "{source}" "{target}" --copy-links --progress --stats-one-line
```

You can change this behaviour in the very start of the script (see the variable named `command`). 

## What about dependencies?

[PyYAML](requirements.txt) only.