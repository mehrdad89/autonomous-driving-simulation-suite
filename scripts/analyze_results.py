import argparse

def analyze_results(result_file):
    print(f"Analyzing results from {result_file}")
    with open(result_file, 'r') as f:
        results = f.readlines()

    analysis = {}
    for line in results:
        key, value = line.strip().split(': ')
        analysis[key] = value
    
    # Simple analysis: Determine if the simulation was successful
    if analysis["success"] == "True" and analysis["collision"] == "False":
        analysis["status"] = "PASS"
    else:
        analysis["status"] = "FAIL"
    
    return analysis

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze simulation results.")
    parser.add_argument('--result_file', type=str, required=True, help="Path to the result file.")
    args = parser.parse_args()

    analysis = analyze_results(args.result_file)
    print(f"Analysis: {analysis}")
    output_file = f"{args.result_file.split('/')[-1].split('.')[0]}_analysis.txt"
    
    with open(output_file, 'w') as f:
        for key, value in analysis.items():
            f.write(f"{key}: {value}\n")
    print(f"Analysis saved to {output_file}")
