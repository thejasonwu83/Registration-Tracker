import requests
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup

def build_request(year, semester, subject_code, course_number, crn=""):
    if not crn:
        return f"http://courses.illinois.edu/cisapp/explorer/schedule/{year}/{semester}/{subject_code}/{course_number}.xml?mode=cascade"
    return f"http://courses.illinois.edu/cisapp/explorer/schedule/{year}/{semester}/{subject_code}/{course_number}/{crn}.xml"

"""
-Mode does not matter for full fledged URL's (that is, all attributes given, down to the CRN)
-Cascade and Detail modes yield the same response for course-specific requests (no CRN)
    -MUST use mode=cascade or mode=detail for course specific requests! Otherwise info is severely lacking
-The catalog requests are of no use: they only return past offerings of courses
"""

# returns a list of section data
def get_course(year, semester, subject_code, course_number, crn):
    url = build_request(year, semester, subject_code, course_number, crn)
    print(f"making request to {url}")
    r = requests.get(url)
    try:
        soup = BeautifulSoup(r.content, 'xml')
        section = soup.find('sectionNumber').text
        enroll = soup.find('enrollmentStatus').text
        return [section, enroll]
    except:
        return ["", ""]
