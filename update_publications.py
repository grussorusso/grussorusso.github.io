import bibtexparser
import os
import re

BIBFILE="./publications.bib"
OUTDIR="content/publications"
SKIP_EXISTING=False
OVERWRITE_EXISTING=True

def supetrim(string):
    return string.replace("\\" , "").replace("{" , "").replace("}" , "").replace("\n"," ")

def mystrip(string):
    return string.strip(' "')

def parse_bib (bibfile):
    with open(bibfile) as bibtex_file:
        return bibtexparser.load(bibtex_file)

def write_entry (entry, outf):
    print("---", file=outf)

    authors = re.split(r"\s*and[\s\n]",entry['author'])
    authors_str = ''
    for author in authors:
        author_strip = supetrim(author)
        author_split = author_strip.split(',')
        if len(author_split)==2:
            author_strip = author_split[1].strip() + ' ' +author_split[0].strip()
        author_split = author_strip.split(' ')
        author_strip = author_split[0][0]+'. '+' '.join(map(str, author_split[1:]))
        authors_str = authors_str+ author_strip+', '
    outf.write(f'authors: "{authors_str[:-2]}"\n')
    outf.write(f'title: "{entry["title"]}"\n')

    if entry["ENTRYTYPE"] == "article":
        info = supetrim(entry["journal"])
        if "volume" in entry:
            info += ", " + entry["volume"]
        if "number" in entry:
            info += ", " + entry["number"]
        if "pages" in entry:
            info += ", " + entry["pages"]
    else:
        info = supetrim(entry["booktitle"])
    outf.write(f'info: "{info}"\n')
    outf.write(f'year: "{entry["year"]}"\n')

    if "url" in entry:
        outf.write(f'doi: "{mystrip(entry["url"])}"\n')
    if "pdf" in entry:
        outf.write(f'pdf: "{mystrip(entry["pdf"])}"\n')
    print("layout: publication", file=outf)
    print("---", file=outf)

    if "abstract" in entry:
        print(entry["abstract"], file=outf)


def process (entry):
    key = entry["ID"]
    if not entry["ENTRYTYPE"] in ["article", "inproceedings", "incollection"]:
        return

    # Determine output filename
    outfile = os.path.join(OUTDIR, f"{key}.md")
    if os.path.exists(outfile):
        if SKIP_EXISTING:
            return
        elif not OVERWRITE_EXISTING:
            outfile = outfile + ".new"

    print(f"Writing: {outfile}")
    with open(outfile, "w") as of:
        write_entry(entry, of)

db = parse_bib(BIBFILE)
for entry in db.entries:
    process(entry)
