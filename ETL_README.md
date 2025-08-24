# LinkedIn ETL Pipeline

An end-to-end ETL (Extract, Transform, Load) pipeline for scraping LinkedIn profile data and exporting it to Excel format.

## ⚠️ Important Disclaimer

This implementation uses **demo data** for demonstration purposes. Real LinkedIn scraping requires:

- Proper authentication and API access
- Compliance with LinkedIn's Terms of Service
- Respect for rate limits and robots.txt
- Legal considerations regarding data scraping
- User consent for data collection

**Always ensure you have proper authorization before scraping any website.**

## Features

- ✅ Extract profile data (currently using demo data)
- ✅ Transform and clean data
- ✅ Export to Excel format (.xlsx)
- ✅ Fallback to CSV format if Excel not available
- ✅ Rate limiting to be respectful to servers
- ✅ Comprehensive logging and metadata
- ✅ Configurable settings
- ✅ Error handling and validation

## Installation

1. Ensure you have Python 3.6+ installed
2. Install required dependencies:

```bash
pip install pandas openpyxl
```

## Usage

### Command Line Interface

```bash
# Run LinkedIn ETL pipeline with default settings
python mocker.py etl linkedin

# Specify custom output directory
python mocker.py etl linkedin --output=my_data

# Specify output format (excel or csv)
python mocker.py etl linkedin --format=excel
```

### Python API

```python
from mocker.etl import LinkedInETL

# Create ETL instance
etl = LinkedInETL(output_dir='my_linkedin_data')

# Run the complete pipeline
output_file = etl.run_pipeline()

# Or run individual steps
raw_data = etl.extract_profile_data()
transformed_data = etl.transform_data(raw_data)
output_file = etl.load_to_excel(transformed_data)
```

## Output Structure

The pipeline creates the following files:

```
linkedin_data/
├── linkedin_profiles_20231201_143022.xlsx  # Main data file
├── etl_metadata.json                       # Pipeline metadata
└── ...
```

### Excel/CSV Columns

| Column | Description |
|--------|-------------|
| full_name | Complete name of the profile |
| job_title | Current job title |
| company_name | Current company |
| location | Geographic location |
| years_of_experience | Years of professional experience |
| skills_list | Comma-separated list of skills |
| education_background | Educational background |
| linkedin_profile | LinkedIn profile URL |
| data_extracted_at | Timestamp of data extraction |

### Metadata File

```json
{
  "pipeline_run_time": "2023-12-01T14:30:22.123456",
  "total_records": 5,
  "output_file": "linkedin_data/linkedin_profiles_20231201_143022.xlsx",
  "profile_urls_count": 0
}
```

## Configuration

Modify `mocker/etl_config.py` to customize:

- Output directory and filename patterns
- Rate limiting settings
- Data fields to extract
- Excel/CSV export settings
- Demo data for testing

## Demo Data

The current implementation includes 5 sample profiles:

1. **John Doe** - Software Engineer at Tech Corp
2. **Jane Smith** - Data Scientist at Data Analytics Inc
3. **Bob Johnson** - Product Manager at Innovation Labs
4. **Alice Chen** - UX Designer at Design Studio
5. **Mike Williams** - DevOps Engineer at Cloud Solutions

## Error Handling

The pipeline includes comprehensive error handling:

- Graceful fallback to CSV if Excel export fails
- Validation of data fields
- Network timeout handling
- Rate limiting compliance
- Logging of all operations

## Ethical Considerations

When implementing real LinkedIn scraping:

1. **Respect robots.txt**: Always check and comply with the site's robots.txt file
2. **Rate limiting**: Implement appropriate delays between requests
3. **Terms of Service**: Ensure compliance with LinkedIn's ToS
4. **User consent**: Obtain proper consent for data collection
5. **Data privacy**: Follow GDPR, CCPA, and other privacy regulations
6. **API usage**: Prefer official APIs when available

## Example Output

```
🚀 Starting LinkedIn ETL Pipeline...
📊 Step 1: Extracting data...
✅ Extracted 5 profiles
🔄 Step 2: Transforming data...
✅ Transformed 5 records
💾 Step 3: Loading data to Excel...
✅ Data successfully exported to: linkedin_data/linkedin_profiles_20231201_143022.xlsx
🎉 ETL Pipeline completed successfully!
📁 Output directory: linkedin_data

📋 Pipeline Summary:
   • Data source: LinkedIn (demo data)
   • Output file: linkedin_data/linkedin_profiles_20231201_143022.xlsx
   • Format: Excel
   • Directory: linkedin_data
```

## Future Enhancements

- [ ] Real LinkedIn API integration
- [ ] Authentication system
- [ ] Advanced data validation
- [ ] Multiple export formats (JSON, XML)
- [ ] Data deduplication
- [ ] Incremental updates
- [ ] Advanced search and filtering
- [ ] Data visualization
- [ ] Scheduling and automation
- [ ] Cloud storage integration

## Troubleshooting

### Common Issues

1. **Excel export not working**: Install pandas and openpyxl
   ```bash
   pip install pandas openpyxl
   ```

2. **Permission errors**: Ensure write permissions to output directory

3. **Import errors**: Verify all dependencies are installed

4. **Rate limiting**: Adjust delay settings in configuration

For more help, check the logs in the output directory or enable debug logging.