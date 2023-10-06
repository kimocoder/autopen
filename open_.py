import general_use
import dependencies
import tools
import os
import subprocess


#OPEN TOOLS IN THE BACKGROUND

def open_(toolname):
    '''
    This function opens the specified tool (toolname)
    '''

    op_rc = -1

    t = ['Kayak', 'caringcaribou', 'Bluelog', 'bluemaho', 'canbus-utils']
    if toolname in t:
        current = os.getcwd()
        path = f'{current}/{toolname}'
        os.chdir(path)

    #CAN TOOLS
    if toolname == 'Kayak':
        kayak_run_path = '/application/target/kayak/bin'
        print ('Changing directory to', kayak_run_path, '...')
        current_dir = os.getcwd()
        path = current_dir + kayak_run_path
        os.chdir(path)
        op_rc = subprocess.run(['./kayak']).returncode
    elif toolname == 'can-utils':
        op_rc = subprocess.run(['gnome-terminal']).returncode
    elif toolname == 'canbus-utils':
        op_rc = subprocess.run(['gnome-terminal']).returncode
    elif toolname == 'caringcaribou':   #will not be able to open
        # recommend adding the functionality to be able to open a specific
        # module but for now it just opens a terminal
        # current_dir = os.getcwd()
        # path = current_dir + '/tool'
        # os.chdir(path)
        # o = '/modules/'
        # op_rc = subprocess.run(['./cc.py', o]).returncode
        pass
    elif toolname == 'pyobd':   #BUGGY
        current = os.getcwd()
        path = f'{current}/pyobd-0.9.3'
        os.chdir(path)
        op_rc = subprocess.run(['./pyobd']).returncode
    elif toolname == 'o2oo':
        current = os.getcwd()
        path = f'{current}/O2OO-0.9'
        os.chdir(path)
        op_rc = subprocess.run(['gnome-terminal']).returncode
    elif toolname == 'can-utils-x':
        op_rc = subprocess.run(['python', 'main.py']).returncode
    elif toolname == 'j1939':
        op_rc = subprocess.run(['gnome-terminal']).returncode
    elif toolname == 'c0f':
        op_rc = subprocess.run(['gnome-terminal']).returncode
    elif toolname == 'udsim':
        op_rc = subprocess.run(['gnome-terminal', '-e', 'udsim', 'can0']).returncode

    elif toolname == 'bluelog':
        op_rc = subprocess.run(['./bluelog']).returncode    #works if you have a bluetooth device up
    elif toolname == 'bluemaho':
        op_rc = subprocess.run(['./bluemaho.py']).returncode
    elif toolname == 'btscanner':
        op_rc = subprocess.run(['gnome-terminal']).returncode

    elif toolname == 'wireshark':
        op_rc = subprocess.run(['gnome-terminal', '-e','wireshark']).returncode
    elif toolname == 'aircrack-ng':
        op_rc = subprocess.run(['gnome-terminal']).returncode
    elif toolname == 'tshark':
        op_rc = subprocess.run(['gnome-terminal']).returncode

    elif toolname == 'gnuradio':
        op_rc = subprocess.run(['gnome-terminal', '-e', 'gnuradio-companion']).returncode
    elif toolname == 'gqrx':
        op_rc = subprocess.run(['gqrx']).returncode

    elif toolname == 'katoolin':
        op_rc = subprocess.run(['gnome-terminal', '-e', 'katoolin']).returncode

    else:
        return 0


    if op_rc != 0:
        print ('STARTUP FAILED: Failed to open', toolname)
        print ('ERROR CODE:', op_rc)
    else:
        print ('STARTUP SUCCESSFUL: Successfully opened', toolname)


    #check path to make sure it's in the autopen directory
    curr = os.getcwd()
    back_index = curr.rfind('/')
    ap_index = curr.find('autopen')
    path = curr[:ap_index+7] if curr[back_index:] != '/autopen' else curr
    os.chdir(path)

    return op_rc

def test(tool):
    return 0

