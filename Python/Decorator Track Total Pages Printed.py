def track_pages(fun):
    total_pages=0
    def inner(document_name,pages):
        nonlocal total_pages
        total_pages+=pages
        fun(document_name,pages)
        print("currently printing",total_pages)
    return inner
@track_pages
def print_document(document_name,pages):
    print(document_name)
    print(pages)
print_document("python",5)
print_document("python",6)
print_document("java",72)