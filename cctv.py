import cv2
import time
import dropbox
import random 
startTime= time.time()
def take_snapshot():
    number= random.randint(0, 200)
    capture= cv2.VideoCapture(0)
    result= True

    while(result):
       ret, frame= capture.read()
       imgName= "MyPicture" + str(number) + ".jpg"
       cv2.imwrite(imgName, frame)
       startTime= time.time()
       result= False
    return imgName
    capture.release()
    cv2.destroyAllWindows()

def uploadImages(imgName):
    access_token= 'sl.BFtknsHVd6jbEH6IqkmBBXMncXSMXgche2J7dYM0peyLQAWkDXAbyUCxoEu-OwzlB5c6jATvlqOrMoorO1tHXKmvvj_1e6GmW_AwAZwpuyp2ARnUWGcJVibaK9geJ_YigJzIw41VzMbm'
    file= imgName
    file_from= file
    file_to= "/images/" + (imgName) 
    dbx= dropbox.Dropbox(access_token)
    f= open(file_from, 'rb') 
    dbx.files_upload(f.read(), file_to)

def main():
    while (True):
      if (time.time() - startTime) > 5:
          name= take_snapshot()
          uploadImages(name)

main()
   
  