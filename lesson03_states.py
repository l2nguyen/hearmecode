# Challenge Level: Beginner

# Background: You have a text file with all of the US state names:
#       states.txt: See section_07_(files).
#
#       You also have a spreadsheet in comma separated value (CSV) format, state_info.csv.  See also section_07_(files)
#       state_info.csv has the following columns: Population Rank, State Name, Population, US House Members, Percent of US Population

# Challenge 1: Open states.txt and use the information to generate an HTML drop-down menu as in: https://github.com/shannonturner/python-lessons/blob/master/playtime/lesson02_states.py

# Challenge 2: Save the HTML as states.html instead of printing it to screen.
# Your states.html should look identical (or at least similar) to the one you created in the Lesson 2 playtime, except you're getting the states from a file instead of a list.

# Reads text file with states names
with open('states.txt', 'r') as states_file:
    states = states_file.read().split("\n")

# Generates html code for drop down menu and saves it into an html file
with open('states.html','w') as html_file:
    html_file.write("<select>\n")
    for index, state in enumerate(states):
        states[index] = state.split("\t")
        html_file.write("\t<option value=\"{0}\">{1}</option>\n".format(states[index][0],states[index][1]))
    html_file.write("<\select>")

# Challenge 3: Using state_info.csv, create an HTML page that has a table for *each* state with all of the state details.

import csv

# open csv file
csvfile = csv.DictReader(open('state_info.csv'))

result = {}  # create empty dictionary

# Generates a nested dictionary with all the info for each state
for row in csvfile:
    key = row.pop('State')
    if key in result:
        pass
    result[key] = row

print result

# Sample output:

with open('states_info.html','w') as state_html:
    state_html.write("<table border=\"1\">\n")  # starts table
    state_html.write("<tr>\n")
    for state, info in sorted(result.items()):
        state_html.write("<td colspan=\"2\">{0}</td>\n".format(state))
        state_html.write("</tr>\n<tr>\n")
        for key, stats in info.items():
            state_html.write("<td> {0}: {1} </td>\n".format(key,stats))
            state_html.write("</tr>")
    state_html.write("</table>")


# <table border="1">
# <tr>
# <td colspan="2"> California </td>
# </tr>
# <tr>
# <td> Rank: 1 </td>
# <td> Percent: 11.91% </td>
# </tr>
# <tr>
# <td> US House Members: 53 </td>
# <td> Population: 38,332,521 </td>
# </tr>
# </table>

# Challenge 4 (Not a Python challenge, but an HTML/Javascript challenge): When you make a choice from the drop-down menu, jump to that state's table.