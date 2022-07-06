import webbrowser
import zmq
#Kommunikation med Webb import

context = zmq.Context()
req_sock = context.socket(zmq.REQ)
req_sock.connect("tcp://127.0.0.1:2272")
sub_sock = context.socket(zmq.SUB)
sub_sock.connect("tcp://127.0.0.1:2273")
sub_sock.setsockopt_string(zmq.SUBSCRIBE, 'KC: ')


def get_key():
    #Implementera senare, tar emot keycode signal fran webben och konverterar till keyNumber
    msg = sub_sock.recv().decode('utf-8')

    return int(msg.replace('KC: ', ''))


def get_cmd(keyNumber):
    if keyNumber == 65: #A
        return "kwkL"
            
    elif keyNumber == 87: #W
        return "kwkF"
        
    elif keyNumber == 68: #D
        return "kwkR"
        
    elif keyNumber == 83: #S
        return "kbk"
        
    elif keyNumber == 32: #Space
        return "kbalance"
        
    elif keyNumber == 80: #P
        return "kpee"
        
    elif keyNumber == 81: #Q
        return "m0 75"
        
    elif keyNumber ==  69: #E 
        return "m0 -75"
    
    elif keyNumber == None:
        return None    

oldKey = 0 

def run():
    global oldKey
    xX_signal_Xx = get_key()
    keyNumber = xX_signal_Xx if oldKey != xX_signal_Xx else None

    cmd = get_cmd(keyNumber) 

    if cmd is not None:
        print(cmd)
        #req_sock.send_string(cmd)
        oldKey = keyNumber 



if __name__ == "__main__":
    while True:
        run()