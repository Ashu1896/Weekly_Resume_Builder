import os
from fpdf import FPDF

def clean_text(text):
    if not isinstance(text, str):
        return text
    # Replace en-dash and em-dash with standard ASCII hyphen
    text = text.replace("\u2013", "-").replace("\u2014", "-")
    # Replace smart double quotes
    text = text.replace("\u201c", '"').replace("\u201d", '"')
    # Replace smart single quotes
    text = text.replace("\u2018", "'").replace("\u2019", "'")
    # Replace standard bullet points with hyphen
    text = text.replace("\u2022", "-")
    # Replace other non-latin1 characters with standard ASCII equivalents
    return text

class ATSResumePDF(FPDF):
    def __init__(self):
        # Enforce standard A4 size, portrait, margins of 15mm (approx 0.6 inch) for excellent layout density
        super().__init__(orientation="P", unit="mm", format="A4")
        self.set_margins(15, 15, 15)
        self.set_auto_page_break(auto=True, margin=15)
        
    def header(self):
        # No automated running header to avoid confusing ATS scanners
        pass
        
    def footer(self):
        # Subtle, clean page numbering in the footer
        self.set_y(-12)
        self.set_font("Helvetica", "I", 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 5, f"Page {self.page_no()} of {{nb}}", align="C", border=0)

    def draw_section_header(self, title):
        self.ln(4)
        # Deep Navy Steel Blue color for headers (#1F4E79) - highly professional
        self.set_text_color(31, 78, 121)
        self.set_font("Helvetica", "B", 12)
        self.cell(0, 6, clean_text(title.upper()), ln=1, align="L")
        
        # Draw a thin, elegant horizontal rule under the header
        self.set_draw_color(31, 78, 121)
        self.set_line_width(0.4)
        x = self.get_x()
        y = self.get_y() - 1
        self.line(x, y, 210 - x, y) # A4 width is 210mm
        self.ln(2.5)

    def draw_candidate_header(self, info):
        self.set_y(15)
        # Candidate Name: 20pt Bold, Dark Charcoal (#1A1A1A)
        self.set_text_color(26, 26, 26)
        self.set_font("Helvetica", "B", 20)
        self.cell(0, 8, clean_text(info["name"].upper()), ln=1, align="C")
        
        # Professional Role Headline: 12pt Regular, Medium Grey
        self.set_text_color(70, 70, 70)
        self.set_font("Helvetica", "B", 11.5)
        self.cell(0, 6, clean_text(info["role_headline"].upper()), ln=1, align="C")
        self.ln(1)
        
        # Contact details in a single clean row separated by standard | character
        self.set_font("Helvetica", "", 9)
        self.set_text_color(80, 80, 80)
        contact_line = f"Email: {info['email']}   |   Phone: {info['phone']}   |   Location: {info['location']}"
        self.cell(0, 5, clean_text(contact_line), ln=1, align="C")
        
        # Social line rendering as separate clickable cells to enable distinct hyperlinks:
        self.set_font("Helvetica", "", 9)
        linkedin_label = "LinkedIn: "
        linkedin_val = info['linkedin']
        separator = "   |   "
        github_label = "GitHub: "
        github_val = info['github']
        
        total_width = (
            self.get_string_width(linkedin_label) +
            self.get_string_width(linkedin_val) +
            self.get_string_width(separator) +
            self.get_string_width(github_label) +
            self.get_string_width(github_val)
        )
        
        start_x = (210 - total_width) / 2
        self.set_x(start_x)
        
        self.set_text_color(80, 80, 80)
        self.cell(self.get_string_width(linkedin_label), 5, linkedin_label, border=0, ln=0)
        
        self.set_text_color(31, 78, 121)
        linkedin_link = linkedin_val if linkedin_val.startswith("http") else f"https://{linkedin_val}"
        self.cell(self.get_string_width(linkedin_val), 5, clean_text(linkedin_val), border=0, ln=0, link=linkedin_link)
        
        self.set_text_color(80, 80, 80)
        self.cell(self.get_string_width(separator), 5, separator, border=0, ln=0)
        
        self.cell(self.get_string_width(github_label), 5, github_label, border=0, ln=0)
        
        self.set_text_color(31, 78, 121)
        github_link = github_val if github_val.startswith("http") else f"https://{github_val}"
        self.cell(self.get_string_width(github_val), 5, clean_text(github_val), border=0, ln=1, link=github_link)
        self.ln(1)

    def draw_summary(self, text):
        self.set_font("Helvetica", "", 9.5)
        # Dark grey body text
        self.set_text_color(40, 40, 40)
        # Use multi_cell for clean wrapping, 1.25x line spacing (4.5mm height for 9.5pt font)
        self.multi_cell(0, 4.5, clean_text(text), border=0, align="J")
        self.ln(1.5)

    def draw_skills(self, skills):
        # Render skills as a clean vertical list of categories with items bolded
        for skill_group in skills:
            self.set_font("Helvetica", "B", 9.5)
            self.set_text_color(50, 50, 50)
            self.write(4.5, clean_text(f"{skill_group['category']}: "))
            
            self.set_font("Helvetica", "", 9.5)
            self.set_text_color(70, 70, 70)
            items_str = ", ".join(skill_group["items"])
            self.write(4.5, clean_text(f"{items_str}\n"))
        self.ln(2)

    def draw_experience_block(self, exp):
        for job in exp:
            # 1. Job Title, Company, Location and Dates
            self.set_font("Helvetica", "B", 10.5)
            self.set_text_color(30, 30, 30)
            
            role_text = f"{job['role']}"
            date_text = f"{job['duration']}"
            company_text = f"{job['company']} -- {job['location']}"
            
            self.set_font("Helvetica", "B", 10)
            self.cell(110, 5, clean_text(role_text), ln=0, align="L")
            self.set_font("Helvetica", "I", 9.5)
            self.set_text_color(100, 100, 100)
            self.cell(70, 5, clean_text(date_text), ln=1, align="R")
            
            self.set_font("Helvetica", "B", 9.5)
            self.set_text_color(70, 70, 70)
            self.cell(0, 4.5, clean_text(company_text), ln=1, align="L")
            self.ln(1)
            
            # 2. Render bullet points using custom hanging indents for neat visuals
            self.set_font("Helvetica", "", 9.5)
            self.set_text_color(50, 50, 50)
            for hl in job["highlights"]:
                self.set_x(18) # Indent slightly
                # Draw en-dash bullet
                self.cell(4, 4.5, "-", border=0, ln=0)
                # Render wrapped text
                self.multi_cell(0, 4.5, clean_text(hl), border=0, align="L")
            self.ln(2)

    def draw_certifications(self, certs):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(50, 50, 50)
        for cert in certs:
            self.set_x(18)
            self.cell(4, 4.5, "-", border=0, ln=0)
            cert_text = f"{cert['name']} ({cert['issuer']}) -- {cert['year']}"
            if cert.get("status") == "In Progress":
                cert_text += " [In Progress]"
            self.cell(0, 4.5, clean_text(cert_text), ln=1, align="L")
        self.ln(1.5)

    def draw_education(self, edu):
        self.set_font("Helvetica", "", 9.5)
        self.set_text_color(50, 50, 50)
        for school in edu:
            # Bullet 1: Degree, Institution, and Graduation Year
            self.set_x(18)
            self.cell(4, 4.5, "-", border=0, ln=0)
            edu_text = f"{school['degree']} - {school['institution']} ({school['year']})"
            self.cell(0, 4.5, clean_text(edu_text), ln=1, align="L")
            
            # Bullet 2: Indented score block directly below the degree
            if "gpa" in school:
                self.set_x(18)
                self.cell(4, 4.5, "-", border=0, ln=0)
                score_text = f"Score: {school['gpa']}"
                self.cell(0, 4.5, clean_text(score_text), ln=1, align="L")

def generate_pdf_resume(data, output_path):
    pdf = ATSResumePDF()
    pdf.alias_nb_pages()
    pdf.add_page()
    
    # 1. Header
    pdf.draw_candidate_header(data["candidate_info"])
    
    # 2. Professional Summary
    pdf.draw_section_header("Professional Summary")
    pdf.draw_summary(data["professional_summary"])
    
    # 3. Technical Skills
    pdf.draw_section_header("Technical Skills")
    pdf.draw_skills(data["skills"])
    
    # 4. Professional Experience
    pdf.draw_section_header("Professional Experience")
    pdf.draw_experience_block(data["professional_experience"])
    
    # 5. Certifications
    pdf.draw_section_header("Certifications")
    pdf.draw_certifications(data["certifications"])
    
    # 6. Education
    pdf.draw_section_header("Education")
    pdf.draw_education(data["education"])
    
    # Save the file
    pdf.output(output_path)

if __name__ == "__main__":
    from customize import customize_resume, load_master_profile
    profile = load_master_profile("master_profile.yml")
    custom_data = customize_resume("devops_engineer", profile)
    generate_pdf_resume(custom_data, "test_resume.pdf")
    print("Test PDF resume generated successfully.")
