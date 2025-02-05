#!/usr/bin/python3

# This is a script to find when a course was opened in past quarters.
# Usage: python find_course_history.py department_name course_number
# Example: python find_course_history.py COMPSCI 222

import urllib2, sys


def find_between(s, first, last):
    try:
        start = s.index(first) + len(first)
        end = s.index(last, start)
        return s[start:end]
    except ValueError:
        return ""


url = 'http://websoc.reg.uci.edu/perl/WebSoc'
webfile = urllib2.urlopen(url).read()

department = sys.argv[1]
course = sys.argv[2]
print('Quarters have course', department, course, ':')

for line in webfile.splitlines():
    if "<option value=\"20" in line:
        param = find_between(line, "value=\"", "\" style")
        term = find_between(line, ">", "<")
        query_url = "http://websoc.reg.uci.edu/perl/WebSoc?Submit=Display+Web+Results&YearTerm=" + param + "&Dept=" + department
        response = urllib2.urlopen(query_url).read()

        for responseLine in response.splitlines():
            if "CourseTitle" in responseLine and course in responseLine:
                print(term)
                break
