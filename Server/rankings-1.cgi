#!/usr/bin/python

import cgi
import cgitb
cgitb.enable()  # for troubleshooting 

import csv
import sys
import operator

weights = {}
form = cgi.FieldStorage()
weights['plflagship'] = float(form.getvalue('plflagship'))
# weights['plothers'] = float(form.getvalue('plothers'))
weights['logic'] = float(form.getvalue('logic'))
weights['softeng'] = float(form.getvalue('softeng'))
weights['opsys'] = float(form.getvalue('opsys'))
weights['arch'] = float(form.getvalue('arch'))
weights['theory'] = float(form.getvalue('theory'))
weights['networks'] = float(form.getvalue('networks'))
weights['security'] = float(form.getvalue('security'))
weights['mlmining'] = float(form.getvalue('mlmining'))
weights['ai'] = float(form.getvalue('ai'))
weights['database'] = float(form.getvalue('database'))
weights['metrics'] = float(form.getvalue('metrics'))
weights['web'] = float(form.getvalue('web'))
weights['hci'] = float(form.getvalue('hci'))
weights['graphics'] = float(form.getvalue('graphics'))

startyear = int(form.getvalue('startyear'))
endyear = int(form.getvalue('endyear'))

"""
startyear = 2005
endyear = 2014

weights = {'plflagship': 1.0,'plothers': 0.5,'logic': 0.5, 'softeng': 0.5, 'opsys': 0.0, 'arch': 0.0, 'theory': 0.0, 'networks': 0.0, 'security': 0.0, 'mlmining': 0.0, 'ai': 0.0, 'database': 0.0,'metrics': 0.0, 'web': 0.0, 'hci': 0.0, 'graphics': 0.0}
"""

univcounts = {}
authcounts = {}
visited = {}

with open('intauthors-all.csv', mode='r') as infile:
    reader = csv.reader(infile)
    for rows in reader:
        aname = rows[0]
        uname = rows[1]
        area = rows[2]
        count = float(rows[3])
        year = int(rows[4])
        if (year >= startyear and year <= endyear and weights.get(area) >= 0.01):
            authcounts[aname] = authcounts.get(aname,0) + count
            if (authcounts[aname] >= 3 and not visited.has_key(aname)):
                univcounts[uname] = univcounts.get(uname, 0) + 1
                visited[aname] = True


print "Content-type: text/html"
print ""
print "<html>"
print "<head>"
print "<title>CS department rankings by productivity</title>"
print "</head>"
print "<body>" 
        
print "<h4>Ranking by group size</h4>"
print "<table>"
i = 0
j = 1
oldv = -100
rankedlist = sorted(univcounts.iteritems(), key=operator.itemgetter(1), reverse = True)  
for (k, v) in rankedlist:
    if (j > 20 and v != oldv):
        break
    if (v <= 0.01):
        break
    j = j + 1
    if (oldv != v):
        i = i + 1
    print  "<tr><td>", i, "</td><td>", k.encode('utf-8'), "</td><td>", v, "</td></tr>"
    oldv = v
print "</table>" 
print "\n"
print "<br>"

print "</body>"
print "</html>" 