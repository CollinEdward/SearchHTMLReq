import requests

req_input = input("What do you want to search: ")

# Function to render html
def html_page(req):
    url = 'http://www.google.com/search?q=' + req
    print(requests.get(url).text)


if __name__ == "__main__":
    html_page(req=req_input)