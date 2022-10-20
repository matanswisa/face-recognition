import cv2 as cv
import face_recognition
import os

absolute_path = os.path.dirname(__file__)
path = absolute_path + "/faces/"

def get_faces_images():
    absolute_path = os.path.dirname(__file__)
    return os.listdir(absolute_path + "/faces/")

def get_encoding_images():
    images = get_faces_images()

    encodings = []
    for img in images:
        img_read = cv.imread(path+img)
        rgb_img = cv.cvtColor(img_read, cv.COLOR_BGR2RGB)
        img_encoding = face_recognition.face_encodings(rgb_img)[0]
        encodings.append(img_encoding)
    return encodings
    # face_recognition.    


def start_recognition_stream():
    cap = cv.VideoCapture(0) # 0 means to load the first webcam

    while True:
        ret, frame = cap.read()

        cv.imshow("Frame", frame)

        key = cv.waitKey(1)
        if key == ord('q'):
            break 

    cap.release()
    cv.destroyAllWindows()


length = len(get_encoding_images())
print(length)
# absolute_path = os.path.dirname(__file__)

# print(os.listdir(absolute_path + "/faces/"))
# img = cv.imread("src/faces/Elon Musk.webp")
# rgb_img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# img_encoding = face_recognition.face_encodings(rgb_img)[0]
# cv.imshow("img",img)
# cv.waitKey(0)