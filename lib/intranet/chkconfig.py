#-*- coding: utf-8 -*-
#
# Copyright (c) 2017 - 2018, doudoudzj
# Copyright (c) 2012 - 2016, VPSMate development team
# All rights reserved.
#
# Intranet is distributed under the terms of the (new) BSD License.
# The full license can be found in 'LICENSE'.

"""Operation of chkconfig in redhat/centos.
"""

import os
import shlex
import subprocess


def set(service, autostart=True):
	"""Add or remove service to autostart list.
	"""
	if autostart:
		cmd = 'chkconfig %s on' % service
	else:
		cmd = 'chkconfig %s off' % service
	p = subprocess.Popen(shlex.split(cmd), stdout=subprocess.PIPE, close_fds=True)
	p.stdout.read()
	return p.wait() == 0 and True or False