import cv2
import glob
import os
import face_recognition
import pickle

class EncodeImages:
    def __init__(self):
        self.known_face_encodings = []
        self.known_face_names = []

        # Resize frame for a faster speed
        self.frame_resizing = 0.75

    def load_encoding_images(self, images_path):
        print("path=",images_path)
        """
        Load encoding images from path
        :param images_path:
        :return:
        """
        # Load Images
        images_path = glob.glob(os.path.join(images_path, "*.*"))
        print(images_path)
        print("{} encoding images found.".format(len(images_path)))

        # Store image encoding and names
        for img_path in images_path:
            img = cv2.imread(img_path)
            rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

            # Get the filename only from the initial file path.
            basename = os.path.basename(img_path)
            (filename, ext) = os.path.splitext(basename)
            # Get encoding
            img_encoding = face_recognition.face_encodings(rgb_img)[0]

            # Store file name and file encoding
            self.known_face_encodings.append(img_encoding)
            self.known_face_names.append(filename)
            encodedlist = self.known_face_encodings
            names = self.known_face_names
            encodefile = open('encodings.pkl', 'wb')
            pickle.dump(encodedlist, encodefile)
            encodefile.close()
            namesfile = open('names.pkl', 'wb')
            pickle.dump(names, namesfile)
            namesfile.close()

encode = EncodeImages()
encode.load_encoding_images("images/")
