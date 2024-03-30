"# Horoscope_WebApp2.0" 

This project is just for fun, to just see if the "https://cron-job.org/"
work well or not😅

Overview:
User can type name(which was unnecessary) and Date of birth to know their constellation and horoscope
Used beautiful soup to scrape the horoscopic data.
The Scraped data is stored in the horoscope.json

> cron-job.org is used to trigger the script.py whose task is the scrape the horoscopic data everyday
> It is triggered when the server recieves a GET request to a certian url (Example: https://dailyhoroscope.onrender.com/runScript)
> The script simple replaces the data store in horoscope.json with a new one.

To view this site live "https://dailyhoroscope.onrender.com/"
