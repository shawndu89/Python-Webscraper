    pip install requests beautifulsoup4

    import requests
    from bs4 import BeautifulSoup

    url = https://finance.yahoo.com
    response = requests.get(url)
    html_content = response.text
 
    # Check if the request was successful
    if response.status_code == 200:
        # Parse the HTML content
        soup = BeautifulSoup(html_content, 'html.parser')

        # Find all elements with a specific tag
        elements = soup.find_all('a')
        for element in elements
        print(element.get('href'))

    else:
        print(f"Failed to retrieve the webpage. Status code: {response.status_code}")

########
    # Find an element by ID
    element = soup.find(id='element_id')
   # Find elements by class
    elements = soup.find_all(class_='class_name')
    # Extract text from an element
    text = element.text
    # Extract attribute from an element
    attribute = element['attribute_name']

    import csv
    #Open the file
    with open('data.csv', 'w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
    # Write header
        writer.writerow(['Symbol', 'Price'])
    # Write data rows
        for item in data:
            writer.writerow([item['Symbol'], item['Price']])
########
