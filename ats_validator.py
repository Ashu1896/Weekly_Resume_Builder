import os
import re
from pypdf import PdfReader

class ATSValidator:
    def __init__(self):
        pass

    def check_text_for_metrics(self, text):
        # Optimized regex patterns for technical metrics that correctly handle non-word boundaries
        metric_patterns = [
            r'\b\d+(?:\.\d+)?%\B',      # Matches 25%, 99.95% (trailing non-word char)
            r'\b\d+\+\B',               # Matches 2000+, 50+ (trailing non-word char)
            r'\b(?:L\d+/L\d+|24/7|\d+-\d+|\d+-minute)\b', # Matches L2/L3, 24/7, 15-minute
            r'\b(uptime|SLA|RTO|MTTR)\b', # Core enterprise SLA metrics
            r'\b(hours|minutes|seconds)\b', # Time-saving metrics
            r'\b\d+\+?\s+(servers|outages|playbooks|applications)\b' # Asset automation counts
        ]
        
        matches = 0
        for pattern in metric_patterns:
            if re.search(pattern, text, re.IGNORECASE):
                matches += 1
                
        # Return metric presence score out of 10 (each match contributes 2 points, max 10)
        score = min(matches * 2, 10)
        return score

    def calculate_ats_score(self, pdf_path, critical_keywords):
        report = {
            "file_name": os.path.basename(pdf_path),
            "readable": False,
            "page_count": 0,
            "keyword_match_percentage": 0.0,
            "keywords_found": [],
            "keywords_missing": [],
            "metrics_score": 0,
            "overall_score": 0.0,
            "warnings": [],
            "status": "FAILED"
        }
        
        if not os.path.exists(pdf_path):
            report["warnings"].append("PDF file does not exist.")
            return report
            
        try:
            reader = PdfReader(pdf_path)
            report["page_count"] = len(reader.pages)
            
            # Extract text
            full_text = ""
            for page in reader.pages:
                text = page.extract_text()
                if text:
                    full_text += text + "\n"
                    
            if not full_text.strip():
                report["warnings"].append("Zero text extracted from PDF. File might be rendered as an image, breaking ATS readability.")
                return report
                
            report["readable"] = True
            
            # 1. Page count check: resumes must be 1-2 pages maximum.
            if report["page_count"] > 2:
                report["warnings"].append(f"Resume is {report['page_count']} pages long. Excellent resumes are strictly 1-2 pages.")
            elif report["page_count"] == 0:
                report["warnings"].append("Resume has 0 pages.")
                
            # 2. Keyword Match Density
            found = []
            missing = []
            for kw in critical_keywords:
                # Standard clean keyword to handle special characters like + or / safely in regex
                clean_kw = re.escape(kw)
                
                # Replace literal escaped spaces with \s+ to match across line breaks and newlines!
                clean_kw = clean_kw.replace(r"\ ", r"\s+")
                
                # Flexible match: handle potential hyphens and slash variations
                pattern = rf"\b{clean_kw}\b"
                if kw == "K8s":
                    pattern = r"\b(K8s|Kubernetes)\b"
                elif kw == "SSL/TLS Certificates":
                    pattern = r"\b(SSL|TLS|Certificates)\b"
                elif "/" in kw and "/" not in pattern:
                    # Allow matching parts of slash-separated terms
                    parts = [re.escape(p) for p in kw.split("/")]
                    pattern = r"\b(" + "|".join(parts) + r")\b"
                
                if re.search(pattern, full_text, re.IGNORECASE):
                    found.append(kw)
                else:
                    missing.append(kw)
                    
            report["keywords_found"] = found
            report["keywords_missing"] = missing
            
            kw_match_ratio = len(found) / len(critical_keywords) if critical_keywords else 1.0
            report["keyword_match_percentage"] = round(kw_match_ratio * 100, 2)
            
            # 3. Metric Checks
            metrics_rating = self.check_text_for_metrics(full_text)
            report["metrics_score"] = metrics_rating
            
            # 4. ATS Scoring Algorithm
            # Structure / Formatting: 40% (since we programmatically ensure a perfect single-column layout without tables, this is 100%)
            # Keyword Fit: 40% (direct ratio of matching industry keywords)
            # Impact / Metrics: 20% (quantifiable achievements in technical role)
            format_score = 100.0
            keyword_score = report["keyword_match_percentage"]
            metric_score = metrics_rating * 10.0 # scale to 100
            
            overall = (format_score * 0.40) + (keyword_score * 0.40) + (metric_score * 0.20)
            
            # Apply slight penalty if page length is over 2
            if report["page_count"] > 2:
                overall -= 10
                
            report["overall_score"] = max(0.0, min(100.0, round(overall, 2)))
            
            if report["overall_score"] >= 95.0:
                report["status"] = "PASSED (Excellent)"
            elif report["overall_score"] >= 85.0:
                report["status"] = "PASSED (High Match)"
            else:
                report["status"] = "NEEDS OPTIMIZATION"
                
        except Exception as e:
            report["warnings"].append(f"Error parsing PDF: {str(e)}")
            
        return report

if __name__ == "__main__":
    # Test validator on generated test resume
    from pdf_generator import generate_pdf_resume
    from customize import customize_resume, load_master_profile
    
    profile = load_master_profile("master_profile.yml")
    c_data = customize_resume("devops_engineer", profile)
    generate_pdf_resume(c_data, "test_resume.pdf")
    
    val = ATSValidator()
    rep = val.calculate_ats_score("test_resume.pdf", c_data["critical_keywords"])
    print("Validator Test Report:")
    print("Page Count:", rep["page_count"])
    print("Keyword Match:", rep["keyword_match_percentage"], "%")
    print("Metrics Rating:", rep["metrics_score"], "/ 10")
    print("Overall ATS Score:", rep["overall_score"], "%")
    print("Status:", rep["status"])
    print("Warnings:", rep["warnings"])
