import requests
from colorama import Fore

list = open("proxy_list.txt","r")
proxies = list.readlines()

online_proxies = []

print(Fore.MAGENTA + """
      
'||''|.  '||''|.    ..|''||   '||' '|' '||' '|' 
 ||   ||  ||   ||  .|'    ||    || |     || |   
 ||...|'  ||''|'   ||      ||    ||       ||    
 ||       ||   |.  '|.     ||   | ||      ||    
.||.     .||.  '|'  ''|...|'  .|   ||.   .||.
      
      ..|'''.| '||'  '||' '||''''|    ..|'''.| '||'  |'  '||''''|  '||''|.   
    .|'     '   ||    ||   ||  .    .|'     '   || .'     ||  .     ||   ||  
    ||          ||''''||   ||''|    ||          ||'|.     ||''|     ||''|'   
    '|.      .  ||    ||   ||       '|.      .  ||  ||    ||        ||   |.  
     ''|....'  .||.  .||. .||.....|  ''|....'  .||.  ||. .||.....| .||.  '|' 
      

                                                    ~by ROLVARN
      
""")

for index, line in enumerate(proxies, start=0):

    try:
        control = requests.get(
             "http://ipinfo.io/json",
             proxies={
                  "http" : line,
                  "https" : line,
             }
        )

    except:
        continue

    if control.status_code == 200:
            online_proxies.append(line)
            print(Fore.GREEN + f"Proxy online: {line.strip()}")


with open("online_proxies.txt","w") as online_p:
     
     online_p.writelines(online_proxies)

print(Fore.YELLOW + f"\n[{index}] Online Proxies saved successfully!")

   


    


                
