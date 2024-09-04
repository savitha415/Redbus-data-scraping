## Redbus data scraping with selenium and dynamic filtering using streamlit

## Video Tutorial
[Watch the video tutorial]([https://www.kapwing.com/videos/66d7ec984cdd205a4e0f2955])

### Technical Tags:
* Web Scraping 
* Selenium
* Streamlit
* SQL
* Data Analysis
* Python
* Interactive Application
* EDA

### Required Packages:
* Selenium
  * WebDriver
  * By
  * WebdriverWait
  * Expected Conditions
  * NoSuchElementException
* pymysql
  * mysql connector
  * Error
* streamlit
* pandas
* time
* re

### Procedure :
* Scraping the datas of both government buses (minimum 10 buses) and private buses from the website redbus using selenium.
  * Firstly, scraped the bus routes and bus links from the available state links in the website.
  * Then from each bus links, scraped the bus details with selenium as dataframe then to csv file.
* After scraping, EDA and treating null values and outliers is done if any.
* Then database was pushed to mysql using basic sql connection.
* Also some EDA is done is sql queries too to enhance the filtration process.
* Developing a streamlit webpage to fetch the stored data in a interactive way for the users to filter and see the results.
  * The streamlit app has three segments.
  * One is the Home page for the details of the application.
  * Bus Details Page for the filters and results.
  * About page for the link of detailed documentation of the project.
