from __future__ import print_function
# импортируем библиотеку tkinter всю сразу
from tkinter import *
from tkinter import messagebox as mb
import random

# главное окно приложения
window = Tk()
# заголовок окна
window.title('Курсовая работа по криптографии Самсонов Д.Л. (вариант 20)')
# размер окна
window.geometry('850x630')
# можно ли изменять размер окна - нет
window.resizable(False, False)

# кортежи и словари, содержащие настройки шрифтов и отступов
font_header = ('Arial', 15)
font_entry = ('Arial', 12)
label_font = ('Arial', 11)
base_padding = {'padx': 10, 'pady': 8}
header_padding = {'padx': 10, 'pady': 12}

# обработчик нажатия на клавишу 'Рассчитать'
def clicked():

    # получаем переменные
    p = p_entry.get()
    p = int(p)
    q = q_entry.get()
    q = int(q)
    gamma = gamma_entry.get()
    gamma = int(gamma)
    x = x_entry.get()
    x = int(x)
    h = h_entry.get()
    h = int(h)
    # u = 5523
    # u = 3650
    # u = 26146
    u = random.randint(2, p-2)

    print("U", u)
    # h = 12974

    def Evklid(num1, num2):
        if num1 == 0:
            return (num2, 0, 1)
        else:
            div, x, y = Evklid(num2 % num1, num1)
        return (div, y - (num2 // num1) * x, x)

    def IsPrime(n):
        d = 2
        while d * d <= n and n % d != 0:
            d += 1
        return d * d > n

    def Proverka_gamma(num):
        if num%4 ==3:
            return True
        else:
            return False

    prime_p = IsPrime(p)
    prime_q = IsPrime(q)
    prov_gamma = Proverka_gamma(gamma)

    if prime_p == True:

        if prime_q == True:

            if prov_gamma == True:


                res = False

                for w in range(2,1000):
                    if not res:
                        #podbor(x, gamma,p)
                        if pow(w,gamma,p) ==1:
                            res = True
                            print(w,gamma)
                            break
                    else:
                        break

                a = w
                print("a ", a , "gamma", gamma)
                z = pow(a,u,p)
                print("z", z)
                UZH = (-u*z*h)%gamma
                print("UZH", UZH)
                POW = pow(u*z*h,2)
                print("POW", POW)
                step = (gamma+1)/4
                print("step", step)
                ZHX = 4*z*h*x
                print("ZHX", ZHX)
                print("H", h)
                print("X", x)
                power =  pow((POW + ZHX) , int(step) , gamma)

                proverka_3 = pow((POW + ZHX), int((gamma-1)/2), gamma)
                print("Проверка на вычет: ", proverka_3)
                if proverka_3 ==1:

                    print("power", power)
                    mod2zh = (2*z*h)%gamma
                    print("mod2zh", mod2zh)



                    e = Evklid(mod2zh, gamma)
                    print("Обратный мультипликативный элемент 2zh: ", e[1])
                    if int(e[1])<0:
                        e_rev = e[1] + gamma
                    else:
                        e_rev = e[1]

                    k_1 = ((UZH + power)*e_rev)%gamma #по мод гамма
                    k_2 = ((UZH - power)*e_rev)%gamma #по мод гамма
                    print("k_1", k_1)
                    print("k_2", k_2)
                    g_1 = (u + k_1)%gamma
                    g_2 = (u + k_2)%gamma
                    print("g_1", g_1)
                    print("g_@", g_2)
                    y_left = pow(a,x,p)%q
                    print("y_left", y_left)
                    print("ak", pow(a,k_1))
                    s_1 = pow(a,g_1,p)
                    s_2 = pow(a,g_2,p)
                    a_step_k_mod_p_1 = pow(a,k_1,p)
                    a_step_k_mod_p_2 = pow(a,k_2,p)
                    print("а в степени к_1 мод р: ", a_step_k_mod_p_1 , "а в степени к_2 мод р: ", a_step_k_mod_p_2)
                    evkl_k_1 = Evklid(a_step_k_mod_p_1,p)
                    evkl_k_2 = Evklid(a_step_k_mod_p_2,p)
                    if int(evkl_k_1[1])<0:
                        evkl_1 = p + evkl_k_1[1]
                    else:
                        evkl_1 = evkl_k_1[1]

                    if int(evkl_k_2[1])<0:
                        evkl_2 = p + evkl_k_2[1]
                    else:
                        evkl_2 = evkl_k_2[1]

                    step_s = ((s_1*evkl_1)%p)*k_1*h #по мод p
                    print("Обратный мультипликативный эл a^k_1: ", evkl_1 , "2$ ", evkl_2 )
                    step_s_2 = ((s_2*evkl_2)%p)*k_2*h #по мод p
                    #print("step_s", step_s)

                    y_right_1 = pow(s_1,step_s, p)%q
                    y_right_2 = pow(s_2,step_s_2, p)%q
                    print("y_right_1", y_right_1)
                    print("y_right_2", y_right_2)

                    # добавление нового элемента
                    math_listbox.insert(0, "U = " + str(u))
                    math_listbox.insert(1, "Z = " + str(z))
                    math_listbox.insert(2, "k_1 = " + str(k_1))
                    math_listbox.insert(3, "k_2 = " + str(k_2))
                    math_listbox.insert(4, "g_1 = " + str(g_1))
                    math_listbox.insert(5, "g_2 = " + str(g_2))
                    math_listbox.insert(6, "S_1 = " + str(s_1))
                    math_listbox.insert(7, "S_2 = " + str(s_2))
                    math_listbox.insert(8, "y = " + str(y_left))
                    math_listbox.insert(9, "y проверочный = " + str(y_right_1))
                    math_listbox.insert(10, "y проверочный_2 = " + str(y_right_2))
                    math_listbox.insert(11, "Первая подпись вида (k,s): " +"(" + str(k_1) + "," + str(s_1) + ")")
                    math_listbox.insert(12, "Вторая подпись вида (k,s): " +"(" + str(k_2) + "," + str(s_2) + ")")
                    math_listbox.insert(13, "---------------------------------------------------------------------------------------------------------------")
                else:
                    mb.showerror("Ошибка!",
                    "Нет корней. Попробуйте еще раз.")
            else:
                mb.showerror("Ошибка!",
                "Введенное gamma не соответствует условию (gamma = 3 mod 4). Введите другое.")
        else:
            mb.showerror("Ошибка!",
            "Данное q не является простым числом. Введите другое.")
    else:
        mb.showerror("Ошибка!",
        "Данное p не является простым числом. Введите другое.")

# заголовок формы: настроены шрифт (font), отцентрирован (justify), добавлены отступы для заголовка
# для всех остальных виджетов настройки делаются также
main_label = Label(window, text='Схемы ЭЦП на основе сложности дискретного логарифмирования', font=font_header, justify=LEFT, **header_padding)
# помещаем виджет в окно по принципу один виджет под другим
main_label.pack()

scrollbar = Scrollbar(window)
scrollbar.pack(side=RIGHT, fill=Y)

#listbox
math_listbox = Listbox(yscrollcommand=scrollbar.set, width=100)
math_listbox.pack(side=RIGHT, fill=BOTH)



# метка для поля ввода p
p_label = Label(window, text='Введите p', font=label_font , **base_padding)
p_label.pack()

# поле ввода p
p_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
p_entry.pack()

# метка для поля ввода q
q_label = Label(window, text='Введите q', font=label_font , **base_padding)
q_label.pack()

# поле ввода q
q_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
q_entry.pack()


# метка для поля ввода gamma
gamma_label = Label(window, text='Введите gamma', font=label_font , **base_padding)
gamma_label.pack()

# поле ввода gamma
gamma_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
gamma_entry.pack()

# метка для поля ввода x
x_label = Label(window, text='Введите x', font=label_font , **base_padding)
x_label.pack()

# поле ввода x
x_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
x_entry.pack()

# метка для поля ввода h
h_label = Label(window, text='Введите h', font=label_font , **base_padding)
h_label.pack()

# поле ввода h
h_entry = Entry(window, bg='#fff', fg='#444', font=font_entry)
h_entry.pack()

# кнопка отправки формы
send_btn = Button(window, text='Рассчитать', command=clicked)
send_btn.pack(**base_padding)


# запускаем главный цикл окна
window.mainloop()
