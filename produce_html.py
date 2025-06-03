# ============================================================================ #
# produce_out.py
# CV Python main script.
# ============================================================================ #

from jinja2 import Environment, FileSystemLoader
import data_loader
from helper_functions import HelperFunctions


# ============================================================================ #
# VERSION
version = 'v1'


# load data
data = data_loader.LoadData()

# load html template
file_template = f'template_{version}.j2'
env = Environment(loader=FileSystemLoader('templates'))
template = env.get_template(file_template)

# produce html output
html_content = template.render(data=data, funcs=HelperFunctions)

# save html to file
file_out = f"out/{version}.html"
with open(file_out, "w") as f:
    f.write(html_content)

print(f"HTML product created: '{file_out}'.")