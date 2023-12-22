from pathlib import Path
import json
import configparser
import sys

def convert_ini_to_json(input_filepath):
  print(f"Reading file {input_filepath}")
  credentialsIni = configparser.ConfigParser()
  credentialsIni.read(input_filepath)

  dict = {}
  for section in credentialsIni.sections():
    dict[section] = {}
    for option in credentialsIni.options(section):
      dict[section][option] = credentialsIni.get(section, option)
  return json.dumps(dict, ensure_ascii=False)

def write_json_to_output_file(json_data):
  output_file = Path("./output/credentials.json")
  output_file.parent.mkdir(exist_ok=True, parents=True)
  output_file.write_text(json_data)
  print("Successfully converted ini file to JSON")
  
def main():
  input_filepath = sys.argv[1]
  json_data = convert_ini_to_json(input_filepath)
  write_json_to_output_file(json_data)

if __name__ == "__main__":
  main()