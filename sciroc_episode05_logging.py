#!/usr/bin/env python
""" Logging functions for SciRoc Episode 05 PickNPack
The functions will help in logging the state of the robot to the server and
updating the central server about the state of the environment and the robot.

This program is free software: you can redistribute it and/or modify it under
the terms of the GNU General Public License as published by the Free Software
Foundation, either version 3 of the License, or (at your option) any later
version.
This program is distributed in the hope that it will be useful, but WITHOUT
ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS
FOR A PARTICULAR PURPOSE. See the GNU General Public License for more details.
You should have received a copy of the GNU General Public License along with
this program. If not, see <http://www.gnu.org/licenses/>.

__author__ = "Deebul Nair"
__contact__ = "deebul.nair@h-brs.de"
__date__ = "30 August, 2021"
__status__ = "Production"
__version__ = "0.0.1"
"""

import requests

SERVER_URL = 'https://docs.google.com/forms/d/e/1FAIpQLSePUiY-BW1yyC18CLIWOf2TK6vPtpDGW4_PlRt7bC_lO8pi2g/formResponse'
USER_AGENT = {'Referer':'https://docs.google.com/forms/d/e/1FAIpQLSePUiY-BW1yyC18CLIWOf2TK6vPtpDGW4_PlRt7bC_lO8pi2g/viewform',
             'User-Agent': "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"}
FORM_DATA = {'team_name' : 'entry.1590344743' ,
             'started' : 'entry.193753102' ,
             'object_picked' : 'entry.1555750726' ,
             'object_placed' : 'entry.1808542488' ,
             'stopped' : 'entry.373581570'  }

class LogStatusSciRoc:
    """Logging Status to SciRoc server """

    def __init__(self, team_name: str):
        """ Initialize team name """
        self.team_name = team_name
        
    def log_run_started(self):
        """ Send message for starting of run """
        send_data = {FORM_DATA['team_name']:self.team_name,
                     FORM_DATA['started']:'TRUE'}
        print (send_data)
        r = requests.post(SERVER_URL, data=send_data, headers=USER_AGENT)
        return r

    def log_object_picked(self, object_name: str):
        """ Log message for object picked """
        send_data = {FORM_DATA['team_name']:self.team_name,
                     FORM_DATA['object_picked']:object_name}
        print (send_data)
        r = requests.post(SERVER_URL, data=send_data, headers=USER_AGENT)
        return r

    def log_object_placed(self, object_name: str):
        """ Log message about placed object """
        send_data = {FORM_DATA['team_name']:self.team_name,
                     FORM_DATA['object_placed']:object_name}
        print (send_data)
        r = requests.post(SERVER_URL, data=send_data, headers=USER_AGENT)
        return r

    def log_run_stopped(self):
        """ Long message that run stopped """
        send_data = {FORM_DATA['team_name']:self.team_name,
                     FORM_DATA['stopped']:'TRUE'}
        print (send_data)
        r = requests.post(SERVER_URL, data=send_data, headers=USER_AGENT)
        return r
        
