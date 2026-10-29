tlist = []
all_time='1h 45m,360s,25m,30m 120s,2h 60s'
times=all_time.split(',')

for time in times:
    parts = time.split()
    for t in parts:
        if 'h' in t:
            tlist.append(int(t.replace('h', '')) * 60)
        elif 'm' in t:
            tlist.append(int(t.replace('m', '')))
        else:
            tlist.append(int(t.replace('s', '')) // 60)
    totalm = sum(tlist)
print(totalm)

#1. сплитануть всю строку
#2. сплитануть строки в списках по пробелу
#3. если в списке h, то убираем h, переводим в int, умножаем на 60, если m то просто убираем m, переводим str в int, если s то по аналоги с h, но делим на 60, все значения сохраняем в список
#4. сумируем индексы полученного списка