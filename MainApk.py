import tkinter as tk
import pandas as pd
from tkinter import messagebox, filedialog, ttk
from PIL import Image, ImageTk
from datetime import datetime
import re
import csv
import shutil

class LoginPage(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame

        self.image_bg = Image.open('bg_login.png')
        self.image_bg = self.image_bg.resize((1550, 790))
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.image_login = Image.open("b_login.png")
        self.image_login = self.image_login.resize((100, 50))
        self.image_login = ImageTk.PhotoImage(self.image_login)
        
        self.image_signup = Image.open("b_signup.png")
        self.image_signup = self.image_signup.resize((100, 50))
        self.image_signup = ImageTk.PhotoImage(self.image_signup)

        self.label_judul = tk.Label(self, text="LOGIN", bg='#3B3B3B',font=('Verdana', 30, 'bold'))
        self.label_username = tk.Label(self, text="Username:", bg='#3B3B3B',font=('Verdana', 14, 'bold'))
        self.label_password = tk.Label(self, text="Password:", bg='#3B3B3B',font=('Verdana', 14, 'bold'))
        self.label_status = tk.Label(self, text="Status:", bg='#3B3B3B',font=('Verdana', 14, 'bold'))
        self.entry_username = tk.Entry(self, bg='#ffffff',font=('Arial', 11, 'bold'))
        self.entry_password = tk.Entry(self, show="*",bg='#ffffff',font=('Arial', 11, 'bold'))
        self.selected_status = tk.StringVar()
        self.radio_admin = tk.Radiobutton(self, text="Admin", value="Admin", bg='#FE6413', activebackground='#3B3B3B', variable=self.selected_status)
        self.radio_user = tk.Radiobutton(self, text="User", value="User", bg='#FE6413',  activebackground='#3B3B3B', variable=self.selected_status)
        self.label_kosong = tk.Label(self, bg='#3B3B3B')

        self.button_login = tk.Button(self, text="Login",image=self.image_login,bg='#3B3B3B', bd=0, relief="flat", activebackground='#3B3B3B',command=self.cek_login)
        self.button_signup = tk.Button(self, text="Sign Up",image=self.image_signup,bg='#3B3B3B', bd=0, relief="flat", activebackground='#3B3B3B', command=self.switch_to_signup)

        self.label_judul.grid(row=1,column=1, columnspan=3)
        self.label_username.grid(row=2, column=1, pady=40)
        self.label_password.grid(row=3, column=1, pady=40)
        self.label_status.grid(row=4, column=1, pady= 40)
        self.entry_username.grid(row=2, column=2, columnspan=2, pady=40)
        self.entry_password.grid(row=3, column=2, columnspan=2, pady=40)
        self.radio_admin.grid(row=4, column=3 )
        self.radio_user.grid(row=4, column= 2, sticky="w")
        self.button_login.grid(row=5, column=2, pady=10, columnspan=2)
        self.button_signup.grid(row=6, column=2, pady=20, columnspan=2)
        self.label_kosong.grid(row=0,column=0, padx=500, pady=80)

    def cek_login(self):
        global username_input
        path_file_csv = 'rental.csv'
        username_input = self.entry_username.get()
        password_input = self.entry_password.get()
        status_input = self.selected_status.get()

        with open(path_file_csv, 'r') as file:
            csv_reader = csv.reader(file)
            header = next(csv_reader)
            username_index = header.index('username')
            password_index = header.index('password')
            status_index = header.index('status')
            try:
                for row in csv_reader:
                    username_valid, password_valid, status_valid = row[username_index], row[password_index], row[status_index]
                    if username_input == username_valid and password_input == password_valid and status_input == status_valid:
                        if status_valid == 'User':
                            messagebox.showinfo("Login Sukses", "Selamat datang, " + username_input + "!"+ '\nSebagai '+ status_valid)
                            self.switch_frame(MainMenu_User)
                        else:
                            messagebox.showinfo("Login Sukses", "Selamat datang, " + username_input + "!" + '\nSebagai '+ status_valid)
                            self.switch_frame(MainMenu_Admin)     
                        return     
            except Exception as e:
                messagebox.showerror("Error", "Terjadi kesalahan: " + str(e))
            messagebox.showerror("Login Gagal", "Username atau password salah. Silakan coba lagi.")

    def switch_to_signup(self):
        self.switch_frame(SignupPage)

class SignupPage(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame

        self.image_bg = Image.open('bg_sign_up.png')
        self.image_bg = self.image_bg.resize((1550, 790))
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.image_login = Image.open("b_back.png")
        self.image_login = self.image_login.resize((100, 50))
        self.image_login = ImageTk.PhotoImage(self.image_login)
        
        self.image_signup = Image.open("b_sign_up.png")
        self.image_signup = self.image_signup.resize((100, 50))
        self.image_signup = ImageTk.PhotoImage(self.image_signup)
        
        self.label_judul = tk.Label(self, text="SIGN-UP", bg='#3B3B3B',font=('Verdana', 30, 'bold'))
        self.label_new_username = tk.Label(self, text="New Username:",bg='#3B3B3B',font=('Verdana', 14, 'bold'))
        self.label_new_username = tk.Label(self, text="New Username:",bg='#3B3B3B',font=('Verdana', 14, 'bold'))
        self.label_new_password = tk.Label(self, text="New Password:",bg='#3B3B3B',font=('Verdana', 14, 'bold'))
        self.label_photoKTP = tk.Label(self, text="Photo KTP:",bg='#3B3B3B', font=('Verdana', 14, 'bold'))
        self.label_key_info = tk.Label(self, text="*Masukkan key untuk admin\nKosongkan jika anda ingin menjadi admin",bg='#3B3B3B')
        self.label_key = tk.Label(self, text="Key:",bg='#3B3B3B',font=('Verdana', 14, 'bold'))
        self.entry_new_username = tk.Entry(self,font=('Arial', 11, 'bold'))
        self.entry_new_password = tk.Entry(self, show="*", font=('Arial', 11, 'bold'))
        self.entry_key = tk.Entry(self, font=('Verdana', 11, 'bold'))
        self.button_browse = tk.Button(self, text="Browse Image", command=self.choose_image)
        self.label_image_path = tk.Label(self, text="", bg='#3B3B3B',font=('Arial', 11, 'bold'))
        self.button_daftar= tk.Button(self, image=self.image_signup, bg='#3B3B3B', bd=0, relief="flat", activebackground='#3B3B3B', command=self.daftar_user)
        self.button_back = tk.Button(self, image=self.image_login, bg='#3B3B3B', bd=0, relief="flat", activebackground='#3B3B3B', command=self.switch_to_login)
        self.label_kosong= tk.Label(self, bg='#3B3B3B')
        
        self.label_judul.grid(row=1,column=1)
        self.label_new_username.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.label_new_password.grid(row=3, column=0, padx=10, pady=10, sticky="e")
        self.entry_new_username.grid(row=2, column=1, padx=10, pady=10)
        self.entry_new_password.grid(row=3, column=1, padx=10, pady=10)
        self.label_photoKTP.grid(row=6, column=0,  padx=10, pady=10, sticky="e")
        self.button_browse.grid(row=7, column=1, pady=10)
        self.label_key.grid(row=4, column=0,padx=10, pady=10, sticky="e")
        self.label_key_info.grid(row=5, column=1, columnspan=3)
        self.entry_key.grid(row=4,column=1)
        self.label_image_path.grid(row=6, column=1, columnspan=3, pady=10)
        self.button_daftar.grid(row=8, column=1, pady=10)
        self.button_back.grid(row=9, column=1, pady=10)
        self.label_kosong.grid(row=0,column=0, padx=500, pady=100)

    def choose_image(self):
        file_path = filedialog.askopenfilename(title="Choose an image", filetypes=[("Image files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            file_name = file_path.split("/")[-1]
            
            destination_folder = "Photo KTP"
            destination_path = f"{destination_folder}/{file_name}"
            
            shutil.copy(file_path, destination_path)
            self.label_image_path.config(text="Image selected: " + file_path,  bg='#3B3B3B')
        else: self.label_image_path.config(text="No image selected")

    def daftar_user(self):
        path_file_csv = 'rental.csv'
        key_admin = '230604'
        new_username_input = self.entry_new_username.get()
        new_password_input = self.entry_new_password.get()
        key = self.entry_key.get()
        status=''
        if key==key_admin and new_username_input != '' and new_password_input != '': 
            status='Admin'
            with open(path_file_csv, 'a', newline='') as file:
                csv_writer = csv.writer(file)
                csv_writer.writerow([new_username_input, new_password_input, status,0,0,0,0,0,0,0,0,0,0,0])
            messagebox.showinfo("Sukses Akun berhasil ditambahkan!\nSebagai "+status )
        elif key == '' and new_username_input != '' and new_password_input != '': 
            status='User'
            with open(path_file_csv, 'a', newline='') as file:
                csv_writer = csv.writer(file)

                csv_writer.writerow([new_username_input, new_password_input, status])
            messagebox.showinfo("Sukses", "Akun berhasil ditambahkan!\nSebagai "+status )
        else: messagebox.showerror('Gagal Daftar','Terjadi kesalahan pada username, password, atau key yang di input\nSilahkan coba lagi!')

    def switch_to_login(self):
        self.switch_frame(LoginPage)

class MainMenu_User(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        global label_waktu
        self.master = master
        self.switch_frame = switch_frame

        self.image_bg = Image.open('bg_menu.png')
        self.image_bg = self.image_bg.resize((1550, 790))
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.image_motor = Image.open("b_motor.png")
        self.image_motor = self.image_motor.resize((300, 180))
        self.image_motor = ImageTk.PhotoImage(self.image_motor)

        self.image_mobil = Image.open("b_mobil.png")
        self.image_mobil = self.image_mobil.resize((300, 180))
        self.image_mobil = ImageTk.PhotoImage(self.image_mobil)

        self.image_sepeda = Image.open("b_sepeda.png")
        self.image_sepeda = self.image_sepeda.resize((300, 180))
        self.image_sepeda = ImageTk.PhotoImage(self.image_sepeda)

        self.image_payment = Image.open("b_payment.png")
        self.image_payment = self.image_payment.resize((300, 180))
        self.image_payment = ImageTk.PhotoImage(self.image_payment)

        self.image_review = Image.open("b_review.png")
        self.image_review = self.image_review.resize((300, 180))
        self.image_review = ImageTk.PhotoImage(self.image_review)

        self.image_login = Image.open("b_back.png")
        self.image_login = self.image_login.resize((300, 180))
        self.image_login = ImageTk.PhotoImage(self.image_login)

        

        #self.label_ket_waktu = tk.Label(self, text="TIME:", bg='#232526',fg='#ffffff',font=('Verdana', 12, 'bold'))
        self.label_judul = tk.Label(self, text="WELLCOME "+username_input, bg='#232526',font=('Verdana', 30, 'bold'))
        label_waktu = tk.Label(self, font=('calibri', 14, 'bold'), foreground='black', bg='#232526', fg='#ffffff')
        self.button_motor = tk.Button(self,image=self.image_motor,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.motor)
        self.button_mobil = tk.Button(self,image=self.image_mobil,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.mobil)
        self.button_sepeda = tk.Button(self,image=self.image_sepeda,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.sepeda)
        self.button_payment = tk.Button(self,image=self.image_payment,bg='#232526', bd=0, relief="flat", activebackground='#232526')
        self.button_review = tk.Button(self,image=self.image_review,bg='#232526', bd=0, relief="flat", activebackground='#232526')
        self.button_login = tk.Button(self,image=self.image_login,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.switch_to_login)
        self.label_kosong= tk.Label(self, bg='#172627')
        self.label_kosong2= tk.Label(self, bg='#172627')


        self.label_judul.grid(row=1, column=2, columnspan=3, pady=35, padx=50)
        #self.label_ket_waktu.grid(row=0, column=5, sticky='w', padx=125)
        label_waktu.grid(row=0, column=4, columnspan=2, pady=40, sticky='e')
        update_waktu()
        self.button_motor.grid(row=2, column=2, padx=15, pady=20)
        self.button_mobil.grid(row=2, column=3, padx=15, pady=20)
        self.button_sepeda.grid(row=2, column=4, padx=15, pady=20)
        self.button_payment.grid(row=3, column=2, padx=15, pady=20)
        self.button_review.grid(row=3, column=3, padx=15, pady=20)
        self.button_login.grid(row=3, column=4)
        self.label_kosong.grid(row=0,column=0, rowspan=9, padx=137, pady=50, sticky='s')
        self.label_kosong2.grid(row=0,column=5, rowspan=9, padx=120, pady=50, sticky='s')

    def switch_to_login(self):
        self.switch_frame(LoginPage)

    def motor(self):
        self.switch_frame(RentalMotor)

    def mobil(self):
        self.switch_frame(RentalMobil)

    def sepeda(self):
        self.switch_frame(RentalSepeda)

    # def pay(self):self.switch_frame(PembayaranRental)
        
class MainMenu_Admin(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        global label_waktu
        self.master = master
        self.switch_frame = switch_frame

        self.image_bg = Image.open('bg_menu.png')
        self.image_bg = self.image_bg.resize((1550, 790))
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.image_data_user = Image.open("b_data_user.png")
        self.image_data_user = self.image_data_user.resize((300, 180))
        self.image_data_user = ImageTk.PhotoImage(self.image_data_user)

        self.image_stock = Image.open("b_stock.png")
        self.image_stock = self.image_stock.resize((300, 180))
        self.image_stock = ImageTk.PhotoImage(self.image_stock)

        self.image_login = Image.open("b_back.png")
        self.image_login = self.image_login.resize((300, 180))
        self.image_login = ImageTk.PhotoImage(self.image_login)

        self.label_judul = tk.Label(self, text="WELLCOME "+username_input, bg='#232526', fg='#ffffff',font=('Verdana', 30, 'bold'))
        #self.label_ket_waktu = tk.Label(self, text="TIME:", bg='#232526',fg='#ffffff',font=('Verdana', 12, 'bold'))
        label_waktu = tk.Label(self, font=('calibri', 14, 'bold'), foreground='black', bg='#232526', fg='#ffffff')
        self.button_data_user = tk.Button(self,image=self.image_data_user,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.switch_to_Datauser)
        self.button_stock = tk.Button(self,image=self.image_stock,bg='#232526', bd=0, relief="flat", activebackground='#232526',  command=self.switch_to_stock)
        self.button_login = tk.Button(self,image=self.image_login,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.switch_to_login)
        self.label_kosong= tk.Label(self, bg='#3C2E19')
        self.label_kosong2= tk.Label(self, bg='#3C2E19')
        
        self.label_judul.grid(row=1, column=2, columnspan=3, pady=85, padx=50, sticky='n')
        #self.label_ket_waktu.grid(row=0, column=5, sticky='w', padx=125)
        label_waktu.grid(row=0, column=4, columnspan=2, pady=40, sticky='e')
        update_waktu()
        self.button_data_user.grid(row=2, column=2, padx=10, pady=45)
        self.button_stock.grid(row=2, column=3, padx=10, pady=10)
        self.button_login.grid(row=2, column=4, padx=10, pady=10)
        self.label_kosong.grid(row=0,column=0, rowspan=9, padx=137, pady=75, sticky='s')
        self.label_kosong2.grid(row=0,column=5, rowspan=9, padx=120, pady=50, sticky='s')

    def switch_to_login(self):
            self.switch_frame(LoginPage)
    
    def switch_to_Datauser(self):
            self.switch_frame(DataUser)

    def switch_to_stock(self):
            self.switch_frame(Stockopname)

class DataUser(tk.Frame):
    def __init__(self,  master, switch_frame):
        tk.Frame.__init__(self, master)
        global label_waktu
        self.master = master
        self.switch_frame = switch_frame

        self.image_bg = Image.open('bg_datauser.png')
        self.image_bg = self.image_bg.resize((1550, 790))
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.image_motor = Image.open("b_motor.png")
        self.image_motor = self.image_motor.resize((300, 180))
        self.image_motor = ImageTk.PhotoImage(self.image_motor)

        self.image_mobil = Image.open("b_mobil.png")
        self.image_mobil = self.image_mobil.resize((300, 180))
        self.image_mobil = ImageTk.PhotoImage(self.image_mobil)

        self.image_sepeda = Image.open("b_sepeda.png")
        self.image_sepeda = self.image_sepeda.resize((300, 180))
        self.image_sepeda = ImageTk.PhotoImage(self.image_sepeda)

        self.image_login = Image.open("b_back.png")
        self.image_login = self.image_login.resize((300, 180))
        self.image_login = ImageTk.PhotoImage(self.image_login)

        label_waktu = tk.Label(self, font=('calibri', 14, 'bold'), foreground='black', bg='#232526', fg='#ffffff', anchor='w')
        self.label_judul = tk.Label(self, text='Data User Yang Ingin Dicari Berdasarkan:', bg='#232526', fg='#ffffff',font=('Verdana', 30, 'bold'))
        self.button_motor = tk.Button(self,image=self.image_motor,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.show_popup_motor)
        self.button_mobil = tk.Button(self,image=self.image_mobil,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.show_popup_mobil)
        self.button_login = tk.Button(self,image=self.image_login,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.switch_to_MenuAdmin)
        self.button_sepeda = tk.Button(self,image=self.image_sepeda,bg='#232526', bd=0, relief="flat", activebackground='#232526', command=self.show_popup_sepeda)
        self.label_kosong= tk.Label(self, bg='#3C2E19')
        self.label_kosong2= tk.Label(self, bg='#3C2E19')

        label_waktu.grid(row=0, column=4, columnspan=2, pady=35, sticky='e')
        update_waktu()
        self.label_judul.grid(row=1, column=2, columnspan=3, pady=55, padx=50, sticky='n')
        self.button_motor.grid(row=2, column=2, padx=15, pady=45)
        self.button_mobil.grid(row=2, column=3, padx=15, pady=45)
        self.button_sepeda.grid(row=2, column=4, padx=15, pady=55)
        self.button_login.grid(row=3, column=3, padx=15, pady=5)
        self.label_kosong.grid(row=0,column=0, rowspan=9, padx=135, sticky='s')
        self.label_kosong2.grid(row=0,column=5, rowspan=9, padx=95, sticky='s')
    
    def show_popup_motor(self):
        pop_up_motor = tk.Toplevel(self)
        pop_up_motor.title('Data User Penyewa Motor')
        csv_data=pd.read_csv('rental.csv')
        csv_data = csv_data[csv_data['status'] == 'User']

        filtered_columns = csv_data.filter(regex=re.compile(r'motor'))
        filtered_columns.insert(0, 'username', csv_data['username'])
        filtered_columns['start'] = csv_data['start']
        filtered_columns['end'] = csv_data['end']
        filtered_columns['pay'] = csv_data['pay']

        self.tree = ttk.Treeview(pop_up_motor)
        self.tree["columns"] = list(filtered_columns.columns)
        
        for col in filtered_columns.columns:
            self.tree.column(col, anchor="w", width=100, stretch=tk.NO)
            self.tree.heading(col, text=col, anchor="w")

        for index, row in filtered_columns.iterrows():
            self.tree.insert("", 0, values=list(row))
        self.tree.pack()
    
    def show_popup_mobil(self):
        pop_up_motor = tk.Toplevel(self)
        pop_up_motor.title('Data User Penyewa Mobil')
        csv_data=pd.read_csv('rental.csv')
        csv_data = csv_data[csv_data['status'] == 'User']

        filtered_columns = csv_data.filter(regex=re.compile(r'mobil'))
        filtered_columns.insert(0, 'username', csv_data['username'])
        filtered_columns['start'] = csv_data['start']
        filtered_columns['end'] = csv_data['end']
        filtered_columns['pay'] = csv_data['pay']

        self.tree = ttk.Treeview(pop_up_motor)
        self.tree["columns"] = list(filtered_columns.columns)
        
        for col in filtered_columns.columns:
            self.tree.column(col, anchor="w", width=100, stretch=tk.NO)
            self.tree.heading(col, text=col, anchor="w")

        for index, row in filtered_columns.iterrows():
            self.tree.insert("", 0, values=list(row))
        self.tree.pack()

    def show_popup_sepeda(self):
        pop_up_motor = tk.Toplevel(self)
        pop_up_motor.title('Data User Penyewa Sepeda')
        csv_data=pd.read_csv('rental.csv')
        csv_data = csv_data[csv_data['status'] == 'User']

        filtered_columns = csv_data.filter(regex=re.compile(r'sepeda'))
        filtered_columns.insert(0, 'username', csv_data['username'])
        filtered_columns['start'] = csv_data['start']
        filtered_columns['end'] = csv_data['end']
        filtered_columns['pay'] = csv_data['pay']

        self.tree = ttk.Treeview(pop_up_motor)
        self.tree["columns"] = list(filtered_columns.columns)
        
        for col in filtered_columns.columns:
            self.tree.column(col, anchor="w", width=100, stretch=tk.NO)
            self.tree.heading(col, text=col, anchor="w")

        for index, row in filtered_columns.iterrows():
            self.tree.insert("", 0, values=list(row))
        self.tree.grid(row=0,column=0)

    def switch_to_MenuAdmin(master):
        master.switch_frame(MainMenu_Admin) 

class Stockopname(tk.Frame):
    def __init__(self,  master, switch_frame):
        tk.Frame.__init__(self, master)
        global label_waktu
        self.master = master
        self.switch_frame = switch_frame

        self.image_bg = Image.open('bg_stock.png')
        self.image_bg = self.image_bg.resize((1550, 790))
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.selected_status= tk.StringVar()


        self.label_kosong= tk.Label(self, bg='#232526')
        self.label_kosong2= tk.Label(self, bg='#232526')
        label_waktu = tk.Label(self, font=('calibri', 14, 'bold'), foreground='black', bg='#232526', fg='#ffffff', anchor='w')

        self.label_motor = tk.Label(self, text='Motor',font=('calibri', 14, 'bold'), bg='#232526' , fg='#ffffff')
        self.radio_scoopy = tk.Radiobutton(self, text="Scoopy", value="motor Scoopy", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740', activebackground='#3B3B3B', variable=self.selected_status)
        self.radio_beat = tk.Radiobutton(self, text="Beat", value="motor Beat", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740',  activebackground='#3B3B3B', variable=self.selected_status)
        self.radio_nmax = tk.Radiobutton(self, text="NMAX", value="motor NMAX", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740', activebackground='#3B3B3B', variable=self.selected_status)
        self.radio_vario = tk.Radiobutton(self, text="Vario", value="motor Vario", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740',  activebackground='#3B3B3B', variable=self.selected_status)
        
        self.label_sepeda = tk.Label(self, text='Sepeda',font=('calibri', 14, 'bold'), bg='#232526', fg='#ffffff')
        self.radio_gunung = tk.Radiobutton(self, text="Sepeda Gunung", value="sepeda Gunung", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740', activebackground='#3B3B3B', variable=self.selected_status)
        self.radio_keranjang = tk.Radiobutton(self, text="Sepeda Keranjang", value="sepeda Keranjang", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740',  activebackground='#3B3B3B', variable=self.selected_status)
        self.radio_lipat = tk.Radiobutton(self, text="Sepeda Lipat", value="sepeda Lipat", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740', activebackground='#3B3B3B', variable=self.selected_status)
        
        self.label_mobil = tk.Label(self, text='Mobil',font=('calibri', 14, 'bold'), bg='#232526', fg='#ffffff')
        self.radio_jazz = tk.Radiobutton(self, text="mobil Jazz", value="mobil Jazz", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740',  activebackground='#3B3B3B', variable=self.selected_status)
        self.radio_xpander = tk.Radiobutton(self, text="mobil Xpander", value="mobil Xpander", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740', activebackground='#3B3B3B', variable=self.selected_status)
        self.radio_pajero = tk.Radiobutton(self, text="mobil Pajero", value="mobil Pajero", bg='#232526',font=('Arial', 11, 'bold'), fg='#FFA740',  activebackground='#3B3B3B', variable=self.selected_status)
        self.label_jumlah = tk.Label(self, text='Masukkan Jumlah Kendaraan: ', font=('calibri', 14, 'bold'),bg='#232526',fg='#ffffff')
        self.entry_jumlah = tk.Spinbox(self, bg='#ffffff',font=('Arial', 11, 'bold'), from_= 0, to=1000)
        self.button_entry = tk.Button(self, text='Setor', command=self.stockopname_system)

        
        self.label_kosong.grid(row=0,column=0,padx=135, pady=95, sticky='s')
        #self.label_kosong2.grid(row=0,column=6, padx=95, sticky='s')
        label_waktu.grid(row=0, column=7, columnspan=2, pady=35, sticky='n')
        update_waktu()
        self.label_motor.grid(row=1, column=1, padx=25, pady=5)
        self.radio_beat.grid(row=2, column=6, padx=25, pady=5)
        self.radio_scoopy.grid(row=2, column=2, padx=25, pady=5)
        self.radio_nmax.grid(row=2, column=3, padx=25, pady=5)
        self.radio_vario.grid(row=2, column=4, padx=25, pady=5)
        self.label_mobil.grid(row=3, column=1, padx=25, pady=5)
        self.radio_jazz.grid(row=4, column=4, padx=25, pady=5)
        self.radio_xpander.grid(row=4, column=2, padx=25, pady=5)
        self.radio_pajero.grid(row=4, column=3, padx=25, pady=5)
        self.label_sepeda.grid(row=5, column=1, padx=25, pady=5)
        self.radio_gunung.grid(row=6, column=4, padx=25, pady=5)
        self.radio_lipat.grid(row=6, column=2, padx=25, pady=5)
        self.radio_keranjang.grid(row=6, column=3, padx=25, pady=5)
        self.label_jumlah.grid(row=7, column=1, columnspan=2, padx=25, pady=15)
        self.entry_jumlah.grid(row=7, column=3, columnspan=2, padx=25, pady=5)
        self.button_entry.grid(row=8, column=3, columnspan=2, padx=25, pady=5)

        '''
    def stockopname_system(self):
        # Membaca data dari file CSV
        file_path = 'rental.csv'
        csv_data = pd.read_csv(file_path)

        # Menentukan username dan motor yang ingin diubah
        username_target = username_input
        value = self.entry_jumlah.get()

        # Mencari indeks baris yang sesuai dengan username
        index_to_change = csv_data.index[csv_data['username'] == username_target].tolist()

        # Mengganti nilai pada kolom 'motor Scoopy' sesuai dengan indeks yang ditemukan
        for index in index_to_change:
            csv_data.at[index, self.selected_status.get()] = value

        Jumlah_Kendaraan = csv_data[self.selected_status.get()].sum()


        csv_data.to_csv(file_path, index=False)
        messagebox.showinfo("Sukses", "Stock Opname berhasil!\nDilakukan Oleh "+ username_input+' Jumlah Kendaraan '+ self.selected_status.get()+' adalah '+ Jumlah_Kendaraan)
'''
    
    def stockopname_system(self):
        # Membaca data dari file CSV
        file_path = 'rental.csv'
        csv_data = pd.read_csv(file_path)

        # Menentukan username dan motor yang ingin diubah
        username_target = username_input
        value = self.entry_jumlah.get()

        # Mencari indeks baris yang sesuai dengan username
        index_to_change = csv_data.index[csv_data['username'] == username_target].tolist()

        # Pastikan nilai yang dimasukkan valid (misalnya, apakah value adalah angka?)
        try:
            value = int(value)
        except ValueError:
            messagebox.showerror("Error", "Masukkan jumlah kendaraan yang valid.")
            return

        # Mengganti nilai pada kolom yang sesuai
        for index in index_to_change:
            csv_data.at[index, self.selected_status.get()] = value

        # Menghitung jumlah kendaraan
        Jumlah_Kendaraan = csv_data[self.selected_status.get()].sum()

        # Menyimpan perubahan kembali ke file CSV
        csv_data.to_csv(file_path, index=False)

        # Menampilkan pesan sukses
        messagebox.showinfo("Sukses", f"Stock Opname berhasil!\nDilakukan Oleh {username_input} Jumlah Kendaraan {self.selected_status.get()} adalah {Jumlah_Kendaraan}")
'''        
class RentalMotor(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame

        colour1 = "#DEE1DD"
        colour2 = "#99AEAD"
        colour3 = "#6D9197"
        colour4 = "#28363D"
        self.master = master
        master.config(bg=colour4)

        self.image_back = Image.open("b_back.png")
        self.image_back = self.image_back.resize((200, 120))
        self.image_back = ImageTk.PhotoImage(self.image_back)

        self.nmax_motor = Image.open("NMAX.jpg")
        self.nmax_motor = self.nmax_motor.resize((300, 150))
        self.nmax_motor = ImageTk.PhotoImage(self.nmax_motor)

        self.vario_motor = Image.open("Vario.jpg")
        self.vario_motor = self.vario_motor.resize((300, 150))
        self.vario_motor = ImageTk.PhotoImage(self.vario_motor)

        self.scoopy_motor = Image.open("Scoopy.jpg")
        self.scoopy_motor = self.scoopy_motor.resize((300, 150))
        self.scoopy_motor = ImageTk.PhotoImage(self.scoopy_motor)

        self.beat_motor = Image.open("Beat.jpg")
        self.beat_motor = self.beat_motor.resize((300, 150))
        self.beat_motor = ImageTk.PhotoImage(self.beat_motor)

        self.vespa_motor = Image.open("Vespa.jpg")
        self.vespa_motor = self.vespa_motor.resize((300, 150))
        self.vespa_motor = ImageTk.PhotoImage(self.vespa_motor)

        # LABEL JUDUL FITUR
        self.label1 = tk.Label(master, text="JENIS MOTOR", font=('Verdana', 30, 'bold'), bg=colour4, fg=colour2)
        self.label1.place(x=475, y=100)

        # BUTTON PILIHAN
        self.button1 = tk.Button(master, text=" NMAX ", image=self.nmax_motor, bd=0, relief="flat", bg=colour1, fg=colour2, width=300, height=150)
        self.button1.place(x=100, y=250)
        self.button2 = tk.Button(master, text=" VARIO ", image=self.vario_motor, bd=0, relief="flat", bg=colour1, fg=colour2, width=300, height=150)
        self.button2.place(x=525, y=250)
        self.button3 = tk.Button(master, text=" SCOOPY ", image=self.scoopy_motor, bd=0, relief="flat", bg=colour1, fg=colour2, width=300, height=150)
        self.button3.place(x=950, y=250)
        self.button4 = tk.Button(master, text=" BEAT ", image=self.beat_motor, bd=0, relief="flat", bg=colour1, fg=colour2, width=300, height=150)
        self.button4.place(x=350, y=500)
        self.button5 = tk.Button(master, text=" VESPA ", image=self.vespa_motor, bd=0, relief="flat", bg=colour1, fg=colour2, width=300, height=150)
        self.button5.place(x=750, y=500)
        self.button_back = tk.Button(master, text=" VESPA ", image=self.image_back, bd=0, relief="flat", command=self.switch_to_MenuUser)
        self.button_back.place(x=1200, y=720)

    def switch_to_MenuUser(master):
        master.switch_frame(MainMenu_User) 

class RentalMobil(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame

        colour1 = "#DEE1DD"
        colour2 = "#99AEAD"
        colour3 = "#6D9197"
        colour4 = "#28363D"
        self.master = master
        master.geometry("1500x750")
        master.config(bg=colour4)

        self.pajero_mobil = Image.open("pajero.jpg")
        self.pajero_mobil = self.pajero_mobil.resize((300, 150))
        self.pajero_mobil = ImageTk.PhotoImage(self.pajero_mobil)

        self.jazz_mobil = Image.open("jazz.jpg")
        self.jazz_mobil = self.jazz_mobil.resize((300, 150))
        self.jazz_mobil = ImageTk.PhotoImage(self.jazz_mobil)

        self.xpander_mobil = Image.open("xpander.jpg")
        self.xpander_mobil = self.xpander_mobil.resize((300, 150))
        self.xpander_mobil = ImageTk.PhotoImage(self.xpander_mobil)

        # LABEL JUDUL FITUR
        self.label1 = tk.Label(master, text="JENIS mobil", font=('Verdana', 30, 'bold'), bg=colour4, fg=colour2)
        self.label1.place(x=475, y=100)

        # BUTTON PILIHAN
        self.button1 = tk.Button(master, text=" NMAX ", image=self.pajero_mobil, bg=colour1, fg=colour2, width=300, height=150)
        self.button1.place(x=100, y=250)
        self.button2 = tk.Button(master, text=" VARIO ", image=self.jazz_mobil, bg=colour1, fg=colour2, width=300, height=150)
        self.button2.place(x=525, y=250)
        self.button3 = tk.Button(master, text=" SCOOPY ", image=self.xpander_mobil, bg=colour1, fg=colour2, width=300, height=150)
        self.button3.place(x=950, y=250)
    
class RentalSepeda(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame

        colour1 = "#DEE1DD"
        colour2 = "#99AEAD"
        colour3 = "#6D9197"
        colour4 = "#28363D"

        
        self.master = master
        master.geometry("1500x750")
        master.config(bg=colour4)

        self.image_back = Image.open("b_back.png")
        self.image_back = self.image_back.resize((200, 120))
        self.image_back = ImageTk.PhotoImage(self.image_back)

        self.gunung_sepeda = Image.open("gunung.jpg")
        self.gunung_sepeda = self.gunung_sepeda.resize((300, 150))
        self.gunung_sepeda = ImageTk.PhotoImage(self.gunung_sepeda)

        self.lipat_sepeda = Image.open("lipat.jpg")
        self.lipat_sepeda = self.lipat_sepeda.resize((300, 150))
        self.lipat_sepeda = ImageTk.PhotoImage(self.lipat_sepeda)

        self.keranjang_sepeda = Image.open("keranjang.jpg")
        self.keranjang_sepeda = self.keranjang_sepeda.resize((300, 150))
        self.keranjang_sepeda = ImageTk.PhotoImage(self.keranjang_sepeda)

        # LABEL JUDUL FITUR
        self.label1 = tk.Label(master, text="JENIS sepeda", font=('Verdana', 30, 'bold'), bg=colour4, fg=colour2)
        self.label1.place(x=475, y=100)

        # BUTTON PILIHAN
        self.button1 = tk.Button(master, text=" NMAX ", image=self.gunung_sepeda, bg=colour1, fg=colour2, width=300, height=150)
        self.button1.place(x=100, y=250)
        self.button2 = tk.Button(master, text=" VARIO ", image=self.lipat_sepeda, bg=colour1, fg=colour2, width=300, height=150)
        self.button2.place(x=525, y=250)
        self.button3 = tk.Button(master, text=" SCOOPY ", image=self.keranjang_sepeda, bg=colour1, fg=colour2, width=300, height=150)
        self.button3.place(x=950, y=250)
        self.button_back = tk.Button(self, image=self.image_back, bg='#ffffff', bd=0, relief=0, command=self.switch_to_Menu)
        self.button_back.place(x=1200, y=250)

    def switch_to_Menu(self):
        self.switch_frame(MainMenu_User)    
'''
'''class PembayaranRental(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame

        
        colour1 = "#DEE1DD"
        colour2 = "#99AEAD"
        colour3 = "#6D9197"
        colour4 = "#28363D"

        self.master = master
        master.geometry("1500x750")
        master.config(bg=colour4)

        self.label_id = Label(master, text="ID Pelanggan:")
        self.label_mulai = Label(master, text="Waktu Mulai (YYYY-MM-DD HH:MM:SS):")
        self.label_selesai = Label(master, text="Waktu Selesai (YYYY-MM-DD HH:MM:SS):")
        self.label_tarif = Label(master, text="Tarif per Jam:")

        self.entry_id = Entry(master)
        self.entry_mulai = Entry(master)
        self.entry_selesai = Entry(master)
        self.entry_tarif = Entry(master)

        self.button_rekam = Button(master, text="Rekam Pembayaran", command=self.rekam_pembayaran)

        self.label_id.grid(row=0, column=0)
        self.label_mulai.grid(row=1, column=0)
        self.label_selesai.grid(row=2, column=0)
        self.label_tarif.grid(row=3, column=0)

        self.entry_id.grid(row=0, column=1)
        self.entry_mulai.grid(row=1, column=1)
        self.entry_selesai.grid(row=2, column=1)
        self.entry_tarif.grid(row=3, column=1)

        self.button_rekam.grid(row=4, column=0, columnspan=2)

    def hitung_biaya(self, waktu_mulai, waktu_selesai, tarif_per_jam):
        try:
            waktu_mulai = datetime.strptime(waktu_mulai, '%Y-%m-%d %H:%M:%S')
            waktu_selesai = datetime.strptime(waktu_selesai, '%Y-%m-%d %H:%M:%S')
            selisih_waktu = (waktu_selesai - waktu_mulai).total_seconds() / 3600
            biaya = selisih_waktu * tarif_per_jam
            return biaya
        except ValueError:
            return None

    def rekam_pembayaran(self):
        id_pelanggan = self.entry_id.get()
        waktu_mulai = self.entry_mulai.get()
        waktu_selesai = self.entry_selesai.get()
        tarif_per_jam = float(self.entry_tarif.get())

        biaya = self.hitung_biaya(waktu_mulai, waktu_selesai, tarif_per_jam)

        if biaya is not None:
            try:
                with open("data_pembayaran.csv", mode='a', newline='') as file:
                    writer = csv.writer(file)
                    writer.writerow([id_pelanggan, waktu_mulai, waktu_selesai, biaya])
                messagebox.showinfo("Pembayaran Berhasil", "Pembayaran berhasil direkam.")
            except Exception as e:
                messagebox.showerror("Kesalahan", f"Terjadi kesalahan: {e}")
        else:
            messagebox.showerror("Kesalahan", "Format waktu tidak valid.")'''

class RentalMobil(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame
        
        colour1 = "#DEE1DD"
        colour2 = "#99AEAD"
        colour3 = "#6D9197"
        colour4 = "#28363D"

        self.image_bg = Image.open('bg_rentalmobil.png')
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)
        
        self.pajero_mobil = Image.open("pajero.jpg")
        self.pajero_mobil = self.pajero_mobil.resize((300, 150))
        self.pajero_mobil = ImageTk.PhotoImage(self.pajero_mobil)

        self.jazz_mobil = Image.open("jazz.jpg")
        self.jazz_mobil = self.jazz_mobil.resize((300, 150))
        self.jazz_mobil = ImageTk.PhotoImage(self.jazz_mobil)

        self.xpander_mobil = Image.open("xpander.jpg")
        self.xpander_mobil = self.xpander_mobil.resize((300, 150))
        self.xpander_mobil = ImageTk.PhotoImage(self.xpander_mobil)

        self.image_pajero = Image.open("b_pajero.png")
        self.image_pajero = self.image_pajero.resize((300, 90))
        self.image_pajero = ImageTk.PhotoImage(self.image_pajero)
        
        self.image_jazz = Image.open("b_jazz.png")
        self.image_jazz = self.image_jazz.resize((300, 90))
        self.image_jazz = ImageTk.PhotoImage(self.image_jazz)

        self.image_xpander = Image.open("b_xpander.png")
        self.image_xpander = self.image_xpander.resize((300, 90))
        self.image_xpander = ImageTk.PhotoImage(self.image_xpander)
        
        self.image_back = Image.open("b_back.png")
        self.image_back = self.image_back.resize((300, 150) )
        self.image_back = ImageTk.PhotoImage(self.image_back)
       

        self.button1 = tk.Button(master, image=self.pajero_mobil, bg=colour1, fg=colour2, width=300, height=150)
        self.button1.place(x=100, y=200)
        self.button2 = tk.Button(master,  image=self.jazz_mobil, bg=colour1, fg=colour2, width=300, height=150)
        self.button2.place(x=525, y=200)
        self.button3 = tk.Button(master, image=self.xpander_mobil, bg=colour1, fg=colour2, width=300, height=150)
        self.button3.place(x=950, y=200)
        self.button4 = tk.Button(self.master,image=self.image_pajero, bg='#232526', bd=0, relief="flat", width=300, height=150, command=self.show_message_box_pajero)
        self.button4.place(x=100, y=400)
        self.button5 = tk.Button(self.master,image=self.image_jazz, bg='#232526', bd=0, relief="flat", width=300, height=150, command=self.show_message_box_jazz)
        self.button5.place(x=525, y=400)
        self.button6 = tk.Button(self.master,image=self.image_xpander, bg='#232526', bd=0, relief="flat", width=300, height=150, command=self.show_message_box_xpander)
        self.button6.place(x=950, y=400)
        self.button_back = tk.Button(master, image=self.image_back, bg='#232526', bd=0, relief="flat", width=300, height=150, command=self.switch_to_Menu)
        self.button_back.place(x=525, y=600)
        self.label1 = tk.Label(master, text="RP 1.1000.000 / hari", font=('Georgia Pro', 20, 'bold'), bg="#232526", fg="#8B3022")
        self.label1.place(x=125, y=380)
        self.label1 = tk.Label(master, text="RP 400.000 / hari", font=('Georgia Pro', 20, 'bold'), bg="#232526", fg="#8B3022")
        self.label1.place(x=570, y=380)
        self.label1 = tk.Label(master, text="RP 550.000/ hari", font=('Georgia Pro', 20, 'bold'), bg="#232526", fg="#8B3022")
        self.label1.place(x=1000, y=380)
       
     

    def show_message_box_pajero(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda ingin meminjam mobil ini?")
    
        if answer == 'yes':
            self.value='mobil Pajero'
            self.pinjam_mobil()
            messagebox.showinfo("Jawaban", "Anda memilih Yes!")
           
        else:
            messagebox.showinfo("Jawaban", "Anda memilih No!")

    def show_message_box_jazz(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda ingin meminjam mobil ini?")
        
        if answer == 'yes':
            self.value='mobil Jazz'
            self.pinjam_mobil()
            messagebox.showinfo("Jawaban", "Anda memilih Yes!")
            
        else:
            messagebox.showinfo("Jawaban", "Anda memilih No!")

    def show_message_box_xpander(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda ingin meminjam mobil ini?")
        if answer == 'yes':
            self.value="mobil Xpander"
            self.pinjam_mobil()
            messagebox.showinfo("Jawaban", "Anda memilih Yes!")
            
        else:
            messagebox.showinfo("Jawaban", "Anda memilih No!")

    def pinjam_mobil(self):
        file_path = 'rental.csv'
        csv_data = pd.read_csv(file_path)
        username_target = username_input
        index_to_change = csv_data.index[csv_data['username'] == username_target].tolist()
        time=datetime.now()
        waktu = time.strftime('%Y-%m-%d, %H:%M:%S')
        for index in index_to_change:
            csv_data.at[index, 'start'] = waktu
            if self.value == "mobil Pajero":
                csv_data.at[index, 'mobil Pajero'] = -1
            elif self.value == "mobil Jazz":
                csv_data.at[index, 'mobil Jazz'] = -1
            elif self.value == "mobil Xpander":
                csv_data.at[index, 'mobil Xpander'] = -1
           

            

            csv_data.to_csv(file_path, index=False)
       
    def switch_to_Menu(self):
        self.switch_frame(MainMenu_User)    

class RentalSepeda(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame

        colour1 = "#DEE1DD"
        colour2 = "#99AEAD"
        colour3 = "#6D9197"
        colour4 = "#28363D"

        self.image_bg = Image.open('bg_sepeda.png')
        self.image_bg = self.image_bg.resize((1515,790))
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.gunung_sepeda = Image.open("gunung.jpg")
        self.gunung_sepeda = self.gunung_sepeda.resize((300, 150))
        self.gunung_sepeda = ImageTk.PhotoImage(self.gunung_sepeda)

        self.lipat_sepeda = Image.open("lipat.jpg")
        self.lipat_sepeda = self.lipat_sepeda.resize((300, 150))
        self.lipat_sepeda = ImageTk.PhotoImage(self.lipat_sepeda)

        self.keranjang_sepeda = Image.open("keranjang.jpg")
        self.keranjang_sepeda = self.keranjang_sepeda.resize((300, 150))
        self.keranjang_sepeda = ImageTk.PhotoImage(self.keranjang_sepeda)

        self.image_gunung = Image.open("b_gunung.png")
        self.image_gunung = self.image_gunung.resize((300, 90))
        self.image_gunung = ImageTk.PhotoImage(self.image_gunung)
        
        self.image_lipat = Image.open("b_lipat.png")
        self.image_lipat = self.image_lipat.resize((300, 90))
        self.image_lipat = ImageTk.PhotoImage(self.image_lipat)

        self.image_keranjang = Image.open("b_keranjang.png")
        self.image_keranjang = self.image_keranjang.resize((300, 90))
        self.image_keranjang = ImageTk.PhotoImage(self.image_keranjang)
        
        self.image_back = Image.open("b_back.png")
        self.image_back = self.image_back.resize((300, 150) )
        self.image_back = ImageTk.PhotoImage(self.image_back)
    
      
        self.button1 = tk.Button(master, image=self.gunung_sepeda, bg=colour1, fg=colour2, width=300, height=150)
        self.button1.place(x=100, y=200)
        self.button2 = tk.Button(master,  image=self.lipat_sepeda, bg=colour1, fg=colour2, width=300, height=150)
        self.button2.place(x=525, y=200)
        self.button3 = tk.Button(master, image=self.keranjang_sepeda, bg=colour1, fg=colour2, width=300, height=150)
        self.button3.place(x=950, y=200)
        self.button4 = tk.Button(self.master,image=self.image_gunung, bg='#232526', bd=0, relief="flat", width=300, height=150, command=self.show_message_box_gunung)
        self.button4.place(x=100, y=400)
        self.button5 = tk.Button(self.master,image=self.image_lipat, bg='#232526', bd=0, relief="flat", width=300, height=150, command=self.show_message_box_lipat)
        self.button5.place(x=525, y=400)
        self.button6 = tk.Button(self.master,image=self.image_keranjang, bg='#232526', bd=0, relief="flat", width=300, height=150, command=self.show_message_box_keranjang)
        self.button6.place(x=950, y=400)
        self.button_back = tk.Button(master, image=self.image_back, bg='#232526', bd=0, relief="flat", width=300, height=150, command=self.switch_to_Menu)
        self.button_back.place(x=525, y=600)
        self.label1 = tk.Label(master, text="RP 50.000 / hari", font=('Georgia Pro', 20, 'bold'), bg="#232526", fg="#8B3022")
        self.label1.place(x=125, y=380)
        self.label1 = tk.Label(master, text="RP 4o.000 / hari", font=('Georgia Pro', 20, 'bold'), bg="#232526", fg="#8B3022")
        self.label1.place(x=570, y=380)
        self.label1 = tk.Label(master, text="RP 30.000/ hari", font=('Georgia Pro', 20, 'bold'), bg="#232526", fg="#8B3022")
        self.label1.place(x=1000, y=380)
    
    def show_message_box_gunung(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda ingin meminjam sepeda ini?")
    
        if answer == 'yes':
            self.value='sepeda Keranjang'
            self.pinjam_sepeda()
            messagebox.showinfo("Jawaban", "Anda memilih Yes!")
           
        else:
            messagebox.showinfo("Jawaban", "Anda memilih No!")

    def show_message_box_lipat(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda ingin meminjam sepeda ini?")
        
        if answer == 'yes':
            self.value='sepeda Lipat'
            self.pinjam_sepeda()
            messagebox.showinfo("Jawaban", "Anda memilih Yes!")
            
        else:
            messagebox.showinfo("Jawaban", "Anda memilih No!")

    def show_message_box_keranjang(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda ingin meminjam sepeda ini?")
        if answer == 'yes':
            self.value="sepeda Keranjang"
            self.pinjam_sepeda()
            messagebox.showinfo("Jawaban", "Anda memilih Yes!")
            
        else:
            messagebox.showinfo("Jawaban", "Anda memilih No!")

    def pinjam_sepeda(self):
        file_path = 'rental.csv'
        csv_data = pd.read_csv(file_path)
        username_target = username_input
        index_to_change = csv_data.index[csv_data['username'] == username_target].tolist()
        time=datetime.now()
        waktu = time.strftime('%Y-%m-%d, %H:%M:%S')
        for index in index_to_change:
            csv_data.at[index, 'start'] = waktu
            if self.value == "sepeda Gunung":
                csv_data.at[index, 'sepeda Gunung'] = -1
            elif self.value == "sepeda Lipat":
                csv_data.at[index, 'sepeda Lipat'] = -1
            elif self.value == "sepeda Keranjang":
                csv_data.at[index, 'sepeda Keranjang'] = -1
           

            

            csv_data.to_csv(file_path, index=False)

    def switch_to_Menu(self):
        self.switch_frame(MainMenu_User)

class RentalMotor(tk.Frame):
    def __init__(self, master, switch_frame):
        tk.Frame.__init__(self, master)
        self.master = master
        self.switch_frame = switch_frame

        width = master.winfo_screenwidth()
        height = master.winfo_screenheight()
        master.geometry(f"{width}x{height}+0+0")

        self.image_bg = Image.open('bg_motor.png')
        self.image_bg = self.image_bg.resize((1520, 790))        
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.nmax_motor = Image.open("NMAX.jpg")
        self.nmax_motor = self.nmax_motor.resize((300, 150))
        self.nmax_motor = ImageTk.PhotoImage(self.nmax_motor)

        self.vario_motor = Image.open("Vario.jpg")
        self.vario_motor = self.vario_motor.resize((300, 150))
        self.vario_motor = ImageTk.PhotoImage(self.vario_motor)

        self.scoopy_motor = Image.open("Scoopy.jpg")
        self.scoopy_motor = self.scoopy_motor.resize((300, 150))
        self.scoopy_motor = ImageTk.PhotoImage(self.scoopy_motor)

        self.beat_motor = Image.open("Beat.jpg")
        self.beat_motor = self.beat_motor.resize((300, 150))
        self.beat_motor = ImageTk.PhotoImage(self.beat_motor)

        self.back2 = Image.open("b_back.png")
        self.back2 = self.back2.resize((300, 150))
        self.back2 = ImageTk.PhotoImage(self.back2)

        self.button1 = tk.Button(master, text=" NMAX ", image=self.nmax_motor, bd=0, relief="flat", width=200, height=200, command=self.show_message_box_nmax)
        self.button1.place(x=100, y=200)
        self.label1 = tk.Label(master, text="Rp 150.000 / hari", font=('Verdana', 12, 'bold'), width=15, bg='#232526', fg='white')
        self.label1.place(x=110, y=425)

        self.button2 = tk.Button(master, text=" VARIO ", image=self.vario_motor, bd=0, relief="flat", width=200, height=200, command=self.show_message_box_vario)
        self.button2.place(x=425, y=200)
        self.label2 = tk.Label(master, text="Rp 120.000 / hari", font=('Verdana', 12, 'bold'), width=15, bg='#232526', fg='white')
        self.label2.place(x=450, y=425)

        self.button3 = tk.Button(master, text=" SCOOPY ", image=self.scoopy_motor, bd=0, relief="flat", width=200, height=200, command=self.show_message_box_scoopy)
        self.button3.place(x=730, y=200)
        self.label3 = tk.Label(master, text="Rp 90.000 / hari", font=('Verdana', 12, 'bold'), width=15, bg='#232526', fg='white')
        self.label3.place(x=750, y=425)

        self.button4 = tk.Button(master, text=" BEAT ", image=self.beat_motor, bd=0, relief="flat", width=200, height=200, command=self.show_message_box_beat)
        self.button4.place(x=1075, y=200)
        self.label4 = tk.Label(master, text="Rp 80.000 / hari", font=('Verdana', 12, 'bold'), width=15, bg='#232526', fg='white')
        self.label4.place(x=1050, y=425)
       
        self.button_back = tk.Button(master, image=self.back2, bd=0, bg='#232526', relief="flat", activebackground='#232526', width=300, height=150, command=self.switch_to_MenuUser)
        self.button_back.place(x=1000, y=500)

    def show_message_box_nmax(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda yakin akan menyewa motor Nmax?")
        if answer == 'yes':
            self.value = "nmax"
            self.sewa_motor()
            messagebox.showinfo("Jawaban", "Berhasil meminjam!")
        else:
            pass
    
    def show_message_box_vario(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda yakin akan menyewa motor vario?")
        if answer == 'yes':
            self.value = "vario"
            self.sewa_motor()
            messagebox.showinfo("Jawaban", "Berhasil meminjam!")
        else:
            pass

    def show_message_box_scoopy(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda yakin akan menyewa motor scoopy?")
        if answer == 'yes':
            self.value = "scoopy"
            self.sewa_motor()
            messagebox.showinfo("Jawaban", "Berhasil meminjam!")
        else:
            pass

    def show_message_box_beat(self):
        answer = messagebox.askquestion("Konfirmasi", "Apakah Anda yakin akan menyewa motor beat?")
        if answer == 'yes':
            self.value = "beat"
            self.sewa_motor()
            messagebox.showinfo("Jawaban", "Berhasil meminjam!")
        else:
            pass

    def sewa_motor(self):
        file_path = 'rental.csv'
        csv_data = pd.read_csv(file_path)
        username_target = username_input
        index_to_change = csv_data.index[csv_data['username'] == username_target].tolist()
        time=datetime.now()
        waktu = time.strftime('%Y-%m-%d, %H:%M:%S')
        for index in index_to_change:
            csv_data.at[index, 'start'] = waktu
            if self.value == "nmax":
                csv_data.at[index, 'motor NMAX'] = -1
            elif self.value == "vario":
                csv_data.at[index, 'motor Vario'] = -1
            elif self.value == "scoopy":
                csv_data.at[index, 'motor Scoopy'] = -1
            elif self.value == "beat":
                csv_data.at[index, 'motor Beat'] = -1

            csv_data.to_csv(file_path, index=False)

    def switch_to_MenuUser(master):
        master.switch_frame(MainMenu_User)

class Review(tk.Frame):
    def _init_(self, master, switch_frame):
        tk.Frame._init_(self, master)
        self.master = master
        self.switch_frame = switch_frame

        self.image_bg = Image.open('bg_review.png')
        self.image_bg = ImageTk.PhotoImage(self.image_bg)
        self.label_bg = tk.Label(self, image=self.image_bg)
        self.label_bg.place(x=0,y=0)

        self.create_widgets()
        
    def create_widgets(self):
        self.canvas_rating = tk.Canvas(self.master, width=450, height=100, bg="#0b6380", bd=0, relief="flat")
        self.canvas_rating.place(x=775, y=250)

        self.stars = [self.canvas_rating.create_text(x, 20, text="★", font=("Arial", 32), fill="gray") for x in range(20, 450, 100)]
        for star in self.stars:
            self.canvas_rating.tag_bind(star, '<Button-1>', lambda event, star=star: self.on_star_click(star, event))

        self.label_review = tk.Label(self.master, text="Berikan Ulasan Anda :", font=("Arial", 16))
        self.label_review.place(x=750, y=360)

        self.text_review = tk.Text(self.master, height=8, width=60)
        self.text_review.place(x=750, y=400)

        self.button_submit = tk.Button(self.master, text="Submit", command=self.submit_review)
        self.button_submit.place(x=1000, y=550)

    def on_star_click(self, star, event):
        current_fill = self.canvas_rating.itemcget(star, 'fill')
        new_fill = "gold" if current_fill == "gray" else "gray"
        self.canvas_rating.itemconfig(star, fill=new_fill)

    def submit_review(self):
        rating = sum(1 for star in self.stars if self.canvas_rating.itemcget(star, 'fill') == 'gold')
        review_text = self.text_review.get("1.0", "end-1c")

        if review_text.strip() == "":
            messagebox.showwarning("Warning!", "Anda belum mengisi Ulasan!")
        else:
            self.save_review_to_file(rating, review_text)
            messagebox.showinfo("Thank You",f"Thank u,see you next time!\nRating: {rating}\nReview: {review_text}")
        
    def save_review_to_file(self, rating, review_text):
        filename = "ulasan.txt"
        with open(filename, "a", encoding="utf-8") as file:
            file.write(f"Rating: {rating} stars\n")
            file.write(f"Review: {review_text}\n\n")
        
class MainApp(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("schematiq rental")
        self.geometry("{0}x{1}+0+0".format(self.winfo_screenwidth(), self.winfo_screenheight()))
        self.iconbitmap('2.ico')

        self.current_frame = None
        self.switch_frame(LoginPage)

    def switch_frame(self, frame_class):
        new_frame = frame_class(self, self.switch_frame)
        if self.current_frame is not None:
            self.current_frame.destroy()
        self.current_frame = new_frame
        self.current_frame.pack(fill="both", expand=True)
        
def update_waktu():
        now = datetime.now()
        string_waktu = now.strftime('%Y-%m-%d, %H:%M:%S')
        label_waktu.config(text="DATE & TIME: "+string_waktu)
        app.after(1000, update_waktu)

app = MainApp()
app.mainloop()
