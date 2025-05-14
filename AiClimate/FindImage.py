from teachable_machine import TeachableMachine
import os



path_to_folder = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))),"Basket")
#entries = os.listdir(path_to_folder)
#path_to_image = os.path.join(path_to_folder, entries[0])
#model_path = (r"C:\Users\popko\OneDrive\Documents\GitHub\AiClimate\AiClimate\keras_model.h5")
model_path = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))),"keras_model.h5")
#labels_file_path = (r"C:\Users\popko\OneDrive\Documents\GitHub\AiClimate\AiClimate\labels.txt")
labels_file_path = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "labels.txt")


def empty_basket():
   os.remove(os.path.join(path_to_folder, os.listdir(path_to_folder)[0]))

# Initialise the TeachableMachine
#model = TeachableMachine(model_path=model_path, labels_file_path=labels_file_path)
# Classify the image
#result = model.classify_image(path_to_image)
# Print results
#print("Shape Label:", result['class_index'])
#print("Shape Name:", result['class_name'])
path_to_image = os.path.join(path_to_folder, path_to_folder[0])
print(path_to_image)

def FindImage():
    model = TeachableMachine(model_path=model_path, labels_file_path=labels_file_path)
    print(path_to_folder[0])
    path_to_image = os.path.join(path_to_folder, os.listdir(path_to_folder)[0])
    result = model.classify_image(path_to_image)
    empty_basket()
    return result['class_name']