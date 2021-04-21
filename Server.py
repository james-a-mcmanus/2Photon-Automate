from pyngrok import ngrok
import SMS
import datetime
import os
import Write_html as wh
def start():
    wh.update("No experiment right now. <br> How's it going anyway?",100)
    os.chdir('C:\\Users\\lvbt\\Documents')
    # Open a HTTP tunnel on the default port 80
    # <NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:80">
    http_tunnel = ngrok.connect(80)
    # [<NgrokTunnel: "http://<public_sub>.ngrok.io" -> "http://localhost:80">]
    tunnels = ngrok.get_tunnels()
    url = str(tunnels[0]).split('NgrokTunnel:')[-1].split('->')[0].split('"')[1].split('//')[-1]
    dt = datetime.datetime.now().strftime('%y%m%d,%Hh')
    SMS.send(url,'keivan.razban@gmail.com','TP-Exp-'+dt)
    os.system('python -m http.server 80')

start()