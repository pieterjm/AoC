import re
import sys
import numpy as np

def doit(filename):
    file = open(filename, 'r')

    events = []
    guardid = 0
        
    while True:
        line = file.readline()
        if not line:
            break
        if len(line) == 0:
            break
        line = line.rstrip().lstrip()
        
        # #1 @ 342,645: 25x20
        # [1518-05-16 00:03] Guard #251 begins shift
        m = re.search('^\[(\d+-\d+-\d+) (\d+):(\d+)\] (.*)',line)
        if m:
            event = {                
                'ymd':m.group(1),
                'hour':int(m.group(2)),
                'minute':int(m.group(3)),
                'message':m.group(4),
                'ts':m.group(1) + " " + m.group(2) + ":" + m.group(3)
            }
            
            if event['message'] == 'falls asleep':
                event['event'] = 0
            elif event['message'] == 'wakes up':
                event['event'] = 1
            elif event['message'].endswith('begins shift'):
                event['event'] = 2
                guardid = int(event['message'].split('#')[1].split()[0])
                event['guardid'] = guardid
            else:
                print(line)
                sys.exit(0)

            events.append(event)
        else:
            print("problem in line: {}".format(line))
            sys.exit(0)


    events.sort(lambda x,y : cmp(x['ts'], y['ts']))
    guardid = 0
    for i in range(len(events)):
        if 'guardid' in events[i]:
            guardid = events[i]['guardid']
        else:
            events[i]['guardid'] = guardid

    guards = {}
    for event in events:
        day = event['ymd']
        if event['hour'] == 0:            
            if not day in guards:
                guards[day] = {}
                
            guardid = event['guardid']
            if not guardid in guards[day]:
                guards[day][guardid] = ['.'] * 60
        
            if event['event'] == 0:
                for t in range(event['minute'],60):
                    guards[day][guardid][t] = '#'
            elif event['event'] == 1:
                for t in range(event['minute'],60):
                    guards[day][guardid][t] = '.'
                
    for day in guards:
        for guardid in guards[day]:        
            print(guardid,"".join(guards[day][guardid]))

    guardsleep = {}
    for day in guards:
        for guardid in guards[day]:
            if not guardid in guardsleep:
                guardsleep[guardid] = [0] * 60
            for t in range(60):
                if guards[day][guardid][t] == '#':
                    guardsleep[guardid][t] += 1

    
    maxsleep = 0
    maxguardid = 0
    maxmin = 0
    for guardid in guardsleep:
        for t in range(len(guardsleep[guardid])):
            if guardsleep[guardid][t] > maxsleep:
                maxsleep = guardsleep[guardid][t]
                maxguardid = guardid
                maxmin = t
    print(maxsleep,maxguardid,maxmin)
    
    return maxmin * maxguardid
                    
filename = sys.argv[1]
print(doit(filename))


