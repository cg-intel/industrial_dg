import os
import glob
import subprocess
import cv2
import numpy as np

image_dir = './source_images'
output_dir = './cropped_images'
os.makedirs(output_dir, exist_ok=True)

json_files = glob.glob(os.path.join(image_dir, '*.json'))

for json_file in json_files:
    base = os.path.splitext(os.path.basename(json_file))[0]
    print(f"Processing: {base}")

    dataset_dir = os.path.join(image_dir, base + '_json')
    if not os.path.exists(dataset_dir):
        subprocess.run(['labelme_json_to_dataset', json_file])

    img_path = os.path.join(dataset_dir, 'img.png')
    mask_path = os.path.join(dataset_dir, 'label.png')

    img = cv2.imread(img_path)
    mask = cv2.imread(mask_path, cv2.IMREAD_GRAYSCALE)

    unique_vals = np.unique(mask)

    foreground_val = [v for v in unique_vals if v != 0][0]
    mask_bool = (mask == foreground_val)
    foreground_mask = mask_bool.astype(np.uint8) * 255

    result = cv2.bitwise_and(img, img, mask=foreground_mask)

    ys, xs = np.where(foreground_mask > 0)
    if len(xs) > 0 and len(ys) > 0:
        x_min, x_max = xs.min(), xs.max()
        y_min, y_max = ys.min(), ys.max()
        cropped = result[y_min:y_max+1, x_min:x_max+1]
        cv2.imwrite(os.path.join(output_dir, f'{base}_cropped.png'), cropped)
