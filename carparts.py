from tkinter import *
import tkinter.messagebox as tmsg

class Carparts(Tk):
    def __init__(self):
        super().__init__()
        self.title("CAR PARTS")
        self.configure(bg="white")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}")
        self.wm_iconbitmap("images/car.ico")

    def logo(self):
        self.icon = PhotoImage(file="images/logo.PNG")
        icon_label = Label(self, image=self.icon, borderwidth=0)
        icon_label.grid(row=0, column=0)

    def parts(self):

        def add_to_cart():
            yes_no = tmsg.askyesno("CONFIRMATION!", "Are you sure want to purchase this part?")
            if yes_no == True:
                tmsg.showinfo("HOORAYY!!", "You have successfully purchased this part!")
            else:
                tmsg.showinfo("Cancelled", "The order was cancelled!")

        self.p1 = PhotoImage(file="images/parts/1.PNG")
        self.p2 = PhotoImage(file="images/parts/2.PNG")
        self.p3 = PhotoImage(file="images/parts/3.PNG")
        self.p4 = PhotoImage(file="images/parts/4.PNG")
        self.p5 = PhotoImage(file="images/parts/5.PNG")
        self.p6 = PhotoImage(file="images/parts/6.PNG")
        self.p7 = PhotoImage(file="images/parts/7.PNG")
        self.p8 = PhotoImage(file="images/parts/8.PNG")
        self.p9 = PhotoImage(file="images/parts/9.PNG")
        self.p10 = PhotoImage(file="images/parts/10.PNG")
        self.p11 = PhotoImage(file="images/parts/11.PNG")
        self.p12 = PhotoImage(file="images/parts/12.PNG")
        self.p13 = PhotoImage(file="images/parts/13.PNG")
        self.p14 = PhotoImage(file="images/parts/14.PNG")
        self.p15 = PhotoImage(file="images/parts/15.PNG")
        self.p16 = PhotoImage(file="images/parts/16.PNG")
        self.p17 = PhotoImage(file="images/parts/17.PNG")
        self.p18 = PhotoImage(file="images/parts/18.PNG")
        self.p19 = PhotoImage(file="images/parts/19.PNG")
        self.p20 = PhotoImage(file="images/parts/20.PNG")
        self.p21 = PhotoImage(file="images/parts/21.PNG")
        self.p22 = PhotoImage(file="images/parts/22.PNG")
        self.p23 = PhotoImage(file="images/parts/23.PNG")
        self.p24 = PhotoImage(file="images/parts/24.PNG")

        b1 = Button(self, image=self.p1, command=add_to_cart)
        b2 = Button(self, image=self.p2, command=add_to_cart)
        b3 = Button(self, image=self.p3, command=add_to_cart)
        b4 = Button(self, image=self.p4, command=add_to_cart)
        b5 = Button(self, image=self.p5, command=add_to_cart)
        b6 = Button(self, image=self.p6, command=add_to_cart)
        b7 = Button(self, image=self.p7, command=add_to_cart)
        b8 = Button(self, image=self.p8, command=add_to_cart)
        b9 = Button(self, image=self.p9, command=add_to_cart)
        b10 = Button(self, image=self.p10, command=add_to_cart)
        b11 = Button(self, image=self.p11, command=add_to_cart)
        b12 = Button(self, image=self.p12, command=add_to_cart)
        b13 = Button(self, image=self.p13, command=add_to_cart)
        b14 = Button(self, image=self.p14, command=add_to_cart)
        b15 = Button(self, image=self.p15, command=add_to_cart)
        b16 = Button(self, image=self.p16, command=add_to_cart)
        b17 = Button(self, image=self.p17, command=add_to_cart)
        b18 = Button(self, image=self.p18, command=add_to_cart)
        b19 = Button(self, image=self.p19, command=add_to_cart)
        b20 = Button(self, image=self.p20, command=add_to_cart)
        b21 = Button(self, image=self.p21, command=add_to_cart)
        b22 = Button(self, image=self.p22, command=add_to_cart)
        b23 = Button(self, image=self.p23, command=add_to_cart)
        b24 = Button(self, image=self.p24, command=add_to_cart)

        b1.grid(row=1, column=0, padx=15, pady=15)
        b2.grid(row=1, column=1, padx=15, pady=15)
        b3.grid(row=1, column=2, padx=15, pady=15)
        b4.grid(row=1, column=3, padx=15, pady=15)
        b5.grid(row=1, column=4, padx=15, pady=15)
        b6.grid(row=1, column=5, padx=15, pady=15)
        b7.grid(row=1, column=6, padx=15, pady=15)
        b8.grid(row=1, column=7, padx=15, pady=15)
        b9.grid(row=2, column=0, padx=15, pady=15)
        b10.grid(row=2, column=1, padx=15, pady=15)
        b11.grid(row=2, column=2, padx=15, pady=15)
        b12.grid(row=2, column=3, padx=15, pady=15)
        b13.grid(row=2, column=4, padx=15, pady=15)
        b14.grid(row=2, column=5, padx=15, pady=15)
        b15.grid(row=2, column=6, padx=15, pady=15)
        b16.grid(row=2, column=7, padx=15, pady=15)
        b17.grid(row=3, column=0, padx=15, pady=15)
        b18.grid(row=3, column=1, padx=15, pady=15)
        b19.grid(row=3, column=2, padx=15, pady=15)
        b20.grid(row=3, column=3, padx=15, pady=15)
        b21.grid(row=3, column=4, padx=15, pady=15)
        b22.grid(row=3, column=5, padx=15, pady=15)
        b23.grid(row=3, column=6, padx=15, pady=15)
        b24.grid(row=3, column=7, padx=15, pady=15)

class About(Carparts):
    def about_us(self):
        print("Carparts has been serving humanity for more than 10 years! Carparts is and always will be your best\n"
              "destination for buying parts of different types of cars online. Our parts come with a whole year\n"
              "warranty - this will assure you of our products quality. If you have an old car, no worries! Cuz we have\n"
              "the parts of almost every car model. Our deliveries are spread in 5 continents. If you become our loyal\n"
              "member, you will get a special discount on each part. Carparts has been ranked best by it's customers.\n"
              "Here, you can get the best quality parts in the best prices now just from your home. So what are you\n"
              "waiting for? You're just a click away to get that new part.")

class ContactUs(Carparts):
    def write_here(self, msg):
        print("Your response has been submitted! Reply is expected within 24 hours.")
        with open("queriesandcomplaints.txt", "a") as f:
            f.write(f"{msg}\n")

class SignUp(Carparts):
    def __init__(self, name, age, email, contact, country):
        super().__init__()
        try:
            self.name = name
            self.age = int(age)
            self.email = email
            self. contact = int(contact)
            self.country = country
        except ValueError:
            print("Please enter a proper age and phone number i.e. in integers.")

    def register(self):
        print("Name: {}\nAge: {}\nEmail: {}\nContact No.: {}\nCountry of Stay: {}\nCONGRATULATIONS! "
              "Your account has been successfully made.".format(self.name, self.age, self.email, self.contact, self.country))
        with open("accounts.txt", "a") as f:
            f.write(f"Name: {self.name}\nAge: {self.age}\nEmail: {self.email}\nContact No.: {self.contact}\nCountry of Stay: {self.country}\n\n")

class AffiliateLink(SignUp):
    def __init__(self, name, age, email, contact, country):
        SignUp.__init__(self, name, age, email, contact, country)

    def get_link(self):
        print("We are glad to find out that you are interested in our affiliate program. Just register and complete the "
              "further processes to get your link!")

class CustomerService(Carparts):
    def freq_question(self):
        print("Q.What if my orders don't arrive on time?\nA.No worries. You will get 5% off on each day late.")

class GetConnected(Carparts):
    def join_us(self):
        print("If you wish to be the first to receive our updates, then subscribe to our YouTube channel, like our "
              "Facebook page and follow us on Twitter!")

# GUI Instance:
gui = Carparts()
gui.logo()
gui.parts()
gui.mainloop()

# About_Us Instance:
# abt = About()
# abt.about_us()

# Contact Instance:
# feedback = ContactUs()
# feedback.write_here("sample text")

# Registering Instance:
# createAccount = SignUp("Huzaifa", 20, "abc@gmail.com", 123456789, "South Africa")
# createAccount.register()

# Affiliate Instance:
# link = AffiliateLink("Huzaifa", 20, "abc@gmail.com", 123456789, "Germany")
# link.get_link()

# FAQ Instance:
# faq = CustomerService()
# faq.freq_question()

# Connect Instance:
# con = GetConnected()
# con.join_us()