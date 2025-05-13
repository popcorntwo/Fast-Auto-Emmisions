from teachable_machine import TeachableMachine
import os

path_to_folder = r"C:\Users\popko\OneDrive\Documents\GitHub\AiClimate\AiClimate\Basket"
#entries = os.listdir(path_to_folder)
#path_to_image = os.path.join(path_to_folder, entries[0])
model_path = (r"C:\Users\popko\OneDrive\Documents\GitHub\AiClimate\AiClimate\keras_model.h5")
labels_file_path = (r"C:\Users\popko\OneDrive\Documents\GitHub\AiClimate\AiClimate\labels.txt")


# Initialise the TeachableMachine
#model = TeachableMachine(model_path=model_path, labels_file_path=labels_file_path)
# Classify the image
#result = model.classify_image(path_to_image)
# Print results
#print("Shape Label:", result['class_index'])
#print("Shape Name:", result['class_name'])

def FindImage():
    model = TeachableMachine(model_path=model_path, labels_file_path=labels_file_path)
    entries = os.listdir(path_to_folder)
    path_to_image = os.path.join(path_to_folder, entries[0])
    result = model.classify_image(path_to_image)
    return result['class_name']