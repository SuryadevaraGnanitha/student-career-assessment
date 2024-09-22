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
                "options": ["Data Science", "AIML","IOT"],
                "showIf": {"education_level": "Bachelor's Degree"}
            },

            "Associate's Degree Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options": ["Bussiness and management", "Arts and Humanity","Information Technology"],
                "showIf": {"education_level": "Associate's Degree"}
            },

            "Master's Degree Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options": ["Health", "STEM","law and legal Studies"],
                "showIf": {"education_level": "Master's Degree"}
            },

            "PhD Domain": {
                "type": "radio",
                "label": "Please select your domain",
                "options": ["Health Sciences", "STEM","Inter disciplinary and Emerging fields"],
                "showIf": {"education_level": "PhD"}
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
                "options": ["Data Engineering","Data Mining"],
                "showIf": {"Bachelor's Degree Domain": "Data Science"}
            },

            "AIML Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["NLP","machine learning"],
                "showIf": {"Bachelor's Degree Domain": "AIML"}
            },

            "IOT Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Health Care IOT","Agricultural IOT"],
                "showIf": {"Bachelor's Degree Domain": "IOT"}
            },

            "Bussiness and management Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Finance","Marketing"],
                "showIf": {"Associate's Degree Domain": "Bussiness and management"}
            },

            "Arts and Humanity Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Philosophy","History"],
                "showIf": {"Associate's Degree Domain": "Arts and Humanity"}
            },

            "Information Technology Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Software Deveopment","Cyber Security"],
                "showIf": {"Associate's Degree Domain": "Information Technology"}
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

            "Health Sciences Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Dental","Pharmacy"],
                "showIf": {"PhD Domain": "Health Sciences"}
            },

            "STEM Sub Domain": {
                "type": "radio",
                "label": "Please select your sub domain",
                "options": ["Physics","telecommunication","Computer Science"],
                "showIf": {"PhD Domain": "STEM"}
            },
            
            "Data Engineering Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["ETL Developer","DataOps Engineer","Data Architect"],
                "showIf": {"Data Science Sub Domain": "Data Engineering"}
            }, 
            
            "Data Mining Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Data Mining Analyst","Business Intelligence (BI) Analyst","Big Data Engineer"],
                "showIf": {"Data Science Sub Domain": "Data Mining"}
            }, 
            
            "Finance Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Investment Banker","Financial Analyst"],
                "showIf": {"Bussiness and management Sub Domain": "Finance"}
            }, 
            
            "Marketing Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Marketing Manager","Brand Manager"],
                "showIf": {"Bussiness and management Sub Domain": "Marketing"}
            }, 
            
            "Philosophy Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Philosophy Researcher","Philosophical Counselor"],
                "showIf": {"Arts and Humanity Sub Domain": "Philosophy"}
            }, 
            
            "History Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Historian","Archivist"],
                "showIf": {"Arts and Humanity Sub Domain": "History"}
            }, 
            
            "Software Deveopment Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Front-End Developer","Back-End Developer","Mobile App Developer"],
                "showIf": {"Information Technology Sub Domain": "Software Deveopment"}
            }, 
            
            "Cyber Security Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Security Consultant","Security Engineer","Security Consultant"],
                "showIf": {"Information Technology Sub Domain": "Cyber Security"}
            }, 
            
            "NLP Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["NLP Research Scientist","Computational Linguist","NLP Engineer"],
                "showIf": {"AIML Sub Domain": "NLP"}
            }, 
            
            "machine learning Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Machine Learning Engineer","ML Research Scientist","ML Ops Engineer"],
                "showIf": {"AIML Sub Domain": "machine learning"}
            }, 
            
            "Health Care IOT Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Clinical IoT Data Analyst","Telemedicine IoT Developer","Remote Patient Monitoring Specialist"],
                "showIf": {"IOT Sub Domain": "Health Care IOT"}
            }, 
            
            "Agricultural IOT Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Agricultural IoT Engineer","Smart Irrigation Systems Engineer"],
                "showIf": {"IOT Sub Domain": "Agricultural IOT"}
            }, 
            
            "Pharmacy Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Pharmacist","Pharmacy Technician"],
                "showIf": {"Health Sub Domain": "Pharmacy"}
            }, 
            
            "Dental Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Orthodontist","Dentist"],
                "showIf": {"Health Sub Domain": "Dental"}
            }, 
            
            "Physics Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Physicist","Astrophysicist"],
                "showIf": {"STEM-masters Sub Domain": "Physics"}
            }, 
            
            "telecommunication Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Telecommunications Engineer","Network Architect"],
                "showIf": {"STEM-masters Sub Domain": "telecommunication"}
            }, 
            
            "Computer Science Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["DevOps Engineer","Cloud Engineer"],
                "showIf": {"STEM-masters Sub Domain": "Computer Science"}
            }, 
            
            "Crminal law Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Criminal Defense Attorney","Public Defender"],
                "showIf": {"law and legal Sub Domain": "Crminal law"}
            }, 
            
            "civil law Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Civil Rights Attorney","Contract Lawyer"],
                "showIf": {"law and legal Sub Domain": "civil law"}
            }, 
            
            "Dental-phd Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Dentist","Dental Hygienist"],
                "showIf": {"Health Sciences Sub Domain": "Dental"}
            }, 
            
            "Pharmacy-phd Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Pharmacist","Clinical Pharmacist"],
                "showIf": {"Health Sciences Sub Domain": "Pharmacy"}
            }, 
            
            "Physics-PhD Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Physicist","Astrophysicist"],
                "showIf": {"STEM Sub Domain": "Physics"}
            }, 
            
            "telecommunication-PhD Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Telecommunications Engineer","Network Architect"],
                "showIf": {"STEM Sub Domain": "telecommunication"}
            }, 
            
            "Computer Science-PhD Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["DevOps Engineer","Cloud Engineer"],
                "showIf": {"STEM Sub Domain": "Computer Science"}
            
            },
            
            "Neuroscience-PhD Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Neurobiologist","Neuroscientist"],
                "showIf": {"Inter disciplinary and Emerging fields Sub Domain": "Neuroscience"}
            },
            "Biotechnology-PhD Roles": {
                "type": "radio",
                "label": "Please select your Role",
                "options": ["Biotechnologist","Geneticist"],
                "showIf": {"Inter disciplinary and Emerging fields Sub Domain": "Biotechnology"}
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
        },
        "phase_instructions": "Please provide your basic details.",
         "user_prompt": [
            {
                "condition": {"$and": [{"education_level": "Bachelor's Degree"},{"Bachelor's Degree Domain": "Data Science"}]},
                "prompt": "I am {name},I recently completed my Bachelor's Degree and have {Skills} skills with academic percentage of {Academic Performance} %  and with {Certifications} certifications in Data Science hand having a goal to become {Data Engineering Roles}. I'm eager to Know My Capability Level."
            },
            {
                "condition": {"$and": [{"age": {"$gte": 25}}, {"experience_years": {"$gte": 5}}]},
                "prompt": "My name is {name}, and I am {age} years old. With a {education_level} and over {experience_years} years of experience in {current_field}, I'm seeking to advance my career to the next level."
            },
            {
                "condition": {"experience_years": {"$lt": 2}},
                "prompt": "I am {name}, {age} years old, with an education level of {education_level} and less than {experience_years} years of experience in {current_field}. I'm looking to enter a field where I can grow and gain more experience."
            }
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

SCORING_DEBUG_MODE = False
DISPLAY_COST = True

COMPLETION_MESSAGE = "Thank you for using the Career Path Recommendation app! We hope our suggestions help guide your professional journey."
COMPLETION_CELEBRATION = True