import sys
import json
import requests


class Forecast(object):
    def __init__(self, account_id, api_token):
        self.url = 'https://api.forecastapp.com/'
        self.account_id = account_id
        self.headers = {
                        'Forecast-Account-ID': account_id,
                        'Authorization': 'Bearer ' + api_token
                       }


    def get(self, endpoint):
        results = requests.get(self.url + endpoint, headers=self.headers)
        print(results.status_code)
        if results.status_code == 200:
            return results.json()
        else:
            raise ValueError("Non-200 error code from server: " + str(results.status_code) + "\n" + results.text)


    def get_account(self):
        return self.get('accounts/' + self.account_id)['account']


    def get_assignments(self):
        return self.get('assignments')['assignments']
    
    
    def get_clients(self):
        return self.get('clients')['clients']


    def get_future_scheduled_hours(self):
        return self.get('aggregate/future_scheduled_hours/20190101')['future_scheduled_hours']


    def get_milestones(self):
        return self.get('milestones')['milestones']


    def get_people(self):
        return self.get('people')['people']
    
    
    def get_placeholder(self):
        return self.get('placeholders/24721')['placeholder']
    
    
    def get_placeholders(self):
        return self.get('placeholders')['placeholders']


    def get_projects(self):
        return self.get('projects')['projects']


    def get_remaining_budgeted_hours(self):
        return self.get('aggregate/remaining_budgeted_hours')['remaining_budgeted_hours']
    
    
    def get_repeated_assignment_sets(self):
        return self.get('repeated_assignment_sets')['repeated_assignment_sets']
    
    
    def get_repeated_assignment_set(self):
        return self.get('repeated_assignment_sets/745206')['repeated_assignment_set']
    
    
    def get_subscription(self):
        return self.get('billing/subscription')['subscription']
    
    
    def get_user_connections(self):
        return self.get('user_connections')['user_connections']
    
    
    def who_am_i(self):
        return self.get('whoami')['current_user']


