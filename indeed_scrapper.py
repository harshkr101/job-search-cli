from requests_html import HTML, HTMLSession

# fetch jobs data

def fetch(role, location):
    role = role.split(' ')
    role = "+".join(role)
    url = "https://in.indeed.com/jobs?q={}&l={}".format(role, location)
    try:
        session = HTMLSession()
        response = session.get(url)
        container = response.html.find(".job_seen_beacon")
        results = []

        for item in container:
            role = (item.find(".jobTitle")[0].text).split('\n')[-1]
            company = item.find(".companyName")[0].text
            location =  item.find(".companyLocation")[0].text
            date = item.find(".date")[0].text
            results.append([role, company, location, date,"Indeed"])
        return results
    except Exception as e:
        print(e)
