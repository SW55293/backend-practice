'''
ASSIGNMENT
Complete the pair_document_with_format function. It takes two lists as input: doc_names and doc_formats. Each 
list contains strings. The doc_names list contains the names of documents, and the doc_formats list contains the 
file formats of the documents.

First, zip up the lists into a single list of tuples with the names as the first index and the formats as the 
second index in each tuple.

Next, filter the list of tuples to only include tuples where the format is one of the given valid_formats.

'''

valid_formats = [
    "docx",
    "pdf",
    "txt",
    "pptx",
    "ppt",
    "md",
]

# Don't edit above this line


def pair_document_with_format(doc_names, doc_formats):
    ll = list(zip(doc_names, doc_formats))
    return filter(lambda x: x[1] in valid_formats,ll)
