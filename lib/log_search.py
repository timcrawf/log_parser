import shlex
from user_agents import parse

class LogSearch:
    def __init__(self, log_location):
        self.logs = self.read_log(log_location)

    def read_log(self, log_location):
        with open(log_location) as f:
            entries = f.readlines()

        return entries

    def parse_user_agent(self, user_agent):
        parsed_user_agent = str(parse(user_agent))

        return parsed_user_agent

    def get_browser_name(self, user_agent):
        parsed_user_agent = self.parse_user_agent(user_agent)
        browser_name = parsed_user_agent.split('/')[2].split(' ')[1]

        return browser_name

    def get_user_agent(self, log_line):
        user_agent = shlex.split(log_line)[13]

        return user_agent

    def count(self, entries, browsers=False, agent=False):
        count_dict = {}

        for entry in entries:
            if browsers == True:
                item = self.get_browser_name(self.get_user_agent(entry))
            if agent == True:
                item = self.parse_user_agent(self.get_user_agent(entry))
            if item in count_dict:
                count_dict[item] += 1
            else:
                count_dict[item] = 1

        return count_dict

    def sort_by_value(self, dictionary):
        sorted_list_tuple = sorted(dictionary.items(), key=lambda x: x[1], reverse = True)

        return sorted_list_tuple

    def sorted_browsers(self):
        return self.sort_by_value(self.count(self.logs, browsers=True))

    def return_malicious_traffic(self, search_terms=['Python', 'curl']):
        return_list = []
        for entry in self.logs:
            parsed_entry = self.parse_user_agent(self.get_user_agent(entry))
            for term in search_terms:
                if parsed_entry.find(term) != -1:
                    return_list.append(entry)
        return return_list
