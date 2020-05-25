import json
from django.core.management.base import BaseCommand, CommandError
from chartjs.models import OrganizationUser, Date
from datetime import datetime


class Command(BaseCommand):
    help = 'Create users from jason file'

    @staticmethod
    def json_to_dict(filename):
        my_dict = {}
        with open(filename) as f:
            my_dict = json.loads(str(f.read()))
        return my_dict

    def handle(self, *args, **kwargs):
        my_dict = self.json_to_dict('Output.json')
        for user in my_dict['users']:
            for time in my_dict['users'][user]['time_of_activity']:
                d = Date.objects.create(data_time=datetime.strptime(str(time), '%m/%d/%Y %H:%M:%S'))
            OrganizationUser.objects.create(user_id=user,
                                            role=my_dict['users'][user]['role'],
                                            malicious_rate=my_dict['users'][user]['malicious_rate'],
                                            list_data_time=d)
