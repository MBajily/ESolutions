# import psycopg2

# # Connect to PostgreSQL
# conn = psycopg2.connect(
#     dbname="readme_to_recover",
#     user="postgres",
#     password="password",
#     host="esol-db-instance.c1o8oa2wc1pv.us-east-1.rds.amazonaws.com",
#     port="5432",
# )

# # Create a cursor
# cursor = conn.cursor()

# client_id = 1
# # client_id = input("Enter client ID: ")

# # Fetch resume data using SQL queries
# cursor.execute("SELECT * FROM client_cv WHERE cv_id = %s", (client_id,))
# resume_data = cursor.fetchall()

# # Close the cursor and connection
# cursor.close()
# conn.close()

# Genders = (("Male", "Male"), ("Female", "Female"))

# Degrees = (
#     ("Intermediate School", "Intermediate School"),
#     ("High School", "High School"),
#     ("Deploma", "Deploma"),
#     ("Bachelor's Degree", "Bachelor's Degree"),
#     ("Master's Degree", "Master's Degree"),
#     ("PhD's Degree", "PhD's Degree"),
# )

# nationality = (
#     ("Saudi", "Saudi"),
#     ("Iraqi", "Iraqi"),
#     ("Kuwaiti", "Kuwaiti"),
#     ("Yemeni", "Yemeni"),
#     ("Omani", "Omani"),
# )

# specializations = (
#     ("CS", "CS"),
#     ("IT", "IT"),
#     ("IS", "IS"),
#     ("Software Engineering", "Software Engineering"),
#     ("Database Management Systems", "Database Management Systems"),
# )

# cities = (
#     ("Riyadh", "Riyadh"),
#     ("Jeddah", "Jeddah"),
#     ("Dammam", "Dammam"),
#     ("Mecca", "Mecca"),
#     ("Abha", "Abha"),
# )

# # print(resume_data)

# # -----------------------------Information-----------------------------
# job_title = "Shit saleer"
# personal_id = resume_data[0][1]
# # client_id = resume_data[0][2]
# first_name = resume_data[0][3]
# second_name = resume_data[0][4]
# third_name = resume_data[0][5]
# last_name = resume_data[0][6]
# email = resume_data[0][7]
# phone_primary = resume_data[0][8]
# phone_secondary = resume_data[0][9]
# birth_date = resume_data[0][10]
# # bio = resume_data[0][11]
# bio = "Highly motivated and results-oriented data professional with a strong foundation in Python, SQL, and Power BI. Experienced in transforming complex data sets into actionable insights to drive business decisions. Seeking a challenging opportunity where I can apply my analytical skills and insights to contribute to a dynamic team."
# gender = resume_data[0][12]
# degree = resume_data[0][13]
# nationality_id = resume_data[0][14]
# specialization_id = resume_data[0][15]
# city_id = resume_data[0][16]
# # create_date = resume_data[0][]
# # is_active = resume_data[0][]

# nationality = nationality[nationality_id][0]
# specialization = specializations[specialization_id][0]
# city = cities[city_id][0]

# # -----------------------------Experience-----------------------------
# company_name = "UNIVERSITY OF GEZIRA"
# title = job_title
# # location = (city + ", Saudi Arabia")
# location = city
# start_date = str(birth_date.strftime("%b %Y"))
# end_date = str(birth_date.strftime("%b %Y"))
# description = "No much to see here."
# experience = [
#     [
#         company_name.upper(),
#         title.upper(),
#         location.upper(),
#         start_date.upper(),
#         "present".upper(),
#         description,
#     ],
#     [
#         company_name.upper(),
#         title.upper(),
#         location.upper(),
#         start_date.upper(),
#         end_date.upper(),
#         bio,
#     ],
# ]
# # experience_id = models.AutoField(primary_key=True)
# # client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
# # company_name = models.CharField(max_length=200, null=True)
# # job_title = models.CharField(max_length=200, null=True)
# # description = models.CharField(max_length=2000, null=True)
# # start_date = models.DateField(null=True)
# # end_date = models.DateField(null=True)
# # -----------------------------Education-----------------------------
# educational_institution = "UNIVERSITY OF GEZIRA"
# title = degree
# # location = (city + ", Saudi Arabia")
# location = city
# end_date = str(birth_date.strftime("%b %Y"))
# education = [
#     [
#         educational_institution.upper(),
#         title.upper(),
#         location.upper(),
#         end_date.upper(),
#     ],
#     [educational_institution, title, location, end_date],
# ]
# # education_id = models.AutoField(primary_key=True)
# # client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
# # educational_institution = models.CharField(max_length=200, null=True)
# # title = models.CharField(max_length=200, null=True)
# # start_date = models.DateField(null=True)
# # description = models.CharField(max_length=2000, null=True)
# # end_date = models.DateField(null=True)
# # -----------------------------Courses-----------------------------
# course_educational_institution = "UNIVERSITY OF GEZIRA"
# course_title = degree
# total_hours = str(10) + " Hours"
# course_date = str(birth_date.strftime("%b %Y"))
# description = "No much to see here."
# courses = [
#     [
#         course_educational_institution.upper(),
#         course_title.upper(),
#         total_hours,
#         course_date.upper(),
#         description,
#     ],
#     [
#         course_educational_institution.upper(),
#         course_title.upper(),
#         total_hours,
#         course_date.upper(),
#         description,
#     ],
# ]

# # course_id = models.AutoField(primary_key=True)
# # client = models.ForeignKey(User, null=True, on_delete=models.SET_NULL)
# # educational_institution = models.CharField(max_length=200, null=True)
# # title = models.CharField(max_length=200, null=True)
# # date = models.DateField(null=True)
# # description = models.CharField(max_length=2000, null=True)
# # total_hours = models.IntegerField(null=True)








from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4

# Create a PDF document
pdf = canvas.Canvas(
    # "output_resume.pdf", pagesize=(595.27,841.89) # A4 size in points
    "output_resume.pdf", pagesize = A4
)

# Set font and size
font_name = "Helvetica"
font_name_Bold = "Helvetica-Bold"
font_size_10 = 10
font_size_11 = 11
font_size_12 = 12
font_size_14 = 14
font_size_18 = 18
font_size_22 = 22
# Set the black as the default color for the text
font_color = (0,0,0)
# Set the maximum width for the text
max_width = 535 
# Specify the starting position for the right-aligned text
start_x = 30
start_y = 790
# Calculate x-coordinate to center the text
page_width = 8.27 * 72  # A4 width in points (1 inch = 72 points)


line = "_____________________________________________________________________"


# ------------------------------------------------------------------------Import data from a JSON file------------------------------------------------------------------------
import json

with open('sample.json', 'r') as file:
    data = json.load(file)

# Converting dictionary items to a list of tuples
data_items = list(data.items())

# ------------------------------------------------------------------------Methods------------------------------------------------------------------------
# To Add new section
def new_section(section_name, section_dic, y):
    # Section Name
    if 110 > y - font_size_14:
        # Move to a new page
        pdf.showPage()
        y = start_y
    new_y = draw_text_on_pdf(
        pdf, section_name.upper(), start_x, y - 20, font_name_Bold, font_size_14
    )
    # Line
    new_y = draw_text_on_pdf(
        pdf, line, start_x, new_y + 30, font_name, font_size_14
    )
    # Checking whether it is a skills section or not
    if 'skills' != section_name.lower():
        try:
            for element in section_dic:
                # Converting the keys of a dictionary into a list to search by keys
                keys_list = list(element.keys())
                # Title
                if 85 > new_y - font_size_11:
                    # Move to a new page
                    pdf.showPage()
                    new_y = start_y
                draw_text_on_pdf(
                    pdf, element[keys_list[0]].title(), start_x, new_y, font_name_Bold, font_size_11
                )
                # Dates
                date_format = "%b %Y"
                present_date = element[keys_list[4]]
                if 'PRESENT' != present_date.upper():
                    date_text = datetime.strptime(element[keys_list[3]], "%Y-%m-%d").strftime(date_format)
                    date_text += f" - {datetime.strptime(present_date, '%Y-%m-%d').strftime(date_format)}" if len(present_date) > 6 else ""
                else:
                    date_text = datetime.strptime(element[keys_list[3]], "%Y-%m-%d").strftime(date_format) + f" - {present_date}"

                new_y = draw_right_text_on_pdf(pdf, date_text, start_x, new_y, font_name, font_size_11)
                # Institution
                new_y = draw_text_on_pdf(
                    pdf, element[keys_list[1]].title(), start_x, new_y, font_name_Bold, font_size_11,
                    max_width, (0.4, 0.4, 0.4)
                )
                # Description
                new_y = draw_text_on_pdf(
                    pdf, element[keys_list[2]], start_x, new_y, font_name, font_size_11
                )
                new_y -= 10
            new_y += 10
        except Exception:
            pass
    else:
        draw_skills_on_pdf(section_dic, new_y)
    
    return new_y


def draw_skills_on_pdf(skills_list, y):
    column1_y = column2_y = y
    for i in range(len(skills_list)):
        if i % 2 == 0:
            draw_text_on_pdf(
                pdf, '•', start_x, column1_y - 2, font_name_Bold, font_size_11, 250
            )
            column1_y = draw_text_on_pdf(
                pdf, skills_list[i].title(), start_x + 10, column1_y - 2, font_name, font_size_11, 250
            )
        else:
            draw_text_on_pdf(
                pdf, '•', start_x + 275, column2_y - 2, font_name_Bold, font_size_11, 250
            )
            column2_y = draw_text_on_pdf(
                pdf, skills_list[i].title(), start_x + 285, column2_y - 2, font_name, font_size_11
            )


def draw_text_on_pdf(pdf, text, x, y, font_name, font_size, max_width = max_width, font_color = font_color):
    # Check if there is enough space on the current page
    if 60 > y - font_size:
        # Move to a new page
        pdf.showPage()
        y = start_y

    pdf.setFont(font_name, font_size)
    pdf.setFillColorRGB(font_color[0],font_color[1],font_color[2])

    lines = []
    current_line = ""

    for word in text.split():
        width = pdf.stringWidth(current_line + " " + word, font_name, font_size)

        if width <= max_width:
            current_line += word + " "
        else:
            lines.append(current_line.strip())
            current_line = word + " "

    lines.append(current_line.strip())

    for line in lines:
        pdf.drawString(x, y, line)
        if 11 == font_size and font_name != font_name_Bold:
            y -= font_size + 3  # Adjust the vertical position for the next line
        else:
            y -= font_size # Adjust the vertical position for the next line


    return y - (font_size / 4)


def draw_right_text_on_pdf(pdf, text, x, y, font_name, font_size):
    if 60 > y - font_size:
        y = start_y

    pdf.setFont(font_name, font_size)
    
    width = pdf.stringWidth(text, font_name, font_size)

    if width <= max_width:
        pdf.drawString(x + max_width - width, y, text)

    y -= font_size

    return y - (font_size / 4)
# -------------------------------------------------------------------------------------------------------------------------------------------------------





# ------------------------------------------------------------------------Begin------------------------------------------------------------------------
# -----------------------------Name-----------------------------
full_name = " ".join(
    name
    for name in [data_items[0][1]['first_name'], data_items[0][1]['second_name'], data_items[0][1]['third_name'], data_items[0][1]['last_name']]
    if name != ''
)
# Centr the name
# Calculate text width
text_width = pdf.stringWidth(full_name.title(), font_name_Bold, font_size_22)
x = (page_width - text_width) / 2
new_y = draw_text_on_pdf(
    pdf, full_name, x, start_y, font_name_Bold, font_size_22
)

# -----------------------------Job Title-----------------------------
text_width = pdf.stringWidth(data_items[0][1]['specialization'], font_name_Bold, font_size_18)
x = (page_width - text_width) / 2

new_y = draw_text_on_pdf(
    pdf, data_items[0][1]['specialization'].title(), x, new_y, font_name_Bold, font_size_18
)

# -----------------------------Contact Info-----------------------------
text = ' | '.join(elm for elm in data_items[1][1].values() if elm != '')
reversed_text = ' | '.join(reversed(text.split(' | ')))
# Centr the Contact Info
text_width = pdf.stringWidth(reversed_text, font_name, font_size_12)
x = (page_width - text_width) / 2
new_y = draw_text_on_pdf(pdf, reversed_text, x, new_y, font_name, font_size_12)

# -----------------------------Summary-----------------------------  
# Section Title          
new_y = draw_text_on_pdf(
    pdf, "SUMMARY", start_x, new_y - 20, font_name_Bold, font_size_14
)
#Line
new_y = draw_text_on_pdf(
    pdf, line, start_x, new_y + 30, font_name, font_size_14
)
# content
new_y = draw_text_on_pdf(pdf, data_items[0][1]['summary'], start_x, new_y, font_name, font_size_11)

# -----------------------------Sections-----------------------------
for i in range(2, len(data_items)):
    new_y = new_section(data_items[i][0], data_items[i][1], new_y)


# ------------------------------------------------------------------------End------------------------------------------------------------------------

# Save the PDF
pdf.save()   



# -----------------------------Experience-----------------------------
# new_y = draw_text_on_pdf(
#     pdf, "EXPERIENCE", start_x, new_y - 20, max_width, font_name_Bold, font_size_14
# )
# new_y = draw_text_on_pdf(
#     pdf, line, start_x, new_y + 30, max_width, font_name, font_size_14
# )
# for exp in experience:
#     draw_text_on_pdf(
#         pdf, exp[1], start_x, new_y, max_width, font_name_Bold, font_size_11
#     )
#     new_y = draw_right_text_on_pdf(
#         pdf,
#         exp[3] + " - " + exp[4] + ", " + exp[2],
#         start_x,
#         new_y,
#         max_width,
#         font_name,
#         font_size_11,
#     )
#     new_y = draw_text_on_pdf(
#         pdf, exp[0], start_x, new_y, max_width, font_name, font_size_11
#     )
#     new_y = draw_text_on_pdf(
#         pdf, exp[5], start_x, new_y, max_width, font_name, font_size_11
#     )
#     new_y -= 10
# new_y += 10

# -----------------------------Education-----------------------------
# new_y = draw_text_on_pdf(
#     pdf, "EDUCATION", start_x, new_y - 20, max_width, font_name_Bold, font_size_14
# )
# new_y = draw_text_on_pdf(
#     pdf, line, start_x, new_y + 30, max_width, font_name, font_size_14
# )
# for edu in education:
#     draw_text_on_pdf(
#         pdf, edu[0], start_x, new_y, max_width, font_name_Bold, font_size_11
#     )
#     new_y = draw_right_text_on_pdf(
#         pdf,
#         edu[3] + ", " + edu[2],
#         start_x,
#         new_y,
#         max_width,
#         font_name,
#         font_size_11,
#     )
#     new_y = draw_text_on_pdf(
#         pdf, edu[1], start_x, new_y, max_width, font_name, font_size_11
#     )
#     # new_y = draw_right_text_on_pdf(
#     #     pdf,
#     #     edu[3],
#     #     start_x,
#     #     new_y,
#     #     max_width,
#     #     font_name,
#     #     font_size_11,
#     # )
#     new_y -= 10
# new_y += 10
# # -----------------------------Courses-----------------------------
# new_y = draw_text_on_pdf(
#     pdf, "COURSES", start_x, new_y - 20, max_width, font_name_Bold, font_size_14
# )
# new_y = draw_text_on_pdf(
#     pdf, line, start_x, new_y + 30, max_width, font_name, font_size_14
# )
# for crs in courses:
#     new_y = draw_text_on_pdf(
#         pdf,
#         crs[1] + " (" + crs[2] + ")",
#         start_x,
#         new_y,
#         max_width,
#         font_name_Bold,
#         font_size_11,
#     )
#     new_y = draw_text_on_pdf(
#         pdf, crs[0] + " - " + crs[3], start_x, new_y, max_width, font_name, font_size_11
#     )
#     new_y = draw_text_on_pdf(
#         pdf, crs[4], start_x, new_y, max_width, font_name, font_size_11
#     )
#     new_y -= 10
# new_y += 10
# # -----------------------------Skills-----------------------------
# new_y = draw_text_on_pdf(
#     pdf, "SKILLS", start_x, new_y - 20, max_width, font_name_Bold, font_size_14
# )
# new_y = draw_text_on_pdf(
#     pdf, line, start_x, new_y + 30, max_width, font_name, font_size_14
# )

# # Add more information as needed