## Log Parser

### Requirements

  You will need to install the user-agents tool using<br/>
    `pip3 install user-agents`

### Arguments

  `-l` Path to log file<br/>
  `-b` Most popular browser at rank<br/>
  `-m` Print any potentionaly malicious traffic, based on<br/>
        seach of Python, and curl<br/>
  `-s` Search browser data by comma separated list

### Examples

The log parser tool can currently be used as such:

To display the most popular web browser use:<br/>
    `python3 log_parser.py -l /path/to/logs -b 1`

To display possibly malicious entries use:<br/>
    `python3 log_parser.py -l /path/to/logs -m`

To search the logs based on browser used use:<br/>
    `python3 log_parser.py -l /path/to/logs -s Chrome,IE`
