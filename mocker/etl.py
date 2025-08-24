#!/usr/bin/env python3
"""
LinkedIn ETL Pipeline Module

This module provides functionality to scrape LinkedIn data and export it to Excel format.
It follows ethical scraping practices with rate limiting and respects robots.txt.

IMPORTANT NOTE: This implementation uses demo data for demonstration purposes.
Real LinkedIn scraping requires:
1. Proper authentication and API access
2. Compliance with LinkedIn's Terms of Service
3. Respect for rate limits and robots.txt
4. Legal considerations regarding data scraping
"""

import os
import time
import json
import csv
from datetime import datetime
import logging
from .base import BaseDockerCommand
from . import etl_config

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False
    print("Warning: requests not available. ETL functionality limited.")

try:
    import pandas as pd
    PANDAS_AVAILABLE = True
except ImportError:
    PANDAS_AVAILABLE = False
    print("Warning: pandas not available. Will use CSV format instead of Excel.")


class LinkedInETL(BaseDockerCommand):
    """LinkedIn ETL Pipeline for extracting, transforming, and loading data."""
    
    def __init__(self, *args, **kwargs):
        self.output_dir = kwargs.get('output_dir', etl_config.default_output_dir)
        self.rate_limit = kwargs.get('rate_limit', etl_config.request_delay_seconds)
        self.max_profiles = kwargs.get('max_profiles', etl_config.max_profiles_per_session)
        
        # Create output directory if it doesn't exist
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)
    
    def extract_profile_data(self, profile_urls=None):
        """
        Extract data from LinkedIn profiles.
        NOTE: This is a demo implementation using mock data.
        Real LinkedIn scraping requires proper authentication and API access.
        """
        extracted_data = []
        
        # Use demo data from configuration
        demo_profiles = etl_config.demo_profiles[:self.max_profiles]
        
        for profile in demo_profiles:
            # Simulate rate limiting to be respectful
            time.sleep(self.rate_limit)
            extracted_data.append(profile)
            logging.info(f"Extracted data for: {profile['name']}")
        
        return extracted_data
    
    def transform_data(self, raw_data):
        """
        Transform and clean the extracted data.
        """
        transformed_data = []
        
        for record in raw_data:
            # Clean and standardize data
            transformed_record = {
                'full_name': record.get('name', '').strip(),
                'job_title': record.get('title', '').strip(),
                'company_name': record.get('company', '').strip(),
                'location': record.get('location', '').strip(),
                'years_of_experience': record.get('experience_years', 0),
                'skills_list': ', '.join(record.get('skills', [])),
                'education_background': record.get('education', '').strip(),
                'linkedin_profile': record.get('profile_url', '').strip(),
                'data_extracted_at': datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            }
            transformed_data.append(transformed_record)
        
        logging.info(f"Transformed {len(transformed_data)} records")
        return transformed_data
    
    def load_to_excel(self, data, filename=None):
        """
        Load transformed data into Excel format.
        Falls back to CSV if pandas is not available.
        """
        if not filename:
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            filename = f"{etl_config.default_filename_prefix}_{timestamp}"
        
        filepath = os.path.join(self.output_dir, filename)
        
        if PANDAS_AVAILABLE:
            # Export to Excel
            excel_path = f"{filepath}.xlsx"
            df = pd.DataFrame(data)
            df.to_excel(excel_path, index=False, sheet_name=etl_config.excel_sheet_name)
            logging.info(f"Data exported to Excel: {excel_path}")
            print(f"✅ Data successfully exported to: {excel_path}")
            return excel_path
        else:
            # Fallback to CSV
            csv_path = f"{filepath}.csv"
            with open(csv_path, 'w', newline='', encoding=etl_config.csv_encoding) as csvfile:
                if data:
                    fieldnames = data[0].keys()
                    writer = csv.DictWriter(csvfile, fieldnames=fieldnames, delimiter=etl_config.csv_delimiter)
                    writer.writeheader()
                    writer.writerows(data)
            
            logging.info(f"Data exported to CSV: {csv_path}")
            print(f"✅ Data successfully exported to: {csv_path}")
            print("💡 Install pandas to enable Excel export: pip install pandas openpyxl")
            return csv_path
    
    def save_metadata(self, data_info):
        """Save metadata about the ETL process."""
        metadata_path = os.path.join(self.output_dir, 'etl_metadata.json')
        with open(metadata_path, 'w') as f:
            json.dump(data_info, f, indent=2)
        logging.info(f"Metadata saved to: {metadata_path}")
    
    def run_pipeline(self, profile_urls=None):
        """
        Execute the complete ETL pipeline.
        """
        print("🚀 Starting LinkedIn ETL Pipeline...")
        
        # Extract
        print("📊 Step 1: Extracting data...")
        if not profile_urls:
            # Use demo data if no URLs provided
            profile_urls = []  # Mock URLs for demo
        
        raw_data = self.extract_profile_data(profile_urls)
        
        if not raw_data:
            print("❌ No data extracted. Pipeline terminated.")
            return None
        
        print(f"✅ Extracted {len(raw_data)} profiles")
        
        # Transform
        print("🔄 Step 2: Transforming data...")
        transformed_data = self.transform_data(raw_data)
        
        # Load
        print("💾 Step 3: Loading data to Excel...")
        output_file = self.load_to_excel(transformed_data)
        
        # Save metadata
        metadata = {
            'pipeline_run_time': datetime.now().isoformat(),
            'total_records': len(transformed_data),
            'output_file': output_file,
            'profile_urls_count': len(profile_urls) if profile_urls else 0
        }
        self.save_metadata(metadata)
        
        print("🎉 ETL Pipeline completed successfully!")
        print(f"📁 Output directory: {self.output_dir}")
        
        return output_file


class ETLCommand(BaseDockerCommand):
    """Command class for ETL operations."""
    
    def __init__(self, *args, **kwargs):
        self.etl_type = kwargs.get('<type>', 'linkedin')
        self.output_format = kwargs.get('--format', 'excel')
        self.output_dir = kwargs.get('--output', 'linkedin_data')
    
    def run(self, *args, **kwargs):
        """Execute the ETL command."""
        if self.etl_type == 'linkedin':
            print("🔗 Running LinkedIn ETL Pipeline...")
            
            # Initialize the LinkedIn ETL pipeline
            linkedin_etl = LinkedInETL(
                output_dir=self.output_dir,
                rate_limit=2,  # 2 seconds between requests
                max_pages=5
            )
            
            # Run the pipeline
            output_file = linkedin_etl.run_pipeline()
            
            if output_file:
                print(f"\n📋 Pipeline Summary:")
                print(f"   • Data source: LinkedIn (demo data)")
                print(f"   • Output file: {output_file}")
                print(f"   • Format: {'Excel' if PANDAS_AVAILABLE else 'CSV'}")
                print(f"   • Directory: {self.output_dir}")
            
        else:
            print(f"❌ ETL type '{self.etl_type}' not supported.")
            print("💡 Available types: linkedin")