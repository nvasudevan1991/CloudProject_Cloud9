vmstat -t 1 >> vmstat.txt &
mpstat -P ALL 1 >> mpstat.txt &
iostat -xz 1 >> iostat.txt &
sar -n DEV 1 >> sar_dev.txt &
sar -n TCP,ETCP 1 >> sar_tct.txt &
sudo /usr/share/bcc/tools/cpudist 1 >> cpudist.txt &
sudo /usr/share/bcc/tools/biolatency -m 1 >> biolatency.txt &
sudo /usr/share/bcc/tools/cpudist 1 >> cpudist.txt &
sudo /usr/share/bcc/tools/cachestat 1 >> cachestat.txt &
sudo /usr/share/bcc/tools/runqlat 1 >> runqlat.txt &
