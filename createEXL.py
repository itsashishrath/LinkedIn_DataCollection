from openpyxl import Workbook
from openpyxl.styles import Font

# Create a new workbook and select the active worksheet
wb = Workbook()
ws = wb.active
ws.title = "Contacts"

# Define the headers for the columns
headers = [
    "Name",
    "LinkedIn Profile URL",
    "College Name",
    "Major/Department",
    "Year of Study",
    "Connection Request Sent (Date)",
    "Request Accepted (Date)",
    "Conversation Started (Date)",
    "Conversation Status",
    "Conversation History"
]

# Apply headers to the worksheet with bold font
for col_num, header in enumerate(headers, 1):
    cell = ws.cell(row=1, column=col_num)
    cell.value = header
    cell.font = Font(bold=True)

# Save the workbook
wb.save("CollegeContacts.xlsx")

print("Excel file 'CollegeContacts.xlsx' has been created with the necessary structure.")
