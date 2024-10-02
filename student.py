from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk


class Student:
    def __init__(self,root):
        self.root=root    
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition System")



        img=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\sies.jpg")
        width, height=1530, 790
        img=img.resize((1530,790), Image.LANCZOS) 
        self.photoimg=ImageTk.PhotoImage(img)

        bg_img=Label(self.root,image=self.photoimg)
        bg_img.place(x=0,y=0,width=1530,height=790)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",35,"bold"),bg="black",fg="white")
        title_lbl.place(x=0,y=0,width=1530,height=45)



        main_frame=Frame(bg_img,bd=2,bg="white")
        main_frame.place(x=20,y=130,width=1480,height=600)


        #left label frame
        Left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Left_frame.place(x=10,y=10,width=760,height=580)

        img_left=Image.open(r"C:\Users\Hp\Desktop\facerec2\college images\students-in-classroom.jpg")
        width, height=740, 130
        img_left=img_left.resize((740,130), Image.LANCZOS) 
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        bg_img=Label(Left_frame,image=self.photoimg_left)
        bg_img.place(x=5,y=0,width=740,height=130)

        #current course information frame
        current_course_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        current_course_frame.place(x=5,y=135,width=740,height=115)

        # department
        dep_label=Label(current_course_frame, text="Department",font=("times new roman",13,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10,sticky=W)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        dep_combo["values"]=("Select Department","Computer","IT","Civil","Mechnical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)


        # course
        course_label=Label(current_course_frame, text="Course",font=("times new roman",13,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)


        #year
        year_label=Label(current_course_frame, text="Course",font=("times new roman",13,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        year_combo["values"]=("Select Year","2023-24","2024-25","2025-26","2026-27")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)


        #sem
        semester_label=Label(current_course_frame, text="Course",font=("times new roman",13,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",13,"bold"),state="readonly",width=20)
        semester_combo["values"]=("Select Semester","sem-1","sem-2")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)


        #class student information frame
        class_student_frame=LabelFrame(Left_frame,bd=2,bg="white",relief=RIDGE,text="current course information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=5,y=250,width=740,height=300)

        # student id
        student_id_label=Label(class_student_frame, text="Student_ID:",font=("times new roman",13,"bold"),bg="white")
        student_id_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        student_id_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        student_id_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        # student name
        student_name_label=Label(class_student_frame, text="Student Name:",font=("times new roman",13,"bold"),bg="white")
        student_name_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        student_name_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        student_name_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        # class division 
        class_div_label=Label(class_student_frame, text="Class Divison:",font=("times new roman",13,"bold"),bg="white")
        class_div_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        class_div_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        class_div_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        # Roll no
        roll_no_label=Label(class_student_frame, text="Roll_No:",font=("times new roman",13,"bold"),bg="white")
        roll_no_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        roll_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        roll_no_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        # gender
        gender_label=Label(class_student_frame, text="Gender:",font=("times new roman",13,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        gender_entry.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        # email
        email_label=Label(class_student_frame, text="Email:",font=("times new roman",13,"bold"),bg="white")
        email_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        email_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        email_entry.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        # phone no
        phone_no_label=Label(class_student_frame, text="Phone_NO:",font=("times new roman",13,"bold"),bg="white")
        phone_no_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        phone_no_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        phone_no_entry.grid(row=3,column=1,padx=10,pady=5,sticky=W)


        # radio Buttons
        radionbtn1=ttk.Radiobutton(class_student_frame,text="Take Photo Sample",value="Yes")
        radionbtn1.grid(row=6,column=0)

        radionbtn2=ttk.Radiobutton (class_student_frame,text="No Photo Sample",value="Yes") 
        radionbtn2.grid(row=6,column=1)

        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE,bg="white")
        btn_frame.place(x=0,y=200,width=715,height=70)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white") 
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=2)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=3)
        






















        





        


        










        #Right label frame
        Right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        Right_frame.place(x=800,y=10,width=660,height=580)


















if __name__ == "__main__":
    root=Tk()
    obj=Student(root)
    root.mainloop() 