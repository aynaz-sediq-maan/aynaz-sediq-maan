import tkinter as tk
from tkinter import messagebox


def Calculate_share():
    try:
        total_bil = float(ent_TotalBill.get())
        num_people = int(ent_NumberOfPeople.get())

        if total_bil <+ 0:
            messagebox.showerror("Error","price has not lower than 0!")
            return
        
        if num_people <= 0:
            messagebox.showerror("Error","Cant num of people lower than 1!")
            return
        
        Dong=total_bil/num_people

        Lbl_Dong.config(text=f"the price for one people: {Dong:.2f}")
    except ValueError:
        messagebox.showerror("Error","please enter a number!")
    except ZeroDivisionError:
        messagebox.showerror("Error","the num of people grater than 0!")
    except Exception as e:
        messagebox.showerror("Error",f"the undefind error: {e}")




root=tk.Tk()
root.title('Dong-Calculate')
root.geometry('500x300')
root.configure(bg='aqua',)


label_TotalBill=tk.Label(root,text='enter TotalBill: ',bg='pink',fg='#cc9900')
label_TotalBill.grid(row=0 , padx=30 , pady=15 , column=0)

ent_TotalBill = tk.Entry(root)
ent_TotalBill.grid(row=0 , padx=5 , pady=15 , column=1 ) 



label_NumberOfPeople=tk.Label(root,text='enter Num of people: ',bg='pink',fg='#cc9900')
label_NumberOfPeople.grid(row=1 , padx=30 , pady=7 , column=0 )

ent_NumberOfPeople = tk.Entry(root)
ent_NumberOfPeople.grid(row=1 , padx=5 , pady=7 , column=1 )


btn_Calculate = tk.Button(root,text='Calculate',bg='pink',fg='#cc9900',command=Calculate_share)
btn_Calculate.grid(row=2 , column=1 , columnspan=3 , pady=20 )



Lbl_Dong= tk.Label(root, text="",font=('Arial', 14, 'bold'),fg='#cc9900',bg='pink')
Lbl_Dong.grid(row=3 , column=1,columnspan=3 , pady=30)

root.mainloop()