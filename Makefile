run-scanner:
	 docker build -t nmap-scanner ./
	 docker run -it --rm nmap-scanner