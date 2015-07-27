#!/usr/bin/python

import sys



if __name__ == '__main__':
	print '<<<<<<<<<< start of configuration >>>>>>>>>>'
	print 'Enter the IP of the config node'
	config_IP = raw_input()
	print 'Enter the username for config node. e.g:root'
	config_user = raw_input()
	print 'Enter the password for above user in config node.'
	config_pass = raw_input()
	f = open('inventory', 'w')
	f.write('[cloud]\n')
	f.write('cloud1')
	f.write(' ')
	f.write('ansible_ssh_host=' + config_IP)
	f.write(' ')
	f.write('ansible_ssh_port=22')
	f.write(' ')
	f.write('ansible_ssh_user=' + config_user)
	f.write(' ')
	f.write('ansible_ssh_pass=' + config_pass)
	f.write(' ')
	f.write('ansible_sudo_pass=' + config_pass)
	f.close()
        f = open('config_vars.yml', 'w')
        f.write('setup_cmd: /opt/contrail/contrail_packages/')
        f.write('\n')
        f.write('fab_cmd: /opt/contrail/utils/')
        f.write('\n')
        f.write('host_ip: ' + config_IP)
        f.close()
	print '<<<<<<<<<< configuration is done >>>>>>>>>>'
	print '<<<<<<<<<< Now you can run this command: >>>>>>>>>> '
	print 'Please copy your desired contrail and openstack image in playbook/files/ directory with contrail.deb name'
	print 'Also please copy and edit your testbed file in playbook/files/ directory with testbed.py name'
	print '<<<<<<<<<< ansible-playbook contrail.yml >>>>>>>>>>'
