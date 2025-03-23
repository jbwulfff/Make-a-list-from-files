import os
import argparse
 
def concat_all_files(root_dir, output_file, exclude_exts=None, include_only_exts=None, skip_dirs=None):
    # Set defaults
    if exclude_exts is None:
        exclude_exts = []
    if skip_dirs is None:
        skip_dirs = []
    with open(output_file, 'w', encoding='utf-8') as outfile:
        for dirpath, dirnames, filenames in os.walk(root_dir):
            # Skip directories in the skip_dirs list
            dirnames[:] = [d for d in dirnames if d not in skip_dirs]
            # If include_only_exts is provided, use only those extensions
            if include_only_exts:
                text_files = [f for f in filenames if any(f.endswith(ext) for ext in include_only_exts)]
            else:
                # Otherwise use the default list but exclude specified extensions
                text_files = [f for f in filenames if f.endswith((
                    # Text documents
                    '.md', '.txt', '.text', '.markdown', '.rst', '.asciidoc', '.adoc', '.asc',
                    # Programming languages
                    '.py', '.js', '.java', '.c', '.cpp', '.cs', '.php', '.rb', '.go', '.swift', '.kt', '.ts',
                    '.html', '.css', '.scss', '.sass', '.less', '.json', '.xml', '.yaml', '.yml', 
                    '.sh', '.bash', '.ps1', '.bat', '.cmd',
                    # Configuration files
                    '.ini', '.cfg', '.conf', '.config', '.properties', '.toml', '.env',
                    # SQL and database
                    '.sql', '.graphql', '.prisma',
                    # Other common code files
                    '.r', '.dart', '.scala', '.groovy', '.lua', '.pl', '.pm', '.hs', '.elm', '.ex', '.exs',
                    '.erl', '.fs', '.fsx', '.f90', '.f95', '.f03', '.f08',
                    # Documentation files
                    '.tex', '.wiki', '.org'
                )) and not any(f.endswith(ext) for ext in exclude_exts)]

            for text_file in text_files:
                file_path = os.path.join(dirpath, text_file)
                rel_path = os.path.relpath(file_path, root_dir)
                file_ext = os.path.splitext(text_file)[1].lower()

                # Add language-specific markdown code block for programming files
                if file_ext in ('.py', '.ipynb'):
                    lang = 'python'
                elif file_ext in ('.js', '.ts'):
                    lang = 'javascript'
                elif file_ext == '.java':
                    lang = 'java'
                elif file_ext in ('.c', '.cpp', '.h', '.hpp'):
                    lang = 'cpp'
                elif file_ext == '.cs':
                    lang = 'csharp'
                elif file_ext == '.php':
                    lang = 'php'
                elif file_ext == '.rb':
                    lang = 'ruby'
                elif file_ext == '.go':
                    lang = 'go'
                elif file_ext == '.swift':
                    lang = 'swift'
                elif file_ext == '.html':
                    lang = 'html'
                elif file_ext in ('.css', '.scss', '.sass', '.less'):
                    lang = 'css'
                elif file_ext == '.json':
                    lang = 'json'
                elif file_ext == '.xml':
                    lang = 'xml'
                elif file_ext in ('.yaml', '.yml'):
                    lang = 'yaml'
                elif file_ext in ('.sh', '.bash'):
                    lang = 'bash'
                elif file_ext == '.sql':
                    lang = 'sql'
                elif file_ext == '.r':
                    lang = 'r'
                elif file_ext in ('.md', '.markdown'):
                    lang = 'markdown'
                else:
                    lang = 'text'

                outfile.write(f'\n<!-- File: {rel_path} -->\n\n```{lang}\n')
                try:
                    with open(file_path, 'r', encoding='utf-8') as infile:
                        content = infile.read()
                        outfile.write(content)
                        if not content.endswith('\n'):
                            outfile.write('\n')
                        outfile.write('```\n')
                except Exception as e:
                    outfile.write(f'<!-- Error reading file: {str(e)} -->\n```\n')
 
def main():
    parser = argparse.ArgumentParser(description='Concatenate text and code files from a directory into a single file.')
    parser.add_argument('input_dir', help='Input directory containing text and code files')
    parser.add_argument('-o', '--output', help='Output filename (default: input_directory_name_combined.md)')
    parser.add_argument('-e', '--exclude', help='Comma-separated list of file extensions to exclude (e.g. ".git,.jpg,.png")')
    parser.add_argument('-i', '--include-only', help='Comma-separated list of file extensions to include (overrides default list)')
    parser.add_argument('-s', '--skip-dirs', help='Comma-separated list of directory names to skip (e.g. ".git,node_modules,venv")')
    args = parser.parse_args()

    input_dir = os.path.normpath(args.input_dir)

    if not args.output:
        dir_name = os.path.basename(input_dir)
        output_file = f"{dir_name}_combined.md"
    else:
        output_file = args.output

    exclude_exts = args.exclude.split(',') if args.exclude else []
    include_only_exts = args.include_only.split(',') if args.include_only else None
    skip_dirs = args.skip_dirs.split(',') if args.skip_dirs else ['.git', 'node_modules', '__pycache__', '.venv', 'venv', '.idea', '.vs']

    print(f"Concatenating text and code files from '{input_dir}' into '{output_file}'...")
    concat_all_files(input_dir, output_file, exclude_exts, include_only_exts, skip_dirs)
    print(f"Done! Output written to '{output_file}'")
 
if __name__ == "__main__":
    main()
