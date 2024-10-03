"""-----------------------------------FETCH AND STORE DAILY CASE STATUS-----------------------------------------------"""
# Function to fetch daily case status and store in CSV
def fetch_and_store_data():
    start_time = time.time()
    logging.info("Started fetching daily case status...")
    url = 'https://supremecourt.gov.np/web/eng/index'

    try:
        response = requests.get(url, verify = False)
        response.raise_for_status()
        html_content = response.text
        soup = BeautifulSoup(html_content, 'html.parser')
        table = soup.find('table', {'width': '100%'})
        if table is None:
            print("Could not find the table on the webpage.")
            return

        rows = table.find_all('tr')
        data = {}
        for row in rows:
            cols = row.find_all(['th', 'td'])
            cols = [col.text.strip() for col in cols]
            if len(cols) == 2:
                data[cols[0]] = {'Count': int(cols[1])}

        df = pd.DataFrame(data).T #transposes df so that cas type becomes column
        df.reset_index(inplace=True) #resetes the index of dataframe
        df.columns = ['Case Type', 'Count']
        csv_file = 'daily_case_status.csv'

        if not os.path.exists(csv_file):
            df.to_csv(csv_file, mode='w', header=True, index=False)
            print("Created new CSV file.")
        else:
            existing_df = pd.read_csv(csv_file)
            for case_type in df['Case Type']:
                if case_type in existing_df['Case Type'].values:
                    existing_df.loc[existing_df['Case Type'] == case_type, ['Count']] = df.loc[df['Case Type'] == case_type, ['Count']].values
                else:
                    existing_df = existing_df.append(df[df['Case Type'] == case_type], ignore_index=True)

            existing_df.to_csv(csv_file, mode='w', header=True, index=False)
            print("CSV file updated.")
    except requests.RequestException as e:
        logging.error(f"Error occurred: {e}")

    end_time = time.time()
    time_taken = end_time - start_time
    logging.info(f"Finished fetching daily case status in {time_taken:.2f} seconds.")
    print(f"Daily case status fetching completed in {time_taken:.2f} seconds.")


# Function to schedule daily data extraction at a specific time
def schedule_tasks():
    try:
        # Schedule daily case status at 10:30 AM and 5:30 PM Nepal time
        schedule.every().day.at("14:08").do(fetch_and_store_data)
        schedule.every().day.at("16:23").do(fetch_and_store_data)

        print("Scraping scheduled for 10:30 AM and 5:30 PM.")

        while True:
            schedule.run_pending()
            time.sleep(1)

    except KeyboardInterrupt:
        print("Scheduling stopped by user.")
    finally:
        session.close()

# Start the scheduling
if __name__ == "__main__":
    schedule_tasks()
