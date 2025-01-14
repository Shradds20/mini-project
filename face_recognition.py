from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector
from time import strftime
from datetime import datetime
import cv2
import os
import numpy as np



class Face_Recognition:
    def __init__(self,root):
        self.root=root    
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")

        title_lbl=Label(self.root,text="FACE RECOGNITION",font=("times new roman",35,"bold"),bg="black",fg="blue")
        title_lbl.place(x=0,y=0,width=1530,height=45)


        img_left=Image.open(r"college images\traindata2.jpeg")
         
        
        img_left=img_left.resize((650,700), Image.LANCZOS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(self.root,image=self.photoimg_left)
        f_lbl.place(x=0,y=55,width=650,height=700)


        img_right=Image.open(r"college images\detectimage.png")
        
        img_right=img_right.resize((950,700), Image.LANCZOS) 
        self.photoimg_right=ImageTk.PhotoImage(img_right)

        f_lbl=Label(self.root,image=self.photoimg_right)
        f_lbl.place(x=650,y=55,width=950,height=700)
        


        b1_1=Button(f_lbl,text="FACE RECOGNITION",cursor="hand2",font=("times new roman",18,"bold"),bg="darkgreen",fg="white",command=self.face_recog)
        b1_1.place(x=365,y=620,width=250,height=40)


    def mark_attendance(self,i,r,n,d):
        with open("shraddha.csv","r+",newline="\n") as f:
            myDataList=f.readline()
            name_list=[]
            for line in myDataList:
                entry=line.split((","))
                name_list.append(entry[0])
            if((i not in name_list) and (r not in name_list)and (n not in name_list)and (d not in name_list) ):
                now=datetime.now()
                d1=now.strftime("%d/%m/%Y")
                dtString=now.strftime("%H:%M:%S")
                f.writelines(f"\n{i},{r},{n},{d},{dtString},{d1},Present")

# //--------------FACE RECOGNITION----=-------------
    def face_recog(self): 
        def draw_boundary(img,classifier,scaleFactor,minNeighbors,color,text,clf):
            gray_image=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY,320,240)
            features=classifier.detectMultiScale(gray_image,scaleFactor,minNeighbors)

            coord=[]
         
            for (x,y,w,h) in features:
                cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),3)
                id,predict=clf.predict(gray_image[y:y+h,x:x+w])
                confidence=int((100*(1-predict/300)))
        
               
                conn=mysql.connector.connect(host="localhost",username="root",password="Shree@2095",database="facerecognizer")
                my_cursor=conn.cursor()

                my_cursor.execute("Select Name from student where Student_id="+str(id))
                n=my_cursor.fetchone()
                n="+".join(n)

                my_cursor.execute("Select Roll from student where Student_id="+str(id))
                r=my_cursor.fetchone()
                r="+".join(r)

                my_cursor.execute("Select Dep from student where Student_id="+str(id))
                d=my_cursor.fetchone()
                d="+".join(d)

                my_cursor.execute("Select Student_id from student where Student_id="+str(id))
                i=my_cursor.fetchone()
                i="+".join(i)




                if confidence>60:
                    cv2.putText(img,f"ID:{i}",(x,y-75),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Roll:{r}",(x,y-55),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Name:{n}",(x,y-30),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    cv2.putText(img,f"Department:{d}",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)
                    self.mark_attendance(i,r,n,d)
                else: 
                    cv2.rectangle(img,(x,y),(x+w,y+h),(0,0,255),3)
                    cv2.putText(img,"Unknown Face",(x,y-5),cv2.FONT_HERSHEY_COMPLEX,0.8,(255,255,255),3)

                coord=[x,y,w,h]

            return coord

        def recognize(img,clf,faceCascade):
            coord=draw_boundary(img,faceCascade,1.1,10,(255,25,255),"FACE",clf)
            return img 

        faceCascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf=cv2.face.LBPHFaceRecognizer_create()
        clf.read("classifier.xml")
        

        video_cap=cv2.VideoCapture(0)

        frame_count = 0
        while True:
            ret,img=video_cap.read()
            frame_count += 1
            if frame_count % 2 == 0:
               img=cv2.resize(img,(640,480))
               img=recognize(img,clf,faceCascade)
               cv2.imshow("Welcome to face recognition",img)

            if cv2.waitKey(1)==13:
                break
        
        video_cap.release()
        cv2.destroyAllWindows()
    


if __name__ == "__main__":
    root=Tk()
    obj=Face_Recognition(root)
    root.mainloop()         