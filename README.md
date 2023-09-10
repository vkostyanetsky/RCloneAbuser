# 📁 🗂️ 🗃 RCloneAbuser

[![black](https://github.com/vkostyanetsky/RCloneAbuser/actions/workflows/black.yml/badge.svg)](https://github.com/vkostyanetsky/RCloneAbuser/actions/workflows/black.yml) [![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

It is a simple Python script, intended to execute [rclone](https://rclone.org) on a list of folders. I use it to back up data from my PC to home NAS: it's a bit more convenient than make a bunch of rclone shortcuts, similar to each other.

## 🤨 Well, how to use it?

First of all, you need to install `rclone` in case if it is not installed yet. For instance, this is how to do it for Windows:

```commandline
winget install Rclone.Rclone
```

As for the script, there are two required parameters: `--config` and `--rclone`. First one is a path to the rclone binary file on your computer. Second one is a path to a YAML config file like [this one](config.yaml). For instance:

```commandline
py abuser.py --config="D:\Apps\RClone\abuser.yaml" --rclone="D:\Apps\RClone\rclone.exe"
```

By the way, you can omit the `rclone` parameter if the app has an alias in your system, so you can call it like this:

```commandline
rclone
```

## 🙂 How to write the config file?

There is a pair of paths per line, separated by colon. First one is a folder whose content must be synced. The second is the folder the first one needs to be synced with.  

For instance:

```yaml
- D:\42: M:\Backup\D\42
```

Here the `D:\42` directory is going to by synced with the `M:\Backup\D\42` directory. 

## 🧐 How does it work with rclone?

The script will execute the following command for an every pair of folders:

```commandline
rclone sync "source" "target" --copy-links --progress --stats-one-line
```

You can easily change this behaviour: look for a `command` variable.