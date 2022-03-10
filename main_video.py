import cv2
from simple_facerec import SimpleFacerec
import os
import smtplib
import imghdr
from email.message import EmailMessage
# Encode faces from a folder
sfr = SimpleFacerec()
sfr.load_encoding_images("images/")
# Load Camera
cap = cv2.VideoCapture(0)
temp_name="Unknown"
return_value,temp_image=cap.read()
number= len(os.listdir(os.path.join(os.getcwd(),"unknown","")))
x=1
while (x!=0 or x!=1): # triggering to take photos
    x=int(input(print("Standby-> 0     Capture Frames-> 1")))
    if(x==1):
        ret, frame = cap.read()

        # Detect Faces
        face_locations, face_names = sfr.detect_known_faces(frame)
        for face_loc, name in zip(face_locations, face_names):
            
            y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
            cv2.putText(frame, name, (x1, y1 - 10),
                        cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
            temp_name=name
            return_value,temp_image=cap.read()
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1)
        if key == 27:
            break
        
        
        path=os.path.join(os.getcwd(),"unknown","")

        
    
        if(temp_name =="Unknown"):
            cv2.imwrite(os.path.join(path,f"Unknown{number}.png"),temp_image)
            Sender_Email = "" 
            Reciever_Email = ""
            Password = "" #type your password here
            newMessage = EmailMessage()
            newMessage['Subject'] = "Alert Theft inside your home" 
            newMessage['From'] = Sender_Email                   
            newMessage['To'] = Reciever_Email                   
            newMessage.set_content('Let me know what you think. Image attached!') 
            with open(os.path.join(path,f"Unknown{number}.png"), 'rb') as f:
                image_data = f.read()
                image_type = imghdr.what(f.name)
                image_name = f.name        
            newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(Sender_Email, Password)              
                smtp.send_message(newMessage)        
            number=number+1   
        x=0
    elif(x==0):
        print("On Standby")
cap.release()
cv2.destroyAllWindows   
        


