# def getStartDate(st):
#     # Extract the year or year range.
#     date_str = st.split("(")[-1].split(")")[0]
#     # Check if it's a valid year or year range.
#     if not date_str.replace('-', '').isdigit():
#         return None
#     # Get the start year.
#     start_year = date_str.split("-")[0]
#     return start_year

# def getEndDate(st):
#     date_str = st.split("(")[-1].split(")")[0]
#     # Check if it's a valid year or year range.
#     if not date_str.replace('-', '').isdigit():
#         return None
#     # If there's a hyphen, get the end year. Otherwise, it's `-1`.
#     if "-" in date_str:
#         end_year = date_str.split("-")[1]
#         if not end_year:
#             end_year = str(int(getStartDate(st)) + 1)
#     else:
#         end_year = '-1'
#     return end_year

import re

def extract_date(st):
    # This regex pattern looks for a date pattern enclosed in parentheses
    pattern = r'\((\d{4}-\d{4}|\d{4}-|\d{4})\)'
    match = re.search(pattern, st)
    
    if not match:
        return None, None

    date_str = match.group(1)
    
    if "-" in date_str:
        start_year, end_year = date_str.split("-")
        
        if not end_year:
            end_year = str(int(start_year) + 1)
    else:
        start_year = date_str
        end_year = '-1'
        
    return start_year, end_year

lst = ["(2020-)", "random stuff (2021-2022)", "hey(2020)", "(I)(2021-2022)(I)"]

for item in lst:
    start, end = extract_date(item)
    print(f"Start Date: {start}, End Date: {end}")
