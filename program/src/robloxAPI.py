import requests
import sys
from selenium import webdriver
from selenium.webdriver.common.by import By   
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

robloxGroupBaseURL = "https://groups.roblox.com/v1/groups/"
rolimonGroupBaseURL = "https://www.rolimons.com/group/"

option = Options()
option.add_argument("--headless")  # Run Chrome in headless mode (without opening a window)

class GroupData:
    
    def getGroupMembers(groupID) -> int:
        response = requests.get(robloxGroupBaseURL + str(groupID))
        error1 = "ERROR (RBLXAPI - getGroupMembers) - groupID is either invalid or doesn't exist! \n"
        error2 = "ERROR (RBLXAPI - getGroupMembers) - Unknown error occurred! Possibly the API is down or your internet is unstable. \n"

        if response.status_code == 200:
            print("\nINFO (RBLXAPI - getGroupMembers) - Successfully connected to Roblox API!")

            data = response.json()
            members = data.get("memberCount")

            print("INFO (RBLXAPI - getGroupMembers) - Returning data... \n")

            return members
        
        elif response.status_code == 400:
            sys.exit(error1)
    
        else:
            sys.exit(error2)

    def getDailyMemberJoins(groupid, amount) -> list:
        driver = webdriver.Chrome(options=option)
        driver.get(rolimonGroupBaseURL + str(groupid))

        wait = WebDriverWait(driver, 20)

        print("INFO (RBLXAPI - getDailyMemberJoins) - Successfully connected to Rolimon's website!")

        print("INFO (RBLXAPI - getDailyMemberJoins) - Opening required elements...")

        # Click the context button for Highcharts
        buttons = wait.until(
            EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".highcharts-contextbutton"))
        )

        buttons[1].click() # Click the second context button, which is for the "Members over time" graph
    
        # Click "View data table"
        wait.until(EC.element_to_be_clickable((By.XPATH, "//li[contains(text(), 'View data table')]"))).click()

        # Wait for the table to appear
        table = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".highcharts-data-table")))

        print("INFO (RBLXAPI - getDailyMemberJoins) - Parsing data...")

        # Parse the page now that the table is loaded
        soup = BeautifulSoup(driver.page_source, "html.parser")

        driver.quit()

        # Parse the table
        table = soup.find("table", {"id": "highcharts-data-table-1"})
        rows = table.find_all("tr")[1:]  # skip header

        # Parse rows
        data = [[c.get_text(strip=True) for c in r.find_all("td")] for r in rows]

        # Return only the latest 'amount' rows
        data = data[-amount:]


        print("INFO (RBLXAPI - getDailyMemberJoins) - Returning data... \n")

        return data

    if __name__ == "__main__":
        print("Running RobloxAPI")
        #members = getGroupMembers(input("RBLX Group ID: "))
        dailyJoins = getDailyMemberJoins(2648601, 15)
        print(dailyJoins)