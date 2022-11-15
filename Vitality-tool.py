"""
```    
isp            Xtra Telecom S.A.    
useragent        Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1    
ip            108.94.10.221    
country            Spain    
city            Barcelona    
state            Catalonia    
referer            HTTP-Referer is empty    
bot            Not    
latitude        41.38880000000000000    
longitude        2.15899000000000000    
accuracy        ip
```
"""

import random, time
from pystyle import *
from fake_useragent import UserAgent

banner = Colorate.Horizontal(Colors.yellow_to_red,'''
██╗   ██╗██╗████████╗ █████╗ ██╗     ██╗████████╗██╗   ██╗    ████████╗ ██████╗  ██████╗ ██╗     
██║   ██║██║╚══██╔══╝██╔══██╗██║     ██║╚══██╔══╝╚██╗ ██╔╝    ╚══██╔══╝██╔═══██╗██╔═══██╗██║     
██║   ██║██║   ██║   ███████║██║     ██║   ██║    ╚████╔╝        ██║   ██║   ██║██║   ██║██║     
╚██╗ ██╔╝██║   ██║   ██╔══██║██║     ██║   ██║     ╚██╔╝         ██║   ██║   ██║██║   ██║██║     
 ╚████╔╝ ██║   ██║   ██║  ██║███████╗██║   ██║      ██║          ██║   ╚██████╔╝╚██████╔╝███████╗
  ╚═══╝  ╚═╝   ╚═╝   ╚═╝  ╚═╝╚══════╝╚═╝   ╚═╝      ╚═╝          ╚═╝    ╚═════╝  ╚═════╝ ╚══════╝

                                        > Coded by TitoDelas <
''')

print(banner)

name = Write.Input("[>] TikTok Username -> ", Colors.blue_to_green, interval=0.0025)
Write.Print(f"[*] Doxing {name}!", Colors.blue_to_green, interval=0.05)

time.sleep(2)

def dox():
  ip = ""
  ip += ".".join(map(str, (random.randint(0, 255) for i in range(4))))
  mac_adr = ("52:54:00:%02x:%02x:%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),))
  ua = UserAgent()

  dox_col = f'''\n\n
  {Col.green}> {Col.reset}| {Col.orange}isp         {Col.reset}| {Col.green}Xtra Telecom S.A.    
  {Col.green}> {Col.reset}| {Col.orange}useragent   {Col.reset}| {Col.green}{ua.random}   
  {Col.green}> {Col.reset}| {Col.orange}ip          {Col.reset}| {Col.green}{ip} 
  {Col.green}> {Col.reset}| {Col.orange}MAC Adress  {Col.reset}| {Col.green}{mac_adr}   
  {Col.green}> {Col.reset}| {Col.orange}country     {Col.reset}| {Col.green}Spain    
  {Col.green}> {Col.reset}| {Col.orange}city        {Col.reset}| {Col.green}Barcelona    
  {Col.green}> {Col.reset}| {Col.orange}state       {Col.reset}| {Col.green}Catalonia    
  {Col.green}> {Col.reset}| {Col.orange}referer     {Col.reset}| {Col.green}HTTP-Referer is empty    
  {Col.green}> {Col.reset}| {Col.orange}bot         {Col.reset}| {Col.green}Not    
  {Col.red}x {Col.reset}| {Col.orange}latitude    {Col.reset}| {Col.red}n/a    
  {Col.red}x {Col.reset}| {Col.orange}longitude   {Col.reset}| {Col.red}n/a    
  {Col.green}> {Col.reset}| {Col.orange}accuracy    {Col.reset}| {Col.green}ip
  {Col.reset}
  '''
  dox = f'''
  > | isp         | Xtra Telecom S.A.    
  > | useragent   | {ua.random}   
  > | ip          | {ip} 
  > | MAC Adress  | {mac_adr}   
  > | country     | Spain    
  > | city        | Barcelona    
  > | state       | Catalonia    
  > | referer     | HTTP-Referer is empty    
  > | bot         | Not    
  x | latitude    | n/a    
  x | longitude   | n/a    
  > | accuracy    | ip
  '''
  print(dox_col)
  save = Write.Input("[>] Save information to a txt file ? [y / n]: ", Colors.blue_to_green, interval=0.0025)
  if save == 'y':
    with open(f'{name}_dox.txt', 'w') as f:
      f.write(f'{dox}')
  else:
    pass
dox()
