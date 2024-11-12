APP_TITLE = "Self Assessment"

APP_INTRO = """This app helps you find Your capability level based on your preferences,skills and qualifications."""

APP_HOW_IT_WORKS = """
This app collects information about your interests, skills and qualifications. It uses a combination of logical conditions and AI to Assess your capability levels based on your preferences.
"""

SHARED_ASSET = {}

HTML_BUTTON = {}

SYSTEM_PROMPT = """You are a student self-assessment advisor. Based on a student's academic performance, skills, and qualification, you can provide personalized feedback and recommendations to help the student identify their current academic standing and potential growth areas."""


PHASES = {
    "phase1": {
        "name": "Personal Information",
        "fields": {
            "name": {
                "type": "text_input",
                "label": "What is your first name?",
                "helper": "First name only, please",
                "value": "Jane"
            },
            "age": {
                "type": "number_input",
                "label": "What is your age?",
                "min_value": 16,
                "max_value": 65,
                "value": 25
            },
            "education_level": {
                "type": "radio",
                "label": "What is your highest level of education?",
                "options": ["Associate's Degree", "Bachelor's Degree", "Master's Degree", "PhD"],
                "value": ""
            },
            "Bachelor's Degree Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options": ["Data Science", "AIML","IOT","Cyber Security","Cloud Computing","Full Stack Development","DevOps","Blockchain","Quantum Computing","Robotics"],
                "showIf": {"education_level": "Bachelor's Degree"}
            },

            "Associate's Degree Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options": ["Business and Management", "Information Technology"],
                "showIf": {"education_level": "Associate's Degree"}
            },

            "Master's Degree Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options": ["STEM","Business","Engineering"],
                "showIf": {"education_level": "Master's Degree"}
            },

            "PhD Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options":  ["Engineering", "STEM","Business"],
                "showIf": {"education_level": "PhD"}
            },
            
            #new
             "Business and Management Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Accounting", "Business Administration", "Marketing", "Finance", "Hospitality Management"],
    "showIf": {"Associate's Degree Domain": "Business and Management"}
  },

  "Information Technology Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Computer Science", "Network Administration", "Web Development", "Cybersecurity", "Database Management"],
    "showIf": {"Associate's Degree Domain": "Information Technology"}
  },
  
  "Business Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Master of Business Administration (MBA)", "Human Resource Management", "International Business"],
    "showIf": {"Master's Degree Domain": "Business"}
  },
  "STEM Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Computer Science", "Data Science", "Engineering", "Mathematics", "Biotechnology"],
    "showIf": {"Master's Degree Domain": "STEM"}
  },
  "Engineering Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Electrical Engineering", "Mechanical Engineering", "Chemical Engineering", "Civil Engineering", "Computer Engineering"],
    "showIf": {"Master's Degree Domain": "Engineering"}
  },
  "STEM PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Computer Science", "Data Science", "Engineering", "Mathematics", "Biotechnology"],
    "showIf": {"PhD Domain": "STEM"}
  },
  "Business PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Master of Business Administration (MBA)", "Human Resource Management", "International Business"],
    "showIf": {"PhD Domain": "Business"}
  },
  

  "Engineering PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Electrical Engineering", "Mechanical Engineering", "Chemical Engineering", "Civil Engineering", "Computer Engineering"],
    "showIf": {"PhD Domain": "Engineering"}
  },
            "Data Science Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Machine Learning", "Statistical Analysis", "Data Visualization", "Big Data Analytics", "Predictive Modeling", "Natural Language Processing"],
                "showIf": {"Bachelor's Degree Domain": "Data Science"}
            },
            "AIML Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Deep Learning", "Computer Vision", "Reinforcement Learning", "Neural Networks", "Expert Systems", "Genetic Algorithms"],
              "showIf": {"Bachelor's Degree Domain": "AIML"}
            },
            "IOT Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Embedded Systems", "Sensor Networks", "Edge Computing", "IoT Security", "IoT Protocols", "Smart Home/City Technologies"],
              "showIf": {"Bachelor's Degree Domain": "IOT"}
            },
            "Cyber Security Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Network Security", "Application Security", "Information Security", "Cryptography", "Ethical Hacking", "Incident Response and Forensics"],
              "showIf": {"Bachelor's Degree Domain": "Cyber Security"}
            },
            "Cloud Computing Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Infrastructure as a Service (IaaS)", "Platform as a Service (PaaS)", "Software as a Service (SaaS)", "Cloud Architecture", "Serverless Computing", "Multi-cloud and Hybrid Cloud Solutions"],
              "showIf": {"Bachelor's Degree Domain": "Cloud Computing"}
            },
            "Full Stack Development Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Front-end Development", "Back-end Development", "Database Management", "API Development", "Web Security", "User Experience (UX) Design"],
              "showIf": {"Bachelor's Degree Domain": "Full Stack Development"}
            },
            "DevOps Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Continuous Integration/Continuous Deployment (CI/CD)", "Infrastructure as Code", "Configuration Management", "Containerization", "Orchestration", "Monitoring and Logging"],
              "showIf": {"Bachelor's Degree Domain": "DevOps"}
            },
            "Blockchain Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Distributed Ledger Technology", "Smart Contracts", "Cryptocurrency", "Decentralized Finance (DeFi)", "Consensus Mechanisms", "Blockchain Security"],
              "showIf": {"Bachelor's Degree Domain": "Blockchain"}
            },
            "Quantum Computing Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Quantum Algorithms", "Quantum Error Correction", "Quantum Cryptography", "Quantum Simulation", "Quantum Hardware", "Quantum Software Development"],
              "showIf": {"Bachelor's Degree Domain": "Quantum Computing"}
            },
            "Robotics Sub Domain": {
              "type": "radio",
              "label": "Please select your sub domain",
              "options": ["Robot Design and Kinematics", "Computer Vision for Robotics", "Robot Operating System (ROS)", "Human-Robot Interaction", "Autonomous Navigation", "Soft Robotics"],
              "showIf": {"Bachelor's Degree Domain": "Robotics"}
            },
            "Bussiness and management Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Finance","Marketing"],
                "showIf": {"Associate's Degree Domain": "Bussiness and management"}
            },
            "Health Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Pharmacy","Dental"],
                "showIf": {"Master's Degree Domain": "Health"}
            },

            "law and legal Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Crminal law","civil law"],
                "showIf": {"Master's Degree Domain": "law and legal Studies"}
            },
         "Accounting Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Accountant", "Auditor", "Bookkeeper", "Financial Controller", "Tax Specialist"],
    "showIf": {"Business and Management Sub Domain": "Accounting"}
  },
  "Business Administration Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Business Manager", "Operations Analyst", "Project Coordinator", "Administrative Assistant", "Business Consultant"],
    "showIf": {"Business and Management Sub Domain": "Business Administration"}
  },
  "Marketing Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Marketing Specialist", "Digital Marketing Manager", "Brand Manager", "Market Research Analyst", "Social Media Coordinator"],
    "showIf": {"Business and Management Sub Domain": "Marketing"}
  },
  "Finance Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Financial Analyst", "Investment Banker", "Financial Planner", "Risk Manager", "Credit Analyst"],
    "showIf": {"Business and Management Sub Domain": "Finance"}
  },
  "Hospitality Management Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Hotel Manager", "Restaurant Manager", "Event Coordinator", "Tourism Officer", "Customer Service Manager"],
    "showIf": {"Business and Management Sub Domain": "Hospitality Management"}
  },
  
  "Computer Science Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Software Developer", "Systems Analyst", "Database Administrator", "IT Consultant", "Artificial Intelligence Specialist"],
    "showIf": {"Information Technology Sub Domain": "Computer Science"}
  },
  "Network Administration Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Network Administrator", "Systems Administrator", "Network Security Specialist", "IT Support Specialist", "Cloud Infrastructure Engineer"],
    "showIf": {"Information Technology Sub Domain": "Network Administration"}
  },
  "Web Development Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Front-end Developer", "Back-end Developer", "Full Stack Developer", "Web Designer", "UX/UI Developer"],
    "showIf": {"Information Technology Sub Domain": "Web Development"}
  },
  "Cybersecurity Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Information Security Analyst", "Penetration Tester", "Security Engineer", "Incident Response Analyst", "Cybersecurity Consultant"],
    "showIf": {"Information Technology Sub Domain": "Cybersecurity"}
  },
  "Database Management Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Database Administrator", "Data Analyst", "Database Developer", "Data Architect", "Business Intelligence Analyst"],
    "showIf": {"Information Technology Sub Domain": "Database Management"}
  },
  
  "MBA Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Business Development Manager", "Management Consultant", "Operations Manager", "Financial Manager", "Marketing Director"],
    "showIf": {"Business Master's Sub Domain": "Master of Business Administration (MBA)"}
  },
  "Human Resource Management Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["HR Manager", "Talent Acquisition Specialist", "Compensation and Benefits Manager", "Training and Development Manager", "Employee Relations Specialist"],
    "showIf": {"Business Master's Sub Domain": "Human Resource Management"}
  },
  "International Business Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["International Business Development Manager", "Global Marketing Manager", "International Trade Specialist", "Foreign Market Analyst", "Cross-Cultural Business Consultant"],
    "showIf": {"Business Master's Sub Domain": "International Business"}
  },
  "Data Science Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Data Scientist", "Machine Learning Engineer", "Business Intelligence Analyst", "Data Architect", "Quantitative Analyst"],
    "showIf": {"STEM Master's Sub Domain": "Data Science"}
  },
  "Engineering Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Mechanical Engineer", "Electrical Engineer", "Civil Engineer", "Chemical Engineer", "Aerospace Engineer"],
    "showIf": {"STEM Master's Sub Domain": "Engineering"}
  },
  "Mathematics Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Mathematician", "Statistician", "Operations Research Analyst", "Actuary", "Cryptographer"],
    "showIf": {"STEM Master's Sub Domain": "Mathematics"}
  },
  "Biotechnology Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Biomedical Engineer", "Biochemist", "Bioinformatics Specialist", "Clinical Research Associate", "Biotechnology Product Developer"],
    "showIf": {"STEM Master's Sub Domain": "Biotechnology"}
  },
  "Computer Science Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Software Developer", "Systems Analyst", "Database Administrator", "IT Consultant", "Artificial Intelligence Specialist"],
    "showIf": {"STEM Master's Sub Domain": "Computer Science"}
  },
  "Electrical Engineering Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Research Engineer", "Systems Engineer", "Telecommunications Engineer", "Control Systems Engineer", "Robotics Engineer"],
    "showIf": {"Engineering Master's Sub Domain": "Electrical Engineering"}
  },
  "Mechanical Engineering Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Research Engineer", "Aerospace Engineer", "Robotics Engineer", "Automotive Engineer", "Biomedical Engineer"],
    "showIf": {"Engineering Master's Sub Domain": "Mechanical Engineering"}
  },
  "Chemical Engineering Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Process Engineer", "Biochemical Engineer", "Materials Scientist", "Nanotechnology Engineer", "Environmental Engineer"],
    "showIf": {"Engineering Master's Sub Domain": "Chemical Engineering"}
  },
  "Civil Engineering Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Structural Engineer", "Geotechnical Engineer", "Transportation Engineer", "Environmental Engineer", "Water Resources Engineer"],
    "showIf": {"Engineering Master's Sub Domain": "Civil Engineering"}
  },
  "Computer Engineering Master's Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Computer Architect", "Embedded Systems Engineer", "VLSI Designer", "Network Engineer", "Cybersecurity Researcher"],
    "showIf": {"Engineering Master's Sub Domain": "Computer Engineering"}
  },
  
  
  "Electrical Engineering PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Research Engineer", "Systems Engineer", "Telecommunications Engineer", "Control Systems Engineer", "Robotics Engineer"],
    "showIf": {"Engineering PhD Sub Domain": "Electrical Engineering"}
  },
  "Mechanical Engineering PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Research Engineer", "Aerospace Engineer", "Robotics Engineer", "Automotive Engineer", "Biomedical Engineer"],
    "showIf": {"Engineering PhD Sub Domain": "Mechanical Engineering"}
  },
  "Chemical Engineering PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Process Engineer", "Biochemical Engineer", "Materials Scientist", "Nanotechnology Engineer", "Environmental Engineer"],
    "showIf": {"Engineering PhD Sub Domain": "Chemical Engineering"}
  },
  "Civil Engineering PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Structural Engineer", "Geotechnical Engineer", "Transportation Engineer", "Environmental Engineer", "Water Resources Engineer"],
    "showIf": {"Engineering PhD Sub Domain": "Civil Engineering"}
  },
  "Computer Engineering PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Computer Architect", "Embedded Systems Engineer", "VLSI Designer", "Network Engineer", "Cybersecurity Researcher"],
    "showIf": {"Engineering PhD Sub Domain": "Computer Engineering"}
  },
  "Data Science phD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Data Scientist", "Machine Learning Engineer", "Business Intelligence Analyst", "Data Architect", "Quantitative Analyst"],
    "showIf": {"STEM PhD Sub Domain": "Data Science"}
  },
  "Engineering phD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Mechanical Engineer", "Electrical Engineer", "Civil Engineer", "Chemical Engineer", "Aerospace Engineer"],
    "showIf": {"STEM PhD Sub Domain": "Engineering"}
  },
  "Mathematics phD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Mathematician", "Statistician", "Operations Research Analyst", "Actuary", "Cryptographer"],
    "showIf": {"STEM PhD Sub Domain": "Mathematics"}
  },
  "Biotechnology phD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Biomedical Engineer", "Biochemist", "Bioinformatics Specialist", "Clinical Research Associate", "Biotechnology Product Developer"],
    "showIf": {"STEM PhD Sub Domain": "Biotechnology"}
  },
  "Computer Science phD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Software Developer", "Systems Analyst", "Database Administrator", "IT Consultant", "Artificial Intelligence Specialist"],
    "showIf": {"STEM PhD Sub Domain": "Computer Science"}
  },
  "MBA phD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Business Development Manager", "Management Consultant", "Operations Manager", "Financial Manager", "Marketing Director"],
    "showIf": {"Business PhD Sub Domain": "Master of Business Administration (MBA)"}
  },
  "Human Resource Management phD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["HR Manager", "Talent Acquisition Specialist", "Compensation and Benefits Manager", "Training and Development Manager", "Employee Relations Specialist"],
    "showIf": {"Business PhD Sub Domain": "Human Resource Management"}
  },
  "International Business phD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["International Business Development Manager", "Global Marketing Manager", "International Trade Specialist", "Foreign Market Analyst", "Cross-Cultural Business Consultant"],
    "showIf": {"Business PhD Sub Domain": "International Business"}
  },
  "Machine Learning Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Machine Learning Engineer", "AI Researcher", "Data Scientist", "Natural Language Processing Specialist", "Computer Vision Engineer"],
    "showIf": {"Data Science Sub Domain": "Machine Learning"}
  },
  "Statistical Analysis Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Statistician", "Data Analyst", "Biostatistician", "Market Research Analyst", "Quality Control Analyst"],
    "showIf": {"Data Science Sub Domain": "Statistical Analysis"}
  },
  "Data Visualization Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Data Visualization Specialist", "Information Designer", "Business Intelligence Analyst", "Data Journalist", "UX/UI Designer for Data"],
    "showIf": {"Data Science Sub Domain": "Data Visualization"}
  },
  "Big Data Analytics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Big Data Engineer", "Data Architect", "Hadoop Developer", "NoSQL Database Administrator", "Data Integration Specialist"],
    "showIf": {"Data Science Sub Domain": "Big Data Analytics"}
  },
  "Predictive Modeling Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Predictive Modeler", "Quantitative Analyst", "Risk Analyst", "Financial Modeler", "Operations Research Analyst"],
    "showIf": {"Data Science Sub Domain": "Predictive Modeling"}
  },
  "Natural Language Processing Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["NLP Engineer", "Computational Linguist", "Speech Recognition Engineer", "Text Analytics Specialist", "Chatbot Developer"],
    "showIf": {"Data Science Sub Domain": "Natural Language Processing"}
  },
  "Deep Learning Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Deep Learning Engineer", "Neural Network Architect", "AI Research Scientist", "Computer Vision Engineer", "Speech Recognition Specialist"],
    "showIf": {"AIML Sub Domain": "Deep Learning"}
  },
  "Computer Vision Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Computer Vision Engineer", "Image Processing Specialist", "Robotics Vision Engineer", "Autonomous Vehicle Vision Specialist", "Medical Imaging AI Developer"],
    "showIf": {"AIML Sub Domain": "Computer Vision"}
  },
  "Reinforcement Learning Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Reinforcement Learning Engineer", "Game AI Developer", "Robotics AI Specialist", "Autonomous Systems Engineer", "Decision Support Systems Developer"],
    "showIf": {"AIML Sub Domain": "Reinforcement Learning"}
  },
  "Neural Networks Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Neural Network Engineer", "AI Model Optimizer", "Neuromorphic Computing Specialist", "Pattern Recognition Engineer", "AI Hardware Designer"],
    "showIf": {"AIML Sub Domain": "Neural Networks"}
  },
  "Expert Systems Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Knowledge Engineer", "Expert System Developer", "AI Consultant", "Decision Support Systems Specialist", "Rule-Based Systems Developer"],
    "showIf": {"AIML Sub Domain": "Expert Systems"}
  },
  "Genetic Algorithms Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Evolutionary Computation Specialist", "Optimization Engineer", "Genetic Programming Developer", "Bioinformatics AI Specialist", "Swarm Intelligence Researcher"],
    "showIf": {"AIML Sub Domain": "Genetic Algorithms"}
  },
  "Embedded Systems Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Embedded Systems Engineer", "Firmware Developer", "IoT Device Programmer", "RTOS Specialist", "Microcontroller Programmer"],
    "showIf": {"IOT Sub Domain": "Embedded Systems"}
  },
  "Sensor Networks Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Sensor Network Engineer", "Wireless Sensor Specialist", "IoT Systems Architect", "Environmental Monitoring Specialist", "Smart City Technology Engineer"],
    "showIf": {"IOT Sub Domain": "Sensor Networks"}
  },
  "Edge Computing Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Edge Computing Engineer", "Fog Computing Specialist", "Distributed Systems Developer", "IoT Edge Developer", "Mobile Edge Computing Specialist"],
    "showIf": {"IOT Sub Domain": "Edge Computing"}
  },
  "IoT Security Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["IoT Security Specialist", "Embedded Systems Security Engineer", "IoT Penetration Tester", "IoT Privacy Consultant", "IoT Cryptography Specialist"],
    "showIf": {"IOT Sub Domain": "IoT Security"}
  },
  "IoT Protocols Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["IoT Protocol Specialist", "MQTT Developer", "CoAP Specialist", "Zigbee Developer", "LoRaWAN Specialist"],
    "showIf": {"IOT Sub Domain": "IoT Protocols"}
  },
  "Smart Home/City Technologies Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Smart Home Systems Engineer", "Smart City Planner", "IoT Solutions Architect", "Connected Device Developer", "Smart Building Systems Specialist"],
    "showIf": {"IOT Sub Domain": "Smart Home/City Technologies"}
  },
  "Network Security Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Network Security Engineer", "Firewall Administrator", "VPN Specialist", "Intrusion Detection Specialist", "Network Security Architect"],
    "showIf": {"Cyber Security Sub Domain": "Network Security"}
  },
  "Application Security Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Application Security Engineer", "Secure Code Reviewer", "Web Application Security Specialist", "Mobile App Security Expert", "DevSecOps Engineer"],
    "showIf": {"Cyber Security Sub Domain": "Application Security"}
  },
  "Information Security Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Information Security Analyst", "IT Auditor", "Security Compliance Specialist", "Data Protection Officer", "Risk Management Specialist"],
    "showIf": {"Cyber Security Sub Domain": "Information Security"}
  },
  "Cryptography Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Cryptographer", "Encryption Specialist", "Crypto Systems Developer", "Blockchain Security","Specialist", "Quantum Cryptography Researcher"],
    "showIf": {"Cyber Security Sub Domain": "Cryptography"}
  },
  "Ethical Hacking Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Ethical Hacker", "Penetration Tester", "Red Team Specialist", "Vulnerability Assessor", "Security Researcher"],
    "showIf": {"Cyber Security Sub Domain": "Ethical Hacking"}
  },
  "Incident Response and Forensics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Incident Response Specialist", "Digital Forensics Analyst", "Malware Analyst", "Cyber Threat Hunter", "Security Operations Center (SOC) Analyst"],
    "showIf": {"Cyber Security Sub Domain": "Incident Response and Forensics"}
  },
  "Infrastructure as a Service (IaaS) Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Cloud Infrastructure Engineer", "IaaS Architect", "Cloud Operations Specialist", "Virtualization Engineer", "Cloud Security Specialist"],
    "showIf": {"Cloud Computing Sub Domain": "Infrastructure as a Service (IaaS)"}
  },
  "Platform as a Service (PaaS) Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["PaaS Developer", "Cloud Application Architect", "PaaS Administrator", "Cloud Integration Specialist", "PaaS Security Engineer"],
    "showIf": {"Cloud Computing Sub Domain": "Platform as a Service (PaaS)"}
  },
  "Software as a Service (SaaS) Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["SaaS Product Manager", "SaaS Developer", "SaaS Architect", "SaaS Implementation Specialist", "SaaS Customer Success Manager"],
    "showIf": {"Cloud Computing Sub Domain": "Software as a Service (SaaS)"}
  },
  "Cloud Architecture Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Cloud Solutions Architect", "Enterprise Architect", "Cloud Network Architect", "Cloud Security Architect", "Multi-Cloud Strategist"],
    "showIf": {"Cloud Computing Sub Domain": "Cloud Architecture"}
  },
  "Serverless Computing Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Serverless Developer", "Serverless Architect", "Function-as-a-Service (FaaS) Specialist", "Event-Driven Computing Engineer", "Serverless DevOps Engineer"],
    "showIf": {"Cloud Computing Sub Domain": "Serverless Computing"}
  },
  "Multi-cloud and Hybrid Cloud Solutions Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Multi-Cloud Engineer", "Hybrid Cloud Architect", "Cloud Integration Specialist", "Cloud Migration Engineer", "Cross-Platform Cloud Developer"],
    "showIf": {"Cloud Computing Sub Domain": "Multi-cloud and Hybrid Cloud Solutions"}
  },
  "Front-end Development Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Front-end Developer", "UI Developer", "JavaScript Developer", "Web Designer", "Mobile Web Developer"],
    "showIf": {"Full Stack Development Sub Domain": "Front-end Development"}
  },
  "Back-end Development Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Back-end Developer", "Server-Side Developer", "API Developer", "Database Developer", "Microservices Developer"],
    "showIf": {"Full Stack Development Sub Domain": "Back-end Development"}
  },
  "Database Management Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Database Administrator", "Database Developer", "Data Architect", "Database Security Specialist", "NoSQL Specialist"],
    "showIf": {"Full Stack Development Sub Domain": "Database Management"}
  },
  "API Development Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["API Developer", "RESTful API Specialist", "GraphQL Developer", "API Architect", "API Integration Specialist"],
    "showIf": {"Full Stack Development Sub Domain": "API Development"}
  },
  "Web Security Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Web Security Specialist", "Application Security Engineer", "Secure Coding Expert", "Web Penetration Tester", "Security Auditor"],
    "showIf": {"Full Stack Development Sub Domain": "Web Security"}
  },
  "User Experience (UX) Design Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["UX Designer", "Interaction Designer", "Information Architect", "Usability Specialist", "UX Researcher"],
    "showIf": {"Full Stack Development Sub Domain": "User Experience (UX) Design"}
  },
  "Continuous Integration/Continuous Deployment (CI/CD) Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["CI/CD Engineer", "Build and Release Engineer", "Automation Specialist", "DevOps Pipeline Engineer", "Configuration Manager"],
    "showIf": {"DevOps Sub Domain": "Continuous Integration/Continuous Deployment (CI/CD)"}
  },
  "Infrastructure as Code Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Infrastructure as Code Specialist", "Cloud Automation Engineer", "Terraform Developer", "Ansible Specialist", "Cloudformation Expert"],
    "showIf": {"DevOps Sub Domain": "Infrastructure as Code"}
  },
  "Configuration Management Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Configuration Management Specialist", "Puppet Developer", "Chef Administrator", "Salt Stack Engineer", "Ansible Architect"],
    "showIf": {"DevOps Sub Domain": "Configuration Management"}
  },
  "Containerization Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Container Specialist", "Docker Engineer", "Kubernetes Administrator", "Container Security Expert", "Microservices Architect"],
    "showIf": {"DevOps Sub Domain": "Containerization"}
  },
  "Orchestration Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Orchestration Engineer", "Kubernetes Specialist", "Docker Swarm Expert", "Mesos Administrator", "Cloud Orchestration Architect"],
    "showIf": {"DevOps Sub Domain": "Orchestration"}
  },
  "Monitoring and Logging Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Monitoring Specialist", "Log Analysis Expert", "Site Reliability Engineer", "Performance Monitoring Engineer", "Observability Specialist"],
    "showIf": {"DevOps Sub Domain": "Monitoring and Logging"}
  },
  "Distributed Ledger Technology Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Blockchain Developer", "Distributed Systems Engineer", "Consensus Algorithm Specialist", "Blockchain Architect", "DLT Security Expert"],
    "showIf": {"Blockchain Sub Domain": "Distributed Ledger Technology"}
  },
  "Smart Contracts Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Smart Contract Developer", "Solidity Programmer", "Ethereum Developer", "Smart Contract Auditor", "Blockchain Legal Consultant"],
    "showIf": {"Blockchain Sub Domain": "Smart Contracts"}
  },
  "Cryptocurrency Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Cryptocurrency Developer", "Crypto Wallet Engineer", "Crypto Exchange Developer", "Tokenization Specialist", "Crypto Economics Analyst"],
    "showIf": {"Blockchain Sub Domain": "Cryptocurrency"}
  },
  "Decentralized Finance (DeFi) Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["DeFi Developer", "DeFi Product Manager", "Liquidity Pool Engineer", "Yield Farming Specialist", "DeFi Security Analyst"],
    "showIf": {"Blockchain Sub Domain": "Decentralized Finance (DeFi)"}
  },
  "Consensus Mechanisms Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Consensus Algorithm Developer", "Proof-of-Stake Specialist", "Blockchain Protocol Engineer", "Distributed Systems Researcher", "Byzantine Fault Tolerance Expert"],
    "showIf": {"Blockchain Sub Domain": "Consensus Mechanisms"}
  },
  "Blockchain Security Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Blockchain Security Specialist", "Crypto Wallet Security Expert", "Smart Contract Auditor", "Blockchain Penetration Tester", "Crypto Forensics Analyst"],
    "showIf": {"Blockchain Sub Domain": "Blockchain Security"}
  },
  "Quantum Algorithms Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Quantum Algorithm Developer", "Quantum Complexity Theorist", "Quantum Machine Learning Researcher", "Quantum Optimization Specialist", "Quantum Cryptography Expert"],
    "showIf": {"Quantum Computing Sub Domain": "Quantum Algorithms"}
  },
  "Quantum Error Correction Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Quantum Error Correction Specialist", "Fault-Tolerant Quantum Computing Researcher", "Quantum Information Theorist", "Quantum Stabilizer Code Developer", "Topological Quantum Computing Expert"],
    "showIf": {"Quantum Computing Sub Domain": "Quantum Error Correction"}
  },
  "Quantum Cryptography Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Quantum Cryptographer", "Post-Quantum Cryptography Specialist", "Quantum Key Distribution Expert", "Quantum Random Number Generator Developer", "Quantum Network Security Analyst"],
    "showIf": {"Quantum Computing Sub Domain": "Quantum Cryptography"}
  },
  "Quantum Simulation Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Quantum Simulator Developer", "Quantum Chemistry Researcher", "Quantum Materials Scientist", "Quantum Many-Body Systems Specialist", "Quantum Biology Researcher"],
    "showIf": {"Quantum Computing Sub Domain": "Quantum Simulation"}
  },
  "Quantum Hardware Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Quantum Hardware Engineer", "Superconducting Qubit Specialist", "Ion Trap Quantum Computer Developer", "Quantum Optics Engineer", "Topological Qubit Researcher"],
    "showIf": {"Quantum Computing Sub Domain": "Quantum Hardware"}
  },
  "Quantum Software Development Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Quantum Software Developer", "Quantum Circuit Designer", "Quantum Programming Language Developer", "Quantum Software Architect", "Quantum Development Kit Specialist"],
    "showIf": {"Quantum Computing Sub Domain": "Quantum Software Development"}
  },
  "Robot Design and Kinematics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Robot Designer", "Kinematic Engineer", "Mechanical Systems Engineer", "CAD Specialist for Robotics", "Robot Prototype Developer"],
    "showIf": {"Robotics Sub Domain": "Robot Design and Kinematics"}
  },
  "Computer Vision for Robotics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Robotics Vision Engineer", "3D Perception Specialist", "Visual SLAM Developer", "Object Recognition for Robotics Expert", "Robotic Scene Understanding Researcher"],
    "showIf": {"Robotics Sub Domain": "Computer Vision for Robotics"}
  },
  "Robot Operating System (ROS) Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["ROS Developer", "ROS Integration Specialist", "ROS2 Migration Expert", "ROS-Industrial Developer", "ROS Navigation Engineer"],
    "showIf": {"Robotics Sub Domain": "Robot Operating System (ROS)"}
  },
  "Human-Robot Interaction Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Human-Robot Interaction Specialist", "Social Robotics Researcher", "Collaborative Robot (Cobot) Programmer", "Robot User Interface Designer", "Robot Behavior Designer"],
    "showIf": {"Robotics Sub Domain": "Human-Robot Interaction"}
  },
  "Autonomous Navigation Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Autonomous Navigation Engineer", "Path Planning Specialist", "Simultaneous Localization and Mapping (SLAM) Developer", "Robotic Control Systems Engineer", "Sensor Fusion Specialist"],
    "showIf": {"Robotics Sub Domain": "Autonomous Navigation"}
  },
  "Soft Robotics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Soft Robotics Engineer", "Biomimetic Robot Designer", "Soft Materials Specialist", "Compliant Mechanism Designer", "Soft Actuator Developer"],
    "showIf": {"Robotics Sub Domain": "Soft Robotics"}
  },
  "Learning Mode": {
                "type": "radio",
                "label": "Please select your Learning Mode",
                "options": ["Online","Offline"],
            },
    "Skills":{
                "type": "text_input",
                "label": "Please mention your skills",
                "value": ""         
                },
    "Certifications":{
                "type": "text_input",
                "label": "Please mention your certifications Related to your domain",
                "value": ""
            },
    "Academic Performance":{
                "type": "text_input",
                "label": "Please mention your Academic percentage",
                "value": ""
            },
"Years of Experience": {
    "type": "radio",
    "label": "How many years of experience do you have in your chosen field?",
    "options": ["0-2 years", "3-5 years", "6-10 years", "11-15 years", "16+ years"]
  },
  "Proficiency Level": {
    "type": "radio",
    "label": "How would you rate your proficiency level in your chosen subdomain?",
    "options": ["Beginner", "Intermediate", "Advanced", "Expert"]
  },
  "Preferred Work Environment": {
    "type": "radio",
    "label": "What type of work environment do you prefer?",
    "options": ["Corporate office", "Startup", "Remote work", "Freelance/Consulting", "Academic/Research", "Government/Public sector"]
  },
  "Project Experience": {
    "type": "multiselect",
    "label": "What types of projects have you worked on? (Select all that apply)",
    "options": ["Small-scale projects", "Large enterprise projects", "Research projects", "Open-source contributions", "Personal projects", "Cross-functional team projects"]
  },
  "Soft Skills": {
    "type": "multiselect",
    "label": "Which soft skills do you consider your strengths? (Select up to 3)",
    "options": ["Communication", "Teamwork", "Problem-solving", "Adaptability", "Leadership", "Time management", "Creativity"]
  },
  "Career Goals": {
    "type": "radio",
    "label": "What are your primary career goals for the next 5 years?",
    "options": ["Advance to a senior position", "Transition to management", "Specialize in a niche area", "Start own business/freelancing", "Contribute to cutting-edge research", "Teach or mentor others in the field"]
  },
  "Learning Preferences": {
    "type": "multiselect",
    "label": "How do you prefer to learn new skills? (Select all that apply)",
    "options": ["Online courses", "In-person workshops", "Books and documentation", "Hands-on projects", "Peer learning/study groups", "Conferences and seminars"]
  },
  "Industry Interests": {
    "type": "multiselect",
    "label": "Which industries are you most interested in working in? (Select up to 3)",
    "options": ["Technology", "Healthcare", "Finance", "Education", "Entertainment", "Retail", "Manufacturing", "Energy", "Non-profit"]
  },
  "Challenges": {
    "type": "text_area",
    "label": "Describe a significant challenge you've faced in your field and how you overcame it:"
  },
  "Tools and Technologies": {
    "type": "text_area",
    "label": "List the primary tools, technologies, or programming languages you're proficient in:"
  },
  "Publication Experience": {
    "type": "radio",
    "label": "Do you have experience with academic or industry publications?",
    "options": ["Yes, as a primary author", "Yes, as a co-author", "Yes, in non-peer reviewed publications", "No publication experience"]
  },
  "Teamwork Preference": {
    "type": "radio",
    "label": "What team size do you prefer working in?",
    "options": ["Solo work", "Small team (2-5 people)", "Medium team (6-15 people)", "Large team (16+ people)"]
  },
  "Professional Memberships": {
    "type": "multiselect",
    "label": "Are you a member of any professional organizations? (Select all that apply)",
    "options": ["IEEE", "ACM", "Industry-specific organization", "Local professional group", "None"]
  },
  #"current_field": {
            #     "type": "text_input",
            #     "label": "What is your current field of work? (If applicable)",
            #     "value": "",
            #     "showIf": {"experience_years": {"$gt": 0}}
            # }
},
         "phase_instructions": "Please provide your basic details.",
         "user_prompt": [
             
             #bachelor's,data science, Machine Learning Roles
             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Machine Learning"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Onfline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Machine Learning Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
                 },

             #bachelor's,data science, Machine Learning Roles
            {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Machine Learning"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Machine Learning Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
                 },

             

             #bachelor's,data science, Statistical Analysis Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Statistical Analysis"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Statistical Analysis Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Statistical Analysis"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Statistical Analysis Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's, datascience, Data Visualization Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Data Visualization"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Data Visualization Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Data Visualization"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Data Visualization Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's, datascience, Big Data Analytics Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Big Data Analytics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Big Data Analytics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Big Data Analytics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Big Data Analytics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's, datascience, Predictive Modeling Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Predictive Modeling"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Predictive Modeling Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Predictive Modeling"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Predictive Modeling Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's, datascience,Natural Language Processing Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Natural Language Processing"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Natural Language Processing Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Natural Language Processing"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Natural Language Processing Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's , AIML, deep LEARNING roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"AIML Sub Domain":"Deep Learning"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Deep Learning Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"AIML Sub Domain":"Deep Learning"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Deep Learning Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's , AIML, computer vision roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"AIML Sub Domain":"Computer Vision"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Computer Vision Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"AIML Sub Domain":"Computer Vision"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Computer Vision Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's , AIML, Reinforcement Learning roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"AIML Sub Domain":"Reinforcement Learning"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Reinforcement Learning Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"AIML Sub Domain":"Reinforcement Learning"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Reinforcement Learning Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's , AIML, Neural Networks roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"AIML Sub Domain":"Neural Networks"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Neural Networks Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"AIML Sub Domain":"Neural Networks"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Neural Networks Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's , AIML, Expert Systems roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"AIML Sub Domain":"Expert Systems"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Expert Systems Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"AIML Sub Domain":"Expert Systems"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Expert Systems Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},
             # bachelor's , AIML, Genetic Algorithms roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"AIML Sub Domain":"Genetic Algorithms"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Genetic Algorithms Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"AIML Sub Domain":"Genetic Algorithms"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Genetic Algorithms Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # bachelor's , IOT, Embedded Systems roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"Embedded Systems"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Embedded Systems Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"Embedded Systems"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Embedded Systems Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # bachelor's , IOT, Sensor Networks Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"Sensor Networks"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Sensor Networks Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"Sensor Networks"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Sensor Networks Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # bachelor's , IOT, Edge Computing Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"Edge Computing"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Edge Computing Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"Edge Computing"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Edge Computing Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # bachelor's , IOT, IoT Security Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"IoT Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {IoT Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"IoT Security"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {IoT Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # bachelor's , IOT, Sensor Networks Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"Sensor Networks"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Sensor Networks Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"Sensor Networks"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Sensor Networks Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's , IOT, IoT Protocols Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"IoT Protocols"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {IoT Protocols Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"IoT Protocols"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {IoT Protocols Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # bachelor's , IOT, Smart Home/City Technologies Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"Smart Home/City Technologies"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Smart Home/City Technologies Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"Smart Home/City Technologies"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Smart Home/City Technologies Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             
             
             # bachelor's ,Cyber Security , Network Security Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cyber Security Sub Domain":"Network Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Network Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cyber Security Sub Domain":"Network Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Network Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cyber Security , Application Security Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cyber Security Sub Domain":"Application Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Application Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cyber Security Sub Domain":"Application Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Application Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cyber Security ,Information Security Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cyber Security Sub Domain":"Information Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Information Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cyber Security Sub Domain":"Information Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Information Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cyber Security ,Cryptography Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cyber Security Sub Domain":"Cryptography"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Cryptography Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cyber Security Sub Domain":"Cryptography"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Cryptography Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cyber Security ,Ethical Hacking Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cyber Security Sub Domain":"Ethical Hacking"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Ethical Hacking Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cyber Security Sub Domain":"Ethical Hacking"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Ethical Hacking Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cyber Security ,Incident Response and Forensics Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cyber Security Sub Domain":"Incident Response and Forensics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Incident Response and Forensics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cyber Security Sub Domain":"Incident Response and Forensics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Incident Response and Forensics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cloud Computing ,Infrastructure as a Service (IaaS) Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cloud Computing Sub Domain":"Infrastructure as a Service (IaaS)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Infrastructure as a Service (IaaS) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cloud Computing Sub Domain":"Infrastructure as a Service (IaaS)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Infrastructure as a Service (IaaS) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cloud Computing ,Platform as a Service (PaaS) Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cloud Computing Sub Domain":"Platform as a Service (PaaS)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Platform as a Service (PaaS) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cloud Computing Sub Domain":"Platform as a Service (PaaS)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Platform as a Service (PaaS) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cloud Computing ,Software as a Service (SaaS) Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cloud Computing Sub Domain":"Software as a Service (SaaS)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Software as a Service (SaaS) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cloud Computing Sub Domain":"Software as a Service (SaaS)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Software as a Service (SaaS) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cloud Computing ,Cloud Architecture Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cloud Computing Sub Domain":"Cloud Architecture"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Cloud Architecture Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cloud Computing Sub Domain":"Cloud Architecture"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Cloud Architecture Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cloud Computing ,Serverless Computing Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cloud Computing Sub Domain":"Serverless Computing"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Serverless Computing Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cloud Computing Sub Domain":"Serverless Computing"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Serverless Computing Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Cloud Computing ,Multi-cloud and Hybrid Cloud Solutions Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Cloud Computing Sub Domain":"Multi-cloud and Hybrid Cloud Solutions"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Multi-cloud and Hybrid Cloud Solutions Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Cloud Computing Sub Domain":"Multi-cloud and Hybrid Cloud Solutions"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Multi-cloud and Hybrid Cloud Solutions Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Full Stack Development,Front-end Development Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Full Stack Development Sub Domain":"Front-end Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Front-end Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Full Stack Development Sub Domain":"Front-end Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Front-end Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Full Stack Development,Back-end Development Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Full Stack Development Sub Domain":"Back-end Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Back-end Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Full Stack Development Sub Domain":"Back-end Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Back-end Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Full Stack Development,Database Management Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Full Stack Development Sub Domain":"Database Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Database Management Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Full Stack Development Sub Domain":"Database Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Database Management Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Full Stack Development,API Development Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Full Stack Development Sub Domain":"API Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {API Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Full Stack Development Sub Domain":"API Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {API Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Full Stack Development,Web Security Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Full Stack Development Sub Domain":"Web Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Web Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Full Stack Development Sub Domain":"Web Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Web Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
            # bachelor's ,Full Stack Development,User Experience (UX) Design Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Full Stack Development Sub Domain":"User Experience (UX) Design"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {User Experience (UX) Design Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Full Stack Development Sub Domain":"User Experience (UX) Design"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {User Experience (UX) Design Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,DevOps,Continuous Integration/Continuous Deployment (CI/CD) Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"DevOps Sub Domain":"Continuous Integration/Continuous Deployment (CI/CD)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Continuous Integration/Continuous Deployment (CI/CD) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"DevOps Sub Domain":"Continuous Integration/Continuous Deployment (CI/CD)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Continuous Integration/Continuous Deployment (CI/CD) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,DevOps,Infrastructure as Code Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"DevOps Sub Domain":"Infrastructure as Code"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Infrastructure as Code Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"DevOps Sub Domain":"Infrastructure as Code"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Infrastructure as Code Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,DevOps,Configuration Management Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"DevOps Sub Domain":"Configuration Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Configuration Management Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"DevOps Sub Domain":"Configuration Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Configuration Management Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,DevOps,Containerization Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"DevOps Sub Domain":"Containerization"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Containerization Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"DevOps Sub Domain":"Containerization"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Containerization Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,DevOps,Orchestration Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"DevOps Sub Domain":"Orchestration"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Orchestration Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"DevOps Sub Domain":"Orchestration"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Orchestration Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,DevOps,Monitoring and Logging Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"DevOps Sub Domain":"Monitoring and Logging"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Monitoring and Logging Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"DevOps Sub Domain":"Monitoring and Logging"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Monitoring and Logging Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Blockchain,Distributed Ledger Technology Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Blockchain Sub Domain":"Distributed Ledger Technology"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Distributed Ledger Technology Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Blockchain Sub Domain":"Distributed Ledger Technology"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Distributed Ledger Technology Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Blockchain,Smart Contracts Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Blockchain Sub Domain":"Smart Contracts"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Smart Contracts Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Blockchain Sub Domain":"Smart Contracts"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Smart Contracts Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Blockchain,Cryptocurrency Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Blockchain Sub Domain":"Cryptocurrency"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Cryptocurrency Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Blockchain Sub Domain":"Cryptocurrency"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Cryptocurrency Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Blockchain,Decentralized Finance (DeFi) Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Blockchain Sub Domain":"Decentralized Finance (DeFi)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Decentralized Finance (DeFi) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Blockchain Sub Domain":"Decentralized Finance (DeFi)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Decentralized Finance (DeFi) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Blockchain,Consensus Mechanisms Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Blockchain Sub Domain":"Consensus Mechanisms"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Consensus Mechanisms Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Blockchain Sub Domain":"Consensus Mechanisms"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Consensus Mechanisms Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Blockchain,Blockchain Security Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Blockchain Sub Domain":"Blockchain Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Blockchain Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Blockchain Sub Domain":"Blockchain Security"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Blockchain Security Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Quantum Computing,Quantum Algorithms Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Quantum Computing Sub Domain":"Quantum Algorithms"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Algorithms Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Quantum Computing Sub Domain":"Quantum Algorithms"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Algorithms Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Quantum Computing,Quantum Error Correction Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Quantum Computing Sub Domain":"Quantum Error Correction"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Error Correction Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Quantum Computing Sub Domain":"Quantum Error Correction"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Error Correction Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Quantum Computing,Quantum Cryptography Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Quantum Computing Sub Domain":"Quantum Cryptography"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Cryptography Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Quantum Computing Sub Domain":"Quantum Cryptography"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Cryptography Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Quantum Computing,Quantum Simulation Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Quantum Computing Sub Domain":"Quantum Simulation"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Simulation Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Quantum Computing Sub Domain":"Quantum Simulation"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Simulation Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Quantum Computing,Quantum Hardware Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Quantum Computing Sub Domain":"Quantum Hardware"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Hardware Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Quantum Computing Sub Domain":"Quantum Hardware"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Hardware Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Quantum Computing,Quantum Software Development Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Quantum Computing Sub Domain":"Quantum Software Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Software Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Quantum Computing Sub Domain":"Quantum Software Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Quantum Software Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Robotics,Robot Design and Kinematics Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Robotics Sub Domain":"Robot Design and Kinematics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Robot Design and Kinematics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Robotics Sub Domain":"Robot Design and Kinematics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Robot Design and Kinematics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Robotics,Computer Vision for Robotics Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Robotics Sub Domain":"Computer Vision for Robotics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Computer Vision for Robotics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Robotics Sub Domain":"Computer Vision for Robotics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Computer Vision for Robotics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Robotics,Robot Operating System (ROS) Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Robotics Sub Domain":"Robot Operating System (ROS)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Robot Operating System (ROS) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Robotics Sub Domain":"Robot Operating System (ROS)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Robot Operating System (ROS) Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Robotics,Human-Robot Interaction Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Robotics Sub Domain":"Human-Robot Interaction"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Human-Robot Interaction Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Robotics Sub Domain":"Human-Robot Interaction"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Human-Robot Interaction Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Robotics,Autonomous Navigation Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Robotics Sub Domain":"Autonomous Navigation"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Autonomous Navigation Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Robotics Sub Domain":"Autonomous Navigation"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Autonomous Navigation Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # bachelor's ,Robotics,Soft Robotics Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Robotics Sub Domain":"Soft Robotics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Soft Robotics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Robotics Sub Domain":"Soft Robotics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Soft Robotics Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },


             # Associate's ,Business and Management,Accounting Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Business and Management Sub Domain":"Accounting"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Accounting Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Business and Management Sub Domain":"Accounting"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Accounting Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},

             # Associate's ,Business and Management,Business Administration Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Business and Management Sub Domain":"Business Administration"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Business Administration Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Business and Management Sub Domain":"Business Administration"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Business Administration Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             # Associate's ,Business and Management,Marketing Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Business and Management Sub Domain":"Marketing"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Marketing Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Business and Management Sub Domain":"Marketing"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Marketing Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             # Associate's ,Business and Management,Finance Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Business and Management Sub Domain":"Finance"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Finance Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Business and Management Sub Domain":"Finance"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Finance Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             # Associate's ,Business and Management,Hospitality Management Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Business and Management Sub Domain":"Hospitality Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Hospitality Management Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Business and Management Sub Domain":"Hospitality Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Hospitality Management Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},



             # Associate's ,Information Technology,Computer Science Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Information Technology Sub Domain":"Computer Science"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Computer Science Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Information Technology Sub Domain":"Computer Science"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with an academic percentage of {Academic Performance}% and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Computer Science Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to know my capability level."
},


             # Associate's ,Information Technology,Network Administration Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Information Technology Sub Domain":"Network Administration"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Network Administration Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Information Technology Sub Domain":"Network Administration"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Network Administration Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # Associate's ,Information Technology,Web Development Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Information Technology Sub Domain":"Web Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Web Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience},  My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Information Technology Sub Domain":"Web Development"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Web Development Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # Associate's ,Information Technology,Cybersecurity Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Information Technology Sub Domain":"Cybersecurity"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Cybersecurity Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Information Technology Sub Domain":"Cybersecurity"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Cybersecurity Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # Associate's ,Information Technology,Database Management Roles

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Information Technology Sub Domain":"Database Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Database Management Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Information Technology Sub Domain":"Database Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Database Management Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             

             # masters , STEM,Computer Science roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"STEM Master's Sub Domain":"Computer Science"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Computer Science Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"STEM Master's Sub Domain":"Computer Science"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Computer Science Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # masters , STEM,Data Science roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"STEM Master's Sub Domain":"Data Science"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Data Science Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"STEM Master's Sub Domain":"Data Science"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Data Science Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # masters , STEM,Engineering roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"STEM Master's Sub Domain":"Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"STEM Master's Sub Domain":"Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # masters , STEM,Mathematics roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"STEM Master's Sub Domain":"Mathematics"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Mathematics Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"STEM Master's Sub Domain":"Mathematics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Mathematics Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # masters , STEM,Biotechnology roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"STEM Master's Sub Domain":"Biotechnology"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Biotechnology Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"STEM Master's Sub Domain":"Biotechnology"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Biotechnology Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # masters ,Business,MBA roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Business Master's Sub Domain":"Master of Business Administration (MBA)"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {MBA Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Business Master's Sub Domain":"Master of Business Administration (MBA)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {MBA Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # masters ,Business,Human Resource Management roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Business Master's Sub Domain":"Human Resource Management"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Human Resource Management Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Business Master's Sub Domain":"Human Resource Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Human Resource Management Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # masters ,Business,International Business roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Business Master's Sub Domain":"International Business"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {International Business Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Business Master's Sub Domain":"International Business"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {International Business Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # masters ,Engineering ,Electrical Engineering Roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Engineering Master's Sub Domain":"Electrical Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Electrical Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Engineering Master's Sub Domain":"Electrical Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Electrical Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # masters ,Engineering ,Mechanical Engineering Roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Engineering Master's Sub Domain":"Mechanical Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Mechanical Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Engineering Master's Sub Domain":"Mechanical Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Mechanical Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # masters ,Engineering ,Chemical Engineering Roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Engineering Master's Sub Domain":"Chemical Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Chemical Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Engineering Master's Sub Domain":"Chemical Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Chemical Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # masters ,Engineering ,Civil Engineering Roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Engineering Master's Sub Domain":"Civil Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Civil Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Engineering Master's Sub Domain":"Civil Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Civil Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # masters ,Engineering ,Computer Engineering Roles
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Engineering Master's Sub Domain":"Computer Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Computer Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Engineering Master's Sub Domain":"Computer Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Computer Engineering Master's Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },


             # PhD ,Engineering ,Electrical Engineering PhD Roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Engineering PhD Sub Domain":"Electrical Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Electrical Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Engineering PhD Sub Domain":"Electrical Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Electrical Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # PhD ,Engineering ,Mechanical Engineering PhD Roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Engineering PhD Sub Domain":"Mechanical Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Mechanical Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Engineering PhD Sub Domain":"Mechanical Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Mechanical Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # PhD ,Engineering ,Chemical Engineering PhD Roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Engineering PhD Sub Domain":"Chemical Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Chemical Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Engineering PhD Sub Domain":"Chemical Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Chemical Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # PhD ,Engineering ,Civil Engineering PhD Roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Engineering PhD Sub Domain":"Civil Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Civil Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Engineering PhD Sub Domain":"Civil Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Civil Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # PhD ,Engineering ,Computer Engineering PhD Roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Engineering PhD Sub Domain":"Computer Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Computer Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Engineering PhD Sub Domain":"Computer Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Computer Engineering PhD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # phD , STEM,Computer Science roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"STEM PhD Sub Domain":"Computer Science"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Computer Science phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"STEM PhD Sub Domain":"Computer Science"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Computer Science phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # phD , STEM,Data Science roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"STEM PhD Sub Domain":"Data Science"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Data Science phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"STEM PhD Sub Domain":"Data Science"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Data Science phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             # phD , STEM,Engineering roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"STEM PhD Sub Domain":"Engineering"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Engineering phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"STEM PhD Sub Domain":"Engineering"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Engineering phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # phD , STEM,Mathematics roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"STEM PhD Sub Domain":"Mathematics"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Mathematics phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"STEM PhD Sub Domain":"Mathematics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Mathematics phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # phD , STEM,Biotechnology roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"STEM PhD Sub Domain":"Biotechnology"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Biotechnology phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"STEM PhD Sub Domain":"Biotechnology"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Biotechnology phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # phD ,Business,MBA roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Business PhD Sub Domain":"Master of Business Administration (MBA)"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {MBA phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Business PhD Sub Domain":"Master of Business Administration (MBA)"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {MBA phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # phD ,Business,Human Resource Management roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Business PhD Sub Domain":"Human Resource Management"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Human Resource Management phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Business PhD Sub Domain":"Human Resource Management"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Human Resource Management phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
             # phD ,Business,International Business roles
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Business PhD Sub Domain":"International Business"}]},
                 "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {International Business phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Business PhD Sub Domain":"International Business"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {International Business phD Roles}. I have {Years of Experience} years of experience in my chosen field, would rate my proficiency as {Proficiency Level}, and prefer to work in a {Preferred Work Environment}. I have worked on {Project Experience}, My soft skills include {Soft Skills}. My primary career goal in the next 5 years is {Career Goals}, and I prefer to learn new skills through {Learning Preferences}. I'm interested in working in the {Industry Interests} industry and have faced challenges such as {Challenges}. I have experience using tools and technologies like {Tools and Technologies}. I have {Publication Experience} related to my work. My teamwork preference is {Teamwork Preference}. Additionally, I hold memberships in professional organizations like {Professional Memberships}. I'm eager to Know My Capability Level."
             },
        ],
        "show_prompt": True,
        "allow_skip": True
    }
    }

PREFERRED_LLM = "gpt-4o-mini"
LLM_CONFIG_OVERRIDE = {}

SCORING_DEBUG_MODE = True
DISPLAY_COST = True

COMPLETION_MESSAGE = "You've reached the end! I hope you learned something!"
COMPLETION_CELEBRATION = False

RAG_IMPLEMENTATION = False # make true only when document exists
SOURCE_DOCUMENT = "sample.pdf" # file uploaded in source_docs if only