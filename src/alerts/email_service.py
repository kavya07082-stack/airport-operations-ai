"""
email_service.py
----------------
Email notification service.
"""

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from typing import List

from src.utils.config import config
from src.utils.logger import get_logger

logger = get_logger(__name__)


class EmailService:
    """SMTP email service for notifications."""
    
    def __init__(self,
                 smtp_server: str = None,
                 smtp_port: int = None,
                 sender_email: str = None,
                 sender_password: str = None):
        """Initialize email service."""
        self.smtp_server = smtp_server or config.SMTP_SERVER
        self.smtp_port = smtp_port or config.SMTP_PORT
        self.sender_email = sender_email or config.SMTP_USER
        self.sender_password = sender_password or config.SMTP_PASSWORD
    
    def send_email(self,
                   subject: str,
                   body: str,
                   recipients: List[str],
                   html: bool = False) -> bool:
        """Send email.
        
        Args:
            subject: Email subject
            body: Email body
            recipients: List of recipient emails
            html: Whether body is HTML
            
        Returns:
            True if sent successfully
        """
        try:
            msg = MIMEMultipart('alternative')
            msg['Subject'] = subject
            msg['From'] = self.sender_email
            msg['To'] = ', '.join(recipients)
            
            mime_type = 'html' if html else 'plain'
            msg.attach(MIMEText(body, mime_type))
            
            with smtplib.SMTP(self.smtp_server, self.smtp_port) as server:
                server.starttls()
                server.login(self.sender_email, self.sender_password)
                server.sendmail(self.sender_email, recipients, msg.as_string())
            
            logger.info(f"Email sent to {recipients}")
            return True
        
        except Exception as e:
            logger.error(f"Failed to send email: {e}")
            return False
    
    def send_alert_email(self,
                        alert_type: str,
                        severity: str,
                        message: str,
                        recipients: List[str]) -> bool:
        """Send formatted alert email."""
        subject = f"[{severity.upper()}] Airport Operations Alert - {alert_type}"
        
        html_body = f"""
        <html>
            <body>
                <h2>⚠️ Airport Operations Alert</h2>
                <p><strong>Alert Type:</strong> {alert_type}</p>
                <p><strong>Severity:</strong> <span style="color: red;">{severity.upper()}</span></p>
                <p><strong>Message:</strong> {message}</p>
                <hr>
                <p><small>This is an automated alert from the Airport Operations AI System.</small></p>
            </body>
        </html>
        """
        
        return self.send_email(subject, html_body, recipients, html=True)
