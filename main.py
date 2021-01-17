from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter import ttk, filedialog, messagebox
import pandas as pd
import numpy as np
import analysis1 as ty
import anova as an
import hydrograph_baseflow as hb
from pandas import DataFrame





df=DataFrame()
df2=DataFrame()
def package1(menuroot):
    menuroot.withdraw()
    root=Toplevel(menuroot)
    root.geometry("733x566")
    root.state('zoomed')
    def OpenFile():
        filename2 = filedialog.askopenfilename(initialdir="/",
                                          title="Select A ZIP",
                                          filetype=(("ZIP files", "*.zip"), ("RAR files","*.rar"),("all files", "*.*")))
        label2_file.configure(text=filename2)



    #code for uploading saved data file
    file_frame = LabelFrame(root, text="Open File")
    file_frame.place(height=800, width=310, x=0, y=0)

    label2_file =ttk.Label(file_frame, text="")
    label2_file.place(x=0, y=10)

    label3_file =ttk.Label(file_frame, text="")
    label3_file.place(x=0, y=50)
    #button for loading saved excel data
    button2 = Button(root, text="Load File", command=lambda: Load_excel_data())
    button2.place(x=100, y=0)
    
    #tabs
    my_notebook=ttk.Notebook(root)
    my_notebook.place(x=310,y=0, height=785, width=1230)
   
    #excel data frame 1
    frame1 = LabelFrame(my_notebook,bg='white')
    frame1.pack(fill="both", expand=1)
    
    #excel data frame 2`
    frame2 = LabelFrame(my_notebook,bg='white')
    frame2.pack(fill="both",expand=1)

    
    my_notebook.add(frame1,text="Discharge")
    my_notebook.add(frame2,text="Rainfall")
    
    
    #hide tabs before importing 
    my_notebook.hide(0)
    my_notebook.hide(1)
    
          
    
    
    
    # This is the Treeview Widget for frame 1
    tv1 = ttk.Treeview(frame1)  
    tv1.place(relheight=1,relwidth=1)

    treescrolly=Scrollbar(frame1,orient="vertical",command=tv1.yview)
    treescrollx=Scrollbar(frame1,orient="horizontal",command=tv1.xview)

    tv1.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")


    # This is the Treeview Widget for frame 2
    tv2 = ttk.Treeview(frame2)  
    tv2.place(relheight=1,relwidth=1)

    treescrolly=Scrollbar(frame2,orient="vertical",command=tv2.yview)
    treescrollx=Scrollbar(frame2,orient="horizontal",command=tv2.xview)

    tv2.configure(xscrollcommand=treescrollx.set,yscrollcommand=treescrolly.set)
    treescrollx.pack(side="bottom",fill="x")
    treescrolly.pack(side="right",fill="y")


   

   
      
    

#function for loading excel data

    def  Load_excel_data():
    #if your file is valid this will load the file into the treeview
        file_path = label2_file["text"]
        file_path2 = label3_file["text"]
        global df 
        global df2 
        df=None
        df2=None
        try:
            
            #if filepath fpr discharge is not empty only load
            if file_path!="":
                excel_filename = r"{}".format(file_path)
                if excel_filename[-4:] == ".csv":
                    df = pd.read_csv(excel_filename)
                else:
                    df = pd.read_excel(excel_filename)
            #if filepath for rainfall is not empty only load
            if file_path2 !="":
                excel_filename2 = r"{}".format(file_path2)
            
                if excel_filename2[-4:] == ".csv":
                    df2 = pd.read_csv(excel_filename2)
                else:
                    df2 = pd.read_excel(excel_filename2)


        except ValueError:
            messagebox.showerror("Information", "The file you have chosen is invalid")
            return None
        except FileNotFoundError:
            messagebox.showerror("Information", f"No such file as {file_path}")
            return None

        clear_data()
        #this part need to change to tabbing
        #################################################
        #if only rainfall load
        if file_path2 !="":
              my_notebook.add(frame2,text="Rainfall")
              my_notebook.select(1)
              tv2["column"] = list(df2.columns)
              tv2["show"] = "headings"
              for column in tv2["columns"]:
                  tv2.heading(column, text=column) 

              df_rows = df2.to_numpy().tolist() 
              for row in df_rows:
                  tv2.insert("", "end", values=row) 
               
              
        
           
        
        #if Discharge is loaded
        
        if file_path !="":
            my_notebook.add(frame1,text="Discharge")
            my_notebook.select(0)
            tv1["column"] = list(df.columns)
            tv1["show"] = "headings"
            for column in tv1["columns"]:
                tv1.heading(column, text=column) 

            df_rows = df.to_numpy().tolist() 
            for row in df_rows:
                tv1.insert("", "end", values=row) 
            
             
             
              
          
            
        #################################################
    def clear_data():
        print("data")
        return None






#it will open new window
    def OpenNew():

            
                newWindow2=Toplevel(root)
                newWindow2.title("HyFFlow")
                newWindow2.geometry("500x230")
                newWindow2.resizable(0,0)
                
                def File_Dialog():
                     filename = filedialog.askopenfilename(initialdir="/",
                                          title="Select A File",
                                          filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
                     label_file.configure(text=filename)
                
            

                label_name=Label(newWindow2,text="File Name: ")
                label_name.place(x=10,y=50)



                file_frame=LabelFrame(newWindow2,bg='white')
                file_frame.place(height=30,width=378,x=10,y=69)


                label_file=Label(file_frame,text="",bg='white')
                label_file.place(x=0,y=0)

    
                b3=Button(newWindow2,text="Browse",height='1',width=7,bg='lightblue',fg='white',font="bold",command=File_Dialog)
                b3.place(x=393,y=69)
               
                
                    
                b4=Button(newWindow2,text="ok",height='1',width=7,bg='lightblue',fg='white',font="bold")
                b4.place(x=200,y=190)
               

    def ScanFile():

        file_path = label2_file["text"]
        file_path2 = label3_file["text"]
        global df
        global scannum

        if scannum == 1:
            df = pd.read_excel(file_path)
            colname = df.columns[1]
        elif scannum == 2:
            df = pd.read_excel(file_path2)
            df = pd.melt(df.reset_index(), value_vars = df.columns.values)
            df.columns = ['rainfallstations', 'rainfall']
            colname = df.columns[1]

        NewWindow = Toplevel(root)
        NewWindow.title("HyFFlow")
        NewWindow.geometry("500x200")
        NewWindow.resizable(0, 0)

        if df.isnull().values.any():
            label_question = Label(NewWindow, text="Excel file contains NULL values, would you like to remove NULL values?")
            label_question.place(x=100, y=69)
            def RemoveNA():
                df[colname].replace('', np.nan, inplace = True)
                df.dropna(inplace = True)
                messagebox.showinfo("Information","NULL values removed, file is imported successfully")
                NewWindow.destroy()
            b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=RemoveNA)
            b1.place(x=130, y=150)

            def NoRemove():
                messagebox.showinfo("Information","Please import another excel file without NULL values")
                NewWindow.destroy()
            b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=NoRemove)
            b2.place(x=280, y=150)
        else:
            messagebox.showinfo("Information", "Excel file contains no error data, file imported successfully")
            NewWindow.destroy()



    def ImportRainfall():
        filename2 = filedialog.askopenfilename(initialdir="/",
                                           title="Select A File",
                                           filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        label3_file.configure(text=filename2)

        NewWindow = Toplevel(root)
        NewWindow.title("HyFFlow")
        NewWindow.geometry("500x200")
        NewWindow.resizable(0, 0)

        label_question = Label(NewWindow, text="Would you like to scan through the data in the Excel Sheet")
        label_question.place(x=100, y=69)

        global scannum
        scannum = 2

        b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=ScanFile)
        b1.place(x=130, y=150)
        def Continue():
            messagebox.showinfo("Innformation","file is imported successfully ")
            NewWindow.destroy()
        b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=Continue)

        b2.place(x=280, y=150)




    def ImportDischarge():
        filename2 = filedialog.askopenfilename(initialdir="/",
                                           title="Select A File",
                                           filetype=(("xlsx files", "*.xlsx"), ("all files", "*.*")))
        label2_file.configure(text=filename2)

        NewWindow = Toplevel(root)
        NewWindow.title("HyFFlow")
        NewWindow.geometry("500x200")
        NewWindow.resizable(0, 0)

        global scannum
        scannum = 1

        label_question = Label(NewWindow, text="Would you like to scan through the data in the Excel Sheet")
        label_question.place(x=100, y=69)

        b1 = Button(NewWindow, text="Yes", height=1, width=7, bg="lightblue", fg="white", font="bold", command=ScanFile)
        b1.place(x=130, y=150)
        def Continue():
            messagebox.showinfo("Innformation","file is imported successfully ")
            NewWindow.destroy()
        b2 = Button(NewWindow, text="No", height=1, width=7, bg="lightblue", fg="white", font="bold", command=Continue)
        b2.place(x=280, y=150)
    





  


          
    #function for exporting file
    def ExportFile():
        print("Need to figure out")

    #function for switching package
    def function():
        print("Need to figure out function")

    #About
    def About():
        print(".......")

    #Function for selecting visualization output
    def Output():
        print("Need to figure out")
    #Function for selecting
    def All():
        print("Need to figure out")






    #Menu

    menu = Menu(root)
    root.config(menu=menu)
    filemenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="Open Graph", command=OpenFile)

    Importexcel_menu = Menu(filemenu, tearoff=0)
    Importexcel_menu.add_command(label="Discharge", command=ImportDischarge)
    Importexcel_menu.add_command(label="Rainfall", command=ImportRainfall)

    filemenu.add_cascade(label="Import Excel", menu=Importexcel_menu)

    #submenu for switching Menu
    Switchpackage_menu = Menu(filemenu, tearoff=0)
    Switchpackage_menu.add_command(label="Fundamentals of the Flow Regime", command=function)
    Switchpackage_menu.add_command(label="Flow Metrics", command=function)
    Switchpackage_menu.add_command(label="Hyrograph Shape", command=function)
    Switchpackage_menu.add_command(label="Long-term Trends on Flow and Rainfall Regimes", command=function)

    filemenu.add_cascade(label="Switch to other package", menu=Switchpackage_menu)

    filemenu.add_command(label="Export", command=ExportFile)
    filemenu.add_separator()
    def closepackage():
        root.destroy() 
        menuroot.deiconify()
    filemenu.add_command(label="Exit", command=closepackage)
    
    #Window Menu
    Windowmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Window", menu=Windowmenu)
    Windowmenu.add_command(label="About", command=About)


    #Analysis Menu
    Analysismenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Analysis", menu=Analysismenu)

    #SubMenu for selecting visualization
    Visualization_menu = Menu(Analysismenu, tearoff=0)

    Visualization_menu.add_checkbutton(label="Hydrograph and hyetrograph" , command=lambda:ty.hydro_graph(root,df,df2))
    Visualization_menu.add_checkbutton(label="Flow duration " , command=lambda:ty.flow_curve(root,df))
    Visualization_menu.add_checkbutton(label="Flood frequency" ,  command=lambda:ty.flood_curve(root,df))
    Visualization_menu.add_checkbutton(label="Median Discharge" ,  command=lambda:ty.medianDischarge(root,df))
    Visualization_menu.add_checkbutton(label="Median RainFall" ,  command=lambda:ty.median_Rain(root,df2))
    Visualization_menu.add_checkbutton(label="Anova" ,  command=lambda:an.anovaa(df2,root))
    Visualization_menu.add_checkbutton(label="Anova Post Hoc" ,  command=lambda:an.posthoc(df2,root))
    Visualization_menu.add_checkbutton(label="Rainfallstations Mean Chart" ,  command=lambda:an.barchart(df2,root))
    Visualization_menu.add_checkbutton(label="Baseflow diagram" , command= lambda:hb.baseflowdiagram(df,root))
    Visualization_menu.add_checkbutton(label="Hydrograph with Baseflow" , command=lambda:hb.hydrograph_baseflow(df,root))
    Visualization_menu.add_checkbutton(label="Plots to show of flow seasonality" , command=Output)
    Visualization_menu.add_checkbutton(label="Rainfall-runoff relations" , command=lambda:hb.linear_regression(df,df2,root))
    Visualization_menu.add_separator()
    Visualization_menu.add_checkbutton(label="select all" , command=All)

    Analysismenu.add_cascade(label="Visualization", menu=Visualization_menu)






    #Help Menu
    helpmenu = Menu(menu, tearoff=0)
    menu.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About", command=About)

    def quit_me():
        root.destroy()
        menuroot.quit()

    root.protocol("WM_DELETE_WINDOW", quit_me)