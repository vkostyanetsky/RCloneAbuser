# RCloneAbuser

[![License: Unlicense](https://img.shields.io/badge/license-Unlicense-blue.svg)](http://unlicense.org/)

Скрипт, который последовательно запускает утилиту [rclone](https://rclone.org) для списка из файлов и папок. Я использую его для бэкапа данных со своего компьютера на домашний NAS: это несколько удобнее, чем держать набор длиннющих, почти одинаковых команд в нескольких cmd-файлах.

## Как настроить?

Нужно создать в файле config.yaml план синхронизации (или несколько) и указать в нем пару источник-получатель (т.е. что синхронизировать и с чем синхронизировать). В план может входить сколько угодно источников и получателей; для каждого будет вызвана следующая команда:

```
rclone sync "{источник}" "{получатель}" --copy-links --progress --stats-one-line
```

Параметры вызова утилиты можно поменять в функции rclone().

## Как пользоваться?

Нужно запустить скрипт abuser.py с параметром plans, указав нужный план синхронизации. Можно указать несколько планов через запятую. Пример:

```
python abuser.py --plans regular,vms
```

Скрипт последовательно пройдет по всем указанным файлам и папкам, синхронизировав источники и получатели. Кроме того, для каждого источника он выведет время, потраченное на синхронизацию.

Пример вывода скрипта:

```
Source: D:\Apps
Target: M:\Drive\Backup\D\Apps
--- 0:1:22 ---

Source: D:\Audio
Target: M:\Drive\Backup\D\Audio
--- 0:0:10 ---
```