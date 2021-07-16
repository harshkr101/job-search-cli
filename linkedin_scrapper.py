import csv
from requests_html import HTML, HTMLSession

# fetch jobs data


def fetch(role, location):
    url = "https://in.linkedin.com/jobs/search?keywords={}&location={}&position=1&pageNum=0".format(
        role, location)
    try:
        session = HTMLSession()
        response = session.get(url)
        container = response.html.find(
            ".jobs-search__results-list", first=True)
        list = container.find("li")
        results = []
        for item in list:
            elements = item.text.split("\n")
            role = elements[0]
            company = elements[2]
            location = elements[3]
            date = elements[-1]
            results.append([role, company, location, date, "LinkedIn"])
        return results
    except Exception as e:
        raise e
