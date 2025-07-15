## Use labelme to label and crop

### Install labelme
```bash
pip install labelme opencv-python numpy
```
Run labelme
```bash
labelme
```
In case of this error: ImportError: DLL load failed while importing onnxruntime_pybind11_state: A dynamic link library (DLL) initialization routine failed.
, do
```bash
pip install onnxruntime==1.19.0
```
See: https://github.com/wkentaro/labelme/issues/1564

### Use labelme to create masks annotations
Images and annotations like:
```bash
/source_images/
  ├── image1.bmp
  ├── image1.json
  ├── image2.bmp
  ├── image2.json
```

### Crop the masked area
```bash
python crop.py
```