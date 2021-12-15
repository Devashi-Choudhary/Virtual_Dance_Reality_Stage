# Virtual Dance Reality Stage : 
It is a feature which offers you to share a stage with another user virtually. It uses the simple concept of Image  background removal using DeepLab Architecture (semantic image segmentation), which is state-of-art DL model from Google-Brain.
 
# Dependencies :
 - [Keras](https://pypi.org/project/Keras/)
 - [OpenCV](https://pypi.org/project/opencv-python/)
 - [Pytube3](https://pypi.org/project/pytube/)
 - [Tensorflow](https://www.tensorflow.org/install/pip)
 - [Pil](https://pypi.org/project/Pillow/)
 - [numpy](https://pypi.org/project/numpy/)
 

# How to execute the code :

### Please mail me at devashi@gmail.com for main.py file and pretrained model.

1. You will first have to download the repository and then extract the contents into a folder.
2. Make sure you have the correct version of Python installed on your machine. This code runs on Python 3.6 above.
3. Now, install the required dependencies. 
4. Now go to src folder and run extract_data.py to download videos data folder. You can add link for downloading. 
5. The pretrained weights for Image Segmention is inside "xception model folder" and the path you need to change in Background_Removal_In_Videos.py accordingly. 
6. Run Background_Removal_In_Videos.py for Background Removal.
> `python main.py --v1 /Input_data/video1.mp4  --v12/Input_Data/video2.mp4  —s /Input_Data/stage4.png  —o /Output_Data/video.mp4` 
where v1, v2 are input video path , s is background stage image, o is output path for saving final video and in code you need to change the position of images to look them alike while merging(default value is (0, 200) for left image and (700,200) for right image)

If already images are saved in folder(Background Removal) then, you need to call Merge_Video() and Convert_Frames_to_Videos() after specifying folder path.

**Note** : For more information about implementation details, please go through [Virtual Dance Reality Stage using Semantic Segmentation](https://devashi-choudhary.medium.com/virtual-dance-reality-stage-using-semantic-segmentation-66ec44d2c4b).

# Results

[![](http://i3.ytimg.com/vi/64MfAH3kc_c/hqdefault.jpg)](https://www.youtube.com/watch?v=64MfAH3kc_c)

# References :
1. The code is inspired from [here](https://github.com/susheelsk/image-background-removal)
2. Understanding the [deeplab](https://colab.research.google.com/github/tensorflow/models/blob/master/research/deeplab/deeplab_demo.ipynb)
3. The video are publically collected from social media like youtube and instagram.

