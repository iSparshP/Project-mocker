# LinkedIn ETL Pipeline Configuration

# Output settings
default_output_dir = "linkedin_data"
default_filename_prefix = "linkedin_profiles"

# Rate limiting (to be respectful to LinkedIn)
request_delay_seconds = 2
max_profiles_per_session = 50

# Data fields to extract and transform
profile_fields = [
    "name",
    "title", 
    "company",
    "location",
    "experience_years",
    "skills",
    "education",
    "profile_url"
]

# Excel export settings
excel_sheet_name = "LinkedIn_Profiles"
include_timestamp = True

# CSV export settings (fallback)
csv_encoding = "utf-8"
csv_delimiter = ","

# Logging settings
log_level = "INFO"
log_format = "%(asctime)s - %(levelname)s - %(message)s"

# Demo data for testing (when not scraping real profiles)
demo_profiles = [
    {
        'name': 'John Doe',
        'title': 'Software Engineer',
        'company': 'Tech Corp',
        'location': 'San Francisco, CA',
        'experience_years': 5,
        'skills': ['Python', 'JavaScript', 'React', 'Node.js'],
        'education': 'Computer Science, Stanford University',
        'profile_url': 'https://linkedin.com/in/johndoe'
    },
    {
        'name': 'Jane Smith',
        'title': 'Data Scientist',
        'company': 'Data Analytics Inc',
        'location': 'New York, NY',
        'experience_years': 3,
        'skills': ['Python', 'Machine Learning', 'SQL', 'TensorFlow'],
        'education': 'Data Science, MIT',
        'profile_url': 'https://linkedin.com/in/janesmith'
    },
    {
        'name': 'Bob Johnson',
        'title': 'Product Manager',
        'company': 'Innovation Labs',
        'location': 'Seattle, WA',
        'experience_years': 7,
        'skills': ['Product Strategy', 'Analytics', 'Leadership', 'Agile'],
        'education': 'MBA, Harvard Business School',
        'profile_url': 'https://linkedin.com/in/bobjohnson'
    },
    {
        'name': 'Alice Chen',
        'title': 'UX Designer',
        'company': 'Design Studio',
        'location': 'Los Angeles, CA',
        'experience_years': 4,
        'skills': ['UI/UX Design', 'Figma', 'User Research', 'Prototyping'],
        'education': 'Design, California College of the Arts',
        'profile_url': 'https://linkedin.com/in/alicechen'
    },
    {
        'name': 'Mike Williams',
        'title': 'DevOps Engineer',
        'company': 'Cloud Solutions',
        'location': 'Austin, TX',
        'experience_years': 6,
        'skills': ['AWS', 'Docker', 'Kubernetes', 'Terraform'],
        'education': 'Computer Engineering, University of Texas',
        'profile_url': 'https://linkedin.com/in/mikewilliams'
    }
]