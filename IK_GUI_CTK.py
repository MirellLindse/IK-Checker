import tkinter
import customtkinter
from CTkMessagebox import CTkMessagebox
from datetime import datetime, date
import time
import os
import pdb  # построчная отладка на всякий случай!

def remove_topmost():
    app.attributes('-topmost', False)

def btnprs():
    global button_pressed
    if button_pressed == False:
        button_pressed = True
        Start()
    elif button_pressed == True:
        Again()

def Start():  # Основная функция, создаёт GUI
    global Length, Sex, Year, Months, Day, BornB, Valid, FullDOB
    Length = customtkinter.CTkLabel(app, text="Length: ")
    Length.pack(padx=40, pady=4)
    Sex = customtkinter.CTkLabel(app, text="Sex: ")
    Sex.pack(padx=40, pady=4)
    Year = customtkinter.CTkLabel(app, text="Year: ")
    Year.pack(padx=40, pady=4)
    Months = customtkinter.CTkLabel(app, text="Month: ")
    Months.pack(padx=40, pady=4)
    Day = customtkinter.CTkLabel(app, text="Day: ")
    Day.pack(padx=40, pady=4)
    FullDOB = customtkinter.CTkLabel(app, text="Full DOB:")
    FullDOB.pack(padx=40, pady=4)
    BornB = customtkinter.CTkLabel(app, text="Born before: ")
    BornB.pack(padx=40, pady=4)
    Valid = customtkinter.CTkLabel(app, text="Valid: ")
    Valid.pack(padx=40, pady=4)
    Main()

def Main():  # Проверка ИК на правильность(Наличие букв, команды Exit, длина(Равна ли 11))
    global ik
    ik = IKEntry.get()
    if any(c.isalpha() for c in ik):
        WrongInf(Len=1)
        WriteInfoWrong()
    else:
        if ik != "":
            if len(ik) != 11:
                WrongInf(Len=1)
                WriteInfoWrong()
            else:
                Length.configure(text="Length:\n OK", text_color="Green")
                YOB()

def YOB():  # Определение года рождения
    global yearG
    if ik[1:3] >= YearNow[2:4]:
        yearG = "19" + ik[1:3]
        if int(yearG) - int(YearNow[2:4]) >= 100:
            WrongInf(Y=1)
        else:
            Year.configure(text="Year:\n" + yearG)
    elif ik[1:3] <= YearNow[2:4]:
        yearG = "20" + ik[1:3]
        Year.configure(text="Year:\n" + yearG)
    SexRec()

def SexRec():  # Определение пола
    if int(ik[0]) == 0:
        WrongInf(Se=1)
        WriteInfoWrong()
    else:
        if (int(ik[0]) % 2) != 0:
            Sex.configure(text="Sex:\n Man")
            return MOB()
        elif (int(ik[0]) % 2) == 0:
            Sex.configure(text="Sex:\n Woman")
            return MOB()

def MOB():  # Определение месяца рождения
    global BMonth
    Month = ["January", "February", "March",
        "April", "May", "June",
        "July", "August", "September",
        "October", "November", "December"]
    BMonthNum = int(ik[3:5]) - 1
    if BMonthNum >= 12:
        WrongInf(Mo=1)
        WriteInfoWrong()
    else:
        BMonth = Month[int(ik[3:5]) - 1]
        Months.configure(text="Month:\n " + BMonth)
    return DOB()

def WrongInf(D=None, Y=None, Mo=None, DOBWrong=None, Len=None, Se=None, Val=None):
    if D is not None:
        Day.configure(text="Day:\n Invalid", text_color="Red")
    if Y is not None:
        Year.configure(text="Year:\n Invalid", text_color="Red")
    if Mo is not None:
        Months.configure(text="Month:\n Invalid Month", text_color="Red")
    if DOBWrong is not None:
        FullDOB.configure(text="DOB:\n Invalid", text_color="Red")
    if Len is not None:
        Length.configure(text="Length:\n Invalid", text_color="Red")
    if Se is not None:
        Sex.configure(text="Sex:\n Invalid", text_color="Red")
    if Val is not None:
        Valid.configure(text="Valid:\n Invalid", text_color="Red")

def DOB():
    if str(BMonth) == "January" or str(BMonth) == "March" or str(BMonth) == "May" or str(BMonth) == "July" or str(BMonth) == "August" or str(BMonth) == "October" or str(BMonth) == "December":
        if int(ik[5:7]) > 31:
            WrongInf(D=1, DOBWrong=1, Mo=1)
            WriteInfoWrong()
        else:
            Day.configure(text="Day:\n " + ik[5:7])
    elif str(BMonth) == "April" or str(BMonth) == "June" or str(BMonth) == "September" or str(BMonth) == "November":
        if int(ik[5:7]) > 30:
            WrongInf(D=1, DOBWrong=1, Mo=1)
            WriteInfoWrong()
        else:
            Day.configure(text="Day:\n " + ik[5:7])
    elif str(BMonth) == "February":
        if int(ik[5:7]) > 29:
            WrongInf(D=1, DOBWrong=1, Mo=1)
            WriteInfoWrong()
        elif int(ik[5:7]) > 28:
            yearG = int(ik[:4])
            if (yearG % 400 == 0) or (yearG % 4 == 0 and yearG % 100 != 0):
                Day.configure(text="Day:\n " + ik[5:7])
            else:
                WrongInf(D=1, DOBWrong=1, Mo=1)
                WriteInfoWrong()
        else:
            Day.configure(text="Day:\n " + ik[5:7])
    else:
        WrongInf(D=1, DOBWrong=1, Mo=1)
        WriteInfoWrong()
    FlDOB()
    BBS()

def FlDOB():
    FullDOB.configure(text="Full DOB:\n " + ik[5:7] + " " + BMonth + " " + yearG)

def BBS():  # Определение кол-ва родившихся до
    bik = int(ik[7:10]) - 1
    BornB.configure(text=("Born before:\n " + str(bik)))
    Validation()

def Validation():
    # Получить последнюю цифру из IK (используйте ik[-1])
    last_digit = int(ik[-1])
    # Определить два набора коеффициентов для вычисления контрольной цифры
    kordajad1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 1)
    kordajad2 = (3, 4, 5, 6, 7, 8, 9, 1, 2, 3)
    # Вычислить сумму коеффициентов, умноженных на соответствующие цифры IK
    sum1 = sum(k * int(ik[i]) for i, k in enumerate(kordajad1))
    sum2 = sum(k * int(ik[i]) for i, k in enumerate(kordajad2))
    # Вычислить остаток от деления суммы на 11
    remainder1 = sum1 % 11
    remainder2 = sum2 % 11
    # Если остаток равен 10, установить контрольную цифру в 0
    if remainder1 == 10:
        control_digit = 0
    else:
        control_digit = remainder1
    # Проверить, совпадает ли вычисленная контрольная цифра с последней цифрой в IK
    if control_digit == last_digit:
        Valid.configure(text=("Valid: OK"), text_color="Green")
    else:
        Valid.configure(text=("Valid: NO"), text_color="Red")
    WriteInfo()

def WriteInfo():  # Запись информации в текстовый документ
    a = Sex.cget("text")
    b = Year.cget("text")
    c = Months.cget("text")
    d = Day.cget("text")
    e = BornB.cget("text")
    f = Valid.cget("text")
    Nam = IKEntry.get()
    data = f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n"
    folder_name = "Valid"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    with open(os.path.join(folder_name, Nam + ".txt"), "w") as file:
        file.write(data)

def WriteInfoWrong():  # Запись информации в текстовый документ в случае неправильного ИК
    a = Sex.cget("text")
    b = Year.cget("text")
    c = Months.cget("text")
    d = Day.cget("text")
    e = BornB.cget("text")
    f = Valid.cget("text")
    Nam = IKEntry.get()
    data = f"{a}\n{b}\n{c}\n{d}\n{e}\n{f}\n"
    folder_name = "Invalid"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    with open(os.path.join(folder_name, Nam + ".txt"), "w") as file:
        file.write(data)

def Again():
    Length.destroy()
    Sex.destroy()
    Year.destroy()
    Months.destroy()
    Day.destroy()
    BornB.destroy()
    Valid.destroy()
    FullDOB.destroy()
    # app.destroy()
    Start()

def GUI():
    global app
    app = customtkinter.CTk()
    CTkMessagebox(title="Внимание!", message="Для корректной работы программы её исполняемый файл должен быть в отдельной папке", icon="warning", option_1="ПОнял")
    app.geometry("400x450")
    app.title("IK Checker")
    app.attributes('-topmost', True)
    app.after(5, remove_topmost)
    app.columnconfigure(40, weight=1)
    app.rowconfigure(40, weight=1)
    w = app.winfo_screenwidth()
    h = app.winfo_screenheight()
    w = w // 2  # середина экрана
    h = h // 2
    w = w - 200  # смещение от середины
    h = h - 200
    global IKEntry
    LabelMain1 = customtkinter.CTkLabel(app, text="Insert IK")
    LabelMain1.pack(padx=40, pady=5)
    IKEntry = customtkinter.CTkEntry(app, width=100)
    IKEntry.pack(padx=40, pady=0)
    IKEntry.configure(width=140)
    Gobtn = customtkinter.CTkButton(app, text="Check", command=btnprs)
    Gobtn.pack(padx=30, pady=10)
    update_time()
    app.mainloop()

def update_time():
    TimeLabel = customtkinter.CTkLabel(app, text="")
    TimeLabel.place(x=150, y=430)
    todays_date = str(date.today())
    current_time = time.strftime('%H:%M:%S')
    TimeLabel.configure(text=str(todays_date) + " " + str(current_time))
    app.after(1000, update_time)

button_pressed = False

YearNow = str(datetime.now().year)

GUI()
