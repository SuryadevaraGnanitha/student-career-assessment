# 1. Page Config - Dict
PAGE_CONFIG = {
    "page_title": "AI MicroApps", # title of app if one app is implemented
    "page_icon": "🎯", # replace based on App if it is single
    "layout": "centered",  # "centered" or "wide"
    "initial_sidebar_state": "expanded"  # Options: "auto", "expanded", "collapsed"
}

# 2. Sidebar State - Hidden, Collapsed, or Expanded
SIDEBAR_HIDDEN = False  # Set to True to completely hide the sidebar

# 3. Templates
TEMPLATES = {
    "ai_assessment": "config",
    "Zodiac Symbol": "config_zodiac",
    "Career Advisor": "config_career_path"
}