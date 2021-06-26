# pingLogAnalyzer

1) Run a ping sript and save the log in a file.
For eg:
      ping 8.8.8.8 >> log &
2) When the log is complete i.e the pingScript is stopped, run the analyzeLog.py program and pass on the name of the log file.
3) Give input telling how many lines of the log file you want to analyze (give 0 for analyzing the complete log file)
4) Get the total ping drop count and the longest ping drop statistics   
