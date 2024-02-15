#SQLAlchemy

from sqlalchemy import create_engine,Column,Integer,String
from sqlalchemy.orm import declarative_base,sessionmaker
db_url="mysql://root:root@127.0.0.1:3306/sqldb"

Eng=create_engine(db_url)##return engine class instance
print(Eng)

Base=declarative_base()##return base class

class Student(Base):
    __tablename__= "student"
    roll=Column(Integer,primary_key=True)
    name=Column(String(34))
    marks=Column(Integer)
    def __str__(self):
        return f"Roll Number:{self.roll}\nName:{self.name}\nMarks{self.marks}"

Base.metadata.create_all(Eng)
print("Table created successfully")

Session=sessionmaker(bind=Eng)
sess=Session()

while True:
    ch=int(input("####MENU####\n1.add record\n2.show record\n3.update recoed\n4.delete record\n5.exit\nEnter your choice:"))

##insert data
    if ch==1:
        l=[]
        n=int(input("how many records you want to add:"))
        for i in range(n):
            r=int(input("Enter roll number:"))
            n=input("Enter name:")
            m=int(input("Enter marks:"))
            ob=Student(roll=r,name=n,marks=m)
            l.append(ob)
            sess.add_all(l)
            print("Data added successfully")

##Retrive Data
    elif ch==2:
        ch=int(input("1.all record retrive\n2.Particular Record Retrive\nEnter your choice"))
        res=sess.query(Student)
        if ch==1:
            for i in res:
               print(i)
        elif ch==2:
            ref_roll=int(input("enter roll number which you want to retrive:"))
            for i in res:
                if ref_roll==i.roll:
                    print(i)

###Update Data
    elif ch==3:
         c=int(input("1.Name\n2.Marks\nEnter your choice:"))
         res=sess.query(Student)
         ref_roll=int(input("Enter roll number which you want to update:"))
         for i in res:
             if ref_roll==i.roll:
                 if c==1:
                     nm=input("Enter new name")
                     sess.query(Student).filter(Student.roll==ref_roll).update({Student.name:nm})
                 elif c==2:
                     marks=int(input("Enter new marks:"))
                     sess.query(Student).filter(Student.roll==ref_roll).update({Student.mark:marks})
         print("Data added successfully")

##Delete Data
    elif ch==4:
        c=int(input("1.Delete All record\n2.Delete particular record\nEnter your choice"))
        res=sess.query(Student)
        if c==1:
              sess.query(Student).delete()
        elif c==2:
            ref_roll=int(input("Enter which roll number you want to delete:"))
            for i in res:
                if ref_roll==i.roll:
                    sess.query(Student).filter(Student.roll==ref_roll).delete()
        print("Data deleted successfully")
            
    sess.commit()
    sess.close()




            
