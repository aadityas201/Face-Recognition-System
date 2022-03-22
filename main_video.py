from email.message import EmailMessage
import imghdr
import smtplib
import cv2
from simple_facerec import SimpleFacerec
from variable import password
import os
from pir_sensor import triggering
# Encode faces from a folder
sfr = SimpleFacerec()

# Load Camera
cap = cv2.VideoCapture(0)
temp_name="Unknown"
return_value,temp_image=cap.read()
number= len(os.listdir(os.path.join(os.getcwd(),"unknown","")))
x=1
while (triggering()): # triggering to take photos
   
    return_value,temp_image=cap.read()
   

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(temp_image)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(temp_image, name, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(temp_image, (x1, y1), (x2, y2), (0, 0, 200), 4)
        temp_name=name

    cv2.imshow("Frame", temp_image)
    key = cv2.waitKey(1)
    if key == 27:
        break
    path=os.path.join(os.getcwd(),"unknown","")

    

    if(temp_name =="Unknown"):
        cv2.imwrite(os.path.join(path,f"Unknown{number}.png"),temp_image)
        Sender_Email = "yoursecuredhome@gmail.com" 
        Reciever_Email = "prajwal.ahetti@gmail.com"
        Password = "rpnpmrouyqjuordo" 
        newMessage = EmailMessage()
        newMessage['Subject'] = "Tresspasser at your doorstep" 
        newMessage['From'] = Sender_Email                   
        newMessage['To'] = Reciever_Email                   
        newMessage.set_content('Let me know what you think. Image attached!') 
        with open(os.path.join(path,f"Unknown{number}.png"), 'rb') as f:
            image_data = f.read()
            image_type = imghdr.what(f.name)
            image_name = f.name        
        newMessage.add_attachment(image_data, maintype='image', subtype=image_type, filename=image_name)
        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
            smtp.login(Sender_Email,Password)              
            smtp.send_message(newMessage)        
        number=number+1
        for i in range(1000) :
            print("standby")
            
               
        
    
cap.release()
cv2.destroyAllWindows   
        


