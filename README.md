#  AutoSync - USB/SD Card Data Backup Tool (.exe)

A Python-based executable tool to **automatically copy files** from USB drives or SD cards into a local folder when executed.

# Features
- Detects and accesses external drives (USB, SD card)
- Copies all files into a predefined folder
- Simple 'press Enter to sync' interface
- Compiled into `.exe` for standalone use

# Built With
- Python
- `os`, `shutil` modules
- PyInstaller (for .exe creation)

# How It Works
1. Insert a USB/SD card into your system.
2. Run `autosync.exe`.
3. Hit **Enter** to begin syncing.
4. Files will be backed up to a local `SyncedData/` folder.

# Example Use Cases
- Backup field research or survey data
- Save important photos from memory cards
- Quick offline file transfer for non-technical users

# Future Improvements
- GUI version with file type filters
- Auto-detect drive paths
- Log file with sync timestamps

 [@mudeep02](https://github.com/mudeep02) 
