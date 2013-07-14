#!/usr/bin/env python

# This is some code for the SWR2 recorder
# 2013-07-14: Accio started

import urllib2
import re
import time
import argparse

##record_len=120;
##outfile="./test-swr2.mp3"

parser = argparse.ArgumentParser()
parser.add_argument("outfile",
                    help="Output file")
parser.add_argument("interval", 
                    help="Time interval of recording, in seconds",
                    type=int)
args = parser.parse_args();

conn=urllib2.urlopen("http://mp3-live.swr.de/swr2_m.m3u")
r1=conn.read()
stream_url=r1.splitlines()[2]
target=open(args.outfile, "w")
conn=urllib2.urlopen(stream_url)
start_time=time.time();
end_time=start_time+args.interval;

while time.time()<end_time:
    target.write(conn.read(1024))

target.close()
    

    
