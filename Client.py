import socket
from tkinter import *
from tkinter import messagebox
from time import *
from PIL import Image, ImageTk
import json

client_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_sock.connect(('127.0.0.1', 53210))

def on_closing():
    if messagebox.askokcancel('Закрытие приложения', 'Вы действительно хотите выйти?'):
        tk.destroy()
        client_sock.close()
def sendmet():
    global f_ex,f1_ex,f2_ex,label_tit_met,en_f_e,button_m,label_tit2_met
    client_sock.sendall(json.dumps(f_ex.get()).encode('utf8'))
    f_ex.set(2)
    n1buffer = client_sock.recv(1024).decode('utf8')
    n1 = json.loads(n1buffer)
    if n1!="n":
        n2buffer = client_sock.recv(1024).decode('utf8')
        n2 = json.loads(n2buffer)
        f1_ex.config(text=n1)
        f2_ex.config(text=n2)
    else:
        label_tit_met.place(relx=0.3, rely=0.05, anchor='nw')
        en_f_e.place(width=150, height=30,relx=0.32, rely=0.1)
        button_m.place(height=50, width=300, relx=0.32, rely=0.2)
        label_tit2_met.place_forget()
        f1_ex.place_forget()
        f2_ex.place_forget()
        build_mat()
def build_mat():
    global kolich,text_m
    arrbuffer = client_sock.recv(1024).decode('utf8')
    arr = json.loads(arrbuffer)
    mas_gor = []
    mas_ver = []
    mas_all = []
    mas_ver2 = []
    mas_zn = []
    for i in range(kolich):
        mas_all.append([])
        mas_gor.append(Label(frame_met, text=i+1, font="Arial 8", bg='#808080',width=8,height=1))
        mas_gor[i].place(x=100+56*i, y=198)
        mas_ver.append(Label(frame_met, text=i + 1, font="Arial 8", bg='#808080', width=8, height=1))
        mas_ver[i].place(x=44, y=220+22*i)
    for i in range(kolich):
        cs = 0
        for j in range(kolich):
            if i>j:
                if (arr[j][i] == 0):
                    mas_all[i].append(Label(frame_met, text="1", font="Arial 8", bg='#00a600', width=8, height=1))
                    cs += 1
                else:
                    mas_all[i].append(Label(frame_met, text="0", font="Arial 8", bg='#999999', width=8, height=1))
            elif j>i:
                if (arr[i][j] == 1):
                    mas_all[i].append(Label(frame_met, text="1", font="Arial 8", bg='#00a600', width=8, height=1))
                    cs += 1
                else:
                    mas_all[i].append(Label(frame_met, text="0", font="Arial 8", bg='#999999', width=8, height=1))
            else:
                mas_all[i].append(Label(frame_met, text="0", font="Arial 8", bg='#999999', width=8, height=1))
            mas_all[i][j].place(x=100 + 56 * j, y=220 + 22 * i)
        mas_zn.append(cs)
    for i in range(kolich):
        mas_ver2.append(
            Label(frame_met, text=mas_zn[i], font="Arial 8", bg='#505050', width=8, height=1, fg='white'))
        mas_ver2[i].place(x=100 + 56 * kolich, y=220 + 22 * i)
    client_sock.sendall(json.dumps(mas_zn).encode('utf8'))
    for i in range(kolich):
        elbuffer = client_sock.recv(1024).decode('utf8')
        el = json.loads(elbuffer)
        text_m.insert(END, str(el[0]) + ". " + str(el[1]) + "\n")




redable=0
vismenu=True
tk = Tk()
tk.title('Приложение ООО "Ресторан"')
tk.geometry("700x600+400+100")
tk.protocol('WM_DELETE_WINDOW', on_closing)
canvas = Canvas(tk)
canvas.place(relwidth='1', relheight='1')
image = Image.open('fon2.jpg')
image = image.resize((700, 600))
image = ImageTk.PhotoImage(image)
im_title = Label(canvas, image=image, bg='#fafafa')
im_title.pack()

tka=Toplevel(tk)

tka.title('Меню "Администратор"')
tka.withdraw()
tka.protocol('WM_DELETE_WINDOW', on_closing)
canvasa = Canvas(tka, bg='#ffffff')
canvasa.place(relwidth=1, relheight=1)

framea = Frame(canvasa, bg='#fa8072')
framea.place(relx=0, rely=0.1, relwidth=0.2, relheight=1)
frameatit = Frame(canvasa, bg='#dc143c')
frameatit.place(relx=0, rely=0, relwidth=1, relheight=0.1)
bdconst=0
labeltit = Label(frameatit, text='Администратор', anchor='e', font="Arial 22", fg='white',bg='#dc143c')
labeltit.place(relx=0.8, rely=0.23)
image0 = Image.open('exit.png')
image0 = image0.resize((40, 40))
image0 = ImageTk.PhotoImage(image0)
im_title0 = Label(frameatit, image=image0,bg='#dc143c')
im_title0.place(relx=0.95, rely=0.2)

labeltit2 = Label(frameatit, text='ООО "Ресторан"', anchor='e', font="Arial 24", fg='white',bg='#dc143c')
labeltit2.place(relx=0.44, rely=0.15,height=70)
image22 = Image.open('ikon.png')
image22 = image22.resize((50, 50))
image22 = ImageTk.PhotoImage(image22)
im_title22 = Label(frameatit, image=image22,bg='#dc143c')
im_title22.place(relx=0.4, rely=0.2)

lmenu = Label(canvasa, text="Меню ", font="Arial 16", fg='#ffffff',bg='#dc143c', bd=bdconst, relief='solid',anchor='w',padx=80)
lmenu.place(x=0, y=25, width=200, height=40)
image11 = Image.open('menu.png')
image11 = image11.resize((30, 30))
image11 = ImageTk.PhotoImage(image11)
im_title11 = Label(lmenu, image=image11,bg='#dc143c')
im_title11.place(x=22,y=0)

ladd = Label(framea, text="Добавить ", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
ladd.place(relx=0, rely=0, relwidth=1, relheight=0.08)
image1 = Image.open('add.png')
image1 = image1.resize((30, 30))
image1 = ImageTk.PhotoImage(image1)
im_title1 = Label(ladd, image=image1,bg='#fa8072')
im_title1.place(x=25,y=15)

lshow = Label(framea, text="Вывести данные", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
lshow.place(relx=0, rely=0.08, relwidth=1, relheight=0.08)
image2 = Image.open('show.png')
image2 = image2.resize((30, 30))
image2 = ImageTk.PhotoImage(image2)
im_title2 = Label(lshow, image=image2,bg='#fa8072')
im_title2.place(x=25,y=15)

lred = Label(framea, text="Редактировать", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
lred.place(relx=0, rely=0.16, relwidth=1, relheight=0.08)
image3 = Image.open('red.png')
image3 = image3.resize((30, 30))
image3 = ImageTk.PhotoImage(image3)
im_title3 = Label(lred, image=image3,bg='#fa8072')
im_title3.place(x=25,y=15)

ldel = Label(framea, text="Удалить", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
ldel.place(relx=0, rely=0.24, relwidth=1, relheight=0.08)
image4 = Image.open('del.png')
image4 = image4.resize((30, 30))
image4 = ImageTk.PhotoImage(image4)
im_title4 = Label(ldel, image=image4,bg='#fa8072')
im_title4.place(x=25,y=15)

lsearch = Label(framea, text="Поиск", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
lsearch.place(relx=0, rely=0.32, relwidth=1, relheight=0.08)
image5 = Image.open('search.png')
image5 = image5.resize((30, 30))
image5 = ImageTk.PhotoImage(image5)
im_title5 = Label(lsearch, image=image5,bg='#fa8072')
im_title5.place(x=25,y=15)

lsort = Label(framea, text="Сортировка", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
lsort.place(relx=0, rely=0.4, relwidth=1, relheight=0.08)
image6 = Image.open('sort.png')
image6 = image6.resize((30, 30))
image6 = ImageTk.PhotoImage(image6)
im_title6 = Label(lsort, image=image6,bg='#fa8072')
im_title6.place(x=25,y=15)

lexp = Label(framea, text="Экспертный метод", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
lexp.place(relx=0, rely=0.48, relwidth=1, relheight=0.08)
image6_1 = Image.open('exp.png')
image6_1 = image6_1.resize((30, 30))
image6_1= ImageTk.PhotoImage(image6_1)
im_title6_1 = Label(lexp, image=image6_1,bg='#fa8072')
im_title6_1.place(x=25,y=15)

lfiltr = Label(framea, text="Фильтрация", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
lfiltr.place(relx=0, rely=0.56, relwidth=1, relheight=0.08)
image7 = Image.open('filtr.png')
image7 = image7.resize((30, 30))
image7 = ImageTk.PhotoImage(image7)
im_title7 = Label(lfiltr, image=image7,bg='#fa8072')
im_title7.place(x=25,y=15)

lotch = Label(framea, text="Вывод отчёта", font="Arial 16", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=80)
lotch.place(relx=0, rely=0.64, relwidth=1, relheight=0.08)
image8 = Image.open('otch.png')
image8 = image8.resize((30, 30))
image8 = ImageTk.PhotoImage(image8)
im_title8 = Label(lotch, image=image8,bg='#fa8072')
im_title8.place(x=25,y=15)

image9 = Image.open('line.png')
image9 = image9.resize((250, 21))
image9 = ImageTk.PhotoImage(image9)
im_title9 = Label(framea, image=image9,bg='#fa8072')
im_title9.place(relx=0.05,rely=0.72)

lreguser = Label(framea, text="Добавить пользователя", font="Arial 12", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=40)
lreguser.place(relx=0, rely=0.85, relwidth=1, relheight=0.05)
ldeluser = Label(framea, text="Удалить пользователя", font="Arial 12", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=40)
ldeluser.place(relx=0, rely=0.79, relwidth=1, relheight=0.05)
lchan = Label(framea, text="Изменить пароль", font="Arial 12", fg='#ffffff',bg='#fa8072', bd=bdconst, relief='solid',anchor='w',padx=40)
lchan.place(relx=0, rely=0.83, relwidth=1, relheight=0.05)


frame_add_user=Frame(canvasa, bg='#ffffff')
label_add_log = Label(frame_add_user, text="Логин: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_log.place(relx=0.15, rely=0.2, anchor='ne')
label_add_pas = Label(frame_add_user, text="Пароль: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_pas.place(relx=0.15, rely=0.3, anchor='ne')
add_login = StringVar()
add_enlog = Entry(frame_add_user, textvariable=add_login,font="Arial 12")
add_password = StringVar()
add_enpas = Entry(frame_add_user, textvariable=add_password,font="Arial 12")
add_enlog.place(width=300, height=30,relx=0.15, rely=0.2)
add_enpas.place(width=300,height=30, relx=0.15, rely=0.3)
label_add_title = Label(frame_add_user, text="Добавление нового пользователя", font="Arial 14", bg='#ffffff')
label_add_title.place(relx=0.15, rely=0.1)


button_add_user = Button(frame_add_user, text="Добавить")
button_add_user.place(height=50, width=300, relx=0.15, rely=0.37)
button_cancel_user = Button(frame_add_user, text="Отмена")
button_cancel_user.place(height=50, width=150, relx=0.21, rely=0.45)


frame_chan=Frame(canvasa, bg='#ffffff')
label_oldpas = Label(frame_chan, text="Старый пароль: ", anchor='e', font="Arial 14", bg='#ffffff')
label_oldpas.place(relx=0.15, rely=0.2, anchor='ne')
label_newpas = Label(frame_chan, text="Новый пароль: ", anchor='e', font="Arial 14", bg='#ffffff')
label_newpas.place(relx=0.15, rely=0.3, anchor='ne')
oldpas = StringVar()
enoldpas = Entry(frame_chan, textvariable=oldpas,font="Arial 12")
newpas = StringVar()
ennewpas = Entry(frame_chan, textvariable=newpas,font="Arial 12")
enoldpas.place(width=300, height=30,relx=0.15, rely=0.2)
ennewpas.place(width=300,height=30, relx=0.15, rely=0.3)
label_chan_title = Label(frame_chan, text="Смена пароля", font="Arial 14", bg='#ffffff')
label_chan_title.place(relx=0.15, rely=0.1)

button_chan_pas = Button(frame_chan, text="Изменить пароль")
button_chan_pas.place(height=50, width=300, relx=0.15, rely=0.37)
button_cancel_chan = Button(frame_chan, text="Отмена")
button_cancel_chan.place(height=50, width=150, relx=0.21, rely=0.45)

frame_del_user=Frame(canvasa, bg='#ffffff')
label_log = Label(frame_del_user, text="Логин пользователя: ", anchor='e', font="Arial 14", bg='#ffffff')
label_log.place(relx=0.2, rely=0.2, anchor='ne')
log_of_user = StringVar()
en_of_user = Entry(frame_del_user, textvariable=log_of_user,font="Arial 12")
en_of_user.place(width=300, height=30,relx=0.2, rely=0.2)
label_deluser_title = Label(frame_del_user, text="Удалить пользователя", font="Arial 14", bg='#ffffff')
label_deluser_title.place(relx=0.2, rely=0.1)
button_deluser = Button(frame_del_user, text="Удалить")
button_deluser.place(height=50, width=300, relx=0.2, rely=0.27)
button_cancel_deluser = Button(frame_del_user, text="Отмена")
button_cancel_deluser.place(height=50, width=150, relx=0.26, rely=0.35)


#########################################фрейм добавления
frame_add=Frame(canvasa, bg='#ffffff')
label_add_f = Label(frame_add, text="Фамилия: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_f.place(relx=0.2, rely=0.1, anchor='ne')
add_f = StringVar()
en_add_f = Entry(frame_add, textvariable=add_f,font="Arial 12")
en_add_f.place(width=300, height=30,relx=0.2, rely=0.1)
label_add_title = Label(frame_add, text="Данные официанта", font="Arial 14", bg='#ffffff')
label_add_title.place(relx=0.2, rely=0)

label_add_i = Label(frame_add, text="Имя: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_i.place(relx=0.2, rely=0.2, anchor='ne')
add_i = StringVar()
en_add_i = Entry(frame_add, textvariable=add_i,font="Arial 12")
en_add_i.place(width=300, height=30,relx=0.2, rely=0.2)

label_add_o = Label(frame_add, text="Отчество: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_o.place(relx=0.2, rely=0.3, anchor='ne')
add_o = StringVar()
en_add_o = Entry(frame_add, textvariable=add_o,font="Arial 12")
en_add_o.place(width=300, height=30,relx=0.2, rely=0.3)

label_add_d = Label(frame_add, text="День: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_d.place(relx=0.2, rely=0.4, anchor='ne')
add_d = StringVar()
en_add_d = Entry(frame_add, textvariable=add_d,font="Arial 12")
en_add_d.place(width=300, height=30,relx=0.2, rely=0.4)

label_add_m = Label(frame_add, text="Месяц: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_m.place(relx=0.2, rely=0.5, anchor='ne')
add_m = StringVar()
en_add_m = Entry(frame_add, textvariable=add_m,font="Arial 12")
en_add_m.place(width=300, height=30,relx=0.2, rely=0.5)

label_add_y = Label(frame_add, text="Год: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_y.place(relx=0.2, rely=0.6, anchor='ne')
add_y = StringVar()
en_add_y = Entry(frame_add, textvariable=add_y,font="Arial 12")
en_add_y.place(width=300, height=30,relx=0.2, rely=0.6)

label_add_s = Label(frame_add, text="Зарплата: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_s.place(relx=0.2, rely=0.7, anchor='ne')
add_s = StringVar()
en_add_s = Entry(frame_add, textvariable=add_s,font="Arial 12")
en_add_s.place(width=300, height=30,relx=0.2, rely=0.7)

label_add_st = Label(frame_add, text="Стаж работы: ", anchor='e', font="Arial 14", bg='#ffffff')
label_add_st.place(relx=0.2, rely=0.8, anchor='ne')
add_st = StringVar()
en_add_st = Entry(frame_add, textvariable=add_st,font="Arial 12")
en_add_st.place(width=300, height=30,relx=0.2, rely=0.8)

button_add = Button(frame_add, text="Добавить")
button_add.place(height=50, width=300, relx=0.2, rely=0.85)
button_cancel_add = Button(frame_add, text="Отмена")
button_cancel_add.place(height=50, width=150, relx=0.45, rely=0.85)

########################фрейм вывода
frame_print=Frame(canvasa, bg='#ffffff')
text_show = Text(frame_print,width=93, height=23, bg="white",
            fg='black', wrap=WORD,font=("Consolas", 16))
text_show.place(relx=0.05,rely=0.1)
button_show = Button(frame_print, text="Вывести")
button_show.place(height=50, width=300, relx=0.2, rely=0.9)
label_show_title = Label(frame_print, text="Вывод данных в табличном виде", font="Arial 14", bg='#ffffff')
label_show_title.place(relx=0.25, rely=0.02)


###############################редактирование
label_red = Label(frame_add, text="Номер для редактирования: ", anchor='e', font="Arial 14", bg='#ffffff')
red_n = StringVar()
en_red_n = Entry(frame_add, textvariable=red_n,font="Arial 12")
button_red_n = Button(frame_add, text="Отобразить")


##################################фрейм удаления
frame_del=Frame(canvasa, bg='#ffffff')
label_del = Label(frame_del, text="Порядковый номер: ", anchor='e', font="Arial 14", bg='#ffffff')
label_del.place(relx=0.2, rely=0.2, anchor='ne')
del_n = StringVar()
en_del_n = Entry(frame_del, textvariable=del_n,font="Arial 12")
en_del_n.place(width=300, height=30,relx=0.2, rely=0.2)
label_add_title = Label(frame_del, text="Удаление данных", font="Arial 14", bg='#ffffff')
label_add_title.place(relx=0.2, rely=0.1)
button_del = Button(frame_del, text="Удалить")
button_del.place(height=50, width=300, relx=0.2, rely=0.27)
button_cancel_del = Button(frame_del, text="Отмена")
button_cancel_del.place(height=50, width=150, relx=0.26, rely=0.35)



###################################фрейм поиска
frame_search=Frame(canvasa, bg='#ffffff')
text_s = Text(frame_search,width=93, height=18, bg="white",
            fg='black', wrap=WORD,font=("Consolas", 16))
text_s.place(relx=0.05,rely=0.1)
button_s = Button(frame_search, text="Поиск")
button_s.place(height=50, width=300, relx=0.2, rely=0.9)
label_s_title = Label(frame_search, text="Фамилия:", font="Arial 14", bg='#ffffff')
label_s_title.place(relx=0.1, rely=0.05)
s_n = StringVar()
en_s_n = Entry(frame_search, textvariable=s_n,font="Arial 12")
en_s_n.place(width=300, height=30,relx=0.2, rely=0.05)

#################################фрейм сортировки
frame_sort=Frame(canvasa, bg='#ffffff')
label_sort = Label(frame_sort, text="Сортировать данные по: ", anchor='e', font="Arial 14", bg='#ffffff')
label_sort.place(relx=0.1, rely=0.15, anchor='nw')
sort_n = IntVar()
sort_fio=Radiobutton(frame_sort,text="ФИО", value=1, variable=sort_n,font="Arial 11", bg='#ffffff')
sort_fio.place(relx=0.1, rely=0.25)
sort_date=Radiobutton(frame_sort,text="Дата", value=2, variable=sort_n,font="Arial 11", bg='#ffffff')
sort_date.place(relx=0.1, rely=0.3)
sort_s=Radiobutton(frame_sort,text="Зарплата", value=3, variable=sort_n,font="Arial 11", bg='#ffffff')
sort_s.place(relx=0.1, rely=0.35)
sort_st=Radiobutton(frame_sort,text="Стаж", value=4, variable=sort_n,font="Arial 11", bg='#ffffff')
sort_st.place(relx=0.1, rely=0.4)
button_sort = Button(frame_sort, text="Сортировать записи")
button_sort.place(height=50, width=300, relx=0.1, rely=0.46)
button_cancel_sort = Button(frame_sort, text="Отмена")
button_cancel_sort.place(height=50, width=150, relx=0.15, rely=0.54)


#################################фрейм фильрации
frame_filtr=Frame(canvasa, bg='#ffffff')
text_f = Text(frame_filtr,width=93, height=18, bg="white",
            fg='black', wrap=WORD,font=("Consolas", 16))
text_f.place(relx=0.05,rely=0.2)
button_f = Button(frame_filtr, text="Фильтрация")
button_f.place(height=50, width=300, relx=0.4, rely=0.05)
label_f1_title = Label(frame_filtr, text="от", font="Arial 14", bg='#ffffff')
label_f1_title.place(relx=0.16, rely=0.05)
f1_n = StringVar()
label_f2_title = Label(frame_filtr, text="до", font="Arial 14", bg='#ffffff')
label_f2_title.place(relx=0.16, rely=0.1)
f2_n = StringVar()
en_f1_n = Entry(frame_filtr, textvariable=f1_n,font="Arial 12")
en_f1_n.place(width=150, height=30,relx=0.2, rely=0.05)
en_f2_n = Entry(frame_filtr, textvariable=f2_n,font="Arial 12")
en_f2_n.place(width=150, height=30,relx=0.2, rely=0.1)
f_r = IntVar()
f1_r=Radiobutton(frame_filtr,text="Зарплата", value=1, variable=f_r,font="Arial 11", bg='#ffffff')
f1_r.place(relx=0.05, rely=0.05)
f2_r=Radiobutton(frame_filtr,text="Стаж", value=2, variable=f_r,font="Arial 11", bg='#ffffff')
f2_r.place(relx=0.05, rely=0.1)


#################################фрейм метода
frame_met=Frame(canvasa, bg='#ffffff')
label_tit_met = Label(frame_met, text="Количество официантов для сравнения:", anchor='e', font="Arial 14", bg='#ffffff')
label_tit_met.place(relx=0.3, rely=0.05, anchor='nw')
f_e = StringVar()
en_f_e = Entry(frame_met, textvariable=f_e,font="Arial 12")
en_f_e.place(width=150, height=30,relx=0.32, rely=0.1)
label_tit2_met = Label(frame_met, text="Выберите лучшего официанта:", anchor='e', font="Arial 14", bg='#ffffff')
#label_tit2_met.place(relx=0.05, rely=0.2, anchor='nw')
button_m = Button(frame_met, text="Начать")
button_m.place(height=50, width=300, relx=0.32, rely=0.17)
text_m = Text(frame_met,width=28, height=7, bg="white",
            fg='black', wrap=WORD,font=("Consolas", 16))
text_m.place(relx=0.7,rely=0.02)
f_ex = IntVar()
f_ex.set(2)
f1_ex=Radiobutton(frame_met,text="Зарплата", value=1, variable=f_ex,font="Arial 14", bg='#ffffff',command=sendmet)
#f1_ex.place(relx=0.05, rely=0.26)
f2_ex=Radiobutton(frame_met,text="Стаж", value=0, variable=f_ex,font="Arial 14", bg='#ffffff',command=sendmet)
#f2_ex.place(relx=0.05, rely=0.32)

############################фрейм отчета
frame_otch=Frame(canvasa, bg='#ffffff')
label_tit_o = Label(frame_otch, text="Печать отчета: otchet.txt", anchor='e', font="Arial 14", bg='#ffffff')
label_tit_o.place(relx=0.3, rely=0.05, anchor='nw')
button_o = Button(frame_otch, text="Напечатать отчет")
button_o.place(height=50, width=300, relx=0.27, rely=0.1)

frame_empty=Frame(canvasa, bg='#ffffff')
frame_empty.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.9)
prevframe=frame_empty

def menu_user():
    global enpas, enlog, labelwrong
    global ladd,ldel,lred,lreguser,ldeluser,lchan,im_title9,lshow,lsearch,lsort,lexp,lfiltr,lotch

    enpas.delete(0, 'end')
    enlog.delete(0, 'end')
    labelwrong.config(text='')
    tk.withdraw()
    tka.deiconify()
    tka.wm_state('zoomed')
    ladd.place_forget()
    ldel.place_forget()
    lred.place_forget()
    lreguser.place_forget()
    ldeluser.place_forget()
    lchan.place_forget()
    im_title9.place_forget()
    labeltit.config(text="Пользователь")
    lshow.place(relx=0, rely=0, relwidth=1, relheight=0.08)
    lsearch.place(relx=0, rely=0.08, relwidth=1, relheight=0.08)
    lsort.place(relx=0, rely=0.16, relwidth=1, relheight=0.08)
    lexp.place(relx=0, rely=0.24, relwidth=1, relheight=0.08)
    lfiltr.place(relx=0, rely=0.32, relwidth=1, relheight=0.08)
    lotch.place(relx=0, rely=0.4, relwidth=1, relheight=0.08)

def menu_admin():
    global enpas,enlog,labelwrong
    enpas.delete(0, 'end')
    enlog.delete(0, 'end')
    labelwrong.config(text='')
    tk.withdraw()
    tka.deiconify()
    tka.wm_state('zoomed')
    labeltit.config(text="Администратор")
    ladd.place(relx=0, rely=0, relwidth=1, relheight=0.08)
    lshow.place(relx=0, rely=0.08, relwidth=1, relheight=0.08)
    lred.place(relx=0, rely=0.16, relwidth=1, relheight=0.08)
    ldel.place(relx=0, rely=0.24, relwidth=1, relheight=0.08)
    lsearch.place(relx=0, rely=0.32, relwidth=1, relheight=0.08)
    lsort.place(relx=0, rely=0.4, relwidth=1, relheight=0.08)
    lexp.place(relx=0, rely=0.48, relwidth=1, relheight=0.08)
    lfiltr.place(relx=0, rely=0.56, relwidth=1, relheight=0.08)
    lotch.place(relx=0, rely=0.64, relwidth=1, relheight=0.08)
    im_title9.place(relx=0.05, rely=0.72)
    lreguser.place(relx=0, rely=0.75, relwidth=1, relheight=0.05)
    ldeluser.place(relx=0, rely=0.79, relwidth=1, relheight=0.05)
    lchan.place(relx=0, rely=0.83, relwidth=1, relheight=0.05)

def ent():
    global global_login
    if (login.get() != "" and password.get() != ""):
        if (adm.get() == True):
            client_sock.sendall("a".encode('utf8'))
        else:
            client_sock.sendall("u".encode('utf8'))
        sleep(0.01)
        client_sock.sendall("e".encode('utf8'))
        sleep(0.01)
        client_sock.sendall(login.get().encode('utf8'))
        sleep(0.01)
        client_sock.sendall(password.get().encode('utf8'))
        ifmenubuffer=client_sock.recv(1024).decode('utf8')
        ifmenu = json.loads(ifmenubuffer)
        if (ifmenu == "a"):
            global_login=login.get()
            menu_admin()
        elif (ifmenu == "u"):
            menu_user()
        else:
            labelwrong.config(text="Данные введены неверно")


def reg():
    global global_login
    if (login.get() != "" and password.get() != ""):
        if (adm.get() == True):
            client_sock.send("a".encode('utf8'))
        else:
            client_sock.send("u".encode('utf8'))
        sleep(0.01)
        client_sock.send("r".encode('utf8'))
        sleep(0.01)
        client_sock.send(login.get().encode('utf8'))
        sleep(0.01)
        client_sock.send(password.get().encode('utf8'))
        ifmenubuffer = client_sock.recv(1024).decode('utf8')
        ifmenu = json.loads(ifmenubuffer)
        if (ifmenu == "a"):
            global_login = login.get()
            menu_admin()
        elif (ifmenu == "u"):
            menu_user()


labtitle = Label(canvas, text='ООО "Ресторан"', relief='ridge', bd=2, bg='#bc544b',
                 font='TimesNewRoman 14 bold')  # , padx='100')
labtitle.place(relwidth=1, relheight=0.1)
frame = Frame(canvas, bg='#fafafa', bd=5, relief='ridge', )
frame.place(relx=0.28, rely=0.32, relwidth=0.4, relheight=0.4)

btn = Button(canvas, text="Войти", command=ent)
btn.place(height=40, width=100, x=300, y=300)
btn1 = Button(canvas, text="Зарегистрироваться", command=reg)
btn1.place(height=30, x=290, y=350)
labelwrong = Label(text="", fg="red", anchor='e', font="Arial 10", bg='#fafafa')
labelwrong.place(x=430, y=220, anchor='ne')
label1 = Label(canvas, text="Логин: ", anchor='e', font="Arial 10", bg='#fafafa')
label1.place(x=300, y=250, anchor='ne')
label2 = Label(canvas, text="Пароль: ", anchor='e', font="Arial 10", bg='#fafafa')
label2.place(x=300, y=275, anchor='ne')

login = StringVar()
enlog = Entry(canvas, textvariable=login)
password = StringVar()
enpas = Entry(canvas, textvariable=password, show='*')
enlog.place(width=100, x=300, y=250)
enpas.place(width=100, x=300, y=275)

adm = IntVar()
admc = Checkbutton(canvas, text="Администратор", variable=adm, bg='#fafafa')
admc.place(x=300, y=390)
def labe(event,f,t):
    if event.type == '7':
        f.config(font="Arial 18")
        t.config(font="Arial 18")
    elif event.type == '8':
        f.config(font="Arial 16")
        t.config(font="Arial 18")
def labtite(event,f):
    global image0
    image0 = Image.open('exit.png')
    if event.type == '7':
        image0 = image0.resize((51, 51))
        image0 = ImageTk.PhotoImage(image0)
        f.config(image=image0)
    elif event.type == '8':
        image0 = image0.resize((40, 40))
        image0 = ImageTk.PhotoImage(image0)
        f.config(image=image0)
def labdop(event,f):
    if event.type == '7':
        f.config(font="Arial 13")
    elif event.type == '8':
        f.config(font="Arial 12")
def exi(event):
    global vismenu, prevframe, frame_empty
    prevframe.place_forget()
    frame_empty.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.9)
    prevframe = frame_empty
    framea.place(relx=0, rely=0.1, relwidth=0.2, relheight=1)
    vismenu = True
    client_sock.sendall(json.dumps("exit").encode('utf8'))
    tka.withdraw()
    tk.deiconify()
def viewmenu(event):
    global vismenu,framea
    if vismenu:
        framea.place_forget()
        vismenu=False
    else:
        framea.place(relx=0, rely=0.1, relwidth=0.2, relheight=1)
        vismenu=True
def cancel(event):
    global vismenu,prevframe,frame_empty
    prevframe.place_forget()
    frame_empty.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.9)
    prevframe=frame_empty
    framea.place(relx=0, rely=0.1, relwidth=0.2, relheight=1)
    vismenu=True
def viewframe(event,frame,red=0):
    global prevframe
    prevframe.place_forget()
    frame.place(relx=0.2, rely=0.1, relwidth=0.8, relheight=0.9)
    prevframe=frame
    if red==1:
        viewred()
    if red==-1:
        notviewred()
def add_user(event):
    label_add_title.config(text="Добавление нового пользователя")
    global add_enpas,add_enlog,add_login, add_password,label_added_user
    if (add_login.get() != "" and add_password.get() != ""):
        client_sock.sendall(json.dumps("add_user").encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(add_login.get()).encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(add_password.get()).encode('utf8'))
        label_add_title.config(text="Пользователь добавлен")
        add_enpas.delete(0, 'end')
        add_enlog.delete(0, 'end')
def chan_pas(event):
    global oldpas,newpas,global_login,ennewpas,enoldpas
    label_chan_title.config(text="Смена пароля")
    if (oldpas.get() != "" and newpas.get() != ""):
        client_sock.sendall(json.dumps("chan_pas").encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(global_login).encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(oldpas.get()).encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(newpas.get()).encode('utf8'))

        chanbuffer = client_sock.recv(1024).decode('utf8')
        changed = json.loads(chanbuffer)
        if(changed=="changed"):
            label_chan_title.config(text="Пароль успешно изменен")
            ennewpas.delete(0, 'end')
            enoldpas.delete(0, 'end')
        else:
            label_chan_title.config(text="Данные введены неверно")
def deluser(event):
    global en_of_user,log_of_user
    label_deluser_title.config(text="Удалить пользователя")
    if (log_of_user.get() != ""):
        client_sock.sendall(json.dumps("deluser").encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(log_of_user.get()).encode('utf8'))

        deletedbuffer = client_sock.recv(1024).decode('utf8')
        deleted = json.loads(deletedbuffer)
        if (deleted == "deleted"):
            label_deluser_title.config(text="Пользователь удален")
            en_of_user.delete(0, 'end')
        else:
            label_deluser_title.config(text="Данные введены неверно")
def add(event,f):
    global en_add_f,en_add_i,en_add_o,en_add_d,en_add_m,en_add_y,en_add_s,en_add_st,en_red_n,red_n
    global add_f, add_i, add_o, add_d, add_m, add_y, add_s, add_st
    global redable
    global text_show,text_f,text_s,text_m
    text_show.delete(1.0, 'end')
    text_f.delete(1.0, 'end')
    text_s.delete(1.0, 'end')
    text_m.delete(1.0, 'end')
    if (add_f.get() != "" and add_i.get() != "" and add_o.get() != "" and add_d.get() != "" and add_m.get() != ""
            and add_y.get() != "" and add_s.get() != "" and add_st.get() != ""):
        if (add_d.get().isnumeric() and add_m.get().isnumeric() and add_y.get().isnumeric() and add_s.get().isnumeric() and
        add_st.get().isnumeric()):
            if (int(add_d.get())>0 and int(add_d.get())<32 and int(add_m.get())>0 and int(add_m.get())<13 and
                    int(add_y.get())>1900 and int(add_y.get())<2050  and
                    int(add_s.get())>0 and int(add_st.get())>=0):
                mas=[]
                mas.append(add_f.get())
                mas.append(add_i.get())
                mas.append(add_o.get())
                mas.append(int(add_d.get()))
                mas.append(int(add_m.get()))
                mas.append(int(add_y.get()))
                mas.append(int(add_s.get()))
                mas.append(int(add_st.get()))
                if redable == 0:
                    client_sock.sendall(json.dumps("add").encode('utf8'))
                elif redable == 1:
                    client_sock.sendall(json.dumps("red").encode('utf8'))
                    client_sock.sendall(json.dumps(red_n.get()).encode('utf8'))
                sleep(0.01)
                client_sock.sendall(json.dumps(mas).encode('utf8'))
                sleep(0.01)
                en_add_f.delete(0, 'end')
                en_add_i.delete(0, 'end')
                en_add_o.delete(0, 'end')
                en_add_d.delete(0, 'end')
                en_add_m.delete(0, 'end')
                en_add_y.delete(0, 'end')
                en_add_s.delete(0, 'end')
                en_add_st.delete(0, 'end')
                if redable == 1:
                    en_red_n.delete(0, 'end')
def show(event):
    global text_show
    client_sock.sendall(json.dumps("show").encode('utf8'))
    sleep(0.01)
    kolbuffer = client_sock.recv(1024).decode('utf8')
    kol = json.loads(kolbuffer)
    p=" "
    text_show.insert(END, "|   №|        Фамилия|            Имя|       Отчество| День| Месяц|  Год| Зарплата|   Стаж|\n")
    text_show.insert(END, "|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
    for i in range(kol):
        arrbuffer = client_sock.recv(1024).decode('utf8')
        arr = json.loads(arrbuffer)
        text_show.insert(END, "|")
        if i+1<10:
            text_show.insert(END, p*3+str(i+1))
        else:
            text_show.insert(END, p * 2+str(i+1))

        text_show.insert(END, "|"+ (p*(15-len(str(arr[0])))) + str(arr[0]))
        text_show.insert(END, "|"+ (p*(15-len(str(arr[1])))) + str(arr[1]))
        text_show.insert(END, "|"+ (p*(15-len(str(arr[2])))) + str(arr[2]))
        text_show.insert(END, "|"+ (p*(5-len(str(arr[3])))) + str(arr[3]))
        text_show.insert(END, "|"+ (p*(6-len(str(arr[4])))) + str(arr[4]))
        text_show.insert(END, "|"+ (p*(5-len(str(arr[5])))) + str(arr[5]))
        text_show.insert(END, "|"+ (p*(9-len(str(arr[6])))) + str(arr[6]))
        text_show.insert(END, "|"+ (p*(7-len(str(arr[7])))) + str(arr[7])+"|\n")
    text_show.insert(END, "|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
def viewred():
    global label_red,en_red_n,button_red_n,redable
    redable=1
    label_red.place(relx=0.5, rely=0.15, anchor='nw')
    en_red_n.place(width=300, height=30, relx=0.5, rely=0.2)
    button_red_n.place(height=50, width=300, relx=0.5, rely=0.25)
def notviewred():
    global label_red, en_red_n, button_red_n,redable
    redable=0
    label_red.place_forget()
    en_red_n.place_forget()
    button_red_n.place_forget()
def red_read(event):
    global en_add_f, en_add_i, en_add_o, en_add_d, en_add_m, en_add_y, en_add_s, en_add_st,en_red_n
    global add_f, add_i, add_o, add_d, add_m, add_y, add_s, add_st,red_n
    global text_show, text_f, text_s,text_m
    text_show.delete(1.0, 'end')
    text_f.delete(1.0, 'end')
    text_s.delete(1.0, 'end')
    text_m.delete(1.0, 'end')
    if red_n.get()!="" and red_n.get().isnumeric():
        client_sock.sendall(json.dumps("red_read").encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(red_n.get()).encode('utf8'))
        obbuffer = client_sock.recv(1024).decode('utf8')
        ob = json.loads(obbuffer)
        if ob!="n":
            en_add_f.insert(END,ob[0])
            en_add_i.insert(END, ob[1])
            en_add_o.insert(END, ob[2])
            en_add_d.insert(END, ob[3])
            en_add_m.insert(END, ob[4])
            en_add_y.insert(END, ob[5])
            en_add_s.insert(END, ob[6])
            en_add_st.insert(END, ob[7])
        else:
            en_red_n.insert(END,"Неверный ввод данных")
def delete(event):
    global en_del_n,del_n
    global text_show, text_f, text_s,text_m
    text_show.delete(1.0, 'end')
    text_f.delete(1.0, 'end')
    text_s.delete(1.0, 'end')
    text_m.delete(1.0, 'end')
    if (del_n.get() != "" and del_n.get().isnumeric()):
        client_sock.sendall(json.dumps("del").encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(del_n.get()).encode('utf8'))
        nbuffer = client_sock.recv(1024).decode('utf8')
        n = json.loads(nbuffer)
        if n=="n":
            en_del_n.insert(END,"Неверный ввод данных")
        else:
            en_del_n.delete(0, 'end')
def search(event):
    global en_s_n, s_n,text_s
    if (s_n.get() != ""):
        client_sock.sendall(json.dumps("search").encode('utf8'))
        sleep(0.01)
        client_sock.sendall(json.dumps(s_n.get()).encode('utf8'))
        nbuffer = client_sock.recv(1024).decode('utf8')
        n = json.loads(nbuffer)
        p = " "
        text_s.insert(END,
                         "|   №|        Фамилия|            Имя|       Отчество| День| Месяц|  Год| Зарплата|   Стаж|\n")
        text_s.insert(END,
                         "|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
        for i in range(n):
            arrbuffer = client_sock.recv(1024).decode('utf8')
            arr = json.loads(arrbuffer)
            text_s.insert(END, "|")
            if arr[8] < 10:
                text_s.insert(END, p * 3 + str(arr[8]+1))
            else:
                text_s.insert(END, p * 2 + str(arr[8]+1))

            text_s.insert(END, "|" + (p * (15 - len(str(arr[0])))) + str(arr[0]))
            text_s.insert(END, "|" + (p * (15 - len(str(arr[1])))) + str(arr[1]))
            text_s.insert(END, "|" + (p * (15 - len(str(arr[2])))) + str(arr[2]))
            text_s.insert(END, "|" + (p * (5 - len(str(arr[3])))) + str(arr[3]))
            text_s.insert(END, "|" + (p * (6 - len(str(arr[4])))) + str(arr[4]))
            text_s.insert(END, "|" + (p * (5 - len(str(arr[5])))) + str(arr[5]))
            text_s.insert(END, "|" + (p * (9 - len(str(arr[6])))) + str(arr[6]))
            text_s.insert(END, "|" + (p * (7 - len(str(arr[7])))) + str(arr[7]) + "|\n")
        text_s.insert(END,
                         "|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
def sort(event):
    global sort_n
    global text_show, text_f, text_s
    text_show.delete(1.0, 'end')
    text_f.delete(1.0, 'end')
    text_s.delete(1.0, 'end')
    client_sock.sendall(json.dumps("sort").encode('utf8'))
    sleep(0.01)
    client_sock.sendall(json.dumps(sort_n.get()).encode('utf8'))
def filtr(event):
    global f_r,f1_n,f2_n,text_f
    if f1_n.get().isnumeric() and f2_n.get().isnumeric():
        if f1_n!="" and f2_n!="" and int(f1_n.get()) <= int(f2_n.get()):
            client_sock.sendall(json.dumps("filtr").encode('utf8'))
            sleep(0.01)
            client_sock.sendall(json.dumps(f_r.get()).encode('utf8'))
            sleep(0.01)
            client_sock.sendall(json.dumps(int(f1_n.get())).encode('utf8'))
            sleep(0.01)
            client_sock.sendall(json.dumps(int(f2_n.get())).encode('utf8'))
            nbuffer = client_sock.recv(1024).decode('utf8')
            n = json.loads(nbuffer)
            p = " "
            text_f.insert(END,
                          "|   №|        Фамилия|            Имя|       Отчество| День| Месяц|  Год| Зарплата|   Стаж|\n")
            text_f.insert(END,
                          "|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
            for i in range(n):
                arrbuffer = client_sock.recv(1024).decode('utf8')
                arr = json.loads(arrbuffer)
                text_f.insert(END, "|")
                if arr[8] < 10:
                    text_f.insert(END, p * 3 + str(arr[8] + 1))
                else:
                    text_f.insert(END, p * 2 + str(arr[8] + 1))

                text_f.insert(END, "|" + (p * (15 - len(str(arr[0])))) + str(arr[0]))
                text_f.insert(END, "|" + (p * (15 - len(str(arr[1])))) + str(arr[1]))
                text_f.insert(END, "|" + (p * (15 - len(str(arr[2])))) + str(arr[2]))
                text_f.insert(END, "|" + (p * (5 - len(str(arr[3])))) + str(arr[3]))
                text_f.insert(END, "|" + (p * (6 - len(str(arr[4])))) + str(arr[4]))
                text_f.insert(END, "|" + (p * (5 - len(str(arr[5])))) + str(arr[5]))
                text_f.insert(END, "|" + (p * (9 - len(str(arr[6])))) + str(arr[6]))
                text_f.insert(END, "|" + (p * (7 - len(str(arr[7])))) + str(arr[7]) + "|\n")
            text_f.insert(END,
                          "|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
def met(event):
    global  label_tit_met,en_f_e,button_m,label_tit2_met,f1_ex,f2_ex,f_e,kolich
    if int(f_e.get()) > 2:
        label_tit_met.place_forget()
        en_f_e.place_forget()
        button_m.place_forget()
        label_tit2_met.place(relx=0.05, rely=0.2, anchor='nw')
        f1_ex.place(relx=0.05, rely=0.26)
        f2_ex.place(relx=0.05, rely=0.32)
        client_sock.sendall(json.dumps("met").encode('utf8'))
        sleep(0.01)
        kolich=int(f_e.get())
        client_sock.sendall(json.dumps(kolich).encode('utf8'))
        n1buffer = client_sock.recv(1024).decode('utf8')
        n1 = json.loads(n1buffer)
        n2buffer = client_sock.recv(1024).decode('utf8')
        n2 = json.loads(n2buffer)
        f1_ex.config(text=n1)
        f2_ex.config(text=n2)


def otch(event):
    client_sock.sendall(json.dumps("otch").encode('utf8'))


ladd.bind('<Enter>',lambda e, f=ladd,t=im_title1: labe(e,f,t))
ladd.bind('<Leave>',lambda e, f=ladd,t=im_title1: labe(e,f,t))
lshow.bind('<Enter>',lambda e, f=lshow,t=im_title2: labe(e,f,t))
lshow.bind('<Leave>',lambda e, f=lshow,t=im_title2: labe(e,f,t))
lred.bind('<Enter>',lambda e, f=lred,t=im_title3: labe(e,f,t))
lred.bind('<Leave>',lambda e, f=lred,t=im_title3: labe(e,f,t))
ldel.bind('<Enter>',lambda e, f=ldel,t=im_title4: labe(e,f,t))
ldel.bind('<Leave>',lambda e, f=ldel,t=im_title4: labe(e,f,t))
lsearch.bind('<Enter>',lambda e, f=lsearch,t=im_title5: labe(e,f,t))
lsearch.bind('<Leave>',lambda e, f=lsearch,t=im_title5: labe(e,f,t))
lsort.bind('<Enter>',lambda e, f=lsort,t=im_title6: labe(e,f,t))
lsort.bind('<Leave>',lambda e, f=lsort,t=im_title6: labe(e,f,t))
lexp.bind('<Enter>',lambda e, f=lexp,t=im_title6_1: labe(e,f,t))
lexp.bind('<Leave>',lambda e, f=lexp,t=im_title6_1: labe(e,f,t))
lfiltr.bind('<Enter>',lambda e, f=lfiltr,t=im_title7: labe(e,f,t))
lfiltr.bind('<Leave>',lambda e, f=lfiltr,t=im_title7: labe(e,f,t))
lotch.bind('<Enter>',lambda e, f=lotch,t=im_title8: labe(e,f,t))
lotch.bind('<Leave>',lambda e, f=lotch,t=im_title8: labe(e,f,t))
lmenu.bind('<Enter>',lambda e, f=lmenu,t=im_title11: labe(e,f,t))
lmenu.bind('<Leave>',lambda e, f=lmenu,t=im_title11: labe(e,f,t))

im_title0.bind('<Enter>',lambda e, f=im_title0: labtite(e,f))
im_title0.bind('<Leave>',lambda e, f=im_title0: labtite(e,f))


lreguser.bind('<Enter>',lambda e, f=lreguser: labdop(e,f))
lreguser.bind('<Leave>',lambda e, f=lreguser: labdop(e,f))
ldeluser.bind('<Enter>',lambda e, f=ldeluser: labdop(e,f))
ldeluser.bind('<Leave>',lambda e, f=ldeluser: labdop(e,f))
lchan.bind('<Enter>',lambda e, f=lchan: labdop(e,f))
lchan.bind('<Leave>',lambda e, f=lchan: labdop(e,f))

im_title0.bind('<Button-1>',exi)
lmenu.bind('<Button-1>',viewmenu)
button_cancel_user.bind('<Button-1>',cancel)
button_cancel_chan.bind('<Button-1>',cancel)
button_cancel_deluser.bind('<Button-1>',cancel)
button_cancel_del.bind('<Button-1>',cancel)
button_cancel_add.bind('<Button-1>',cancel)
button_cancel_sort.bind('<Button-1>',cancel)
lreguser.bind('<Button-1>',lambda e, f=frame_add_user: viewframe(e,f))
lchan.bind('<Button-1>',lambda e, f=frame_chan: viewframe(e,f))
ldeluser.bind('<Button-1>',lambda e, f=frame_del_user: viewframe(e,f))


ladd.bind('<Button-1>',lambda e, f=frame_add,red=-1: viewframe(e,f,red))
lshow.bind('<Button-1>',lambda e, f=frame_print: viewframe(e,f))
lred.bind('<Button-1>',lambda e, f=frame_add,red=1: viewframe(e,f,red))
ldel.bind('<Button-1>',lambda e, f=frame_del: viewframe(e,f))
lsearch.bind('<Button-1>',lambda e, f=frame_search: viewframe(e,f))
lsort.bind('<Button-1>',lambda e, f=frame_sort: viewframe(e,f))
lfiltr.bind('<Button-1>',lambda e, f=frame_filtr: viewframe(e,f))
lexp.bind('<Button-1>',lambda e, f=frame_met: viewframe(e,f))
lotch.bind('<Button-1>',lambda e, f=frame_otch: viewframe(e,f))

button_add_user.bind('<Button-1>',add_user)
button_chan_pas.bind('<Button-1>',chan_pas)
button_deluser.bind('<Button-1>',deluser)
button_add.bind('<Button-1>',lambda e, f=redable: add(e,f))
button_show.bind('<Button-1>',show)
button_red_n.bind('<Button-1>',red_read)
button_del.bind('<Button-1>',delete)
button_s.bind('<Button-1>',search)
button_sort.bind('<Button-1>',sort)
button_f.bind('<Button-1>',filtr)
button_m.bind('<Button-1>',met)
button_o.bind('<Button-1>',otch)
tk.mainloop()
client_sock.close()
