import os
import shutil
import random

def organize_images(folder_path, sort_by="name"):
    # Define the main output folder and subfolders for train, validation, and test
    organize_folder = os.path.join(folder_path, "organize_data")
    train_folder = os.path.join(organize_folder, "train")
    validation_folder = os.path.join(organize_folder, "validation")
    test_folder = os.path.join(organize_folder, "test")

    # Create the directories if they don’t already exist
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)
    os.makedirs(test_folder, exist_ok=True)

    # List all image files in the folder
    images = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, filename))]

    # Sort the images based on the chosen criterion
    if sort_by == "name":
        images.sort()  # Sort alphabetically by filename
    
    # Shuffle images after sorting to ensure random distribution into train/validation/test
    random.shuffle(images)

    # Define split ratios (e.g., 70% train, 15% validation, 15% test)
    train_split = int(0.7 * len(images))
    validation_split = int(0.85 * len(images))  # train + validation

    # Distribute images into train, validation, and test
    for idx, image_path in enumerate(images):
        filename = os.path.basename(image_path)
        if idx < train_split:
            shutil.copy(image_path, os.path.join(train_folder, filename))
            print(f"Copied to train: {filename}")
        elif idx < validation_split:
            shutil.copy(image_path, os.path.join(validation_folder, filename))
            print(f"Copied to validation: {filename}")
        else:
            shutil.copy(image_path, os.path.join(test_folder, filename))
            print(f"Copied to test: {filename}")

    print(f"Images have been organized into '{organize_folder}' with 'train', 'validation', and 'test' subfolders.")

# Example usage
folder_path = '/Users/lokeshdas/Desktop/organized_swinfusr_data/Data_SwinFusr/visible'  # Update with the correct path

# Use "name" to sort alphabetically or "modification_time" to sort by modification date
organize_images(folder_path, sort_by="name")
