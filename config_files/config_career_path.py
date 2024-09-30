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
                "options": ["Business and Management", "Arts and Humanities", "Information Technology", "Health Sciences", "Social Sciences"],
                "showIf": {"education_level": "Associate's Degree"}
            },

            "Master's Degree Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options": ["Health", "STEM","law and legal Studies","Business", "STEM", "Health Sciences", "Social Sciences", "Arts and Humanities", "Education"],
                "showIf": {"education_level": "Master's Degree"}
            },

            "PhD Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options":  ["Natural Sciences", "Engineering", "Social Sciences", "Humanities", "Health Sciences", "Interdisciplinary Studies","Health Sciences", "STEM","Inter disciplinary and Emerging fields"],
                "showIf": {"education_level": "PhD"}
            },
            
            #new
             "Business and Management Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Accounting", "Business Administration", "Marketing", "Finance", "Hospitality Management"],
    "showIf": {"Associate's Degree Domain": "Business and Management"}
  },
  "Arts and Humanities Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Liberal Arts", "Fine Arts", "Graphic Design", "Music", "Theatre"],
    "showIf": {"Associate's Degree Domain": "Arts and Humanities"}
  },
  "Information Technology Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Computer Science", "Network Administration", "Web Development", "Cybersecurity", "Database Management"],
    "showIf": {"Associate's Degree Domain": "Information Technology"}
  },
  "Health Sciences Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Nursing", "Medical Assisting", "Dental Hygiene", "Radiologic Technology", "Emergency Medical Services"],
    "showIf": {"Associate's Degree Domain": "Health Sciences"}
  },
  "Social Sciences Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Psychology", "Sociology", "Criminal Justice", "Early Childhood Education", "Human Services"],
    "showIf": {"Associate's Degree Domain": "Social Sciences"}
  },
  "Business Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Master of Business Administration (MBA)", "Finance", "Marketing", "Human Resource Management", "International Business"],
    "showIf": {"Master's Degree Domain": "Business"}
  },
  "STEM Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Computer Science", "Data Science", "Engineering", "Mathematics", "Biotechnology"],
    "showIf": {"Master's Degree Domain": "STEM"}
  },
  "Health Sciences Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Public Health", "Nursing", "Health Administration", "Occupational Therapy", "Physician Assistant Studies"],
    "showIf": {"Master's Degree Domain": "Health Sciences"}
  },
  "Social Sciences Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Psychology", "Sociology", "Economics", "Political Science", "Anthropology"],
    "showIf": {"Master's Degree Domain": "Social Sciences"}
  },
  "Arts and Humanities Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Fine Arts", "Literature", "History", "Philosophy", "Linguistics"],
    "showIf": {"Master's Degree Domain": "Arts and Humanities"}
  },
  "Education Master's Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Curriculum and Instruction", "Educational Leadership", "Special Education", "Higher Education Administration", "Educational Technology"],
    "showIf": {"Master's Degree Domain": "Education"}
  },
  "Natural Sciences PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Physics", "Chemistry", "Biology", "Astronomy", "Environmental Science"],
    "showIf": {"PhD Domain": "Natural Sciences"}
  },
  "Engineering PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Electrical Engineering", "Mechanical Engineering", "Chemical Engineering", "Civil Engineering", "Computer Engineering"],
    "showIf": {"PhD Domain": "Engineering"}
  },
  "Social Sciences PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Psychology", "Sociology", "Economics", "Political Science", "Anthropology"],
    "showIf": {"PhD Domain": "Social Sciences"}
  },
  "Humanities PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Literature", "History", "Philosophy", "Linguistics", "Art History"],
    "showIf": {"PhD Domain": "Humanities"}
  },
  "Health Sciences PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Medicine", "Public Health", "Nursing", "Pharmacology", "Neuroscience"],
    "showIf": {"PhD Domain": "Health Sciences"}
  },
  "Interdisciplinary Studies PhD Sub Domain": {
    "type": "radio",
    "label": "Please select your sub domain",
    "options": ["Bioinformatics", "Cognitive Science", "Environmental Studies", "Nanotechnology", "Digital Humanities"],
    "showIf": {"PhD Domain": "Interdisciplinary Studies"}
  },



            "Inter disciplinary and Emerging fields Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Neuroscience","Biotechnology"],
                "showIf": {"PhD Domain": "Inter disciplinary and Emerging fields"}
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

            "STEM-masters Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Physics","telecommunication","Computer Science"],
                "showIf": {"Master's Degree Domain": "STEM"}
            },

            "law and legal Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Crminal law","civil law"],
                "showIf": {"Master's Degree Domain": "law and legal Studies"}
            },
            "STEM Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Physics","telecommunication","Computer Science"],
                "showIf": {"PhD Domain": "STEM"}
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
  "Liberal Arts Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Writer", "Journalist", "Teacher", "Public Relations Specialist", "Human Resources Coordinator"],
    "showIf": {"Arts and Humanities Sub Domain": "Liberal Arts"}
  },
  "Fine Arts Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Artist", "Art Director", "Curator", "Art Therapist", "Art Teacher"],
    "showIf": {"Arts and Humanities Sub Domain": "Fine Arts"}
  },
  "Graphic Design Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Graphic Designer", "UI/UX Designer", "Art Director", "Creative Director", "Production Artist"],
    "showIf": {"Arts and Humanities Sub Domain": "Graphic Design"}
  },
  "Music Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Musician", "Music Teacher", "Sound Engineer", "Music Therapist", "Music Producer"],
    "showIf": {"Arts and Humanities Sub Domain": "Music"}
  },
  "Theatre Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Actor", "Director", "Stage Manager", "Playwright", "Drama Teacher"],
    "showIf": {"Arts and Humanities Sub Domain": "Theatre"}
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
  "Nursing Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Registered Nurse", "Nurse Practitioner", "Clinical Nurse Specialist", "Nurse Educator", "Nurse Manager"],
    "showIf": {"Health Sciences Sub Domain": "Nursing"}
  },
  "Medical Assisting Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Medical Assistant", "Clinical Assistant", "Medical Office Administrator", "EKG Technician", "Phlebotomist"],
    "showIf": {"Health Sciences Sub Domain": "Medical Assisting"}
  },
  "Dental Hygiene Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Dental Hygienist", "Dental Assistant", "Oral Health Educator", "Dental Office Manager", "Dental Sales Representative"],
    "showIf": {"Health Sciences Sub Domain": "Dental Hygiene"}
  },
  "Radiologic Technology Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Radiologic Technologist", "MRI Technologist", "CT Technologist", "Mammography Technologist", "Interventional Radiologist"],
    "showIf": {"Health Sciences Sub Domain": "Radiologic Technology"}
  },
  "Emergency Medical Services Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Emergency Medical Technician (EMT)", "Paramedic", "Emergency Room Technician", "Flight Paramedic", "EMS Educator"],
    "showIf": {"Health Sciences Sub Domain": "Emergency Medical Services"}
  },
  "Psychology Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Clinical Psychologist", "Counseling Psychologist", "School Psychologist", "Industrial-Organizational Psychologist", "Neuropsychologist"],
    "showIf": {"Social Sciences Sub Domain": "Psychology"}
  },
  "Sociology Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Sociologist", "Social Worker", "Market Research Analyst", "Human Resources Specialist", "Community Service Manager"],
    "showIf": {"Social Sciences Sub Domain": "Sociology"}
  },
  "Criminal Justice Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Police Officer", "Probation Officer", "Forensic Scientist", "Criminal Investigator", "Corrections Officer"],
    "showIf": {"Social Sciences Sub Domain": "Criminal Justice"}
  },
  "Early Childhood Education Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Preschool Teacher", "Childcare Center Director", "Special Education Teacher", "Child Life Specialist", "Early Intervention Specialist"],
    "showIf": {"Social Sciences Sub Domain": "Early Childhood Education"}
  },
  "Human Services Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Social Worker", "Case Manager", "Community Outreach Worker", "Mental Health Counselor", "Substance Abuse Counselor"],
    "showIf": {"Social Sciences Sub Domain": "Human Services"}
  },
  "MBA Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Business Development Manager", "Management Consultant", "Operations Manager", "Financial Manager", "Marketing Director"],
    "showIf": {"Business Master's Sub Domain": "Master of Business Administration (MBA)"}
  },
  "Human Resource Management Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["HR Manager", "Talent Acquisition Specialist", "Compensation and Benefits Manager", "Training and Development Manager", "Employee Relations Specialist"],
    "showIf": {"Business Master's Sub Domain": "Human Resource Management"}
  },
  "International Business Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["International Business Development Manager", "Global Marketing Manager", "International Trade Specialist", "Foreign Market Analyst", "Cross-Cultural Business Consultant"],
    "showIf": {"Business Master's Sub Domain": "International Business"}
  },
  "Data Science Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Data Scientist", "Machine Learning Engineer", "Business Intelligence Analyst", "Data Architect", "Quantitative Analyst"],
    "showIf": {"STEM Master's Sub Domain": "Data Science"}
  },
  "Engineering Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Mechanical Engineer", "Electrical Engineer", "Civil Engineer", "Chemical Engineer", "Aerospace Engineer"],
    "showIf": {"STEM Master's Sub Domain": "Engineering"}
  },
  "Mathematics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Mathematician", "Statistician", "Operations Research Analyst", "Actuary", "Cryptographer"],
    "showIf": {"STEM Master's Sub Domain": "Mathematics"}
  },
  "Biotechnology Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Biomedical Engineer", "Biochemist", "Bioinformatics Specialist", "Clinical Research Associate", "Biotechnology Product Developer"],
    "showIf": {"STEM Master's Sub Domain": "Biotechnology"}
  },
  "Public Health Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Epidemiologist", "Health Policy Analyst", "Environmental Health Specialist", "Health Education Specialist", "Biostatistician"],
    "showIf": {"Health Sciences Master's Sub Domain": "Public Health"}
  },
  "Health Administration Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Hospital Administrator", "Healthcare Manager", "Health Information Manager", "Healthcare Consultant", "Medical Practice Manager"],
    "showIf": {"Health Sciences Master's Sub Domain": "Health Administration"}
  },
  "Occupational Therapy Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Occupational Therapist", "Ergonomics Consultant", "Rehabilitation Specialist", "Pediatric Occupational Therapist", "Geriatric Occupational Therapist"],
    "showIf": {"Health Sciences Master's Sub Domain": "Occupational Therapy"}
  },
  "Physician Assistant Studies Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Physician Assistant", "Surgical Physician Assistant", "Emergency Medicine Physician Assistant", "Family Medicine Physician Assistant", "Specialty Physician Assistant"],
    "showIf": {"Health Sciences Master's Sub Domain": "Physician Assistant Studies"}
  },
  "Economics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Economist", "Economic Analyst", "Financial Economist", "Policy Analyst", "Market Research Analyst"],
    "showIf": {"Social Sciences Master's Sub Domain": "Economics"}
  },
  "Political Science Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Political Analyst", "Policy Advisor", "Campaign Manager", "Lobbyist", "Diplomat"],
    "showIf": {"Social Sciences Master's Sub Domain": "Political Science"}
  },
  "Anthropology Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Anthropologist", "Archaeologist", "Cultural Resource Manager", "Museum Curator", "Corporate Anthropologist"],
    "showIf": {"Social Sciences Master's Sub Domain": "Anthropology"}
  },
  "Literature Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Literary Critic", "Editor", "Technical Writer", "Copywriter", "Librarian"],
    "showIf": {"Arts and Humanities Master's Sub Domain": "Literature"}
  },
  "Linguistics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Linguist", "Translator", "Interpreter", "Computational Linguist", "Speech-Language Pathologist"],
    "showIf": {"Arts and Humanities Master's Sub Domain": "Linguistics"}
  },
  "Curriculum and Instruction Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Curriculum Developer", "Instructional Coordinator", "Educational Consultant", "Training and Development Specialist", "E-Learning Designer"],
    "showIf": {"Education Master's Sub Domain": "Curriculum and Instruction"}
  },
  "Educational Leadership Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["School Principal", "Superintendent", "Dean of Students", "Education Policy Analyst", "Education Program Director"],
    "showIf": {"Education Master's Sub Domain": "Educational Leadership"}
  },
  "Special Education Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Special Education Teacher", "Inclusion Specialist", "Behavior Intervention Specialist", "Special Education Coordinator", "Assistive Technology Specialist"],
    "showIf": {"Education Master's Sub Domain": "Special Education"}
  },
  "Higher Education Administration Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["College Administrator", "Academic Advisor", "Admissions Director", "Student Affairs Coordinator", "University Registrar"],
    "showIf": {"Education Master's Sub Domain": "Higher Education Administration"}
  },
  "Educational Technology Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Instructional Technologist", "E-Learning Developer", "Educational Software Designer", "Technology Integration Specialist", "Digital Learning Coordinator"],
    "showIf": {"Education Master's Sub Domain": "Educational Technology"}
  },
  "Physics PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Research Physicist", "Quantum Physicist", "Astrophysicist", "Medical Physicist", "Condensed Matter Physicist"],
    "showIf": {"Natural Sciences PhD Sub Domain": "Physics"}
  },


 "Chemistry PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Research Chemist", "Analytical Chemist", "Organic Chemist", "Pharmaceutical",  "Chemist", "Biochemist", "Materials Scientist"],
    "showIf": {"Natural Sciences PhD Sub Domain": "Chemistry"}
  },

  "Biology PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Molecular Biologist", "Geneticist", "Ecologist", "Microbiologist", "Neuroscientist"],
    "showIf": {"Natural Sciences PhD Sub Domain": "Biology"}
  },
  "Astronomy PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Astronomer", "Cosmologist", "Planetary Scientist", "Radio Astronomer", "Astrobiologist"],
    "showIf": {"Natural Sciences PhD Sub Domain": "Astronomy"}
  },
  "Environmental Science PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Environmental Scientist", "Climate Change Analyst", "Ecologist", "Geoscientist", "Conservation Scientist"],
    "showIf": {"Natural Sciences PhD Sub Domain": "Environmental Science"}
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
  "Humanities PhD Literature Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Literary Scholar", "Comparative Literature Researcher", "Literature Professor", "Literary Critic", "Textual Editor"],
    "showIf": {"Humanities PhD Sub Domain": "Literature"}
  },
  "Humanities PhD History Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Historical Researcher", "Archivist", "Museum Curator", "History Professor", "Historical Consultant"],
    "showIf": {"Humanities PhD Sub Domain": "History"}
  },
  "Humanities PhD Philosophy Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Philosophy Professor", "Ethics Consultant", "Logic Researcher", "Philosophical Writer", "Bioethicist"],
    "showIf": {"Humanities PhD Sub Domain": "Philosophy"}
  },
  "Humanities PhD Linguistics Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Linguistics Researcher", "Computational Linguist", "Phonetician", "Sociolinguist", "Language Acquisition Specialist"],
    "showIf": {"Humanities PhD Sub Domain": "Linguistics"}
  },
  "Humanities PhD Art History Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Art Historian", "Museum Curator", "Art Conservator", "Art Critic", "Cultural Heritage Specialist"],
    "showIf": {"Humanities PhD Sub Domain": "Art History"}
  },
  "Medicine PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Medical Researcher", "Clinical Scientist", "Biomedical Scientist", "Pharmacologist", "Medical Geneticist"],
    "showIf": {"Health Sciences PhD Sub Domain": "Medicine"}
  },
  "Pharmacology PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Pharmacologist", "Drug Developer", "Toxicologist", "Clinical Research Scientist", "Pharmaceutical Consultant"],
    "showIf": {"Health Sciences PhD Sub Domain": "Pharmacology"}
  },
  "Neuroscience PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Neuroscientist", "Cognitive Scientist", "Neurobiologist", "Neuroengineering Researcher", "Brain-Computer Interface Specialist"],
    "showIf": {"Health Sciences PhD Sub Domain": "Neuroscience"}
  },
  "Bioinformatics PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Bioinformatician", "Computational Biologist", "Genomics Data Analyst", "Systems Biologist", "Biostatistician"],
    "showIf": {"Interdisciplinary Studies PhD Sub Domain": "Bioinformatics"}
  },
  "Cognitive Science PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Cognitive Scientist", "Artificial Intelligence Researcher", "Human-Computer Interaction Specialist", "Neurolinguist", "Cognitive Psychologist"],
    "showIf": {"Interdisciplinary Studies PhD Sub Domain": "Cognitive Science"}
  },
  "Environmental Studies PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Environmental Policy Analyst", "Sustainability Consultant", "Ecosystem Manager", "Climate Change Researcher", "Environmental Education Specialist"],
    "showIf": {"Interdisciplinary Studies PhD Sub Domain": "Environmental Studies"}
  },
  "Nanotechnology PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Nanotechnology Researcher", "Nanomaterials Scientist", "Nanoelectronics Engineer", "Nanomedicine Specialist", "Nanofabrication Engineer"],
    "showIf": {"Interdisciplinary Studies PhD Sub Domain": "Nanotechnology"}
  },
  "Digital Humanities PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Digital Archivist", "Data Visualization Specialist", "Cultural Analytics Researcher", "Digital Curator", "Humanities Computing Specialist"],
    "showIf": {"Interdisciplinary Studies PhD Sub Domain": "Digital Humanities"}
  },
  "Neuroscience Interdisciplinary PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Neuroscience Researcher", "Brain-Computer Interface Developer", "Neuroimaging Specialist", "Computational Neuroscientist", "Neuroethicist"],
    "showIf": {"Inter disciplinary and Emerging fields Sub Domain": "Neuroscience"}
  },
  "Biotechnology Interdisciplinary PhD Roles": {
    "type": "radio",
    "label": "Please select your Role",
    "options": ["Biotechnologist", "Genetic Engineer", "Bioproduct Developer", "Bioprocess Engineer", "Synthetic Biologist"],
    "showIf": {"Inter disciplinary and Emerging fields Sub Domain": "Biotechnology"}
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
                "label": "Please select your Role",
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
#   "Certifications": {
#     "type": "multiselect",
#     "label": "Do you hold any relevant certifications? (Select all that apply)",
#     "options": ["Professional certification", "Academic certification", "Industry-specific certification", "Vendor-specific certification", "None"]
#   },
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
  "Technical Skills": {
    "type": "text_area",
    "label": "List your top 5 technical skills relevant to your chosen subdomain:"
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
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Machine Learning"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Machine Learning Roles}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Machine Learning"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Machine Learning Roles}. I'm eager to Know My Capability Level."
             },

             #bachelor's,data science, Statistical Analysis Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Statistical Analysis"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Statistical Analysis Roles}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Statistical Analysis"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Statistical Analysis Roles}. I'm eager to Know My Capability Level."
             },

             # bachelor's, datascience, Data Visualization Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Data Visualization"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Data Visualization Roles}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Data Visualization"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Data Visualization Roles}. I'm eager to Know My Capability Level."
             },

             # bachelor's, datascience, Big Data Analytics Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Big Data Analytics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Big Data Analytics Roles}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Big Data Analytics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Big Data Analytics Roles}. I'm eager to Know My Capability Level."
             },

             # bachelor's, datascience, Big Data Analytics Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"Data Science Sub Domain":"Big Data Analytics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Big Data Analytics Roles}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"Data Science Sub Domain":"Big Data Analytics"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Big Data Analytics Roles}. I'm eager to Know My Capability Level."
             },

             # bachelor's , AIML, MACHINE LEARNING roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"AIML Sub Domain":"machine learning"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {machine learning Roles}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"AIML Sub Domain":"machine learning"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {machine learning Roles}. I'm eager to Know My Capability Level."
             },

             # bachelor's , IOT, Health Care IOT Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"Health Care IOT"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Health Care IOT Roles}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"Health Care IOT"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Health Care IOT Roles}. I'm eager to Know My Capability Level."
             },

             # bachelor's , IOT, Agricultural IOT Roles

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Offline"},{"IOT Sub Domain":"Agricultural IOT"}]},
                "prompt": "I am {name}, I recently completed my {education_level} in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Agricultural IOT Roles}. I'm eager to Know My Capability Level."
             },

             {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Learning Mode": "Online"},{"IOT Sub Domain":"Agricultural IOT"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Bachelor's Degree Domain} and having a goal to become {Agricultural IOT Roles}. I'm eager to Know My Capability Level."
             },

             #ASSOICIATE,business and management,finance roles

            {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Bussiness and management Sub Domain":"Finance"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Finance Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Bussiness and management Sub Domain":"Finance"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Finance Roles} . I'm eager to Know My Capability Level."
             },

             #ASSOICIATE,business and management,Marketing Roles

            {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Bussiness and management Sub Domain":"Marketing"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Marketing Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Bussiness and management Sub Domain":"Marketing"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Marketing Roles} . I'm eager to Know My Capability Level."
             },

            #ASSOICIATE,Arts and Humanity,philosophy

            {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Arts and Humanity Sub Domain":"Philosophy"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Philosophy Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Arts and Humanity Sub Domain":"Philosophy"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Philosophy Roles} . I'm eager to Know My Capability Level."
             },

             #ASSOICIATE,Arts and Humanity,History

            {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Arts and Humanity Sub Domain":"History"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {History Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Arts and Humanity Sub Domain":"History"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {History Roles} . I'm eager to Know My Capability Level."
             },

             #ASSOICIATE,Information technology,Software Deveopment

            {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Information Technology Sub Domain":"Software Deveopment"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Software Deveopment Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Information Technology Sub Domain":"Software Deveopment"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Software Deveopment Roles} . I'm eager to Know My Capability Level."
             },

             #ASSOICIATE,Information technology,Cyber Security

            {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Offline"},{"Information Technology Sub Domain":"Cyber Security"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Cyber Security Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Associate's Degree"},{"Learning Mode": "Online"},{"Information Technology Sub Domain":"Cyber Security"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Associate's Degree Domain} and having a goal to become {Cyber Security Roles} . I'm eager to Know My Capability Level."
             },

             #MASTER'S,HEALTH,PHARMACY
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Health Sub Domain":"Pharmacy"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Pharmacy Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Health Sub Domain":"Pharmacy"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Pharmacy Roles} . I'm eager to Know My Capability Level."
             },
             
             #MASTER'S HEALTH,DENTAL

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"Health Sub Domain":"Dental"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Dental Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"Health Sub Domain":"Dental"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Dental Roles} . I'm eager to Know My Capability Level."
             },

             #MASTER'S,STEM,Physics
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"STEM-masters Sub Domain":"Physics"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Physics Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"STEM-masters Sub Domain":"Physics"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Physics Roles} . I'm eager to Know My Capability Level."
             },
             
             #MASTER'S, STEM,telecommunication

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"STEM-masters Sub Domain":"telecommunication"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {telecommunication Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"STEM-masters Sub Domain":"telecommunication"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {telecommunication Roles} . I'm eager to Know My Capability Level."
             },

             #MASTER'S, STEM,Computer Science

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"STEM-masters Sub Domain":"Computer Science"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Computer Science Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"STEM-masters Sub Domain":"Computer Science"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Computer Science Roles} . I'm eager to Know My Capability Level."
             },

             #MASTER'S,law and legal Studies,Crminal law
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"law and legal Sub Domain":"Crminal law"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Crminal law Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"law and legal Sub Domain":"Crminal law"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {Crminal law Roles} . I'm eager to Know My Capability Level."
             },
             
             #MASTER'S,law and legal Studies,civil law

             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Offline"},{"law and legal Sub Domain":"civil law"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {civil law Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "Master's Degree"},{"Learning Mode": "Online"},{"law and legal Sub Domain":"civil law"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {Master's Degree Domain} and having a goal to become {civil law Roles} . I'm eager to Know My Capability Level."
             },

             #PhD,Health Sciences,Dental

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Health Sciences Sub Domain":"Dental"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Dental-phd Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Health Sciences Sub Domain":"Dental"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Dental-phd Roles} . I'm eager to Know My Capability Level."
             },

             #PhD,Health Sciences,Pharmacy

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Health Sciences Sub Domain":"Pharmacy"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Pharmacy-phd Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Health Sciences Sub Domain":"Pharmacy"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Pharmacy-phd Roles} . I'm eager to Know My Capability Level."
             },

             #PhD,STEM,PHYSICS

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"STEM Sub Domain":"Physics"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Physics-PhD Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"STEM Sub Domain":"Physics"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Physics-PhD Roles} . I'm eager to Know My Capability Level."
             },

              #PhD,STEM,telecommunication

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"STEM Sub Domain":"telecommunication"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {telecommunication-PhD Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"STEM Sub Domain":"telecommunication"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {telecommunication-PhD Roles} . I'm eager to Know My Capability Level."
             },

              #PhD,STEM,Computer Science

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"STEM Sub Domain":"Computer Science"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Computer Science-PhD Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"STEM Sub Domain":"Computer Science"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Computer Science-PhD Roles} . I'm eager to Know My Capability Level."
             },

             #PhD,Inter disciplinary and Emerging fields,NEURO SCIENCE

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Inter disciplinary and Emerging fields Sub Domain":"Neuroscience"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Neuroscience-PhD Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Inter disciplinary and Emerging fields Sub Domain":"Neuroscience"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Neuroscience-PhD Roles} . I'm eager to Know My Capability Level."
             },

             #PhD,Inter disciplinary and Emerging fields,NEURO SCIENCE

             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Offline"},{"Inter disciplinary and Emerging fields Sub Domain":"Biotechnology"}]},
                 "prompt": "I am {name}, I recently completed my {education_level}  in Offline mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Biotechnology-PhD Roles}. I'm eager to Know My Capability Level."
             },
             {
                "condition": {"$and": [{"education_level": "PhD"},{"Learning Mode": "Online"},{"Inter disciplinary and Emerging fields Sub Domain":"Biotechnology"}]},
                  "prompt": "I am {name}, I recently completed my {education_level} in Online mode and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in {PhD Domain} and having a goal to become {Biotechnology-PhD Roles} . I'm eager to Know My Capability Level."
             },




        ],
        "show_prompt": True,
        "allow_skip": True
    },
    "phase2": {
        "name": "Career Preferences",
        "fields": {
            "preferred_working_style": {
                "type": "radio",
                "label": "What is your preferred working style?",
                "options": ["Team-oriented", "Independent"]
            },
            "technical_or_non_technical": {
                "type": "radio",
                "label": "Do you prefer a technical or non-technical role?",
                "options": ["Technical", "Non-technical"]
            },
            "willing_to_relocate": {
                "type": "radio",
                "label": "Are you willing to relocate?",
                "options": ["Yes", "No"],
            },
            "desired_salary": {
                "type": "number_input",
                "label": "What is your desired salary? (in $K)",
                "min_value": 30,
                "max_value": 300,
                "value": 60
            }
        },
        "phase_instructions": "Let us know more about your career preferences.",
        "user_prompt": [
            {
                "condition": {"$and": [
                    {"preferred_working_style": "Independent"},
                    {"technical_or_non_technical": "Technical"}
                ]},
                "prompt": "I prefer working independently and I am interested in a technical role. I have {experience_years} years of experience in {current_field}, and I am looking for a career that suits my skills and preferences."
            },
            {
                "condition": {"$and": [
                    {"preferred_working_style": "Independent"},
                    {"technical_or_non_technical": "Non-technical"}
                ]},
                "prompt": "I prefer working independently in a non-technical role. I have {experience_years} years of experience in {current_field}, and I am looking for a career that allows me to leverage my skills in a flexible work environment."
            },
            {
                "condition": {"$and": [
                    {"preferred_working_style": "Team-oriented"},
                    {"technical_or_non_technical": "Technical"}
                ]},
                "prompt": "I enjoy working in a team and am interested in a technical role. I have {experience_years} years of experience in {current_field}, and I am looking for a collaborative environment where I can contribute my technical skills."
            },
            {
                "condition": {"$and": [
                    {"preferred_working_style": "Team-oriented"},
                    {"technical_or_non_technical": "Non-technical"}
                ]},
                "prompt": "I enjoy working in a team and prefer non-technical roles. I have {experience_years} years of experience in {current_field}, and I am looking for a career that aligns with my interests and abilities."
            },
            {
                "condition": {"$and": [
                    {"willing_to_relocate": "Yes"},
                    {"desired_salary": {"$gt": 100}}
                ]},
                "prompt": "I am open to relocating for a job opportunity, and I am aiming for a salary above $100K. Please suggest a career path that fits these preferences."
            }
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