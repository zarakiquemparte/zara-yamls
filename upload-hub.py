from huggingface_hub import HfApi, login
import argparse
import json
from pathlib import Path

home_dir = Path.home()

def get_args():
  parser = argparse.ArgumentParser()
  parser.add_argument("--model_path", type=str)
  parser.add_argument("--repo_id", type=str)
  return parser.parse_args()

args = get_args()

print("Uploading to HuggingFace hub...")

# login()
api = HfApi()
api.upload_folder(
  folder_path=args.model_path,
  repo_id=args.repo_id,
)
