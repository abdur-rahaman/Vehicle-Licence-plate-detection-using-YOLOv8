# Vehicle-Licence-plate-detection-using-YOLOv8

Process:
1. create anaconda environment with python 3.9
2. install ultralytics : pip install ultralytics
2. check your python and pytorch version in "terminal" using command:
-python (hit enter)
-import torch (hit enter)
-import.__version__ (enter)
3. go to pytorch website: copy pytorch version depend on your system: for selection: your OS: linux-PIP- Python- CUDA 11.7
[After selecting those you will get a path copy and paste it to your terminal command]
4. check cuda is available or not using ( torch.cuda.is_available)
5. to run and train the data:
[ yolo task=detect mode=train epochs=100 data=data_custom.yaml model=yolov8m.pt imgsz=640 batch=8 ]
6. To test the data:f
[ yolo task=detect mode=predict model=yolov8m_custom.pt show=true conf=0.5 source=test1.jpg ]
