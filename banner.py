#-*-coding: utf-8 -*-
import random
red = '\033[31m' # Red
white = '\033[1;37m' # White
green = '\033[32m' # Green
orange = '\033[0;33m' # Orange
header1 = """
\033[1;37m

      ..      .        _            .          .. 
   x                                        ```````             ```` ```                                    
                              ````       `.--:////////:-..`      `` `                               
                          ```     .:+sydmmNNddNNhhhyhhmNmmNmdyo/-`     ```                          
                      ```    `:oymNMMMMs-/:/y.::.y.`:..h`-//osydmNdy+-`    ``                       
                    ``   `-ohmhs/yMMMMN.-NNydm- hm`.o-.: ://o`-/./MMMNmy+-    ``                    
                  `   `:smNh+:`://mMMMMs-//:hMs:dm/////:./++..:`-yMMMMdymNdo-   ``                  
                `   .odmyhNs`s-`+o+yMMMMNmNNMMMMMMMMMMMNNmdhohd./MMMMMm/`:smNh+.   `                
              `   :ymhyds:-o./d:/sdNMMMMMMMMh:sNMMd++NMMMMMMMMMNmMMMMMy`:ds/+dNms-   ``             
           ``   :hNMm..::+o/-+NNMMMMMMMMMMMm.  -/-`  oMMMMMMMMMMMMMMMm:+Nh- ://dMNs-   `            
          `   -yNy//ho`::+oNNMMMMMMMMMMMMMMo         .mMMMMMMMMMMMMMMMNMh..s+/hdhhNNs.   `          
        ``  `oNm:.+`-+`:NMMMMMMMMMMMMMMMMMN.          sMMMMMMMMMMMMMMMMMMms://-:.`dMMm/`  `         
       `   -dms//.`-ssyNMMMMMMMMMMMMMMMMMMd`          -MMMMMMMMMMMMMMMMMMMMNys--`+h+sNNy.   `       
      `   +Nh-:`:. -yMMMMMMMMMMMMMMMMMMMMMNhyssooooosydMMMMMMMMMMMMMMMMMMMMMMMd``:-`/mNMd:   `      
     `  `sMMs-.`o.+NMMMMMMMMMMMMMMMMMNmmhyydmmNNNNNNmmdyyhdmNMMMMMMMMMMMMMMMMMMhs/.-/--dMN/   `     
    `  `sMMMMNh+-sNMMMMMMMMMMMMMMNho/-.`    `..----..``   `.-:oymMMMMMMMMMMMMMMMNo+/-:smMMN+   `    
   `  `sMMMMMMMMNMMMMMMMMMMMMMMMMd/-.`                      `..:hMMMMMMMMMMMMMMMMMhodMMMMMMN/   `   
  `   +MMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhso++/::--------::/+oossdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN:   `  
  `  -NMMMMMMMMMMMMMMMMMMMMMMMMMMMMmo-``.yh:://+yh+//::sM+.``-odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMm`  `  
 `  `dMMMMMMMMMMMMMMMMMMMMMMMMMMMmo.     `syo+odMMdo+oymh`     `:yNMMMMMMMMMMMMMMMMMMMMMMMMMMMs   ` 
 `  +MMMMMMMMMMMMMMMMMMMMMMMMMMMMNmhys+:.``oNMMMMMMMMNy- `.-/oshdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMN-  ` 
`  `dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs.  -hNMMMMMh-   .odNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs   `
`  :MMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNs-`    :hNMN/   `./oymMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN`  `
   oMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNho:`  :m:  -sdNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM:  `
   yMMMMMMMmshdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMNhos/ /dMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMM+   
   dMMMMMMMNs///+mMMMMMMMMMMMMMmdMMMMMMMMMMmyyymm-hMMMMMMMMNdsNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs   
   mMMMMMMMMmhh///+yNMMMMMMNsyMNhhMMMMMMMMm+///dNmMMMMMMMMhsmmMNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMy   
   dMMMMMMMMNdy+s////+sdNdNMNMMMMysNMMdhmdo/////mMMNmNMMMdomMNo:mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMs   
   yMMMMMMMMMMNsyh//////:/:mMMMMm//////////////symo+++ooo+dMMd//hMNmMMMMMMMMMMMMMMMMMMMMMMMMMMMM+   
   oMMMMMMMMMMMMdodo/////++dMMMMMs////////////+NMy/hy/+omNMMMd/yNdy/o++shdyhNMNMMMMMMMMMMMMMMMMM:  `
`  -MMMMMMMMMMMMMhsdsooooosysdNNNNy+ooooooooosNMmoooooyymsyshmsdNyshy///ohy+osoymNNMMMMMMMMMMMMN`  `
`   dMMMMMMMMMMMMMNddmmNNMNNmdmdmMNdmdmmmmNNdmMMdmNyNNdNMMMdddhdddddNhmmNmmNNMMNMMNmMMMMMMMMMMMs   `
 `  /MMMMMMMMMMMMMMMMMNmNMMMmNMMMMMMMMMMMNmNmMMMMdMddmNhNMMMNNNNNMNmNMmmmmNNNMMMMMMmMMMMMMMMMMN.  ` 
 `  `dMMMMMMMMMMMMMMMMmmNmmmdmNNNMMMNMMMMMMMMMMMMmmhNmmddMMMMMMMMMMMMNdNddMMNNmMMMMmMMMMMMMMMMs   ` 
  `  -NMMMMMMMMMMMMMMMMMMMMNdmNNNmmmNNmdddNdNMMMMMNhmmMMMMMNNNMmNNMNdmMMdmMMMMmmMMMmMMMMMMMMMd`  `  
  `   +MMMMMMMMMMMMMMMMMMMMMMNNNmNNmNNNmmmddddmddmddddddddddmNdhddNdmMMMMMMMMmmmmmNmMMMMMMMMN-  ``  
   `   oMMMMMMMMMMMMMMMMMMMMNMMMMMMMMMMMNNNNNmNNddddmNNmdmdMMMMMMMMMMMMMMMMMMMNNMMNNMMMMMMMN/   `   
    `  `sMMMMMMMMMMMNMMMMMMNmMMMMMMMMMMMMMMMMMMMMNNNNmmdmNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMN/   `    
     `  `oNMMMMMMMms-sMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNdmNMMMMMMMMMN/   `     
      `   /mMMMMm+-:yNMNmMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMo`::/sdMMMMMd-   `      
           -hMMMmohNMMd/.yMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMNMMMm---:+yMMMNs.  ``       
        ``  `+mMMMMMNo.- so/mMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMd:oNMMm--NMMMMd/   `         
          `   .yNMMMm+hs .-yMMMddNMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMMmhhNMMy.-dMMmmMMMmo`   `          
            `   -yNMMMMh-oNMMMy`::+mMMMMMMMMMMMMMMMMMMMMMMMMNNMMMo./:odMMm//NMMMMms.   `            
              `   -smMMMMMMMMy`:No yMMMdssymMMMMNNMMNNMMMdo+//mMMh//+..NMMMMMMMmo.   `              
                `   .+dNMMMMMs::/.+NMMs`+h/.dMMM+.+m:-NMMh .//hMMMh//odMMMMMNh/`   `                
                  ``   -odNMMMMNmmMMMMo`sd:`hMMM/ --`.NMMM: +o+hMMMMMMMMMNh+.   ``                  
                    ``    -+ymNMMMMMMMNho+odMMMM+`mo..NMMMdsydmMMMMMMNmy/.    ``                    
                       ``    `-+ydNMMMMMMMMMMMMMNmMMNNMMMMMMMMMMNNds/.     `                        
                          ```     `-/oshmNNMMMMMMMMMMMMMNNmdhs+:.`     ```                          
                              `````       `.--::///:::-..`       ````                               
                                    ````````            ```` ```                                    
                  CREATE FRAMEWORK
 """
                  
header2 = """ 
\033[1;37m                 
 _______________________
< Evil Create Framework >
 -----------------------
 EDITOR:SigiT.P - Mr.Zeth
 Official Team: Brave Cyber Team 
 """
header3 = """
\033[1;37m
oooooooooooo              o8o  oooo  
`888'     `8              `""  `888  
 888         oooo    ooo oooo   888  
 888oooo8     `88.  .8'  `888   888  
 888    "      `88..8'    888   888  
 888       o    `888'     888   888  
o888ooooood8     `8'     o888o o888o  Creators.
"""

header4 = """
\033[1;36m

__________      ___________
___  ____/__   ____(_)__  /
__  __/  __ | / /_  /__  / 
_  /___  __ |/ /_  / _  /  -Creators
/_____/  _____/ /_/  /_/
"""   
header5 = """
\033[31m

██╗   ██╗ ██████╗██████╗ ████████╗
██║   ██║██╔════╝██╔══██╗╚══██╔══╝
██║   ██║██║     ██████╔╝   ██║   
╚██╗ ██╔╝██║     ██╔══██╗   ██║   
 ╚████╔╝ ╚██████╗██║  ██║   ██║   
  ╚═══╝   ╚═════╝╚═╝  ╚═╝   ╚═╝   
"""
header6 = """
\033[31m

 .S    S.    .S   .S_sSSs     .S       S.     sSSs  
.SS    SS.  .SS  .SS~YS%%b   .SS       SS.   d%%SP  
S%S    S%S  S%S  S%S   `S%b  S%S       S%S  d%S'    
S%S    S%S  S%S  S%S    S%S  S%S       S%S  S%|     
S&S    S%S  S&S  S%S    d*S  S&S       S&S  S&S     
S&S    S&S  S&S  S&S   .S*S  S&S       S&S  Y&Ss    
S&S    S&S  S&S  S&S_sdSSS   S&S       S&S  `S&&S   
S&S    S&S  S&S  S&S~YSY%b   S&S       S&S    `S*S  
S*b    S*S  S*S  S*S   `S%b  S*b       d*S     l*S  
S*S.   S*S  S*S  S*S    S%S  S*S.     .S*S    .S*P  
 SSSbs_S*S  S*S  S*S    S&S   SSSbs_sdSSS   sSS*S   
  YSSP~SSS  S*S  S*S    SSS    YSSP~YSSY    YSS'    
            SP   SP      \033[1;37m           Creators\033[31m
            Y    Y  
\033[1;37m
"""
def xe_header():
    headers = [header1, header2, header3, header4, header5, header6]
    return random.choice(headers)