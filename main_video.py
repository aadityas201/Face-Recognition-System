from email.message import EmailMessage
import imghdr
import smtplib
import cv2
from simple_facerec import SimpleFacerec
from variable import password

# Encode faces from a folder
sfr = SimpleFacerec()

# Load Camera
cap = cv2.VideoCapture(0)

temp_name = " "
return_value, temp_image=cap.read()
while True:
    ret, frame = cap.read()

    # Detect Faces
    face_locations, face_names = sfr.detect_known_faces(frame)
    
    for face_loc, name in zip(face_locations, face_names):
        temp_name=name
        return_value, temp_image=cap.read()
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv2.putText(frame, name, (x1, y1 - 10),
                    cv2.FONT_HERSHEY_DUPLEX, 1, (0, 0, 200), 2)
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 0, 200), 4)
      
    cv2.imshow("Frame", frame)
    key = cv2.waitKey(1)
    if key == 27:
        break

print(temp_name)
if(temp_name == "Unknown"):
    cv2.imwrite('unknown.png',temp_image)
    sender_email = "aaddiishinde201@gmail.com"
    receiver_email = "prajwal.ahetti@gmail.com"
    password = password
    newMessage = EmailMessage()
    newMessage['Subject'] = "Alert!! Trespassing "
    newMessage['From'] = sender_email
    newMessage['To'] = receiver_email
    newMessage.set_content('We have sent you the image ')
    with open('unknown.png', 'rb') as f:
        image_data = f.read()
        image_type = imghdr.what(f.name)
        image_name = f.name
    newMessage.add_attachment(image_data, maintype = 'image', subtype = image_type, filename = image_name)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email,password)
        smtp.send_message(newMessage)
        print("Sent")
else:
    cv2.imwrite(f"{temp_name}.png", temp_image)
 

    


cap.release()
cv2.destroyAllWindows
