import csv

csv_data = '''S. No.,Category,Topic
1,Certificates,Download Income Certificate Online
2,Certificates,Download Caste Certificate Online
3,Certificates,Apply for OBC Certificate Online
4,Certificates,Download BPL Certificate Online
5,Certificates,Download Death Certificate Online
45,Certificates,Apply for Residence Certificate
34,Certificates,Apply for Marriage Certificate Online
41,Certificates,Apply for First-Class Graduate Certificate
53,Certificates,Apply for Patta Transfer Online
52,Certificates,Download First-Class Certificate Registration Details
6,Ration Card Services,Apply for New Ration Card Online
7,Ration Card Services,Verify Mobile Number on Ration Card
8,Ration Card Services,Remove Family Member from Ration Card
9,Ration Card Services,Reactivate Deleted Ration Card
10,Ration Card Services,Check Ration Card Application Status
11,Ration Card Services,Download Ration Card Online
12,Ration Card Services,Apply for Ration Card Password
13,PAN Card Services,Retrieve Lost or Forgotten PAN Number
14,PAN Card Services,Get e-PAN
15,PAN Card Services,Link PAN with Aadhaar
16,PAN Card Services,Check PAN-Aadhaar Link Status
17,PAN Card Services,Update PAN Card Details
18,PAN Card Services,Update e-PAN
40,PAN Card Services,Reprint or Update PAN Card
19,Voter ID Services,Apply for Voter ID Card
20,Voter ID Services,Update Voter ID Card Details
21,Voter ID Services,Link Voter ID with Aadhaar
22,Voter ID Services,Change Photo/Colour in Voter ID Card
23,Aadhaar Services,Aadhaar Card: FAQs and Details
24,Aadhaar Services,Verify Aadhaar Details in Database
25,Aadhaar Services,Check Aadhaar-linked Mobile Number
26,Aadhaar Services,Use Masked Aadhaar
27,Aadhaar Services,Download Aadhaar Card
28,Aadhaar Services,Download Child\'s Aadhaar Card
29,Aadhaar Services,Download Aadhaar for Newborn
30,Aadhaar Services,Change Name in Aadhaar
31,Aadhaar Services,Download Aadhaar PVC Card
32,Aadhaar Services,Change Mobile Number in Aadhaar
33,Aadhaar Services,Edit Name or Mobile Number in Aadhaar
37,Government Records / Corrections,Change Name in Government Records
38,Government Records / Corrections,Download Government Certificates
39,Government Records / Corrections,Correct Date of Birth in School
35,Welfare Schemes,Apply for Pension Online
36,Digital Services,Download and Use DigiLocker
42,Passport Services,Apply for a Passport
43,Passport Services,Check Passport Application Status
44,Passport Services,Download Passport Application Form
'''

reader = csv.reader(csv_data.splitlines())
header = next(reader)  # Skip header row

menu_entries = {}
for row in reader:
    category = row[1].strip()
    topic = row[2].strip()
    
    # Sanitize topic for URL (lowercase, replace spaces with hyphens, remove special chars)
    sanitized_topic = topic.lower().replace(' ', '-').replace('/', '-').replace(':', '').replace('(', '').replace(')', '').replace('.', '')
    sanitized_topic = ''.join(char for char in sanitized_topic if char.isalnum() or char == '-')

    if category not in menu_entries:
        menu_entries[category] = []
    menu_entries[category].append({'name': topic, 'url': f'/{category.lower().replace(" ", "-")}/{sanitized_topic}/'})


config_menu_output = """
[menu]
  [[menu.main]]
    name = "Home"
    url = "/"
    weight = 1
"""

weight_counter = 1
for category, topics in menu_entries.items():
    weight_counter += 1
    config_menu_output += f"""
  [[menu.main]]
    name = "{category}"
    weight = {weight_counter}
    identifier = "{category.lower().replace(" ", "-")}"
"""
    for topic in topics:
        config_menu_output += f"""
  [[menu.main]]
    name = "{topic['name']}"
    url = "{topic['url']}"
    parent = "{category.lower().replace(" ", "-")}"
    weight = {weight_counter}
"""
        weight_counter += 1 # Increment weight for sub-items


with open('/home/ubuntu/document_site/config.toml', 'a') as f:
    f.write(config_menu_output)

print('Generated menu configuration and appended to config.toml')


