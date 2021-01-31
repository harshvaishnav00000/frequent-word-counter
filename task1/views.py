from django.shortcuts import render, redirect
from .models import counter

def frequency(request):
    return render(request, 'frequency.html')

def result(request):
    dbs = counter()
    data = counter.objects.all()
    s = ""
    ct = 0
    c = request.POST['count']
    a = c[7:]
    for i in data:
        if str(i.storedurl) == str(c):
            b = []
            st = str(i.value)
            cnt = 1
            f = ""
            for i in st:
                if i == " ":
                    if cnt == -1:
                        b.append([f,s])
                        f = ""
                        s = ""
                    cnt = cnt * (-1)
                if cnt == 1:
                    f += i
                if cnt == -1:
                    s += i
            print(b)
            ct = 1
            break

    if ct == 0:
        b = {}
        for i in a:
            if i in "qazxswedcvfrtgbnhyujmkilop1234567890":
                s += i
            else:
                if s == "":
                    pass
                elif s in b:
                    b[s] += 1
                else:
                    b[s] = 1
                s = ""
        if s != "":
            if s in b:
                b[s] += 1
            else:
                b[s] = 1

        b = sorted(b.items())
        if len(b) > 10:
            b = b[:10]

        st = ""
        for i in b:
            st += str(i[0]) + " " + str(i[1]) + " "

        dbs.storedurl = c
        dbs.value = st
        dbs.save()

    d = ""
    if ct == 0:
        d = "Freshly processed"
    if ct == 1:
        d = "Extracting from database"
    send = b
    return render(request, 'result.html', {'item': send, 'inputurl': c, 'd': d})