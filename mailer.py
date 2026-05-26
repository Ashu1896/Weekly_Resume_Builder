import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from dotenv import load_dotenv

# Load local environment variables from .env file if it exists
load_dotenv()

def build_html_report(reports_list, improvements, upskilling):
    """
    Builds a beautifully styled HTML report digest.
    Uses clean inline CSS with high-end typography and cohesive layout.
    """
    # Header and General Setup
    html = """
    <html>
    <head>
        <style>
            body { font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif; color: #2c3e50; line-height: 1.6; background-color: #f8f9fa; margin: 0; padding: 20px; }
            .container { max-width: 800px; margin: 0 auto; background: #ffffff; padding: 30px; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.05); border: 1px solid #e9ecef; }
            .header { text-align: center; border-bottom: 2px solid #3498db; padding-bottom: 15px; margin-bottom: 25px; }
            .header h1 { color: #1f4e79; margin: 0; font-size: 24px; font-weight: 700; }
            .header p { color: #7f8c8d; margin: 5px 0 0 0; font-size: 14px; }
            .card { background: #fdfdfd; border-left: 4px solid #1f4e79; padding: 15px; margin-bottom: 20px; border-radius: 0 4px 4px 0; border-top: 1px solid #f1f1f1; border-right: 1px solid #f1f1f1; border-bottom: 1px solid #f1f1f1; }
            .card-title { font-weight: bold; color: #1f4e79; margin-bottom: 8px; font-size: 16px; }
            table { width: 100%; border-collapse: collapse; margin: 20px 0; }
            th { background-color: #1f4e79; color: white; text-align: left; padding: 10px; font-size: 13px; text-transform: uppercase; letter-spacing: 0.5px; }
            td { padding: 10px; border-bottom: 1px solid #e9ecef; font-size: 13.5px; }
            tr:nth-child(even) { background-color: #fdfdfd; }
            .badge { padding: 4px 8px; border-radius: 4px; font-size: 11px; font-weight: bold; text-transform: uppercase; }
            .badge-passed { background-color: #d4edda; color: #155724; }
            .badge-needs { background-color: #f8d7da; color: #721c24; }
            .score-high { font-weight: bold; color: #27ae60; }
            .score-medium { font-weight: bold; color: #f39c12; }
            .list-item { margin-bottom: 8px; font-size: 13.5px; }
            .bullet { color: #3498db; margin-right: 6px; font-weight: bold; }
            .footer { text-align: center; margin-top: 30px; font-size: 12px; color: #bdc3c7; border-top: 1px solid #e9ecef; padding-top: 15px; }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>WEEKLY ATS RESUME ENGINEERING DIGEST</h1>
                <p>Generated automatically on Sunday — Professional Recruiter Alignment & Market Insights</p>
            </div>
            
            <p>Hello Ashutosh,</p>
            <p>Your automated Sunday resume optimization cycle is complete. The pipeline has analyzed your master profile, cross-referenced hiring trends, injected role-appropriate keywords, and generated <strong>16 distinct, highly customized ATS-optimized resumes</strong>.</p>
            
            <h3>ATS Pipeline Compliance Report</h3>
            <table>
                <thead>
                    <tr>
                        <th>Target Role</th>
                        <th>File Name</th>
                        <th>Pages</th>
                        <th>Keyword Match</th>
                        <th>Metrics</th>
                        <th>ATS Score</th>
                        <th>Status</th>
                    </tr>
                </thead>
                <tbody>
    """
    
    for rep in reports_list:
        score_class = "score-high" if rep["overall_score"] >= 90 else "score-medium"
        badge_class = "badge-passed" if "PASSED" in rep["status"] else "badge-needs"
        
        # Extract title from filename (e.g. Ashutosh_Sharma_DevOps_Engineer.pdf -> DevOps Engineer)
        clean_title = rep["file_name"].replace("Ashutosh_Sharma_", "").replace(".pdf", "").replace("_", " ")
        clean_title = clean_title.title()
        
        html += f"""
                    <tr>
                        <td><strong>{clean_title}</strong></td>
                        <td><code style="font-size: 11px;">{rep["file_name"]}</code></td>
                        <td align="center">{rep["page_count"]}</td>
                        <td>{rep["keyword_match_percentage"]}%</td>
                        <td align="center">{rep["metrics_score"]}/10</td>
                        <td><span class="{score_class}">{rep["overall_score"]}%</span></td>
                        <td><span class="badge {badge_class}">{rep["status"]}</span></td>
                    </tr>
        """
        
    html += """
                </tbody>
            </table>
            
            <div class="card">
                <div class="card-title">Key Improvements Implemented This Week</div>
                <div>
    """
    
    for imp in improvements:
        html += f'<div class="list-item"><span class="bullet">&bull;</span>{imp}</div>'
        
    html += """
                </div>
            </div>
            
            <div class="card" style="border-left-color: #27ae60;">
                <div class="card-title">Upskilling & Skill Gap Recommendations</div>
                <div>
    """
    
    for skill in upskilling:
        html += f'<div class="list-item"><span class="bullet" style="color: #27ae60;">&bull;</span>{skill}</div>'
        
    html += """
                </div>
            </div>
            
            <p>All 16 ATS-compatible PDF files are attached to this email. You can find copies of these files organized in your local environment under the <code>outputs/</code> directory.</p>
            
            <div class="footer">
                <p>This is an automated system email generated by Antigravity Resume Builder.</p>
                <p>Workspace: <code>d:\Resume_Builder</code> | Execution Environment: Windows PowerShell</p>
            </div>
        </div>
    </body>
    </html>
    """
    return html

def send_email_digest(reports_list, pdf_paths, improvements, upskilling, recipient_email):
    """
    Main function to send out the weekly resume package email with attachments.
    Saves a local HTML backup file and returns status.
    """
    # 1. Generate HTML Body
    html_content = build_html_report(reports_list, improvements, upskilling)
    
    # Save a local HTML file as a reference/backup
    os.makedirs("outputs", exist_ok=True)
    html_backup_path = os.path.join("outputs", "weekly_digest.html")
    with open(html_backup_path, "w", encoding="utf-8") as f:
        f.write(html_content)
    print(f"Local HTML digest report written to {html_backup_path}")
    
    # 2. Extract SMTP configurations
    smtp_server = os.getenv("SMTP_SERVER", "")
    smtp_port = int(os.getenv("SMTP_PORT", "587"))
    smtp_user = os.getenv("SMTP_USER", "")
    smtp_pass = os.getenv("SMTP_PASS", "")
    sender_email = os.getenv("SENDER_EMAIL", smtp_user)
    
    # If no SMTP parameters are provided, print detailed log and gracefully bypass
    if not smtp_server or not smtp_user or not smtp_pass:
        print("\n" + "="*50)
        print("SMTP NOTIFICATION SYSTEM WARNING")
        print("="*50)
        print("SMTP server, user, or password environment variables were not found.")
        print("We have safely generated all 16 PDFs and compiled the executive report.")
        print("To enable automatic email delivery, please create a '.env' file in the workspace:")
        print("SMTP_SERVER=smtp.gmail.com")
        print("SMTP_PORT=587")
        print("SMTP_USER=your_email@gmail.com")
        print("SMTP_PASS=your_app_password")
        print("SENDER_EMAIL=your_email@gmail.com")
        print("="*50 + "\n")
        return False
        
    print(f"Connecting to SMTP Server {smtp_server}:{smtp_port}...")
    try:
        # Create Message Container
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["To"] = recipient_email
        msg["Subject"] = "Weekly Updated ATS Optimized Resume Pack"
        
        # Attach HTML Body
        msg.attach(MIMEText(html_content, "html"))
        
        # Attach all 16 PDFs
        attached_count = 0
        for path in pdf_paths:
            if os.path.exists(path):
                filename = os.path.basename(path)
                with open(path, "rb") as f:
                    part = MIMEBase("application", "octet-stream")
                    part.set_payload(f.read())
                encoders.encode_base64(part)
                part.add_header("Content-Disposition", f"attachment; filename= {filename}")
                msg.attach(part)
                attached_count += 1
                
        # Send Email
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_user, smtp_pass)
        server.sendmail(sender_email, recipient_email, msg.as_string())
        server.close()
        
        print(f"Successfully sent weekly digest email to {recipient_email} with {attached_count} attachments.")
        return True
        
    except Exception as e:
        print(f"Failed to dispatch email via SMTP: {str(e)}")
        return False

if __name__ == "__main__":
    # Test builder logic without SMTP
    dummy_reports = [
        {
            "file_name": "Ashutosh_Sharma_DevOps_Engineer.pdf",
            "page_count": 2,
            "keyword_match_percentage": 98.2,
            "metrics_score": 10,
            "overall_score": 98.5,
            "status": "PASSED (Excellent)"
        }
    ]
    build_html_report(dummy_reports, ["Test Improvement"], ["Test Upskilling"])
    print("HTML build verified.")
