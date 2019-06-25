from lib.log_search import LogSearch
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--log", dest='log_location',
                  help="Path to log file")
parser.add_option("-b", "--browser", dest='rank',
                  help="Most popular browser at rank")
parser.add_option("-m", "--malicious", action="store_const", const= 'Python,curl,Spider,Nimbostratus-Bot,Nimbostratus-Bot,YandexBot',
                  dest='search_terms', help="Print any potentionaly malicious traffic, based on\nsearch of Pyhton, curl,Spider, Nimbostratus-Bot, and YandexBot")
parser.add_option("-s", "--search-terms", dest='search_terms',
                  help="search browser data by comma separated list")
(options, args) = parser.parse_args()

if options.log_location == None:
    print("Must include path to logfile")
    exit()

log_search_instance = LogSearch(options.log_location)

if options.rank != None:
    browser_list = log_search_instance.sorted_browsers()
    if int(options.rank)-1 >= len(browser_list):
        rank_position = len(browser_list)-1
        print("Selection out of range: using {}".format(rank_position+1))
    else:
        rank_position = int(options.rank)-1

    browser_tuple = browser_list[rank_position]

    print("The browser at position {} is: {}".format(rank_position+1, browser_tuple[0]))
    print("{} had {} hits".format(browser_tuple[0], browser_tuple[1]))

if options.search_terms != None:
    for entry in log_search_instance.search_browsers(search_terms=options.search_terms.split(',')):
        print(entry)
