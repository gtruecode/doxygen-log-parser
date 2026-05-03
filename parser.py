import sys
import csv
import re
import os

def parse_doxygen_warnings(log_file):
    """
    Parses a Doxygen warnings log file and outputs a CSV.
    
    Doxygen warning lines look like:
    /path/to/file.cpp:42: warning: some message
    """
    # This pattern matches standard doxygen warning lines
    pattern = re.compile(r'^(.+?):(\d+):\s+warning:\s+(.+)$')
    
    output_file = "warnings_output.csv"
    
    with open(log_file, 'r') as infile, open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        writer.writerow(["Line", "File", "Message"])  # CSV header
        
        for raw_line in infile:
            raw_line = raw_line.strip()
            match = pattern.match(raw_line)
            if match:
                file_path = match.group(1)
                line_number = match.group(2)
                message = match.group(3)
                writer.writerow([line_number, file_path, message])
    
    print(f"Done! Output saved to: {output_file}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 parser.py <warnings_log_file>")
        sys.exit(1)
    
    log_file = sys.argv[1]
    if not os.path.exists(log_file):
        print(f"Error: File not found: {log_file}")
        sys.exit(1)
    
    parse_doxygen_warnings(log_file)