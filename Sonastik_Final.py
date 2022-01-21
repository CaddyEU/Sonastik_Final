def read_file(f):
    file=open(f,'r',encoding="utf-8-sig")
    mas=[] 
    for rida in file:
        mas.append(rida.strip())
    file.close()
    return mas
##############################################################################
def list_file(f,list_):
    file=open(f,'w',encoding="utf-8-sig")
    for k in list_:
        file.write(k+"\n")
    file.close()
    return list_
##############################################################################
def save_file(f,text):    
    file=open(f,'a',encoding="utf-8-sig")
    file.write(text+"\n")
    file.close()
    mas=[]
    mas=read_file(f)
    return mas
##############################################################################
def new_words():
    rus_word=input("Введи слово на русском:")
    est_word=input("Sisesta sõna eesti keeles:")
    rus_list=save_file("rus.txt",rus_word)
    est_list=save_file("est.txt",est_word)
    return rus_list, est_list
##############################################################################
def translate(rus_list,est_list):
    word=input("Введите слово для перевода: ")
    if word in rus_list:
        ind=rus_list.index(word)
        print(f"{word} - {est_list[ind]}")
    elif word in est_list:
        ind=est_list.index(word)
        print(f"{word} - {rus_list[ind]}")
    else:
        print(f"{word.upper()} отсутствует в словаре")
        v=input("Желаете добавить слово в словарь?")
        if v.lower()=="да": new_words()
##############################################################################
def fix(rus_list,est_list):
    typo=input("Введите слово с ошибкой: ")
    if typo in rus_list:
        ind=rus_list.index(typo)#index
        print(f"Будет исправлена пара слов{typo} - {est_list[ind]}")
        rus_list.pop(ind)
        est_list.pop(ind)
        rus_list=list_file("rus.txt",rus_list)
        est_list=list_file("est.txt",est_list)
        new_words()
        
    elif typo in est_list:
        ind=est_list.index(typo)
        print(f"Будет исправлена пара слов{typo} - {rus_list[ind]}")
        rus_list.pop(ind)
        est_list.pop(ind)
        rus_list=list_file("rus.txt",rus_list)
        est_list=list_file("est.txt",est_list)
        new_words()
    else:
        print(f"{typo.upper()} отсутствует в словаре")
    rus_list=read_file("rus.txt")
    est_list=read_file("est.txt")
    return rus_list,est_list
##############################################################################
def quiz(rus_list,est_list):
    quiz_est = input("Как будет на эстонском слово - мама?: ")
    if quiz_est in est_list:
        print("Верно, молодец!")
    else:
        print("Не верно!")
            
    quiz_rus = input("Kuidas on vene keeles sõna - koer?: ")
    if quiz_rus in rus_list:
        print("Õige, tubli!")
    else:
        print("Ei ole!")
##############################################################################
rus_list=read_file("rus.txt")
est_list=read_file("est.txt")
print(rus_list)
print(est_list)
while True:
    v=input("Перевод-1,Новое слово-2,Исправить ошибку-3,Проверка знаний-4: ")
    if v=="1":
        translate(rus_list,est_list)
    elif v=="2":
        rus_list, est_list=new_words()
    elif v=="3":
        print(rus_list,est_list)
        rus_list,est_list=fix(rus_list,est_list)
        print(rus_list,est_list)
    elif v=="4":
        quiz(rus_list,est_list)
