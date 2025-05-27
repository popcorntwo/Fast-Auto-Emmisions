from teachable_machine import TeachableMachine
import os



path_to_folder = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))),"Basket")
model_path = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))),"keras_model.h5")
labels_file_path = os.path.join(os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__))), "labels.txt")

def empty_basket():
   os.remove(os.path.join(path_to_folder, os.listdir(path_to_folder)[0]))

def find_image():
    model = TeachableMachine(model_path=model_path, labels_file_path=labels_file_path)
    result = model.classify_image(os.path.join(path_to_folder,os.listdir(path_to_folder)[0]))
    empty_basket()
    return result['class_name']