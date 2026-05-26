import yaml

# A comprehensive mapping of role-specific configurations
# This includes custom summaries, prioritized skills, and keyword mappings for all 16 target roles.
# Summaries are optimized to explicitly contain target keywords for a perfect ATS match.
ROLE_CONFIGS = {
    "linux_administrator": {
        "title": "Linux Administrator",
        "summary": "Results-driven Linux Administrator with 5+ years of experience administering, troubleshooting, and securing enterprise infrastructure. Expertise in Red Hat Enterprise Linux (RHEL 7/8/9), managing server fleets of 2000+ servers. Highly skilled in LVM storage, shell scripting (Bash/Python), systemd, OS migration, patching, and system hardening per CIS benchmarks. Proven track record of achieving 99.95% server uptime SLA. Proficient in Apache and Tomcat middleware deployments.",
        "skills_order": ["linux_administration", "middleware_web", "scripting_automation", "security_compliance", "automation_iac", "databases"],
        "highlight_tags": ["linux", "rhel", "sysadmin", "troubleshooting", "middleware", "bash"],
        "critical_keywords": ["RHEL", "LVM", "systemd", "Shell Scripting", "Kernel Tuning", "OS Migration", "Patching", "Troubleshooting", "Apache", "Tomcat", "SLA", "Enterprise Infrastructure"]
    },
    "senior_linux_administrator": {
        "title": "Senior Linux Administrator",
        "summary": "Seasoned Senior Linux Administrator with 5+ years of deep technical expertise architecting, maintaining, and automating large-scale enterprise RHEL infrastructure. Proven leader in executing complex OS migration projects migrating 1000+ servers with zero downtime. Expert in kernel parameter tuning (improving latency by 25%), CIS security hardening, high availability design, LVM storage orchestration, and advanced configuration management via Ansible. Strong track record of troubleshooting and maintaining 99.95% SLA across critical operations.",
        "skills_order": ["linux_administration", "security_compliance", "automation_iac", "monitoring_observability", "middleware_web", "databases"],
        "highlight_tags": ["linux", "rhel", "sysadmin", "enterprise", "hardening", "ansible", "performance"],
        "critical_keywords": ["Enterprise RHEL", "CIS Benchmarks", "Kernel Tuning", "Ansible", "High Availability", "LVM", "OS Migration", "Security Hardening", "Troubleshooting", "SLA"]
    },
    "devops_engineer": {
        "title": "DevOps Engineer",
        "summary": "Automation-focused DevOps Engineer with 5+ years of experience driving CI/CD practices, pipeline automation, and containerized microservices orchestration. Expert in streamlining software delivery lifecycles, developing 50+ Ansible playbooks to reduce deployment times by 75%, and provisioning secure AWS architectures with Terraform. Adept at bridging the gap between development and operations to implement robust shift-left observability pipelines, container validation (Docker, Kubernetes/K8s), and self-healing systems using Git.",
        "skills_order": ["containers_devops", "automation_iac", "aws_services", "monitoring_observability", "linux_administration", "databases"],
        "highlight_tags": ["devops", "cicd", "ansible", "terraform", "docker", "kubernetes", "automation"],
        "critical_keywords": ["CI/CD", "DevOps", "Terraform", "Ansible", "Docker", "Kubernetes", "Jenkins", "Git", "Infrastructure as Code", "Pipeline Automation", "GitHub"]
    },
    "aws_devops_engineer": {
        "title": "AWS DevOps Engineer",
        "summary": "Certified AWS Cloud & DevOps Engineer with 5+ years of experience architecting, securing, and automating enterprise cloud infrastructures. Deep expertise in core AWS services (EC2, S3, IAM, CloudWatch, RDS, VPC) and provisioning multi-region cloud resources programmatically via Terraform and CloudFormation. Experienced in building high-availability cloud solutions, managing IAM policies, automated certificate renewal, and migrating workloads to containerized architectures (Docker, EKS/ECS). Excellent command of AWS observability and logging.",
        "skills_order": ["aws_services", "automation_iac", "containers_devops", "monitoring_observability", "cloud_infrastructure", "security_compliance"],
        "highlight_tags": ["aws", "cloud", "terraform", "iac", "security", "cloudwatch"],
        "critical_keywords": ["AWS", "Terraform", "CloudWatch", "VPC", "EC2", "S3", "IAM Policies", "Auto Scaling", "Infrastructure as Code", "Route 53", "ECS", "CloudTrail"]
    },
    "cloud_engineer": {
        "title": "Cloud Engineer",
        "summary": "Dynamic Cloud Engineer with 5+ years of experience designing, building, and optimizing scalable, high-performance AWS cloud architectures. Skilled in provisioning virtual environments (VPC, EC2, S3, RDS), enforcing strict cloud security governance through IAM, and implementing resilient disaster recovery protocols. Proficient in automating cloud resources via Terraform, cost optimization, and reducing operational overhead by 40% using automated archival policies.",
        "skills_order": ["aws_services", "cloud_infrastructure", "automation_iac", "monitoring_observability", "linux_administration", "security_compliance"],
        "highlight_tags": ["aws", "cloud", "terraform", "infrastructure", "cost", "storage"],
        "critical_keywords": ["AWS Cloud", "Terraform", "VPC", "EC2", "S3", "RDS", "IAM", "Cloud Architecture", "Disaster Recovery", "Cost Optimization", "High Availability"]
    },
    "platform_engineer": {
        "title": "Platform Engineer",
        "summary": "Platform Engineer with a passion for building robust, self-service developer platforms and standardizing Kubernetes/cloud-native infrastructure. Over 5+ years of technical experience automating environment provisioning with Terraform and configuration management with Ansible. Focused on Platform Engineering, improving developer velocity, enforcing centralized compliance policies, containerizing complex enterprise workloads (Docker), and integrating shift-left observability tools into CI/CD pipelines.",
        "skills_order": ["containers_devops", "automation_iac", "aws_services", "linux_administration", "monitoring_observability", "security_compliance"],
        "highlight_tags": ["platform", "kubernetes", "docker", "terraform", "ansible", "cicd"],
        "critical_keywords": ["Platform Engineering", "Kubernetes", "Docker", "Terraform", "Ansible", "CI/CD Pipelines", "Self-Service", "Infrastructure as Code", "Centralized Compliance", "Observability"]
    },
    "site_reliability_engineer": {
        "title": "Site Reliability Engineer (SRE)",
        "summary": "Reliability-driven Site Reliability Engineer with 5+ years of experience managing large-scale server fleets and cloud infrastructures. Expert in Site Reliability Engineering, observability pipelines (Dynatrace, Datadog, Prometheus, Grafana), setting up custom capacity dashboards, and intelligent alerting to reduce false positives by 65%. Proven success engineering self-healing systems that reduced ticketing by 45% and achieving a 15-minute MTTR under a strict uptime SLA.",
        "skills_order": ["monitoring_observability", "cloud_infrastructure", "linux_administration", "automation_iac", "security_compliance", "databases"],
        "highlight_tags": ["sre", "monitoring", "observability", "troubleshooting", "incident", "mttr", "dr"],
        "critical_keywords": ["Site Reliability Engineering", "SRE", "Observability", "Dynatrace", "Datadog", "Prometheus", "Grafana", "Incident Response", "MTTR", "Disaster Recovery", "Uptime SLA", "Self-Healing"]
    },
    "infrastructure_engineer": {
        "title": "Infrastructure Engineer",
        "summary": "Infrastructure Engineer with 5+ years of experience managing robust systems and fleets of 2000+ servers (RHEL/Ubuntu, HP-UX, AIX, Nutanix hypervisors). Proven expert in Infrastructure Engineering, executing OS upgrade operations, standardizing server deployments, designing high-availability storage architectures (LVM/RAID), and configuring high-uptime operations. Skilled in hardware management, storage administration, and infrastructure-as-code automation using Ansible and Terraform.",
        "skills_order": ["linux_administration", "cloud_infrastructure", "automation_iac", "security_compliance", "middleware_web", "databases"],
        "highlight_tags": ["infrastructure", "linux", "rhel", "sysadmin", "enterprise", "storage"],
        "critical_keywords": ["Infrastructure Engineering", "RHEL", "System Administration", "LVM", "Ansible", "High Availability", "Nutanix", "Hardware Management", "OS Upgrade", "Storage Administration"]
    },
    "automation_engineer": {
        "title": "Automation Engineer",
        "summary": "Automation Specialist with 5+ years of experience streamlining IT operations, creating configuration management playbooks, and building complex scripting frameworks. Master of Ansible (50+ enterprise playbooks), Python scripting, and Bash scripting. Proven ability to configure cron jobs, automate daily health checks, and execute process optimization, reducing operational overhead by 40% and enhancing overall operational efficiency.",
        "skills_order": ["automation_iac", "containers_devops", "linux_administration", "monitoring_observability", "aws_services", "databases"],
        "highlight_tags": ["automation", "ansible", "python", "bash", "cron", "sec_automation"],
        "critical_keywords": ["Automation", "Ansible Playbooks", "Python Scripting", "Bash Scripting", "Cron Jobs", "Process Optimization", "CI/CD", "Terraform", "Self-Healing", "Operational Efficiency"]
    },
    "cloud_operations_engineer": {
        "title": "Cloud Operations Engineer",
        "summary": "Operations-focused Cloud Operations Engineer with 5+ years of experience monitoring, patching, and maintaining complex AWS and Linux systems. Expert in incident troubleshooting, patch management, cost control, SLA compliance, backup policies, and monitoring dashboards. Proven track record of managing 2000+ server environments, adhering to strict SLAs, and executing compliance hardening per CIS benchmarks.",
        "skills_order": ["aws_services", "monitoring_observability", "linux_administration", "security_compliance", "cloud_infrastructure", "databases"],
        "highlight_tags": ["aws", "cloud", "ops", "monitoring", "security", "sysadmin"],
        "critical_keywords": ["Cloud Operations", "AWS", "CloudWatch", "Incident Troubleshooting", "Patch Management", "Cost Control", "SLA Compliance", "Backup Policies", "Monitoring Dashboards", "Linux Systems"]
    },
    "middleware_engineer": {
        "title": "Middleware Engineer",
        "summary": "Middleware Engineer with 5+ years of specialized experience deploying, configuring, and optimizing high-volume web and application servers. Deep expertise in Apache HTTPD, Nginx, Apache Tomcat, and JBoss. Expert in middleware clustering, SSL/TLS certificates automation, JVM tuning, load balancing, connection pools setup, reverse proxy configurations, and troubleshooting high-concurrency enterprise traffic.",
        "skills_order": ["middleware_web", "linux_administration", "security_compliance", "automation_iac", "monitoring_observability", "databases"],
        "highlight_tags": ["middleware", "tomcat", "apache", "ssl", "performance"],
        "critical_keywords": ["Middleware", "Apache Tomcat", "Apache HTTPD", "Nginx", "SSL/TLS Certificates", "JVM Tuning", "Clustering", "Load Balancing", "Connection Pools", "Troubleshooting", "Reverse Proxy"]
    },
    "cicd_engineer": {
        "title": "CI/CD Engineer",
        "summary": "Continuous Integration & Deployment Specialist with 5+ years of expertise designing and optimizing reliable build automation, release engineering, and artifact management workflows. Master at integrating testing, scanning (SonarQube), and deployment triggers using Jenkins, GitHub Actions, and Git. Focused on accelerating release cycles, reducing manual deployment errors by 90%, and automating environment provisioning via Infrastructure as Code.",
        "skills_order": ["containers_devops", "automation_iac", "aws_services", "monitoring_observability", "linux_administration", "databases"],
        "highlight_tags": ["devops", "cicd", "jenkins", "git", "release", "automation"],
        "critical_keywords": ["CI/CD Pipelines", "Jenkins", "Git", "GitHub Actions", "Build Automation", "SonarQube", "Release Engineering", "Ansible", "Terraform", "Docker", "Artifact Management"]
    },
    "production_support_engineer": {
        "title": "Production Support Engineer (L2/L3)",
        "summary": "Production Support Specialist with 5+ years of experience troubleshooting high-severity incidents, conducting deep-dive root cause analysis (RCA), and supporting mission-critical enterprise systems. Strong skills in incident management, SLA compliance, log analysis, L2/L3 support, and ticketing systems. Achieved a consistent 15-minute MTTR and reduced ticket counts by 45% via self-healing workflows.",
        "skills_order": ["monitoring_observability", "linux_administration", "security_compliance", "databases", "aws_services", "automation_iac"],
        "highlight_tags": ["support", "incident", "troubleshooting", "rca", "sysadmin"],
        "critical_keywords": ["Production Support", "Incident Management", "Root Cause Analysis", "RCA", "SLA Compliance", "Log Analysis", "Troubleshooting", "Dynatrace", "Datadog", "MTTR", "L2/L3 Support", "Ticketing Systems"]
    },
    "system_engineer": {
        "title": "System Engineer",
        "summary": "Analytical Systems Engineer with 5+ years of experience designing, patching, and maintaining robust system architectures. Expert in System Engineering, Red Hat Enterprise Linux (RHEL), volume management (LVM/RAID), OS upgrades, backup systems, and shell scripting. Highly skilled in security hardening, centralized configurations, and automating daily operations via Bash/Python.",
        "skills_order": ["linux_administration", "security_compliance", "automation_iac", "monitoring_observability", "databases", "middleware_web"],
        "highlight_tags": ["linux", "rhel", "sysadmin", "troubleshooting", "security", "logging"],
        "critical_keywords": ["System Engineering", "RHEL", "LVM", "RAID", "DNS", "DHCP", "Security Hardening", "System Administration", "OS Upgrades", "Backup Systems", "Shell Scripting"]
    },
    "kubernetes_engineer": {
        "title": "Kubernetes Engineer",
        "summary": "Cloud-Native Systems Engineer specializing in container orchestration, microservices hosting, and Kubernetes cluster engineering. Practical experience administering Docker and K8s environments. Adept at YAML configuration, cluster administration, Helm charts, ingress controllers, persistent storage classes, and cloud native architectures automated via Infrastructure as Code.",
        "skills_order": ["containers_devops", "automation_iac", "aws_services", "monitoring_observability", "security_compliance", "linux_administration"],
        "highlight_tags": ["kubernetes", "docker", "terraform", "devops", "cloud"],
        "critical_keywords": ["Kubernetes", "K8s", "Docker", "Helm", "Containers", "Microservices", "Ingress", "Terraform", "YAML", "Cluster Administration", "Cloud Native", "CI/CD"]
    },
    "release_engineer": {
        "title": "Release Engineer",
        "summary": "Software Configuration and Release Engineer with 5+ years of experience managing version control branching, build environments, and coordinating application deployments. Expert in Release Engineering, branching strategy, build automation, and deployment coordination. Proven ability to implement change management, manage software configuration management, and reduce manual configuration errors by 90%.",
        "skills_order": ["containers_devops", "automation_iac", "monitoring_observability", "linux_administration", "security_compliance", "databases"],
        "highlight_tags": ["release", "git", "jenkins", "cicd", "automation"],
        "critical_keywords": ["Release Engineering", "Git", "GitHub", "GitLab", "Jenkins", "Version Control", "Branching Strategy", "Build Automation", "Deployment Coordination", "Software Configuration Management", "Change Management"]
    }
}

def load_master_profile(path="master_profile.yml"):
    with open(path, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)

def customize_resume(role_key, master_profile):
    if role_key not in ROLE_CONFIGS:
        raise ValueError(f"Role '{role_key}' is not configured.")
    
    config = ROLE_CONFIGS[role_key]
    
    # 1. Start with copy of candidate basic info
    customized = {
        "candidate_info": dict(master_profile["candidate_info"]),
        "certifications": list(master_profile["certifications"]),
        "education": list(master_profile["education"])
    }
    
    # Override role title in headline
    customized["candidate_info"]["role_headline"] = config["title"]
    
    # 2. Inject role-specific summary
    customized["professional_summary"] = config["summary"]
    
    # 3. Sort/Structure skills according to the role's prioritized order
    master_skills = master_profile["core_competencies"]
    custom_skills = []
    
    # Extract ordered skill groups
    for skill_group in config["skills_order"]:
        if skill_group in master_skills:
            # Map snake_case keys to standard readable headings
            header_map = {
                "aws_services": "AWS Cloud Services",
                "cloud_infrastructure": "Cloud Architecture & Operations",
                "automation_iac": "Automation & Infrastructure as Code",
                "linux_administration": "Linux System Administration",
                "monitoring_observability": "Monitoring & Observability",
                "security_compliance": "Security & Compliance Hardening",
                "containers_devops": "Containers & DevOps Pipelines",
                "databases": "Databases & Web Middleware",
                "middleware_web": "Middleware & Web Servers",
                "scripting_automation": "Scripting & Custom Automation"
            }
            heading = header_map.get(skill_group, skill_group.replace("_", " ").title())
            custom_skills.append({
                "category": heading,
                "items": master_skills[skill_group]
            })
            
    customized["skills"] = custom_skills
    
    # 4. Filter and re-prioritize experience highlights based on relevance tags
    custom_experience = []
    for job in master_profile["professional_experience"]:
        custom_job = {
            "company": job["company"],
            "location": job["location"],
            "role": job["role"],
            "duration": job["duration"],
            "highlights": []
        }
        
        # Sort highlights: highlights that contain tags present in our role's 'highlight_tags' go first
        sorted_highlights = []
        tagged_matches = []
        other_matches = []
        
        for hl in job["highlights"]:
            # Check how many tags match our role's highlight_tags
            matching_tags_count = len(set(hl["tags"]).intersection(set(config["highlight_tags"])))
            if matching_tags_count > 0:
                tagged_matches.append((matching_tags_count, hl))
            else:
                other_matches.append(hl)
                
        # Sort tagged matches descending by number of matching tags
        tagged_matches.sort(key=lambda x: x[0], reverse=True)
        
        # Merge back: prioritized first, then others to preserve full career history
        full_sorted = [x[1] for x in tagged_matches] + other_matches
        
        # Limit experience bullets per role to ensure we fit standard 1-2 page formatting constraints.
        # Senior Capgemini role gets up to 12 points (core experience), others get up to 4-5.
        max_bullets = 12 if "Capgemini" in job["company"] else 4
        custom_job["highlights"] = [hl["description"] for hl in full_sorted[:max_bullets]]
        
        custom_experience.append(custom_job)
        
    customized["professional_experience"] = custom_experience
    customized["critical_keywords"] = config["critical_keywords"]
    
    return customized

if __name__ == "__main__":
    profile = load_master_profile()
    res = customize_resume("sre", profile)
    print("SRE Customized Resume Title:", res["candidate_info"]["role_headline"])
    print("SRE Summary Sample:", res["professional_summary"])
    print("Prioritized Skill Categories:", [s["category"] for s in res["skills"]])
