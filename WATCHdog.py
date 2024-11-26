import platform
import subprocess
import time
import datetime 

COUNTER = 0

def myping(ovpnService_ip):
    # Choose parame based on OS
    parame = "-n" if platform.system().lower() == "windows" else "-c"
    # Compose ping command
    command = ["ping", parame, "1", ovpnService_ip]
    response = subprocess.call(command)
    return response == 0


def reSTART_service():
    try:
        subprocess.run(['sudo', 'systemctl', 'restart', 'open_cli_when_START_os.service'], check=True)
        log('The service (OpenVPN cli) open_cli_when_START_os.service is reSTARTED normally')
    except subprocess.CalledProcessError as e:
        log(F'Error when reSTARTING The service (OpenVPN cli) open_cli_when_START_os.service: {e}')
        
def TimeNow():
    now = datetime.datetime.now()
    return now.strftime('%Y-%m-%d %H:%M:%S')

def log(arg):
    with open('/PATH/TO/YOUR/LOG_FILE.TXT', 'a') as F:
        F.write(F"{TimeNow()} {arg}\n")


if __name__ == '__main__':
    log('WATCHdog runs. LETS check!')
    for i in range(3):
        if COUNTER < 3:
            if myping("INTERNAL_IP_OF_THE_OPENVPN_SERVER._FOR_EXAMPLE_10.8.0.1"):
                print(COUNTER)
                log('The OpenVPN server pings normally. NEXT CHECK AFTER 5 mins. The end...')
                break
            else:
                time.sleep(1)
                print(COUNTER)
            COUNTER += 1
            log(F'Try number {COUNTER}. The RESULT is NEGATIVE')
    else:
        log('10.8.0.1 never pinged. The service is being RESTARTED (OpenVPN cli) open_cli_when_START_os.service')
        reSTART_service()
            
