PHASES = {
    "phase1": {
        "name": "User Details",
        "fields": {
            "name": {
                "type": "text_input",
                "label": "What is your name?",
            },
            "Domain": {
                "type": "check_box",
                "label": "Choose your Domain",
                "options": [
                    "STEM (Science, Technology, Engineering, Mathematics)",
                    "Humanities",
                    "Social Sciences",
                    "Business",
                    "Health Sciences",
                    "Law",
                    "Technological Domains",
                    "Leadership and Entrepreneurship",
                    "Personal Development Domains",
                    "Professional and Career-Oriented Domains",
                    "Digital and Online Domains"
                ]
            },
            "Subdomain": {
                "type": "check_box",
                "label": "Choose your Sub Domain",
                "options": [],  # Options will be populated based on the domain selected
                "showIf": {
                    "Domain": [
                        "STEM (Science, Technology, Engineering, Mathematics)",
                        "Humanities",
                        "Social Sciences",
                        "Business",
                        "Health Sciences",
                        "Law",
                        "Technological Domains",
                        "Leadership and Entrepreneurship",
                        "Personal Development Domains",
                        "Professional and Career-Oriented Domains",
                        "Digital and Online Domains"
                    ]
                }
            },
            "Roles": {
                "type": "check_box",
                "label": "Choose your Role",
                "options": [],  # Options will be populated based on the subdomain selected
                "showIf": {
                    "Subdomain": []  # Will be dynamically populated based on subdomain
                }
            }
        },
        "dynamic_fields": {
            "Domain": {
                "STEM (Science, Technology, Engineering, Mathematics)": {
                    "Subdomain": {
                        "options": ["Physics", "Chemistry", "Biology", "Computer Science", "Mathematics", "Engineering"]
                    },
                    "Roles": {
                        "Physics": ["Research Scientist", "Physicist"],
                        "Chemistry": ["Chemist", "Research Scientist"],
                        "Biology": ["Biotechnologist", "Biologist", "Research Scientist"],
                        "Computer Science": ["Software Developer", "Data Analyst", "AI Specialist"],
                        "Mathematics": ["Mathematician", "Data Analyst"],
                        "Engineering": ["Engineer", "Mechanical Engineer", "Civil Engineer"]
                    }
                },
                "Humanities": {
                    "Subdomain": {
                        "options": ["History", "Literature", "Philosophy", "Linguistics", "Cultural Studies"]
                    },
                    "Roles": {
                        "History": ["Historian", "Researcher"],
                        "Literature": ["Writer", "Editor"],
                        "Philosophy": ["Philosopher", "Educator"],
                        "Linguistics": ["Linguist", "Language Analyst"],
                        "Cultural Studies": ["Cultural Analyst", "Researcher"]
                    }
                },
                "Social Sciences": {
                    "Subdomain": {
                        "options": ["Sociology", "Psychology", "Anthropology", "Political Science", "Economics"]
                    },
                    "Roles": {
                        "Sociology": ["Sociologist", "Social Worker"],
                        "Psychology": ["Psychologist", "Therapist"],
                        "Anthropology": ["Anthropologist", "Researcher"],
                        "Political Science": ["Political Analyst", "Policy Advisor"],
                        "Economics": ["Economist", "Financial Analyst"]
                    }
                },
                "Business": {
                    "Subdomain": {
                        "options": ["Finance", "Marketing", "Management", "Accounting", "Economics"]
                    },
                    "Roles": {
                        "Finance": ["Financial Analyst", "Accountant"],
                        "Marketing": ["Marketing Manager", "Digital Marketing Specialist"],
                        "Management": ["Business Consultant", "Manager"],
                        "Accounting": ["Accountant", "Auditor"],
                        "Economics": ["Economist", "Data Analyst"]
                    }
                },
                "Health Sciences": {
                    "Subdomain": {
                        "options": ["Medicine", "Nursing", "Public Health", "Pharmacy", "Dentistry"]
                    },
                    "Roles": {
                        "Medicine": ["Doctor", "Surgeon"],
                        "Nursing": ["Nurse", "Healthcare Administrator"],
                        "Public Health": ["Public Health Specialist", "Healthcare Consultant"],
                        "Pharmacy": ["Pharmacist", "Pharmacy Technician"],
                        "Dentistry": ["Dentist", "Dental Hygienist"]
                    }
                },
                "Law": {
                    "Subdomain": {
                        "options": ["Constitutional Law", "Criminal Law", "International Law"]
                    },
                    "Roles": {
                        "Constitutional Law": ["Lawyer", "Legal Researcher"],
                        "Criminal Law": ["Lawyer", "Judge"],
                        "International Law": ["Policy Advisor", "Legal Consultant"]
                    }
                },
                "Technological Domains": {
                    "Subdomain": {
                        "options": ["Programming and Software Development", "Data Science and Analytics", "Cybersecurity", "Information Technology"]
                    },
                    "Roles": {
                        "Programming and Software Development": ["Software Developer", "Game Designer", "Web Developer"],
                        "Data Science and Analytics": ["Data Scientist", "Machine Learning Engineer", "AI Specialist"],
                        "Cybersecurity": ["Cybersecurity Analyst", "Ethical Hacker"],
                        "Information Technology": ["IT Support Specialist", "Systems Administrator", "Cloud Architect"]
                    }
                },
                "Leadership and Entrepreneurship": {
                    "Subdomain": {
                        "options": ["Startup Incubators", "Leadership Programs", "Business Competitions"]
                    },
                    "Roles": {
                        "Startup Incubators": ["Entrepreneur", "Startup Founder"],
                        "Leadership Programs": ["Business Leader", "Innovation Manager"],
                        "Business Competitions": ["Business Coach", "Startup Mentor"]
                    }
                },
                "Personal Development Domains": {
                    "Subdomain": {
                        "options": ["Time Management", "Mental and Emotional Health", "Communication Skills"]
                    },
                    "Roles": {
                        "Time Management": ["Productivity Coach", "Time Management Consultant"],
                        "Mental and Emotional Health": ["Mental Health Counselor", "Stress Management Consultant"],
                        "Communication Skills": ["Public Speaker", "Speech Coach"]
                    }
                },
                "Professional and Career-Oriented Domains": {
                    "Subdomain": {
                        "options": ["Internships and Work Experience", "Career Planning and Development", "Certifications and Continuing Education"]
                    },
                    "Roles": {
                        "Internships and Work Experience": ["Intern", "Apprentice", "Volunteer"],
                        "Career Planning and Development": ["Career Counselor", "HR Specialist"],
                        "Certifications and Continuing Education": ["Professional Trainer", "Workshop Facilitator"]
                    }
                },
                "Digital and Online Domains": {
                    "Subdomain": {
                        "options": ["E-Learning Platforms", "Student Portals", "Social Media for Students"]
                    },
                    "Roles": {
                        "E-Learning Platforms": ["E-Learning Developer", "Online Course Instructor"],
                        "Student Portals": ["LMS Administrator", "Educational Technologist"],
                        "Social Media for Students": ["Social Media Manager", "Content Creator"]
                    }
                }
            }
        },
        "phase_instructions": "",
        "user_prompt": [
            {
                "condition": {"system": "Western"},
                "prompt": """My name is {name}. I was born on {month} {day}, {year}. Please provide me my Western zodiac symbol, and give a short horoscope for the day."""
            },
            {
                "condition": {"system": "Chinese"},
                "prompt": """My name is {name}. I was born in the year {year}. Please provide me my Chinese zodiac symbol, and give a short horoscope for the day."""
            }
        ],
        "show_prompt": True,
        "allow_skip": True
    }
}
