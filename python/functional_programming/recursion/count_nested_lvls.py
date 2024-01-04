'''
ASSIGNMENT
Complete the count_nested_levels function.

It should recursively search for the target_document_id in the nested_documents dictionary and 
return the number of nested levels of that document.

If the target document doesn't exist, the function should return -1.
'''

def count_nested_levels(nested_documents, target_document_id, level=1):
    # recursively search for the target_document_id in the 
    # nested_documents dictionary

    for ids in nested_documents:
        if ids == target_document_id:
            return level

        find_level = count_nested_levels(nested_documents[ids], target_document_id, level + 1)
            

        if find_level != -1:
            return find_level

    return -1
        
    
    # return the number of nested levels of that document.
