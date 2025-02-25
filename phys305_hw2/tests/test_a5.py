# This is a pytest script to test the YAML file submission for assignment 5.
# It ensures that the file is valid, properly formatted, and meets the requirements.

import yaml

def test_format():
    """
    Test the format of the YAML file 'phys305_hw2/a5.yaml' to ensure:
    1. It is a valid YAML file.
    2. It is a dictionary with the required keys: 'team' and 'date'.
    """

    # Open and read the YAML file
    with open("src/phys305_hw2/a5.yaml") as f:
        try:
            # Parse the YAML content safely
            d = yaml.safe_load(f)
        except yaml.YAMLError as e:
            # Print the error if YAML parsing fails
            print("YAML Parsing Error:", e)
            assert False, "Invalid YAML file format"

        # Ensure the loaded content is a dictionary
        assert isinstance(d, dict), "The YAML file must be a dictionary."
        assert d['team']
        assert d['date']
