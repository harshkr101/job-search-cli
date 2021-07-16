from requests_html import HTML, HTMLSession

# fetch jobs data


def fetch(role, location):
    url = "https://in.indeed.com/jobs?q={}&l={}".format(role, location)
    try:
        session = HTMLSession()
        response = session.get(url)
        container = response.html.find(
            ".job_seen_beacon", first=True)
        print(container)
        subcontainer = container.find("td")
        print("SUB", subcontainer)
        results = []
        for item in subcontainer:
            print("item", item)

        return results
    except Exception as e:
        raise e


fetch("Software Engineer", "Noida")
