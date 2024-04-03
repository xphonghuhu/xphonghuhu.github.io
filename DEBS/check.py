import sys
import hashlib

def calculate_hash(file_path, hash_algorithm):
    try:
        with open(file_path, "rb") as file:
            content = file.read()
            hash_object = hashlib.new(hash_algorithm)
            hash_object.update(content)
            return hash_object.hexdigest()
    except FileNotFoundError:
        return "File not found"

def check_deb_file(file_path):
    print(f"Checking file: {file_path}")
    algorithms = ["md5", "sha1", "sha256", "sha512"]
    for algorithm in algorithms:
        hash_value = calculate_hash(file_path, algorithm)
        print(f"{algorithm.upper()}: {hash_value}")

# Lấy đường dẫn tệp tin .deb từ đối số dòng lệnh
if len(sys.argv) > 1:
    deb_file_path = sys.argv[1]
    check_deb_file(deb_file_path)
else:
    print("Please provide the path to the .deb file as an argument.")