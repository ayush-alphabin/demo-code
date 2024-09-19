import json
import os
import sys
import requests
import pytest
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from apiservice.Logger import Logger
import Wealth_App.configs.global_configs
import logging
from dotenv import load_dotenv, find_dotenv

sys.path.append(os.getcwd())
load_dotenv(find_dotenv())

def pytest_addoption(parser):
    parser.addoption("--host", action="store", dest="host", default="uat")
    parser.addoption("--log_level", action="store", dest="log_level", default="info")
    
def pytest_configure(config):
    selected_host = config.getoption("host")
    log_level = config.getoption("log_level")
    Wealth_App.configs.global_configs.selected_environment = selected_host.lower()

    # Generate timestamped HTML report
    marker = config.getoption("-m") or 'all'
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    report_dir = "report"
    if not os.path.exists(report_dir):
        os.makedirs(report_dir)
    report_file = f"{timestamp}_Result_{marker}.html"
    
    if not config.option.htmlpath:
        config.option.htmlpath = os.path.join(report_dir, report_file)

@pytest.fixture(scope="session", autouse=True)
def before_after():
    print("\n\n------------Before-----------\n")
    yield
    print("\n\n------------After------------\n")

@pytest.fixture(scope="function")
def logger(request):
    logger = logging.getLogger(request.node.name)
    handler = logging.StreamHandler()

    if request.config.getoption("--reportportal"):
        try:
            from pytest_reportportal import RPLogger, RPLogHandler
            rp_handler = RPLogHandler(request.node.config._reporter)
            rp_handler.setLevel(logging.INFO)
            logger.addHandler(rp_handler)
        except ImportError:
            logger.warning("pytest-reportportal not installed, using StreamHandler for logging.")
    else:
        logger.addHandler(handler)

    logger.setLevel(logging.INFO)
    return logger

# Load variables from .env file
SENDER_EMAIL = os.getenv("SENDER_EMAIL")
RECEIVER_EMAIL = os.getenv("RECEIVER_EMAIL")
SMTP_SERVER='smtp.gmail.com'
SMTP_PORT=587
SENDER_EMAIL='ayush.alphabin@gmail.com'
SMTP_PASSWORD='zsyn tdzl zdnm mnvc'
SMTP_PASSWORD = os.getenv("SMTP_PASSWORD")
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")

def send_email(subject, body):
    # Create the email message
    msg = MIMEMultipart()
    msg["From"] = SENDER_EMAIL
    msg["To"] = RECEIVER_EMAIL
    msg["Subject"] = subject

    # Add the body of the email
    msg.attach(MIMEText(body, "plain"))

    try:
        # Connect to the SMTP server and send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SMTP_PASSWORD)
        text = msg.as_string()
        server.sendmail(SENDER_EMAIL, RECEIVER_EMAIL, text)
        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")
    finally:
        server.quit()

def pytest_terminal_summary(terminalreporter, exitstatus):
    passed = len(terminalreporter.stats.get('passed', []))
    failed = len(terminalreporter.stats.get('failed', []))
    skipped = len(terminalreporter.stats.get('skipped', []))
    errors = len(terminalreporter.stats.get('error', [])) if 'error' in terminalreporter.stats else 0

    # Check which marker (e.g., smoke, regression) was used
    marker = terminalreporter.config.getoption("-m")
    test_type = marker if marker else None  # Set test_type to None if no marker is present

    # Set the color and emoji based on the test result
    color = "#36a64f" if failed == 0 else "#ff0000"  # '#36a64f' = green, '#ff0000' = red for Slack

    # Pytest logo URL
    pytest_logo_url = "https://upload.wikimedia.org/wikipedia/commons/thumb/b/ba/Pytest_logo.svg/640px-Pytest_logo.svg.png"

    # Construct the Slack message payload
    blocks = [
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"*Test Results*"
            }
        },
        {
            "type": "divider"
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": f"Test completed at {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}"
            }
        }
    ]

    # Only add the marker section if a valid marker is provided
    if test_type:
        blocks.insert(1, {
            "type": "context",
            "elements": [
                {
                    "type": "plain_text",
                    "text": f"Marker={test_type}",
                    "emoji": True
                }
            ]
        })

    # Construct the Slack message with attachments
    message = {
        "username": "PytestBot",  # Custom username like "PytestBot"
        "icon_url": pytest_logo_url,  # Pytest logo as the profile icon
        "blocks": blocks,
        "attachments": [
            {
                "color": color,
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"*Summary:* Tests passed={passed}, failed={failed}, skipped={skipped}, errors={errors}"
                        }
                    }
                ]
            }
        ]
    }

    headers = {"Content-Type": "application/json"}

    # Send the Slack message
    response = requests.post(SLACK_WEBHOOK_URL, data=json.dumps(message), headers=headers)

    if response.status_code != 200:
        raise ValueError(f"Request to Slack returned an error {response.status_code}, the response is:\n{response.text}")

    # Construct email body
    emoji = "✅" if failed == 0 else "❌"
    tag_info = f"Marker = {test_type}\n\n" if test_type else ""
    failed_info = f"        ❌ Failed: {failed}\n" if failed > 0 else ""
    skipped_info = f"        ⚠️ Skipped: {skipped}\n" if skipped > 0 else ""
    errors_info = f"        🚨 Errors: {errors}\n" if errors > 0 else ""
    passed_info = f"        ✅ Passed: {passed}\n" if passed > 0 else ""

    email_body = f"""
        {emoji}  Test Results Summary
        {'-' * 40}
        {tag_info}{passed_info}{failed_info}{skipped_info}{errors_info}
        {'-' * 40}

        Test completed at: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}
    """

    # Send email with test results
    send_email("Test Run Results", email_body)