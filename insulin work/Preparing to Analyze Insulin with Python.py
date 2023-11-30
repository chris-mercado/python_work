def delete_texts_and_save(file_path, target_texts, output_file_path):
    # Read the content of the file
    with open(file_path, 'r') as file:
        content = file.read()

    # Modify the content (remove each target text)
    modified_content = content
    for target_text in target_texts:
        modified_content = modified_content.replace(target_text, '')

    # Write the modified content to a new file
    with open(output_file_path, 'w') as output_file:
        output_file.write(modified_content)

# Example usage
input_file_path = 'preproinsulin-seq.txt'  # Replace with your input file path
output_file_path = 'preproinsulin-seq-clean1.txt'  # Replace with your desired output file path
target_texts = [' ', 'ORIGIN', '//']
delete_texts_and_save(input_file_path, target_texts, output_file_path)