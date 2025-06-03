import os
import yaml


class LoadData:
    def __init__(self):
        file_mapping = {
            "personal": "personal.yaml",
            "education": "education.yaml",
            "experience": "experience.yaml",
            "research": "research.yaml",
            "presentations": "presentations.yaml",
            "teaching": "teaching.yaml",
            "awards": "awards.yaml",
            "publications": "publications.yaml",
        }

        for key, filename in file_mapping.items():
            path = os.path.join("data", filename)
            if not os.path.exists(path):
                raise FileNotFoundError(f"YAML file not found: {path}")

            with open(path, "r") as f:
                data = yaml.safe_load(f)

            # Directly assign parsed data (list/dict) to an attribute
            setattr(self, key, data)
