"""Project Description:         This module contains functions that can be easily utilized in jupyter notebooks    for the use of cloud classification.     Created on 4/11/23 @author Corey Walkercontact:         cdw0063@uah.edu    Note:         Please site this module if the functions are used in another analysis and     published.     """#imports import cv2import osimport randomimport shutil#enter the appropriate filepaths here:swirlldata = '../Tensorflow/workspace/swirll_demo/images'#if the above filepath does not exist, you need to download the data and from the #readme on the github swirll-cam-classifier README.md page and use the sortfiles#for root, directory, files in os.walk(swirlldata):    for f in files:        if f.endswith('.xml'):            print(f)    