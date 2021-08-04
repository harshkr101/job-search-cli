import linkedin_scrapper
import indeed_scrapper
import csv

results = []


def fetch_linkedin(job_role, job_location):
    result = linkedin_scrapper.fetch(job_role, job_location)
    results.append(result)

def fetch_indeed(job_role,job_location):
    result = indeed_scrapper.fetch(job_role, job_location)
    results.append(result)



def save_to_file(data):
   with open("jobs.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(results)


# driver code
if __name__ == '__main__':
    job_role = input("Enter job role: ")
    job_location = input("Enter job location: ")
    fetch_indeed(job_role,job_location)
    fetch_linkedin(job_role,job_location)
    print(results)