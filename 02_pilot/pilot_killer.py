import os
import commands

def pilot_killer(user,rp_session_id,pilot):


    # This can be run from root. If you want to run from user space delete
    # the user parameter in the function definition and uncomment the next line
    #user=os.getenv('USER')
    bootstrapper3_file=open('/home/%s/radical.pilot.sandbox/%s-%s/agent_0.bootstrap_3.log'%(user,rp_session_id,pilot),'r')
    bootstrapper3_lines=bootstrapper3_file.readlines()
    bootstrapper3_pid=int(bootstrapper3_lines[1].split('pid:')[1])
    os.kill(bootstrapper3_pid,15)

