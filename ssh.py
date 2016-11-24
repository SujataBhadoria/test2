import paramiko
import sys

def usage():
    '''Prints usage message'''
    print "usage:\n ssh.py server1,server2,server3.... servern"
    sys.exit(0)

def connect(hostname):
    '''Connects to hostname'''
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(hostname)
    except:
        print 'Error While conencting to ', hostname
        return
    return ssh

def run_command(con, command):
    '''Runs the command on server'''
    try:
        inp, out, err = con[0].exec_command(command)
    except:
        print 'Error while executing command on server %s', con[1]
        return
    return out

def print_out(out):
    '''Prints response from server'''
    for line in out.readlines():
        print line,

if __name__ == '__main__':
    if len(sys.argv) == 1:
        usage()
    connect_list = []
    host_list = sys.argv[1].split(',')
    print host_list
    for host in host_list:
        print host
        con = connect(host)
        if con is not None:
            connect_list.append((con, host))
    if len(connect_list) != 0:
        print 'Logged in.\n Type "exit" to disconnect or any other command to run on servers.'
    else:
        print 'Not able to connect to servers'
        sys.exit(1)
    while True:
        command = raw_input("$")
        if command == 'exit':
            sys.exit(0)
        for con in connect_list:
            print 'Response from host %s'% con[1]
            out = run_command(con, command)
            if out is not None:
                print_out(out)

