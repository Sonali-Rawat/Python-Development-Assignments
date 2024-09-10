# Python program that reads a JSON file containing NASA APOD data and prints the keys “explanation” and “title”


import json

# Sample JSON data (replace this with the actual JSON data from the URL)
json_data = '''
{
   "date":"2024-09-10",
   "explanation":"The dark Horsehead Nebula and the glowing Orion Nebula are contrasting cosmic vistas. Adrift 1,500 light-years away in one of the night sky's most recognizable constellations, they appear in opposite corners of the above stunning mosaic. The familiar Horsehead nebula appears as a dark cloud, a small silhouette notched against the long glow of hydrogen -- here shown in gold -- at the lower left. Alnitak is the easternmost star in Orion's belt and is seen as the brightest star just below and to the left of the Horsehead. To the left of Alnitak is the Flame Nebula, with clouds of bright emission and dramatic dark dust lanes. The magnificent emission region, the Orion Nebula (aka M42), lies at the upper right. Immediately to its left is a prominent reflection nebula sometimes called the Running Man. Pervasive tendrils of glowing hydrogen gas are easily traced throughout the region.   Astrophysicists: Browse 3,500+ codes in the Astrophysics Source Code Library",
   "hdurl":"https://apod.nasa.gov/apod/image/2409/OrionOrange_Grelin_9371.jpg",
   "media_type":"image",
   "title":"Horsehead and Orion Nebulas",
   "url":"https://apod.nasa.gov/apod/image/2409/OrionOrange_Grelin_1080.jpg" 
}
'''

# Load the JSON data into a Python dictionary
data = json.loads(json_data)

# Print the keys 'explanation' and 'title'
print("Explanation:", data['explanation'])
print("Title:", data['title'])
