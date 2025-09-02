from src.cool_names import get_only_names
from src.cool_names import writing_file, file_path

result = get_only_names("src/data/names.txt")
print(*result, sep="\n")
writing_file(result, file_path)
