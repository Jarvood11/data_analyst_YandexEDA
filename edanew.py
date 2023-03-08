#st=str(["a", "b", "c", "a", "b", "c", "c", "c"])
st = str(input())
if st == '[]' or st == '[""]' or st == '' or st == '""':
    nums = 0
elif ',' not in st:
    nums = 1
else:
    st = st[2:]
    st = st[:-2]
    #print(st)
    if ',' in st:
        s = st.split('", "')
        #print(s)
        #s = s.replace('"', '').replace('[', '').replace(']', '').replace(',', '').replace(' ', '')
        #s = s.replace('"', '')
        #s = s.replace('[', '')
        #s = s.replace(']', '')
        #s = s.replace(',', '')
        #s = s.replace(' ', '')

        candys = list(s)
        #candys = ['a', 'a', 'a', 'b', 'b', 'b', 'b', 'c', 'c', 'c', 'c', 'c']
        #candys=["a", "b", "c", "a", "b", "c", "c", "c"]["a", "a", "a", "b", "b", "b", "c", "c", "c"]
        #candys=['a', 'a', 'b', 'b', 'b','b','c', 'c', 'c','c', 'c', 'c']
        #candys = ['a', 'a', 'a', 'a', 'b', 'b', 'b', 'b', 'e', 'e', 'e', 'e']
        #print(candys)
        # Функция для удаления дубликатов в списке
        def del_duplicate(l):
            n = []
            for i in l:
                if i not in n:
                    n.append(i)
            return n

        # Считаем количество каждого типа конфет
        count = []
        for i, val in enumerate(candys):
            count.append(candys.count(val))
    
        # Удаляем дубликаты
        numbers = del_duplicate(count)
        #print(numbers)
        n = max(numbers)
        flag = 1
        for i in range(1, n+1):
            for j in numbers:
                if j % i != 0:
                    flag = 0
            if flag == 1:
                nums = i
            flag = 1
        #print ("Максимальное число друзей:", nums)
print(nums)
