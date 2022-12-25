# convert size gets and array of bytes and generates a suitable 
# size unit.
def convert_size(bytes, suffix="B"):
    factor = 1024
    
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor