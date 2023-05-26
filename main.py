# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License
# as published by the Free Software Foundation either version
# 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
# See the GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this script. If not, see <https://www.gnu.org/licenses/>.

import time
from nsdotpy.session import NSSession
from bs4 import BeautifulSoup
from datetime import datetime

def now():
    return datetime.now().strftime("%I:%M:%S %p") # Returns time in this format: 04:20:19 PM

try:
    # The variable below is for the Ctrl+C text to be right below to the line
    # The input() function forces all printed text to be on the same line, but regular print functions won't
    # So depending on the current phase of execution, you should add a \n or not
    logging_in = True
    nation_name = input(f"{now()} Please enter your Nation Name: ")
    password = input(f"{now()} Please enter your Password: ")

    logging_in = False
    session = NSSession(
        "Hellfire",
        "0.5.1",
        "The Chinese Soviet",
        nation_name,
        "enter",
        "https://github.com/Celinova/Hellfire"
    )

    authenticated = session.login(nation_name, password)

    if authenticated:
        print(f"{now()} Authentication successful!")
    else:
        print(f"{now()} Authentication failed.")

    last_time = time.time()  # initialize time of the last response
    banned_nations = set()  # set of banned nations

    while True:
        # Load the reports page
        reports_url = "https://www.nationstates.net/template-overall=none/page=reports"
        # Define the report settings
        report_settings = {
            "report_hours": "0.01",
            "report_self": "0",
            "report_region": "1",
            "report_dossier": "0",
        }

        # Include these settings in the POST request to load the reports page
        reports_response = session._html_request(reports_url, auth=(nation_name, password), data=report_settings)

        current_time = time.time()  # get the current time
        elapsed_time = ((current_time - last_time) * 1000).__round__()  # calculate the elapsed time in milliseconds
        print(f"{now()} Time elapsed since last response: {elapsed_time} ms")
        last_time = current_time  # update the time of the last response

        # Process the response with BeautifulSoup
        reports_soup = BeautifulSoup(reports_response.text, "html.parser")
        if str(reports_response.status_code) != "200":
          print(now() + " " + reports_response.status_code)
        
        # Parse arriving nations
        for report in reports_soup.find_all('li'):
            if " arrived from " in report.text:
                nation = report.find('a', class_='nlink').find('span', class_='nnameblock').text
                if nation not in banned_nations:
                    success = session.banject(nation)
                    if success:
                        now = datetime.now().strftime("%I:%M:%S %p")
                        print(f"{now} Successfully banjected {nation}.")
                        banned_nations.add(nation)
                    else:
                        now = datetime.now().strftime("%I:%M:%S %p")
                        print(f"{now} Failed to banject {nation}.")
                        banned_nations.add(nation)
except KeyboardInterrupt:
    if logging_in:
      print("\nHellfire closed by user.")
      quit()
    else:
      print("Hellfire closed by user.")
      quit()
