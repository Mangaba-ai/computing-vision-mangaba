import os

old_path = "C:/Users/Lenovo/compute-vision-supernova/yolov12"
new_path = "C:/Users/Lenovo/compute-vision-supernova/computing vision mangaba enjoy"

try:
    os.rename(old_path, new_path)
    print(f"Successfully renamed {old_path} to {new_path}")
except OSError as e:
    print(f"Error renaming directory: {e}")
