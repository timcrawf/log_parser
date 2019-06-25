from lib.log_search import LogSearch
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-l", "--log", dest='log_location',
                  help="Path to log file")
parser.add_option("-b", "--browser", dest='rank',
                  help="Most popular browser at rank")
parser.add_option("-m", "--malicious", action="store_const", const= 'Python,curl',
                  dest='search_terms', help="Print any potentionaly malicious traffic, based on\nsearch of Pyhton and curl")
parser.add_option("-s", "--search-terms", dest='search_terms',
                  help="search browser data by comma separated list")
(options, args) = parser.parse_args()

if options.log_location == None:
    print("Must include path to logfile")
    exit()

log_search_instance = LogSearch(options.log_location)

if options.rank != None:
    browser_list = log_search_instance.sorted_browsers()
    browser_tuple = browser_list[(int(options.rank)-1)]

    print("The browser at position {} is: {}".format(options.rank, browser_tuple[0]))
    print("{} had {} hits".format(browser_tuple[0], browser_tuple[1]))

if options.search_terms != None:
    for entry in log_search_instance.return_malicious_traffic(search_terms=options.search_terms.split(',')):
        print entry
