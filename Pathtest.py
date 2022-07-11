import os


input_folder = 'samples'
output_folder = 'results'

for img in os.listdir(input_folder):
    img_path = os.path.join(input_folder, img)
    print(img_path)
    folder_path = output_folder + os.sep + img
    # print(folder_path)
