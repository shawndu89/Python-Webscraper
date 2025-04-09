    pip install requests beautifulsoup4

    import requests
    url = 'your_target_url'
    response = requests.get(url)
    html_content = response.text

    from bs4 import BeautifulSoup
    soup = BeautifulSoup(html_content, 'html.parser')

    # Find all elements with a specific tag
    elements = soup.find_all('tag_name')
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
        writer.writerow(['column1', 'column2'])
    # Write data rows
        for item in data:
            writer.writerow([item['column1'], item['column2']])
