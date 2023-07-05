from tkinter import *
from tkinter import Tk, Button, Label, Frame, filedialog, messagebox, ttk
from PIL import ImageTk, Image
import mysql.connector
# import sqlite3
import pandas as pd


class HomePage:
    # def __init__(self,login_window ):
    #     self.login_window = login_window

    def __init__(self):
        # GUI PART
        self.home_window = Tk()
        self.home_window.title("Home Page")
        self.home_window.geometry('900x600')
        self.home_window.resizable(0, 0)

        # bg_color = "#FFA3AC"
        self.bg_color = "lavender"
        self.home_window.configure(background=self.bg_color)

        # report heading
        self.welcome_label = Label(self.home_window, text="Report Generator", font=(
            "Helvetica", 30), bg=self.bg_color, fg="#00043C")
        self.welcome_label.pack(padx=20, pady=20)

        # logout button
        self.logout_button = Button(self.home_window, text="Log Out", font=(
            "Helvetica", 12, 'bold'), bg='red', fg='white', command=self.logout)
        self.logout_button.place(x=800, y=35)
        self.menu()
        self.GUIofapp()

        self.host = 'localhost'
        self.username = 'root'
        self.password = 'Shruti098%'
        self.database = 'userdata'
        # self.table_name = 'sampledb'

        # # Connect to the MySQL database
        # self.conn = mysql.connector.connect( host = self.host, user = self.username, password = self.password, database = self.database )
        # self.cursor = self.conn.cursor()

    def GUIofapp(self):

        # frame 1
        self.frame1 = Frame(self.home_window, bg=self.bg_color, bd=2, relief="groove", width=500, height=500)
        self.frame1.pack(padx=(40,20), pady=30, side=LEFT, fill=BOTH, expand=True)
        
        # frame 2
        self.frame2 = Frame(self.home_window, bg=self.bg_color, bd=2, relief="ridge", width=500, height=500)
        self.frame2.pack(padx=(20,40), pady=30, side=LEFT, fill=BOTH, expand=True)

        # self.frame1.place(x=75, y=200)
        # self.frame2.place(x=400, y=200)

        # Add a heading 1 in frame 1
        self.heading1 = Label(self.frame1, text='Upload Excel File', font=('Microsoft Yahei UI Light', 20, 'bold'), bg=self.bg_color, fg='#00043C')
        self.heading1.pack(padx=10, pady=10)

        # Add a button *Choose a File* in frame 1
        self.button1 = Button(self.frame1, text='Choose a File', font=("Helvetica", 16, 'bold'), bg='green3', fg='white', command=self.open_file)
        self.button1.pack(padx=10, pady=10)

        # Add a Label 1 in frame 1
        self.filename_label = Label(self.frame1, text="", font=('Microsoft Yahei UI Light', 9, 'bold'), wraplength=280, bg=self.bg_color) # Adjust wrap length as needed
        self.filename_label.pack()

        # Add a button  *Upload to DataBase*  in frame 1
        self.button12 = Button(self.frame1, text='Upload to DataBase', font=("Helvetica", 16, 'bold'), bg='green3', fg='white', command=self.send_data_to_database)
        self.button12.pack(padx=10, pady=10)

        # Add a heading 2 for frame 2 
        self.heading2 = Label(self.frame2, text="Generate Report", font=('Microsoft Yahei UI Light', 20, 'bold'), bg=self.bg_color, fg='#00043C')
        self.heading2.pack(padx=10, pady=10)

        # Add a heading 3 in frame 2
        self.subheading2 = Label(self.frame2, text="Select options from Dropdown", font=('Microsoft Yahei UI Light', 14), bg=self.bg_color, fg='#00043C')
        self.subheading2.pack(padx=10, pady=10)

        # Create the first dropdown
        self.options_list1 = ["Select", "Gender", "State", "Organization Sector", "Organization belongs to SME/Non-SME","Officer belongs to SC/ST (Yes/No)", "Officer belongs to PWD category (Yes/No)"]
        
        self.dropdown1 = ttk.Combobox(self.frame2, values=self.options_list1, state="readonly")
        self.dropdown1.set("Select")
        self.dropdown1.configure(font=("Helvetica", 16), background="blue")
        
        
        self.dropdown1.pack(padx=10, pady=(30, 10))

        # Create the second dropdown
        self.options_list2 = []

        self.dropdown2 = ttk.Combobox(self.frame2, values=self.options_list2, state="readonly")
        self.dropdown2.set("Select")
        self.dropdown2.configure(font=("Helvetica", 16), background="blue")
        self.dropdown2.pack(padx=10, pady=(10, 30))

        self.dropdown1.bind("<<ComboboxSelected>>", self.update_dropdown2)

        # Add a button to *generate report* in frame 2
        self.report_button = Button(self.frame2, text="Generate", font=("Helvetica", 16, 'bold'), bg="#FF9800", fg="#ffffff")
        self.report_button.pack(padx=10, pady=10)

    def update_dropdown2(self, event):

        selected_option = self.dropdown1.get()

        if selected_option == "Select":
            self.options_list2 = ["Select"]
            # break
        elif selected_option == "Gender":
            self.options_list2 = ["Male", "Female"]
            # break
        elif selected_option == "State":
            self.options_list2 = ["Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana", "Himachal Pradesh", "Jharkhand", "Karnataka", "Kerala","Madhya Pradesh", "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "New Delhi", "Odisha", "Punjab", "Rajasthan", "Sikkim", "Tamil Nadu", "Telangana", "Tripura", "Uttarakhand", "Uttar Pradesh", "West Bengal"]
            # break
        elif selected_option == "Organization Sector":
            self.options_list2 = ('Central Government Ministry', 'State Government Ministry', 'Defence', 'PSU', 'Finance','Banking', 'Power', 'Energy', 'Telecom', 'Transport''Manufacturing', 'LEA', 'Academia', 'Private', 'IT', 'ITeS')
            # break
        elif selected_option == "Organization belongs to SME/Non-SME":
            self.options_list2 = ["SME", "Non-SME"]
            # break
        elif selected_option == "Officer belongs to SC/ST (Yes/No)":
            self.options_list2 = ["Yes", "No"]
            # break
        elif selected_option == "Officer belongs to PWD category (Yes/No)":
            self.options_list2 = ["Y", "N"]
            # break
        else:
            self.options_list2 = ["Select"]

        self.dropdown2["values"] = self.options_list2
        self.dropdown2.current(0)

    def menu(self):
        def myfun():
            print("File menu working")

        def quitw():
            result = messagebox.askquestion(
                "Quit", "Are you sure you want to quit?")
            if result == "yes":
                root.destroy()

        # making a menu bar
        self.mymenu = Menu(self.home_window)
        self.mymenu.add_command(label="File", command=myfun)
        # self.mymenu.add_command(label="Home", command=open_second_script)
        self.mymenu.add_command(label="Quit", command=quitw)
        self.mymenu.add_command(label="Help", command=myfun)
        self.home_window.config(menu=self.mymenu)

    def open_file(self):

        filename = filedialog.askopenfilename(title="Select Excel file", filetypes=[("Excel files", "*.xlsx;*.xls")])

        if filename:

            # self.data = pd.read_excel(filename)
            # self.send_data_to_database(self.data)
            self.excel_data = pd.read_excel(filename)

            # df.empty: This condition checks if the DataFrame df is empty, meaning it does not contain any rows or columns. It is typically used to check if the DataFrame has any data.
            if self.excel_data.empty:
                messagebox.showinfo(title="Failure", message="Excel file is empty!!")
                return

            # print(self.excel_data)

            # self.tick_mark_label.config(text="✔ File Loaded Successfully", fg="green")

            self.filename_label.config(text="Selected file: " + filename, fg='green2')
            messagebox.showinfo(title="Success", message="Excel file opened successfully.")
            
            check = True
        else:

            self.filename_label.config(text="❌ File Loading Failed", fg="red")
            messagebox.showinfo(title="Failure", message="Excel file opening failed. Try Again!!!")

            # self.tick_mark_label.config(text="❌ File Loading Failed", fg="red")
            check = False

    def send_data_to_database(self):
        
        # Connect to the MySQL database
        self.conn = mysql.connector.connect( host = self.host, user = self.username, password = self.password, database = self.database )
        self.cursor = self.conn.cursor()

        insert_query = ''' INSERT INTO sampledb (
            TrainingProgramName,
            TrainingProgramDate,
            Name,
            Designation,
            Gender,
            Email,
            MobileNumber,
            Organization,
            OfficeAddress,
            State,
            OrganizationSector,
            OrganizationCategorySMEorNonSME,
            OfficerBelongsToSCOrST,
            OfficerBelongsToPWD
        ) values (
            %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        )
        '''
        success_count = 0
        for index, row in self.excel_data.iterrows():
            record_data = []
            # for value in row:
            
            # for column_name, value in row.items():

            for column_name in row.index:
                if column_name != 'SNo':  # Skip the 'SNo' column
                    value = row[column_name]        # to comment later
                    if pd.isnull(value):
                        record_data.append(None)  # Convert NaN values to None (null)
                    else:
                        record_data.append(value)
                
            # print('index = ',index)
            # print('row = ',row)
            # print('record_data = ',record_data)
            try:
                self.cursor.execute(insert_query, record_data)  # Execute the query
                self.conn.commit() 
                success_count += 1

            except Exception as e:
                print("Error inserting record:", e)

        self.cursor.close()
        self.conn.close()

        if (success_count == 0):
            messagebox.showerror("Error","Error inserting record")
        else :
            # Display a message box with the success count
            messagebox.showinfo("Query Execution Result", f"Query executed successfully for {success_count} records.")

        # column_mapping = {
        #     # 'S.No'                 : 'SNo',
        #     'Training Program Name' : 'TrainingProgramName',
        #     'Training Program Date' : 'TrainingProgramDate',
        #     'Name of the Officer'   : 'Name',
        #     'Designation'           : 'Designation',
        #     'Gender'                : 'Gender',
        #     'Email Address'         : 'Email',
        #     'Mobile Number'         : 'MobileNumber',
        #     'Organization'          : 'Organization',
        #     'State'                 : 'State',
        #     'Organization Sector'   : 'OrganizationSector',
        #     'Office Address with State/UT details'     : 'OfficeAddress',
        #     'Organization belongs to SME/Non-SME'      : 'OrganizationCategorySMEorNonSME',
        #     'Officer belongs to SC/ST (Yes/No)'        : 'OfficerBelongsToSCOrST',
        #     'Officer belongs to PWD category (Yes/No)' : 'OfficerBelongsToPWD'
        # }
        
        # # Rename the columns in the DataFrame
        # self.excel_data.rename(columns=column_mapping, inplace=True)


        
        # Create a table (if it doesn't exist)
        # create_table_query = '''CREATE TABLE IF NOT EXISTS officer_data (
        #     ID INT AUTO_INCREMENT PRIMARY KEY,
        #     SNo VARCHAR(10)
        #     TrainingProgramName VARCHAR(255),
        #     TrainingProgramDate VARCHAR(10),
        #     Name VARCHAR(255),
        #     Designation VARCHAR(255),
        #     Gender VARCHAR(10),
        #     Email VARCHAR(255),
        #     MobileNumber VARCHAR(15),
        #     Organization VARCHAR(255),
        #     OfficeAddress VARCHAR(255),
        #     State VARCHAR(255),
        #     OrganizationSector VARCHAR(50),
        #     OrganizationCategorySMEorNonSME ENUM('SME', 'Non SME'),
        #     OfficerBelongsToSCOrST ENUM('Yes', 'No'),
        #     OfficerBelongsToPWD ENUM('Yes', 'No')
        # )
        # '''
        # self.cursor.execute(create_table_query)

        # Insert the data into the database
        # for _, row in self.excel_data.iterrows():
        #     values = tuple(row)
        #     insert_query = '''
        #     INSERT INTO officer_data (SNo, TrainingProgramName, TrainingProgramDate, Name, Designation, Gender, Email, MobileNumber, Organization, OfficeAddress, State, OrganizationSector, OrganizationCategorySMEorNonSME, OfficerBelongsToSCOrST, OfficerBelongsToPWD)
        #     VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s
        #     '''
        #     self.cursor.execute(insert_query, values)
        
        # self.conn.commit()
        # print("Excel data uploaded successfully!")

        # # Close the database connection
        # self.conn.close()

        # pass


    # def send_data_to_database(self):
    #     # Connect to the MySQL database
    #     con = mysql.connector.connect(
    #         host=self.host,
    #         user=self.username,
    #         password=self.password,
    #         database=self.database
    #     )

    #     # Create a cursor object to interact with the database
    #     cursor = con.cursor()

    #     # Map Excel column names to database column names
    #     excel_columns_mapping = {
    #         # 'S.No'                 : 'SNo',
    #         'Training Program Name' : 'TrainingProgramName',
    #         # 'TrainingProgramName'   : 'Training Program Name',
    #         'Training Program Date' : 'TrainingProgramDate',
    #         'Name of the Officer'   : 'Name',
    #         'Designation'           : 'Designation',
    #         'Gender'                : 'Gender',
    #         'Email Address'         : 'Email',
    #         'Mobile Number'         : 'MobileNumber',
    #         'Organization'          : 'Organization',
    #         'State'                 : 'State',
    #         'Organization Sector'   : 'OrganizationSector',
    #         'Office Address with State/UT details'     : 'OfficeAddress',
    #         'Organization belongs to SME/Non-SME'      : 'OrganizationCategorySMEorNonSME',
    #         'Officer belongs to SC/ST (Yes/No)'        : 'OfficerBelongsToSCOrST',
    #         'Officer belongs to PWD category (Yes/No)' : 'OfficerBelongsToPWD'
    #     }
    #     column_mapping = {excel_column: db_column for excel_column,db_column in excel_columns_mapping.items()}
        
    #     # Extract the database column names
    #     db_columns = list(column_mapping.values())

    #     # Generate placeholders for the SQL query
    #     placeholders = ', '.join(['%s'] * len(db_columns))

    #     # Iterate over each row in the Excel data
    #     for _, row in self.excel_data.iterrows():
    #         # Extract the values from the Excel row based on the column mapping
    #         values = [row[excel_column] for excel_column in column_mapping.keys()]

    #         # SQL query to insert data into the table
    #         sql_query = f"INSERT INTO {self.table_name} ({', '.join(db_columns)}) VALUES ({placeholders})"

    #         # Execute the SQL query for each row of data
    #         cursor.execute(sql_query, values)

    #     # Commit the changes to the database
    #     con.commit()
    #     messagebox.showinfo(title="Success", message="Excel file uploaded successfully.")

    #     # Close the cursor and database connection
    #     cursor.close()
    #     con.close()

    def fetch_data():
        pass

    def generate_report():
        pass

    def logout(self):
        self.home_window.destroy()
        self.login_window.deiconify()

    def run(self):
        self.home_window.mainloop()


# Example usage:
if __name__ == "__main__":
    # home_page = HomePage(login_window)
    home_page = HomePage()
    home_page.run()
