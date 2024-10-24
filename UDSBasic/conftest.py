import pytest
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication


@pytest.hookimpl(tryfirst=True)
def pytest_configure(config):
    """Setup for the pytest session."""
    config.option.htmltitle = "Diag Automation"


@pytest.hookimpl(optionalhook=True)
def pytest_html_results_summary(prefix, summary, postfix):
    """Add custom information to the HTML summary."""
    summary.append('<h2 style="text-align: center; color: blue;">Project Name - Diagnostics Test Automation</h2>')
    summary.append('<h2 style="text-align: center; color: blue;">Client Name - 42Dot</h2>')
    summary.append('<h2 style="text-align: center; color: blue;">Protocols used - UDS and DoIP</h2>')

    # summary.append(
    #     '<div style="text-align: center; color: blue; font-weight: bold;">Project Name: <strong>Canoe Diag</strong></div>')
    # summary.append(
    #     '<div style="text-align: center; color: green; font-weight: bold;">Tester: <strong>Anand</strong></div>')
    # summary.append(
    #     '<div style="text-align: center; color: orange; font-weight: bold;">Environment: <strong>Test</strong></div>')


# @pytest.hookimpl(optionalhook=True)
# def pytest_html_results_table_row(report, cells):
#     """Customize the results table row in the HTML report."""
#     if report.failed:
#         cells[0] = f"<b style='color:red;'>{cells[0]}</b>"  # Highlight failed tests
#     elif report.passed:
#         cells[0] = f"<b style='color:green;'>{cells[0]}</b>"  # Highlight passed tests
#
#     # Append a custom value if needed
#     custom_value = "Custom Value"  # Replace with your actual value
#     cells.append(custom_value)  # Add a new column with custom data


def send_email(report_file):
    """Send the HTML report via email."""
    sender_email = "Test.Digital@bluebinaries.com"
    receiver_email = "gopinath.sambath@bluebinaries.com"
    subject = "Diag Automation Test Report"
    body = "Hi All," \
           "Please find the attachment"

    try:
        with smtplib.SMTP('smtp.example.com', 587) as server:
            server.starttls()
            server.login(sender_email, "Tor49261")

            # Create the email message
            msg = MIMEMultipart()
            msg['From'] = sender_email
            msg['To'] = receiver_email
            msg['Subject'] = subject
            msg.attach(MIMEText(body, 'plain'))

            # Attach the report
            with open(report_file, 'rb') as f:
                attach = MIMEApplication(f.read(), _subtype='html')
                attach.add_header('Content-Disposition', 'attachment', filename=report_file)
                msg.attach(attach)

            # Send the email
            server.send_message(msg)
            print(f"Email sent successfully to {receiver_email}.")
    except Exception as e:
        print(f"Failed to send email: {e}")


@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    """Send the email with the report after the test session finishes."""
    report_file = "report.html"  # Specify the report file name
    send_email(report_file)
