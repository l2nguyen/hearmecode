# Challenge Level: Beginner

# NOTE: Please don't use anyone's *real* contact information during these exercises, especially if you're putting it up on Github!

# Background: You have a dictionary with people's contact information.  You want to display that information as an HTML table.

contacts = {
    'Shannon': {'phone': '202-555-1234', 'twitter': '@svt827', 'github': '@shannonturner'},
    'Beyonce': {'phone': '303-404-9876', 'twitter': '@beyonce', 'github': '@bey'},
    'Tegan and Sara': {'phone': '301-777-3313', 'twitter': '@teganandsara', 'github': '@heartthrob'}
}

# Goal 1: Loop through that dictionary to print out everyone's contact information.

# Sample output:

# Shannon's contact information is:
#   Phone: 202-555-1234
#   Twitter: @svt827
#   Github: @shannonturner 

# Beyonce's contact information is:
#   Phone: 303-404-9876
#   Twitter: @beyonce
#   Github: @bey

for person, info in sorted(contacts.items()):
    print "{0}\'s contact info:".format(person)  # Prints person's name
    for site, handle in info.items():
        print "\t{0}: {1}".format(site,handle)  # Prints person's contact info

# Goal 2:  Display that information as an HTML table.

# Sample output:

# <table border="1">
# <tr>
# <td colspan="2"> Shannon </td>
# </tr>
# <tr>
# <td> Phone: 202-555-1234 </td>
# <td> Twitter: @svt827 </td>
# <td> Github: @shannonturner </td>
# </tr>
# </table>

# ...

# Goal 3: Write all of the HTML out to a file called contacts.html and open it in your browser.

with open('contacts.html','w') as html_file:
    for person, info in sorted(contacts.items()):
        html_file.write("<table border=\"1\">\n")
        html_file.write("<tr>\n")
        html_file.write("<td colspan=\"2\"> {0} </td>\n".format(person))
        html_file.write("</tr>\n")
        html_file.write("<tr>\n")
        for site, handle in info.items():
            html_file.write("<td> {0}: {1} </td>\n".format(site,handle))
        html_file.write("</tr>\n")
        html_file.write("</table>\n")

# Goal 4: Instead of reading in the contacts from the dictionary above, read them in from contacts.csv, which you can find in lesson_07_(files).
import csv

# open csv file
csvfile = csv.DictReader(open('contacts.csv'))

contacts2 = {}  # create empty dictionary

# Generates a nested dictionary with all the info for each state
for row in csvfile:
    key = row.pop('Name')
    if key in contacts2:
        pass
    contacts2[key] = row

print contacts2

with open('contacts.html','w') as html_file:
    for person, info in sorted(contacts2.items()):
        html_file.write("<table border=\"1\">\n")
        html_file.write("<tr>\n")
        html_file.write("<td colspan=\"2\"> {0} </td>\n".format(person))
        html_file.write("</tr>\n")
        html_file.write("<tr>\n")
        for site, handle in info.items():
            html_file.write("<td> {0}: {1} </td>\n".format(site,handle))
        html_file.write("</tr>\n")
        html_file.write("</table>\n")
