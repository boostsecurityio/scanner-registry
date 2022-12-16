import os
import yaml

# Get the directory of the script and the locations of the CWEs lists
script_dir = os.path.dirname(os.path.realpath(__file__))
cwes_files = {
    'owasp-top-10': os.path.join(script_dir, 'owasp-top-10_2021.cwes.lst'),
    'cwe-top-25': os.path.join(script_dir, 'cwe-top-25_2022.cwes.lst')
}

# Load the CWEs lists
cwes_lists = {}
for cwe_list_name, cwes_file in cwes_files.items():
    with open(cwes_file, 'r') as f:
        cwes_lists[cwe_list_name] = [line.strip() for line in f]

# Assume the root directory is two levels up from the script directory
root_dir = os.path.join(script_dir, '../../')

# Find and parse the rules.yaml files
for dirpath, _, filenames in os.walk(root_dir):
    for filename in filenames:
        if filename == 'rules.yaml':
            # Load and parse the rules.yaml file
            rules_file = os.path.join(dirpath, filename)
            with open(rules_file, 'r') as f:
                rules = yaml.safe_load(f)['rules']

            # Validate and fix the categories of each rule
            for rule_key, rule in rules.items():
                categories = rule['categories']
                for cwe_list_name, cwes_list in cwes_lists.items():
                    if any(cwe in cwes_list for cwe in categories) and cwe_list_name not in categories:
                        # Add the missing category to the list of categories
                        categories.append(cwe_list_name)
                        # Save the updated rules back to the YAML file
                        with open(rules_file, 'w') as f:
                            yaml.safe_dump({'rules': rules}, f, sort_keys=False)
                            print(f'Added "{cwe_list_name}" category to rule {rule_key} in {rules_file}')
