import shutil
import sys

# Function to perform file deduplication
def file_deduplication(path):
    lines_seen = set()  # Set to store seen lines

    # Open the output file in write mode
    outfile = open(path + "new", "w")

    # Open the input file in read mode
    with open(path, "r") as f:
        for line in f:
            if line not in lines_seen:  # Check if line is not already seen
                outfile.write(line)  # Write line to output file
                lines_seen.add(line)  # Add line to set of seen lines

    outfile.close()  # Close the output file
    print("[*] Done")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("[!] Wrong parameter")
        print("Usage:")
        print(f"{sys.argv[0]} <filepath>")
        sys.exit(0)
    else:
        file_deduplication(sys.argv[1])  # Call the file_deduplication function with the provided filepath
