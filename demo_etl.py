#!/usr/bin/env python3
"""
LinkedIn ETL Pipeline Demo

This script demonstrates the LinkedIn ETL pipeline functionality.
It extracts demo profile data and exports it to Excel format.

Usage:
    python demo_etl.py [output_directory]

Example:
    python demo_etl.py linkedin_demo_data
"""

import sys
import os
from datetime import datetime

# Add the project root to the path
current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, current_dir)

def run_demo(output_dir='linkedin_demo_data'):
    """Run the LinkedIn ETL pipeline demo"""
    
    print("🔗 LinkedIn ETL Pipeline Demo")
    print("=" * 50)
    print(f"📅 Demo run time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print(f"📁 Output directory: {output_dir}")
    print()
    
    try:
        from mocker.etl import LinkedInETL
        
        # Create ETL instance with demo configuration
        print("🔧 Initializing LinkedIn ETL pipeline...")
        etl = LinkedInETL(
            output_dir=output_dir,
            rate_limit=1,  # Faster for demo
            max_profiles=5
        )
        
        print("✅ ETL pipeline initialized successfully")
        print()
        
        # Run the complete pipeline
        print("🚀 Running complete ETL pipeline...")
        print("-" * 30)
        output_file = etl.run_pipeline()
        
        if output_file:
            print()
            print("🎉 Demo completed successfully!")
            print("=" * 50)
            print(f"📄 Output file: {output_file}")
            print(f"📂 Directory: {output_dir}")
            
            # Show file size
            if os.path.exists(output_file):
                file_size = os.path.getsize(output_file)
                print(f"📊 File size: {file_size:,} bytes")
            
            print()
            print("💡 Next steps:")
            print("   • Open the Excel file to view the extracted data")
            print("   • Check the etl_metadata.json for pipeline details")
            print("   • Modify mocker/etl_config.py to customize settings")
            print()
            print("⚠️  Remember: This demo uses mock data.")
            print("   Real LinkedIn scraping requires proper authentication!")
            
        else:
            print("❌ Demo failed - no output file generated")
            return False
            
    except ImportError as e:
        print(f"❌ Import error: {e}")
        print("💡 Make sure you're running from the project root directory")
        return False
    except Exception as e:
        print(f"❌ Demo failed: {e}")
        import traceback
        traceback.print_exc()
        return False
    
    return True

def main():
    """Main function to handle command line arguments"""
    
    # Check for output directory argument
    output_dir = 'linkedin_demo_data'
    if len(sys.argv) > 1:
        output_dir = sys.argv[1]
    
    # Run the demo
    success = run_demo(output_dir)
    
    if success:
        print(f"✅ LinkedIn ETL demo completed successfully!")
        sys.exit(0)
    else:
        print(f"❌ LinkedIn ETL demo failed!")
        sys.exit(1)

if __name__ == '__main__':
    main()