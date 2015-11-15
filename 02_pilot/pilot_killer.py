import os
import commands

def pilot_killer():


    user=os.getenv('USER')
    sandbox = os.listdir('/home/%s/radical.pilot.sandbox/'%user)
    for folder in sandbox:
        if folder.startswith('rp.'):
            bootstrapper3_file=open('/home/%s/radical.pilot.sandbox/%s/agent_0.bootstrap_3.log'%(user,folder),'r')
            bootstrapper3_lines=bootstrapper3_file.readlines()
            bootstrapper3_pid=int(bootstrapper3_lines[1].split('pid:')[1])
            try:
                os.kill(bootstrapper3_pid,15)
            except:
                pass


if __name__ == "__main__":

    print 'Killing all active pilots'
    pilot_killer()
