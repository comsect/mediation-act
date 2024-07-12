import os

# Directory where Markdown files will be created
directory = 'docs/en'

# Create the directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Generate Markdown files from file1.md to file170.md
for num in range(1, 65):
    filename = f'{num}.md'
    filepath = os.path.join(directory, filename)
    front_matter = f'''---\ndescription: {num}\n---'''
    # Create and write content to the Markdown file
    with open(filepath, 'w') as f:
        f.write(front_matter)
    
    print(f'Created {filename}')
