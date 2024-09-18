import os

def delete_htaccess_files(directory):
    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(directory):
        # Check if .htaccess is in the current directory
        if '.htaccess' in files:
            htaccess_path = os.path.join(root, '.htaccess')
            try:
                os.remove(htaccess_path)
                print(f"Deleted: {htaccess_path}")
            except Exception as e:
                print(f"Error deleting {htaccess_path}: {e}")

# Specify the directory you want to start the search from
directory_to_search = "C:\\Users\\rupar\\Documents\\GitHub\\ba5f8274-1f43-40cc-b456-99752a127aac\\wp-content\\uploads\\WP-manga\\data\\manga_6019198ee2ac3"

delete_htaccess_files(directory_to_search)
