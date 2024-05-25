# Automatic Python File Sorting Script

## Scripting Practice Project (Data Analyst Project 02)

This Python script facilitates the automatic sorting of files within a specified directory into separate folders based on their file extensions. It is particularly useful for organizing cluttered download folders.

## How It Works

The script utilizes the `os` and `shutil` modules to interact with the file system and move files. Here's a breakdown of the process:

1. **Specify Source and Destination Directories**: Set the `path` variable to the directory containing the files to be sorted.

2. **Define Folder Names**: Specify the names of folders where files will be sorted based on their file extensions.

3. **Check and Create Folders**: Ensure that the destination folders exist. If not, create them.

4. **Sort Files**: Iterate through the files in the source directory and move them to the appropriate destination folder based on their file extensions.

5. **Completion Message**: Once sorting is complete, a message will indicate that the files have been moved to the correct folders.

## Usage

1. Modify the `path` variable to point to your desired source directory.
2. Customize the `folder_name` list to match your preferred folder names.
3. Run the script.

## Example

```python
python afs.py
```

## Requirements

- Python 3.x
- Standard libraries: `os`, `shutil`

## Note

- Ensure that you have necessary permissions to move files within the specified directories.
- This script does not handle nested directories. It only operates on files within the specified source directory.
