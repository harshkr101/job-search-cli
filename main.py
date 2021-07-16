import linkedin_scrapper
import csv

results = []


def main(job_role, job_location):
    result = list(linkedin_scrapper.fetch(job_role, job_location))
    results.append(result)
    printJobs()


def printJobs():
    for result in results:
        for res in result:
            print()
            print("Role:", res[0])
            print("Company:", res[1])
            print("Location", res[2])
            print("Date:", res[3])
            print("Source:", res[-1])
            print()


'''    with open("results.csv", "w", newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerows(results)'''


# driver code
if __name__ == '__main__':
    job_role = input("Enter job role: ")
    job_location = input("Enter job location: ")
    main(job_role, job_location)
