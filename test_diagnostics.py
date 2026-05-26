from customize import load_master_profile, customize_resume, ROLE_CONFIGS
from pdf_generator import generate_pdf_resume
from ats_validator import ATSValidator

profile = load_master_profile()
validator = ATSValidator()

for role_key in ROLE_CONFIGS.keys():
    c_data = customize_resume(role_key, profile)
    pdf_path = f"outputs/temp_{role_key}.pdf"
    generate_pdf_resume(c_data, pdf_path)
    report = validator.calculate_ats_score(pdf_path, c_data["critical_keywords"])
    print(f"Role: {role_key} | Score: {report['overall_score']}%")
    if report["keywords_missing"]:
        print("  Missing Keywords:", report["keywords_missing"])
