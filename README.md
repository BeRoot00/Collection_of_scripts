## Script Collection

This repository contains a collection of scripts that I use for various tasks and projects. Each script is designed to perform a specific task and can be used independently or integrated into other projects.

### vuln_banner.py

This script is a network vulnerability scanner that checks if a server is vulnerable to specific exploits. It connects to a specified list of IP addresses on predefined ports and captures the server banners. It then compares the banners against a list of known vulnerabilities to identify potential security risks.

Before running the script, ensure that you have the following:
- Python 3 installed
- The socket module available
- The vuln_banners.txt file with a list of known vulnerabilities

### crack_passwd_hash.py
This is a Python script that attempts to crack passwords by comparing them with entries in a wordlist. It utilizes the crypt module for password encryption and checking.

Prerequisites
- Python 3.x
- A wordlist file (wordlist.txt) containing a list of potential passwords.
- A password file (passwd.txt) with the hashed passwords.

On modern NixBased Operating systems, the /etc/shadow file stores the hashed password and provides the ability to use more secure hashing algorithms.

### web_perf.py

This code analyzes the response time of a web server by sending multiple requests and measuring the duration of each request. It also generates a histogram of the durations to visualize the distribution.

Prerequisites
- Python 3.x
- Required packages: schedule, requests, matplotlib, numpy

### file_deduplication.py
This is a Python script that performs file deduplication. It reads a file, removes duplicate lines, and writes the result to a new file.
  
## Contribution

Contributions are welcome! If you want to improve these scripts, fix any issues, or add new features, feel free to submit a pull request. Please provide a clear description of your changes and make sure to test any modified scripts before submitting your contribution.
