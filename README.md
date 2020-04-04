# PFT Linux ([Post on 4PDA](http://4pda.ru/forum/index.php?s=&showtopic=952274&view=findpost&p=94908974))

## Main authors of PFT

- friendki11er - author of the original PFT tool for Windows, file to get half-root rights ([post with PFT](http://4pda.ru/forum/index.php?s=&showtopic=952274&view=findpost&p=85383238))
- jno - ported PFT for Linux
- Zalexanninev15 - minor edits for PTF port for Linux, exclusive installer, new PFT port for Linux and PFT Linux Project

## Description

Installer (for tools) & tools for flash/dump partitions for ZTE Blade V9 Vita and ZTE Blade A7 Vita for Linux. The tools used ADB and emmcdl tools.

## System requirements

- For Linux distros: Mint/Ubuntu/Debian, Manjaro (without Installer)
- Additional: Internet (only for Installer)

## Instruction for use

1. Download and run this script for the correct install "adb", "emmcdl" and PFT Linux
2. Run the script "pft.sh" ("./pft.sh") (port by jno) or "npft" (port by Zalexaninnev15)

## Instructions for PFT Linux by Zalexanninev15

1. Write "9)", write your password and re-login in to your account
2. Write "8)" and write your password
3. Set your smartphone into EDL mode:

- ADB: Write "2)" and wait, then check the port in item "3)", enter "S"
- DFU: Item 4. , write "1)", item 4. (the port may change, so it may be necessary to change it (enter "N" when they ask about the port, then follow the instructions and the port will be checked))

4. Check the appearance of the diagnostic port "/dev/ttyUSB0". Write "3" and "S"

5. Flash and Backup (but it has not yet been implemented, so use the port by jno )

## All Errors of emmcdl

**Status: 21 The device is not ready:**

Most likely your smartphone has left EDL mode, enter this mode again.

**WARNING: Flash programmer failed to load trying to continue:**

Maybe this is a crash in emmcdl. If the flash/dump is on, then you should not worry, but if not, then it is worth putting your smartphone back into EDL mode.

**Status: 2 The system cannot find the file specified:**

An error may occur due to spaces in the path (folder) to something. You should also check for the availability of the file.

**Status: 6 The handle is invalid:**

Failure to work with diagnostic port. You should again transfer the smartphone to EDL mode.
