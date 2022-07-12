print("Tema 14.2: La prueba del signo")
res = int(input("Intervalo de confianza = 0 ó Prueba de hipótesis = 1? "))
if res == 0:
    k = int(input("Introduce el valor crítico: "))
    F = int(input("Inserte el número de filas: "))
    C = int(input("Inserte el número de columnas: "))
    matrix = []
    print("Introduce los datos: ")

    for i in range(F):
        a = []
        for j in range(C):
            a.append(float(input()))
        matrix.append(a)

    for i in range(k):
        a.pop(0)
        a.pop(-1)
    print(a)
elif res == 1:
    print("Jajajaja, no se puede programar")
    import webbrowser
    webbrowser.open_new_tab("https://rr2---sn-q4fl6nsy.googlevideo.com/videoplayback?expire=1657533699&ei=o6DLYrH4KoSN_9EP9aGe-Ao&ip=2604%3Aa880%3A800%3A10%3A%3Ab73%3A9001&id=o-AHqb4cOZ9OYD2KmMHnqJQmqCIjDsQncw-8bmunBx2HV8&itag=22&source=youtube&requiressl=yes&spc=lT-KhsACLqSDdTA6NQuHIcjumY90dy0&vprv=1&mime=video%2Fmp4&ns=VPYaztork-qjZidvwt5n4qkH&cnr=14&ratebypass=yes&dur=4.017&lmt=1645566827867039&fexp=24001373,24007246&c=WEB&txp=5318224&n=wpgJ4Qy2AWNVji2aIrVQ&sparams=expire%2Cei%2Cip%2Cid%2Citag%2Csource%2Crequiressl%2Cspc%2Cvprv%2Cmime%2Cns%2Ccnr%2Cratebypass%2Cdur%2Clmt&sig=AOq0QJ8wRQIgN11quGIsg-AUjpJQKgsfqmNIP_zWE_PunXoqLezHV4QCIQDtaKQOli-W8LUUBXpd6SzKpyHlCm78G0Jur0P71TPn3Q%3D%3D&rm=sn-ab5ee77l&req_id=1e6cf4353675a3ee&redirect_counter=2&cm2rm=sn-0opoxu-jwne7s&cms_redirect=yes&cmsv=e&ipbypass=yes&mh=Hk&mip=2806:1016:d:40cf:68c4:2dd:7b4e:5889&mm=29&mn=sn-q4fl6nsy&ms=rdu&mt=1657511821&mv=m&mvi=2&pl=57&lsparams=ipbypass,mh,mip,mm,mn,ms,mv,mvi,pl&lsig=AG3C_xAwRQIgepcE8RrluqkzGoKDq_8p6CDNmDm-3L6er6_HV0CXSF8CIQDBChgDm26NizriLSAs9ZyYXxmILoMioMmiXJO_RL0hJw%3D%3D")

S = int(input("Do you want to exit(Y=1/N=2)? "))
if S == 1:
    import main
else:
    import Tema14p2
