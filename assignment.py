import requests
from bs4 import BeautifulSoup

def scrape_project_details(project_url):
    response = requests.get(project_url)
    soup = BeautifulSoup(response.content, 'html.parser')

    gstin = soup.find(string="GSTIN No").find_next('td').string.strip() if soup.find(string="GSTIN No") else 'N/A'
    pan = soup.find(string="PAN No").find_next('td').string.strip() if soup.find(string="PAN No") else 'N/A'
    name = soup.find(string="Name").find_next('td').string.strip() if soup.find(string="Name") else 'N/A'
    address = soup.find(string="Permanent Address").find_next('td').string.strip() if soup.find(string="Permanent Address") else 'N/A'

    return {
        'GSTIN No': gstin,
        'PAN No': pan,
        'Name': name,
        'Permanent Address': address
    }


def scrape_projects():
    url = 'https://hprera.nic.in/PublicDashboard'
    response = requests.get(url,verify=False)
    soup = BeautifulSoup(response.content, 'html.parser')

    projects = []
    project_links = soup.find_all('a', class_='btn btn-default', string='View Details')[:6]

    for link in project_links:
        project_url = 'https://hprera.nic.in' + link.get('href') 
        project_details = scrape_project_details(project_url)
        projects.append(project_details)


    for project in projects:
        print("GSTIN No:", project['GSTIN No'])
        print("PAN No:", project['PAN No'])
        print("Name:", project['Name'])
        print("Permanent Address:", project['Permanent Address'])
        print("-" * 40)


scrape_projects()
