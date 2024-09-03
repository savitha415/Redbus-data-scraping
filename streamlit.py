import streamlit as st
import mysql.connector
from mysql.connector import Error

# Define the MySQL database connection
def create_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="Savi@415",
        database="redbus_datas"
    )

# Function to execute a query
def run_query(query):
    try:
        connection = create_connection()
        cursor = connection.cursor(dictionary=True)
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except Error as e:
        st.write(f"Error: {e}")
        return []
    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

# Fetch distinct 'from_city' locations from the database
def get_from_locations():
    query = "SELECT DISTINCT from_city FROM bus_details"
    locations = run_query(query)
    return [row['from_city'] for row in locations if row['from_city']] if locations else []

# Fetch distinct 'to_city' locations from the database
def get_to_locations():
    query = "SELECT DISTINCT to_city FROM bus_details"
    locations = run_query(query)
    return [row['to_city'] for row in locations if row['to_city']] if locations else []

# Streamlit app with three pages
st.set_page_config(layout="centered")  # Center the content on the page

st.sidebar.title("Navigation")
page = st.sidebar.selectbox("Choose a page", ["🏠 Home", "🚌 RedBus Details", "📖 About"])

if page == "🏠 Home":
    st.title(":red[Redbus Data Scraping and Filtering with Streamlit Application]")
    st.subheader(":red[Technical Tags:]")
    
    topics = [
        "🔸 Web Scraping",
        "🔸 Selenium",
        "🔸 Streamlit",
        "🔸 SQL",
        "🔸 Data Analysis",
        "🔸 Python",
        "🔸 Interactive Application",
        "🔸 HTML for XPath"
    ]

    for topic in topics:
        st.write(topic)

    st.subheader(":red[Aim:]")
    objectives = [
        "🔸 Successfully scrape a minimum of 10 Government State Bus Transport data from Redbus website using Selenium. Also include the private bus information for the selected routes.",
        "🔸 Store the data in a structured SQL database.",
        "🔸 Develop an interactive Streamlit application for data filtering.",
        "🔸 Ensure the application is user-friendly and efficient."
    ]

    for objective in objectives:
        st.write(objective)

elif page == "🚌 RedBus Details":
    st.title(':red[_RedBus_ Data Filter Application]')

    # Fetch and display 'from_city' and 'to_city' locations
    from_locations = get_from_locations()
    to_locations = get_to_locations()
    
    from_location = st.selectbox("Select 'From' Location", options=from_locations)
    to_location = st.selectbox("Select 'To' Location", options=to_locations)

    # Star Rating filter
    rating_options = {
        "Any": None,
        "1-3": (1, 3),
        "3-4": (3, 4),
        "4-5": (4, 5)
    }
    rating_range = st.selectbox("Select Star Rating Range", list(rating_options.keys()))

    # Price Range filter
    price_options = {
        "Any": None,
        "Below 500": (0, 500),
        "500-800": (500, 800),
        "Above 800": (800, float('inf'))  # Special handling for "Above 800"
    }
    price_range = st.selectbox("Select Price Range", list(price_options.keys()))

    # Add a submit button
    if st.button("Submit"):
        # Build SQL query
        query = """
        SELECT DISTINCT
            Route,
            Bus_Name, 
            Bus_Type, 
            Departing_Time, 
            Reaching_Time, 
            Duration,
            Star_Rating, 
            Price, 
            Seats_Availability
        FROM bus_details
        WHERE 1=1
        """

        if from_location:
            query += f" AND from_city = '{from_location}'"

        if to_location:
            query += f" AND to_city = '{to_location}'"

        if rating_options[rating_range]:
            rating_min, rating_max = rating_options[rating_range]
            query += f" AND Star_Rating BETWEEN {rating_min} AND {rating_max}"

        if price_options[price_range]:
            price_min, price_max = price_options[price_range]
            if price_max == float('inf'):
                query += f" AND Price >= {price_min}"
            else:
                query += f" AND Price BETWEEN {price_min} AND {price_max}"

        # Run the query and display results
        result = run_query(query)

        # Show the number of available buses
        num_buses = len(result)
        st.write(f"Number of available buses: {num_buses}")

        if result:
            st.dataframe(result)
        else:
            st.write("No results found for the selected filters.")


elif page == "📖 About":
    st.title(":red[About This Project]")
    st.subheader("For detailed source code,")
    st.subheader("Documentation about the data,")
    st.subheader("SQL scripts,")
    st.subheader("And the details of the interactive Streamlit webpage,")
    st.subheader("Visit the GitHub link below:")

    st.markdown("[Click here](https://github.com/savitha415)")

