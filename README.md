# AutoSync USB & SD Card Data Backup Tool

A lightweight `.exe` utility built using Python to automatically sync data from inserted USB drives or SD cards into a secure folder on the system.

#   Features
- Detects and reads external storage devices (USB/SD)
- Automatically copies files upon execution
- Saves backup into a pre-defined folder
- Packaged as an executable `.exe` for easy use

# Tech Stack
- Python
- PyInstaller (for `.exe` packaging)
- OS module / shutil for file handling

# Use Cases
- Offline file backups
- Field work / survey data sync
- Safe-copy mechanism for external drives

# How to Use
1. Insert USB or SD card
2. Run the `.exe` file
3. Press `Enter` to sync — files will be copied automatically

# Output
- Synced files are stored in a `SyncedData/` folder on your PC
