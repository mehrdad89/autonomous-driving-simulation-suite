import argparse

def generate_report(analysis_file):
    print(f"Generating report from {analysis_file}")
    with open(analysis_file, 'r') as f:
        analysis = f.readlines()
    
    report_content = "Autonomous Driving Simulation Report\n"
    report_content += "-----------------------------------\n\n"
    for line in analysis:
        report_content += f"{line}"
    
    return report_content

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate a report from the analysis.")
    parser.add_argument('--analysis_file', type=str, required=True, help="Path to the analysis file.")
    parser.add_argument('--output', type=str, required=True, help="Output report file.")
    args = parser.parse_args()

    report = generate_report(args.analysis_file)
    
    with open(args.output, 'w') as f:
        f.write(report)
    print(f"Report generated and saved to {args.output}")
