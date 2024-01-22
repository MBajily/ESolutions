from datetime import datetime
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from django.http import HttpResponse
import json
from .client_views import cv_download



# ------------------------------------------------------------------------Begin------------------------------------------------------------------------
# -----------------------------Name-----------------------------
def export_pdf(request):
    data = json.loads(cv_download(request))
    # Converting dictionary items to a list of tuples
    data_items = list(data.items())

    # Create a response object with the appropriate content type
    response = HttpResponse(content_type='application/pdf')

    # Set the Content-Disposition header to force a download
    response['Content-Disposition'] = 'attachment; filename="%s_resume.pdf"' %(data_items[0][1]['first_name'] + "_" + data_items[0][1]['last_name'])

    # Create a PDF canvas
    pdf = canvas.Canvas(response, pagesize=A4)

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
                        max_width, (0.25, 0.25, 0.25)
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
    

    full_name = " ".join(
        name
        for name in [data_items[0][1]['first_name'], data_items[0][1]['last_name']]
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
    pdf.showPage()
    pdf.save()
    return response