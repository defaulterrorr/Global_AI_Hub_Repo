import random

def isReady():
    print("Hazirsaniz baslayalim. Evet ise 'E'ye, Hayir ise 'H'ye basiniz: ")
    start_syc=0
    while 1==1:
        if start_syc>0:
            take_a_value = input("Simdi hazir misiniz?.Evet ise 'E'ye, Hayir ise 'H'ye basiniz: ")
        else:
            take_a_value = input('Seciminiz?: ')
        is_start= take_a_value =="e" or take_a_value =="E"or\
        take_a_value =="h" or take_a_value =="H"
        if not is_start :
         print("Hatali secim yaptiniz.Evet ise 'E'ye, Hayir ise 'H'ye basiniz: ")
        else:
            if take_a_value =="h" or take_a_value =="H":
                start_syc=start_syc+1
                if start_syc>10:
                  print("10 defadan fazla HAYIR sectiniz. Oyun sistem tarafindan baslatildi.")
                  break
            else:
                break  
    return take_a_value              

def tas_kagit_makas_USER():
    while True:
    
        is_t_k_m_user = int(input(
        "TAS icin 1'e basiniz.\n"
        "KAGIT icin 2'e basiniz.\n"
        "MAKAS icin 3'e basiniz: \n"))
        if is_t_k_m_user==1 or is_t_k_m_user==2 or is_t_k_m_user==3:
            break
        else :
            print("Hatali secim yaptiniz. Lütfen tekrar bir sayi giriniz")
            continue
    return is_t_k_m_user


def tas_kagit_makas_match():

    syc_user=0
    syc_pc=0 
    syc_list=0

    list_loop=[]
    start_point=1
    end_point=4

    while True:
    
        is_t_k_m_user=tas_kagit_makas_USER()
    
        is_t_k_m_pc = random.randint(start_point, end_point)
        list_loop.append(is_t_k_m_pc)

        if (is_t_k_m_user==1 and is_t_k_m_pc==2) or \
            (is_t_k_m_user==2 and is_t_k_m_pc==3) or \
            (is_t_k_m_user==3 and is_t_k_m_pc==1) :
            syc_pc=syc_pc+1
            print(f"{syc_list+1}. turu kaybettiniz.")
        elif (is_t_k_m_user==1 and is_t_k_m_pc==3) or \
             (is_t_k_m_user==2 and is_t_k_m_pc==1) or \
            (is_t_k_m_user==3 and is_t_k_m_pc==2) :
            syc_user=syc_user+1
            print(f"{syc_list+1}. turu kazandiniz.")
        else:
            syc_user=syc_user+1
            syc_pc=syc_pc+1
            print(f"{syc_list+1}. turda berabere kaldiniz.")

        syc_list=syc_list+1
        if syc_pc-syc_user>1:
            print("Oyunu kaybettiniz :( ")
        elif syc_pc-syc_user>1:
            print("OYUNU KAZANDINIZ :) ")
        else:
            print(f"Siz:{syc_user}-{syc_pc}:Robot")

        if abs(syc_pc-syc_user)>1:
            break
    return list_loop    
        

print("\nRobot ile oynayacaginiz tas kagit makas oyununa hosgeldiniz!\n"
      "Toplamda 2 tur kazanan ilk oyuncu oyunu kazanacaktir\n\n"
      "Her turda:\n"
      "- Kazanabilirsiniz\n"
      "- Kaybedebilirsiniz\n"
      "- Beraber kalabilirsiniz\n")


list_values = []
while True:
    isReady()
    print("\nBasliyoruz..") 
    list_temp=tas_kagit_makas_match()
#    list_values[0].append(list_temp[0])
#    list_values[1].append(list_temp[1])
    print("Robot secimleri: ",list_temp)
    take_a_value_rep = input("Tekrar oynamak ister misiniz. Evet ise 'E'ye, Hayir ise 'H'ye basiniz: ")
    if take_a_value_rep=="e" or take_a_value_rep=="E":
        print("-----------")
        continue
    else:
        break        


    




    
         
         