# RCloneAbuser

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

Скрипт для последовательного запуска утититы rclone для нужного набора файлов и папок.

## Как настроить?

Нужно создать в файле config.yaml хотя бы один план синхронизации и указать в нем хотя бы одну пару источник-получатель (т.е. что синхронизировать и с чем синхронизировать).

## Как пользоваться?

Запустить скрипт с параметром plans, указав нужный план синхронизации. Можно указать несколько планов через запятую.

```
python abuser.py --plans regular,vms
```
## 

Пример вывода скрипта:

```
Source: D:\Apps
Target: M:\Drive\Backup\D\Apps
--- 0:1:22 ---

Source: D:\Audio
Target: M:\Drive\Backup\D\Audio
--- 0:0:10 ---
```