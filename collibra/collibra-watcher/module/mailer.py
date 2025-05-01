# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText

def createIssueTable(clbraDomain, issues):
    html = "<html><body><table border='1'>"
    html += "<tr>"
    html += "<th>Data Element</th>"
    html += "<th>Issue</th>"
    html += "</tr>"

    url = "https://" + clbraDomain + "/"
    for issue in issues:
        html += "<tr>"
        html += f"<td><a href=\"{url}asset/{issue[0][0]}\">{issue[0][1]}</a></td>"
        html += f"<td>{issue[1]}</td>"
        html += "</tr>"

    # for key in data_dict.keys():
    #     html += f"<th>{key}</th>"
    # html += "</tr><tr>"
    # for value in data_dict.values():
    #     html += f"<td>{value}</td>"
    html += "</table></body></html>"
    return html

def sendMail(clbraDomain, dataStewardMailIds, issues):
    print("Send mail to: " + str(dataStewardMailIds))

    mailBody = createIssueTable(clbraDomain, issues)
    print("Mail body: " + mailBody)

# def create_html_table(data_dict):
#     html = "<html><body><table border='1'>"
#     html += "<tr>"
#     for key in data_dict.keys():
#         html += f"<th>{key}</th>"
#     html += "</tr><tr>"
#     for value in data_dict.values():
#         html += f"<td>{value}</td>"
#     html += "</tr></table></body></html>"
#     return html

# def send_email(subject, html_content, recipient_email, sender_email, sender_password):
#     msg = MIMEMultipart('alternative')
#     msg['Subject'] = subject
#     msg['From'] = sender_email
#     msg['To'] = recipient_email

#     part = MIMEText(html_content, 'html')
#     msg.attach(part)

#     try:
#         server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
#         server.login(sender_email, sender_password)
#         server.sendmail(sender_email, recipient_email, msg.as_string())
#         server.quit()
#         print("Email sent successfully!")
#     except Exception as e:
#         print(f"Failed to send email. Error: {e}")

# Example usage
# data = {
#     "Name": "John Doe",
#     "Age": 30,
#     "Department": "Finance"
# }

# html_table = create_html_table(data)
# send_email(
#     subject="Employee Information",
#     html_content=html_table,
#     recipient_email="recipient@example.com",
#     sender_email="your_email@example.com",
#     sender_password="your_password"
# )
