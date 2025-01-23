import os
import shutil
from sklearn.model_selection import train_test_split

# Path for normal and covid images
covid_directory = 'C:\\Users\\georg\\Desktop\\Kaggle datasets\\Covid_xrays_dataset\\COVID-19_Radiography_Dataset\\COVID\\images'
normal_directory = 'C:\\Users\\georg\\Desktop\\Kaggle datasets\\Covid_xrays_dataset\\COVID-19_Radiography_Dataset\\Normal\\images'

# Define your target directories for train, val, and test sets
train_covid_directory = 'C:\\Users\\georg\\Desktop\\Covid_dataset\\Covid train'
val_covid_directory = 'C:\\Users\\georg\\Desktop\\Covid_dataset\\Covid val'
test_covid_directory = 'C:\\Users\\georg\\Desktop\\Covid_dataset\\Covid test'

train_normal_directory = 'C:\\Users\\georg\\Desktop\\normal_dataset\\normal train'
val_normal_directory = 'C:\\Users\\georg\\Desktop\\normal_dataset\\normal val'
test_normal_directory = 'C:\\Users\\georg\\Desktop\\normal_dataset\\normal test'

# Check if directories exist ( if directories does not exist it will create them ).
os.makedirs(train_covid_directory, exist_ok=True)
os.makedirs(val_covid_directory, exist_ok=True)
os.makedirs(test_covid_directory, exist_ok=True)

os.makedirs(train_normal_directory, exist_ok=True)
os.makedirs(val_normal_directory, exist_ok=True)
os.makedirs(test_normal_directory, exist_ok=True)

# Get the list of images in each folder
covid_images = os.listdir(covid_directory)
normal_images = os.listdir(normal_directory)

# Split the images into train, val, and test sets
covid_train, covid_temp = train_test_split(covid_images, test_size=0.2, random_state=42)
covid_val, covid_test = train_test_split(covid_temp, test_size=0.5, random_state=42)

normal_train, normal_temp = train_test_split(normal_images, test_size=0.2, random_state=42)
normal_val, normal_test = train_test_split(normal_temp, test_size=0.5, random_state=42)

# Move the images to the appropriate folders
def move_images(image_list, source_dir, target_dir):
    for image in image_list:
        shutil.move(os.path.join(source_dir, image), os.path.join(target_dir, image))

# Move COVID images to their respective folders
move_images(covid_train, covid_directory, train_covid_directory)
move_images(covid_val, covid_directory, val_covid_directory)
move_images(covid_test, covid_directory, test_covid_directory)

# Move Normal images to their respective folders
move_images(normal_train, normal_directory, train_normal_directory)
move_images(normal_val, normal_directory, val_normal_directory)
move_images(normal_test, normal_directory, test_normal_directory)
