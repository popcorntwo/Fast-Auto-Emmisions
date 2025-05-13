from teachable_machine import TeachableMachine

model_path = input("Enter the path to your model (.h5) file: ")
labels_file_path = input("Enter the path to your labels file: ")
image_path = input("Enter the path to the image you want to classify: ")

# Initialise the TeachableMachine
model = TeachableMachine(model_path=model_path, labels_file_path=labels_file_path)

# Classify the image
result = model.classify_image(image_path)

# Print results
print("Shape Label:", result['class_index'])
print("Shape Name:", result['class_name'])