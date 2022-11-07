import os

class Page:
    def __init__(self, page_path, content):
        self.page_path = f"{page_path}.md"
        self.page_name = page_path
        self.content = content

def main():
    root = Page("root", "# Root Page\n")
    pages = [root]
    curdir = os.listdir(".")
    for file in curdir:
        if os.path.isdir(file) and file != '.obsidian':
            new_page = Page(file,f"# {file}\n")
            pages.append(new_page)
    pages = gen_root(pages)
    page = gen_page(pages)
    for page in pages:
        print(f"Path:\n{page.page_path}\nContent:\n{page.content}")
    write_page(pages)


def gen_root(pages):
    for page in pages:
        if page.page_path != "root.md":
            pages[0].content += f"## [[{page.page_name}]]\n"
    return pages

def gen_page(pages):
    for page in pages:
        if page.page_path != "root.md":
            files = os.listdir(page.page_name)
            for file in files:
                file_path = f"{page.page_name}/{file}"
                if os.path.isfile(file_path):
                    file_name = file.split('.')[0]
                    page.content += f"## [[{file_name}]]\n"
                elif os.path.isdir(file_path):
                    new_page = Page(f"{file_path}", f"# {file}\n")
                    new_page.page_path = f"./{file_path}.md"
                    pages.append(new_page)
    
    return pages

def write_page(pages):
    for page in pages:
        with open(page.page_path, 'w') as f:
            f.write(page.content)
if __name__ == "__main__":
    main()
