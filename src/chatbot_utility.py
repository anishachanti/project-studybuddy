import os

working_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(working_dir)

def get_chapter_list(selected_subject):
    subject_name = selected_subject.lower()
    chapters_dir = f"{parent_dir}/data/class_12/{subject_name}"
    
    # Defensive: if the directory doesn't exist return empty list
    if not os.path.isdir(chapters_dir):
        return []
        
    # Get list of PDF files and remove the .pdf extension
    chapters_list = []
    for filename in os.listdir(chapters_dir):
        if filename.lower().endswith('.pdf'):
            # Remove .pdf extension
            name = filename[:-4]
            chapters_list.append(name)
    
    # Simple alphabetical sort
    chapters_list.sort()
    return chapters_list