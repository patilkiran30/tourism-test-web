import re

def update_file(filepath):
    with open(filepath, 'r') as f:
        content = f.read()

    # Define the mapping from alt text/titles to their respective URLs
    replacements = [
        (r'<div class="destination-card animate-on-scroll">\s*<img src="([^"]+)" alt="Paris">\s*<div class="destination-info">\s*<h3>Paris, France</h3>\s*</div>\s*</div>',
         r'<a href="paris.html" class="destination-card animate-on-scroll">\n                <img src="\1" alt="Paris">\n                <div class="destination-info">\n                    <h3>Paris, France</h3>\n                </div>\n            </a>'),
        
        (r'<div class="destination-card animate-on-scroll">\s*<img src="([^"]+)" alt="Venice">\s*<div class="destination-info">\s*<h3>Venice, Italy</h3>\s*</div>\s*</div>',
         r'<a href="venice.html" class="destination-card animate-on-scroll">\n                <img src="\1" alt="Venice">\n                <div class="destination-info">\n                    <h3>Venice, Italy</h3>\n                </div>\n            </a>'),
         
        (r'<div class="destination-card animate-on-scroll">\s*<img src="([^"]+)" alt="Kyoto">\s*<div class="destination-info">\s*<h3>Kyoto, Japan</h3>\s*</div>\s*</div>',
         r'<a href="kyoto.html" class="destination-card animate-on-scroll">\n                <img src="\1" alt="Kyoto">\n                <div class="destination-info">\n                    <h3>Kyoto, Japan</h3>\n                </div>\n            </a>'),
         
        (r'<div class="destination-card animate-on-scroll">\s*<img src="([^"]+)" alt="Sydney">\s*<div class="destination-info">\s*<h3>Sydney, Australia</h3>\s*</div>\s*</div>',
         r'<a href="sydney.html" class="destination-card animate-on-scroll">\n                <img src="\1" alt="Sydney">\n                <div class="destination-info">\n                    <h3>Sydney, Australia</h3>\n                </div>\n            </a>'),

        (r'<div class="destination-card animate-on-scroll">\s*<img src="([^"]+)" alt="Amsterdam">\s*<div class="destination-info">\s*<h3>Amsterdam, Netherlands</h3>\s*</div>\s*</div>',
         r'<a href="amsterdam.html" class="destination-card animate-on-scroll">\n                <img src="\1" alt="Amsterdam">\n                <div class="destination-info">\n                    <h3>Amsterdam, Netherlands</h3>\n                </div>\n            </a>'),

        (r'<div class="destination-card animate-on-scroll">\s*<img src="([^"]+)" alt="Rio de Janeiro">\s*<div class="destination-info">\s*<h3>Rio de Janeiro, Brazil</h3>\s*</div>\s*</div>',
         r'<a href="rio.html" class="destination-card animate-on-scroll">\n                <img src="\1" alt="Rio de Janeiro">\n                <div class="destination-info">\n                    <h3>Rio de Janeiro, Brazil</h3>\n                </div>\n            </a>'),
    ]

    for pattern, replacement in replacements:
        content = re.sub(pattern, replacement, content)

    with open(filepath, 'w') as f:
        f.write(content)

update_file('index.html')
update_file('destinations.html')
