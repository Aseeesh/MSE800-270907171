# process_junk.py
# Script to process junk.txt file with proper file handling

def process_junk_file():
    """
    Process junk.txt file:
    1. Count total lines
    2. Add new line at the end
    3. Convert all text to lowercase
    4. Save processed file
    """
    
    filename = "junk.txt"
    
    # Step 1: Read and count lines
    print("=" * 50)
    print("PROCESSING JUNK.TXT FILE")
    print("=" * 50)
    
    # Open file for reading
    infile = open(filename, "r")
    
    # Read all lines into a list
    lines = infile.readlines()
    total_lines = len(lines)
    print(f"✅ Total number of lines: {total_lines}")
    
    # Close the file after reading
    infile.close()
    print("✅ File closed after reading")
    
    # Step 2 & 3: Process the content
    print("\n🔄 Processing file contents...")
    
    # Convert all text to lowercase and strip trailing newlines
    processed_lines = []
    for line in lines:
        # Convert to lowercase and keep the newline character
        processed_line = line.lower()
        processed_lines.append(processed_line)
    
    # Step 2: Add new line at the end
    new_line = "text file nanalyssis\n"
    processed_lines.append(new_line)
    
    print(f"✅ Added new line: '{new_line.strip()}'")
    print(f"✅ Converted all text to lowercase")
    
    # Step 4: Save the processed file
    print("\n💾 Saving processed file...")
    
    # Open file for writing (this will overwrite the original)
    outfile = open(filename, "w")
    
    # Write all processed lines
    for line in processed_lines:
        outfile.write(line)
    
    # Close the file after writing
    outfile.close()
    print("✅ Processed file saved successfully!")
    print("✅ File closed after writing")
    
    # Verify the changes
    print("\n" + "=" * 50)
    print("VERIFICATION")
    print("=" * 50)
    
    # Reopen to verify
    verify_file = open(filename, "r")
    new_lines = verify_file.readlines()
    verify_file.close()
    
    print(f"✅ New total lines: {len(new_lines)}")
    print(f"✅ Last line: {new_lines[-1].strip()}")
    print(f"✅ First line (lowercase): {new_lines[0].strip()}")
    
    return True

# Execute the function
if __name__ == "__main__":
    try:
        process_junk_file()
        print("\n" + "=" * 50)
        print("🎉 TASK COMPLETED SUCCESSFULLY!")
        print("=" * 50)
    except FileNotFoundError:
        print("❌ Error: junk.txt file not found in the current directory!")
    except Exception as e:
        print(f"❌ An error occurred: {e}")