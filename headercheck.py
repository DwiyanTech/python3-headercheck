import sys ,requests , urllib3

# Create By LunaticTech , Dwiyan 
# Masih Belajar 


print("-----------------------------------------\n"
      "| HEADER CHECKER BY LUNATIC TECH PYTHON|\n"
      "| Gunakan Dengan Bijak Entar Berusaha Update :) |\n"
      "| COPYRIGHT BY LUNATIC TECH LICENSE GPL V 3\n"
      "--------------------------------------------"
      "\n\n")

if sys.version_info[0] < 3:
    print("Kamu menggunakan Python 2 atau dibawahnya silahkan Gunakan python 3")
    exit()

def internetcheck():
    try:
        urllib3.connection_from_url("http://google.com")
        return True
    except urllib3.exceptions.ConnectionError:
        return False

if internetcheck() == True :
    while True:
        cmd = input("checker =>")
        if cmd == "header" :
            URL = input("url =>")
            hasil = requests.get(URL)
            print(hasil.headers)
        if cmd == "response":
            URL = input("URL => ")
            hasil = requests.get(URL)
            print("Server Response Code => "+hasil.status_code)
        if cmd == "get-content":
            URL = input("URL => ")
            hasil = requests.get(URL)
            print(hasil.text)
        if cmd == "encoding":
            URL = input("URL => ")
            hasil = requests.get(URL)
            print(hasil.encoding)
        if cmd == "exit" :
            print("Have a Nice Dream :)")
            exit()
else:
    print("Check Your Internet Connection :(")
    exit()
