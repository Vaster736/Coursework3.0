import socket
from pickle import *
from subprocess import Popen
import json
from time import *
# filename = "database.dat"
# mas=[]
# with open(filename, "wb") as file:
#     dump(mas, file)
class User:
    def __init__(self,login,password):
        self.__login=login
        self.__password = password
    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self,log):
        self.__login=log

    @password.setter
    def password(self, pas):
        self.__password = pas

class Admin:
    def __init__(self,login,password):
        self.__id=0
        self.__login=login
        self.__password = password
    @property
    def login(self):
        return self.__login

    @property
    def password(self):
        return self.__password

    @login.setter
    def login(self,log):
        self.__login=log

    @password.setter
    def password(self, pas):
        self.__password = pas

class FIO:
    def __init__(self):
        self.__fam=""
        self.__im = ""
        self.__ot = ""

    @property
    def fam(self):
        return self.__fam

    @property
    def im(self):
        return self.__im

    @property
    def ot(self):
        return self.__ot

    @fam.setter
    def fam(self, fam):
        self.__fam = fam

    @im.setter
    def im(self, im):
        self.__im = im

    @ot.setter
    def ot(self, ot):
        self.__ot = ot

class Date:
    def __init__(self):
        self.__d = 0
        self.__m = 0
        self.__y = 0

    @property
    def d(self):
        return self.__d

    @property
    def m(self):
        return self.__m

    @property
    def y(self):
        return self.__y

    @d.setter
    def d(self, d):
        self.__d = d

    @m.setter
    def m(self, m):
        self.__m = m

    @y.setter
    def y(self, y):
        self.__y = y



class Sotrudnik:
    def __init__(self):
        self.__fio=FIO()
        self.__date = Date()
        self.__salary = 0


    def setfio(self,f,i,o):
        self.__fio.fam=f
        self.__fio.im = i
        self.__fio.ot = o
    def setdate(self,d,m,y):
        self.__date.d=d
        self.__date.m = m
        self.__date.y = y


    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        self.__salary = salary

class Waiter(Sotrudnik):
    def __init__(self):
        Sotrudnik.__init__(self)
        self.__stazh = 0

    @property
    def stazh(self):
        return self.__stazh

    @stazh.setter
    def stazh(self, stazh):
        self.__stazh = stazh

filename = "database.dat"
with open(filename, "rb") as file:
    mas = load(file)



serv_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM, proto=0)
Popen('python Client.py')
serv_sock.bind(('', 53210))
serv_sock.listen(10)
print("Сервер запущен")

sock, client_addr = serv_sock.accept()
use='s'

while True:
    menubuffer = 's'
    try:
        use = sock.recv(1024).decode('utf8')
        ent = sock.recv(1024).decode('utf8')
        log = sock.recv(1024).decode('utf8')
        pas = sock.recv(1024).decode('utf8')
    except:
        break
    if not use:
        break
    if(use == "a"):
        filename = "admin.dat"
        with open(filename, "rb") as file:
            mas = load(file)
    else:
        filename = "user.dat"
        with open(filename, "rb") as file:
            mas = load(file)
    if(ent == "e"):
        flag = 0
        for el in mas:
            if(el.login == log and el.password == pas):
                flag = 1
        if(flag == 1):
            if(use == "a"):
                sock.sendall(json.dumps("a").encode('utf8'))
            else:
                sock.sendall(json.dumps("u").encode('utf8'))
        else:
            sock.sendall(json.dumps("n").encode('utf8'))
            menubuffer=False
    else:
        mas.append(User(log,pas))
        with open(filename, "wb") as file:
            dump(mas, file)
        if (use == "a"):
            sock.sendall(json.dumps("a").encode('utf8'))
        else:
            sock.sendall(json.dumps("u").encode('utf8'))

    while menubuffer:
        menubuffer = sock.recv(1024).decode('utf8')
        if not menubuffer:
            break
        try:
            menu = json.loads(menubuffer)
        except:
            break
        if(menu == "exit"):
            break
        elif(menu == "add_user"):
            logbuffer = sock.recv(1024).decode('utf8')
            log = json.loads(logbuffer)
            pasbuffer = sock.recv(1024).decode('utf8')
            pas = json.loads(pasbuffer)
            filename = "user.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            mas.append(User(log, pas))
            with open(filename, "wb") as file:
                dump(mas, file)
        elif(menu == "chan_pas"):
            filename = "admin.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            logbuffer = sock.recv(1024).decode('utf8')
            log = json.loads(logbuffer)
            oldpasbuffer = sock.recv(1024).decode('utf8')
            oldpas = json.loads(oldpasbuffer)
            newpasbuffer = sock.recv(1024).decode('utf8')
            newpas = json.loads(newpasbuffer)
            flag=0
            for i in range(len(mas)):
                if mas[i].login==log and mas[i].password==oldpas:
                    mas[i].password=newpas
                    flag=1
            with open(filename, "wb") as file:
                dump(mas, file)
            if(flag==0):
                sock.sendall(json.dumps("not_changed").encode('utf8'))
            else:
                sock.sendall(json.dumps("changed").encode('utf8'))
        elif(menu == "deluser"):
            logbuffer = sock.recv(1024).decode('utf8')
            log = json.loads(logbuffer)
            filename = "user.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            flag = 0
            i=0
            lenmas = len(mas)
            while(i<lenmas):
                if(mas[i].login==log):
                    mas.pop(i)
                    lenmas -= 1
                    flag = 1
                else:
                    i += 1
            with open(filename, "wb") as file:
                dump(mas, file)
            if (flag == 1):
                sock.sendall(json.dumps("deleted").encode('utf8'))
            else:
                sock.sendall(json.dumps("not_deleted").encode('utf8'))
        elif(menu == "add"):
            arrbuffer = sock.recv(1024).decode('utf8')
            arr = json.loads(arrbuffer)
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            waiter=Waiter()
            waiter.fam=arr[0]
            waiter.im = arr[1]
            waiter.ot = arr[2]
            waiter.d = arr[3]
            waiter.m = arr[4]
            waiter.y = arr[5]
            waiter.salary = arr[6]
            waiter.stazh = arr[7]
            mas.append(waiter)
            with open(filename, "wb") as file:
                dump(mas, file)
        elif(menu == "show"):
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            sock.sendall(json.dumps(len(mas)).encode('utf8'))
            for i in range(len(mas)):
                sleep(0.01)
                arr=[]
                arr.append(mas[i].fam)
                arr.append(mas[i].im)
                arr.append(mas[i].ot)
                arr.append(mas[i].d)
                arr.append(mas[i].m)
                arr.append(mas[i].y)
                arr.append(mas[i].salary)
                arr.append(mas[i].stazh)
                sock.sendall(json.dumps(arr).encode('utf8'))
        elif(menu == "red_read"):
            rednbuffer = sock.recv(1024).decode('utf8')
            redn = int(json.loads(rednbuffer))
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            if redn<=0 or redn>len(mas):
                sock.sendall(json.dumps("n").encode('utf8'))
            else:
                i=int(redn)-1
                arr = []
                arr.append(mas[i].fam)
                arr.append(mas[i].im)
                arr.append(mas[i].ot)
                arr.append(mas[i].d)
                arr.append(mas[i].m)
                arr.append(mas[i].y)
                arr.append(mas[i].salary)
                arr.append(mas[i].stazh)
                sock.sendall(json.dumps(arr).encode('utf8'))
        elif(menu == "red"):
            rednbuffer = sock.recv(1024).decode('utf8')
            redn = int(json.loads(rednbuffer))
            arrbuffer = sock.recv(1024).decode('utf8')
            arr = json.loads(arrbuffer)
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            waiter = Waiter()
            waiter.fam = arr[0]
            waiter.im = arr[1]
            waiter.ot = arr[2]
            waiter.d = arr[3]
            waiter.m = arr[4]
            waiter.y = arr[5]
            waiter.salary = arr[6]
            waiter.stazh = arr[7]
            mas[redn-1]=waiter
            with open(filename, "wb") as file:
                dump(mas, file)
        elif(menu == "del"):
            delbuffer = sock.recv(1024).decode('utf8')
            deln = int(json.loads(delbuffer))
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            if deln <= 0 or deln > len(mas):
                sock.sendall(json.dumps("n").encode('utf8'))
            else:
                i = int(deln) - 1
                mas.pop(i)
                with open(filename, "wb") as file:
                    dump(mas, file)
                sock.sendall(json.dumps("d").encode('utf8'))
        elif (menu == "search"):
            delbuffer = sock.recv(1024).decode('utf8')
            sn = json.loads(delbuffer)
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            sc=0
            for i in range(len(mas)):
                if mas[i].fam==sn:
                    sc+=1
            sock.sendall(json.dumps(sc).encode('utf8'))
            for i in range(len(mas)):
                if mas[i].fam == sn:
                    sleep(0.01)
                    arr=[]
                    arr.append(mas[i].fam)
                    arr.append(mas[i].im)
                    arr.append(mas[i].ot)
                    arr.append(mas[i].d)
                    arr.append(mas[i].m)
                    arr.append(mas[i].y)
                    arr.append(mas[i].salary)
                    arr.append(mas[i].stazh)
                    arr.append(i)
                    sock.sendall(json.dumps(arr).encode('utf8'))
        elif (menu == "sort"):
            sbuffer = sock.recv(1024).decode('utf8')
            s = json.loads(sbuffer)
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            if s==1:
                for i in range(len(mas) - 1):
                    m = i
                    j = i + 1
                    while j < len(mas):
                        if mas[j].fam < mas[m].fam:
                            m = j
                        j = j + 1
                    mas[i], mas[m] = mas[m], mas[i]
            elif s==2:
                for i in range(len(mas) - 1):
                    m = i
                    j = i + 1
                    while j < len(mas):
                        if mas[j].y < mas[m].y:
                            m = j
                        elif mas[j].y == mas[m].y:
                            if mas[j].m < mas[m].m:
                                m = j
                            elif mas[j].m == mas[m].m:
                                if mas[j].d < mas[m].d:
                                    m = j
                        j = j + 1
                    mas[i], mas[m] = mas[m], mas[i]
            elif s==3:
                for i in range(len(mas) - 1):
                    m = i
                    j = i + 1
                    while j < len(mas):
                        if mas[j].salary < mas[m].salary:
                            m = j
                        j = j + 1
                    mas[i], mas[m] = mas[m], mas[i]
            elif s==4:
                for i in range(len(mas) - 1):
                    m = i
                    j = i + 1
                    while j < len(mas):
                        if mas[j].stazh < mas[m].stazh:
                            m = j
                        j = j + 1
                    mas[i], mas[m] = mas[m], mas[i]
            with open(filename, "wb") as file:
                dump(mas, file)
        elif (menu == "filtr"):
            rbuffer = sock.recv(1024).decode('utf8')
            r = json.loads(rbuffer)
            n1buffer = sock.recv(1024).decode('utf8')
            n1 = json.loads(n1buffer)
            n2buffer = sock.recv(1024).decode('utf8')
            n2 = json.loads(n2buffer)
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            if r == 1:
                sc=0
                for i in range(len(mas)):
                    if mas[i].salary>=n1 and mas[i].salary<=n2:
                        sc+=1
                sock.sendall(json.dumps(sc).encode('utf8'))
                for i in range(len(mas)):
                    if mas[i].salary>=n1 and mas[i].salary<=n2:
                        sleep(0.01)
                        arr = []
                        arr.append(mas[i].fam)
                        arr.append(mas[i].im)
                        arr.append(mas[i].ot)
                        arr.append(mas[i].d)
                        arr.append(mas[i].m)
                        arr.append(mas[i].y)
                        arr.append(mas[i].salary)
                        arr.append(mas[i].stazh)
                        arr.append(i)
                        sock.sendall(json.dumps(arr).encode('utf8'))
            else:
                sc = 0
                for i in range(len(mas)):
                    if mas[i].stazh >= n1 and mas[i].stazh <= n2:
                        sc += 1
                sock.sendall(json.dumps(sc).encode('utf8'))
                for i in range(len(mas)):
                    if mas[i].stazh >= n1 and mas[i].stazh <= n2:
                        sleep(0.01)
                        arr = []
                        arr.append(mas[i].fam)
                        arr.append(mas[i].im)
                        arr.append(mas[i].ot)
                        arr.append(mas[i].d)
                        arr.append(mas[i].m)
                        arr.append(mas[i].y)
                        arr.append(mas[i].salary)
                        arr.append(mas[i].stazh)
                        arr.append(i)
                        sock.sendall(json.dumps(arr).encode('utf8'))
        elif (menu == "met"):
            filename = "database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            kolbuffer = sock.recv(1024).decode('utf8')
            kol = json.loads(kolbuffer)
            arr = []
            for i in range(kol):
                arr.append([])
                for j in range(i + 1):
                    arr[i].append(0)
                for j in range(i + 1, kol):
                    sock.sendall(json.dumps(mas[i].fam).encode('utf8'))
                    sleep(0.01)
                    sock.sendall(json.dumps(mas[j].fam).encode('utf8'))
                    cbuffer = sock.recv(1024).decode('utf8')
                    c = json.loads(cbuffer)
                    arr[i].append(c)
            sock.sendall(json.dumps("n").encode('utf8'))
            sleep(0.02)
            sock.sendall(json.dumps(arr).encode('utf8'))
            sleep(0.02)
            arrbuffer = sock.recv(1024).decode('utf8')
            arr = json.loads(arrbuffer)
            for i in range(kol):
                m = max(arr)
                ind = arr.index(m)
                sock.sendall(json.dumps([ind + 1, mas[ind].fam]).encode('utf8'))
                arr[ind] = -1
                sleep(0.01)
        elif (menu == "otch"):
            filename="database.dat"
            with open(filename, "rb") as file:
                mas = load(file)
            file = "otchet.txt"
            with open(file, "w") as f:
                p=" "
                f.write("|   №|        Фамилия|            Имя|       Отчество| День| Месяц|  Год| Зарплата|   Стаж|\n")
                f.write("|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
                f.write("|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
                for i in range(len(mas)):
                    f.write("|")
                    if i + 1 < 10:
                        f.write(p * 3 + str(i + 1))
                    else:
                        f.write(p * 2 + str(i + 1))

                    f.write("|" + (p * (15 - len(str(mas[i].fam)))) + str(mas[i].fam))
                    f.write("|" + (p * (15 - len(str(mas[i].im)))) + str(mas[i].im))
                    f.write("|" + (p * (15 - len(str(mas[i].ot)))) + str(mas[i].ot))
                    f.write("|" + (p * (5 - len(str(mas[i].d)))) + str(mas[i].d))
                    f.write("|" + (p * (6 - len(str(mas[i].m)))) + str(mas[i].m))
                    f.write("|" + (p * (5 - len(str(mas[i].y)))) + str(mas[i].y))
                    f.write("|" + (p * (9 - len(str(mas[i].salary)))) + str(mas[i].salary))
                    f.write("|" + (p * (7 - len(str(mas[i].stazh)))) + str(mas[i].stazh) + "|\n")
                    f.write("|____|_______________|_______________|_______________|_____|______|_____|_________|_______|\n")
                cs = 0
                for i in range(len(mas)):
                    cs += mas[i].salary
                f.write("\n  Общие затраты на зарплаты                                                     " + str(cs)+"\n")
                f.write("___________________________________________________________________________________________\n\n")
                cs=0
                for i in range(len(mas)):
                    cs+=mas[i].salary
                cs =int(cs/ len(mas))
                f.write("  Средняя заработная плата                                                      " + str(cs)+"\n")
                f.write("___________________________________________________________________________________________\n\n")
                cs = 0
                for i in range(len(mas)):
                    cs += mas[i].stazh
                cs =int(cs/ len(mas))
                f.write("  Средний стаж работы                                                           " + str(cs)+"\n")
                f.write("___________________________________________________________________________________________\n\n")



sock.close()