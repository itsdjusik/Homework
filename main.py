from src.clean_names import get_only_names

# from src.clean_names import writing_file, file_path
from src.name_filter import create_name_filter, path_name_filter

result = get_only_names("src/data/names.txt")
print(*result, sep="\n")
# writing_file(result, file_path)
create_name_filter(path_name_filter)
