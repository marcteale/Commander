#  _  __
# | |/ /___ ___ _ __  ___ _ _ ®
# | ' </ -_) -_) '_ \/ -_) '_|
# |_|\_\___\___| .__/\___|_|
#              |_|
#
# Keeper Commander
# Copyright 2017 Keeper Security Inc.
# Contact: ops@keepersecurity.com
#

class SharedFolder:
    """Defines a Keeper Shared Folder"""

    def __init__(self,shared_folder_uid='',revision='',default_manage_records=False,
                 default_manage_users=False,default_can_edit=False,default_can_share=False,
                 name='',records=[],users=[],teams=[]):
        self.shared_folder_uid = shared_folder_uid
        self.revision = revision
        self.default_manage_records = default_manage_records
        self.default_manage_users = default_manage_users
        self.default_can_edit = default_can_edit
        self.default_can_share = default_can_share
        self.name = name
        self.records = records
        self.users = users
        self.teams = teams

    def load(self,sf,revision=''):
        self.default_manage_records = sf['default_manage_records']
        self.default_manage_users = sf['default_manage_users']
        self.default_can_edit = sf['default_can_edit']
        self.default_can_share = sf['default_can_share']
        self.name = sf['name']
        self.records = sf['records'] if 'records' in sf else []
        self.users = sf['users'] if 'users' in sf else []
        self.teams = sf['teams'] if 'teams' in sf else []
        self.revision = revision

    def display(self):
        print('')
        print('{0:>20s}: {1:<20s}'.format('Shared Folder UID',self.shared_folder_uid))
        print('{0:>20s}: {1}'.format('Revision',self.revision))
        print('{0:>20s}: {1}'.format('Name',self.name))
        print('{0:>20s}: {1}'.format('Default Manage Records',self.default_manage_records))
        print('{0:>20s}: {1}'.format('Default Manage Users',self.default_manage_users))
        print('{0:>20s}: {1}'.format('Default Can Edit',self.default_can_edit))
        print('{0:>20s}: {1}'.format('Default Can Share',self.default_can_share))
        print('')
        print('{0:>20s}:'.format('Record Permissions'))

        if len(self.records) > 0:
            for r in self.records:
                print('{0:>20s}: {1}: {2}, {3}: {4}'.format(r['record_uid'],'Can Edit',r['can_edit'],'Can Share',r['can_share']))

        print('')
        print('{0:>20s}:'.format('User Permissions'))

        if len(self.users) > 0:
            for u in self.users:
                print('{0:>20s}: {1}: {2}, {3}: {4}'.format(u['username'],'Can Manage Records',u['manage_records'],'Can Manage Users',u['manage_users']))

        print('')
        print('{0:>20s}:'.format('Team Permissions'))

        if len(self.teams) > 0:
            for t in self.teams:
                print('{0:>20s}: {1}: {2}, {3}: {4}'.format(t['name'],'Can Manage Records',t['manage_records'],'Can Manage Users',t['manage_users']))

        print('')

    def to_string(self):
        target = self.shared_folder_uid + str(self.users) + str(self.teams)
        return target

    def to_lowerstring(self):
        return self.to_string().lower()

    def to_dictionary(self):
        teams = []
        team_uids = []

        for t in self.teams:
            teams.append(t['name'])
            team_uids.append(t['team_uid'])

        return {
            'uid': self.shared_folder_uid,
            'name': self.name,
            'default_manage_records': self.default_manage_records,
            'default_manage_users': self.default_manage_users,
            'default_can_edit': self.default_can_edit,
            'default_can_share': self.default_can_share,
            'users': [u['username'] for u in self.users],
            'record_uids': [r['record_uid'] for r in self.records],
            'teams': teams,
            'team_uids': team_uids,
        }
