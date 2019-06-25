## Log Parser

###Requirements
  You will need to install the user-agents tool using
    `pip3 install user-agents`

###Arguments

  `-l` Path to log file
  `-b` Most popular browser at rank
  `-m` Print any potentionaly malicious traffic, based on
        seach of Python, and curl
  `-s` Search browser data by comma separated list

###Examples

The log parser tool can currently be used as such:

To display the most popular web browser use:
    `python3 log_parser.py -l /path/to/logs -b 1`

To display possibly malicious entries use:
    `python3 log_parser.py -l /path/to/logs -m`

To search the logs based on browser used use:
    `python3 log_parser.py -l /path/to/logs -s Chrome,IE`
