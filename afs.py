import os, shutil # Import the os and shutil modules, will be used to move files, and get file paths.

# Define the source and destination directories
path = "/Users/williamhellemsmoody/Downloads/"

file_name = os.listdir(path)

# Create the folder if it does not exist
folder_name = ['png_files', 'jpeg_files', 'pdf_files', 'doc_files', 'txt_files', 'sql_files', 'csv_files', 'xlsx_files', 'html_files', 'exe_files', 'zip_files']

# Dictionary to map file extensions to folder names
extension_to_folder = {
    '.png': folder_name[0],
    '.jpg': folder_name[1],
    '.jpeg': folder_name[1],
    '.PDF': folder_name[2],
    '.doc': folder_name[3],
    '.docx': folder_name[3],
    '.txt': folder_name[4],
    '.sql': folder_name[5],
    '.csv': folder_name[6],
    '.xlsx': folder_name[7],
    '.html': folder_name[8],
    '.exe': folder_name[9],
    '.zip': folder_name[10]
}


# Iterate over the files in dir and move to correct folder using shutil.move method
def does_folder_exist():
    for pos in range(len(folder_name)): 
        if not os.path.exists(path + folder_name[pos]): 
            os.makedirs(path + folder_name[pos])
        else: 
            print('Directory Already Exists!')

def move_files():
    # Move files to dir folders
    for file in file_name:
        _, ext = os.path.splitext(file)
        if ext.lower() in extension_to_folder:
            dest_folder = os.path.join(path, extension_to_folder[ext.lower()])
            shutil.move(os.path.join(path, file), dest_folder)
    print("All Files have been moved to the correct folders")


#NOTE Call the functions to check if the folder exists and move the files.
does_folder_exist()
move_files()
    

            
