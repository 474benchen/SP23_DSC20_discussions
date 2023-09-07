def disc_example(file_path):
    '''
    Function that takes in a file, reads the data as a list, and then
    converts each line into a dictionary entry where the first 
    element is the key and the subsequent elements are values.

    Args:
        file_path (string): name of the file being accessed
    
    Returns:
        A dictionary where the keys are the first element
        of every line in the file and the values are the 
        subsequent elements.

    // Broken version of the function
    >>> disc_example('files/disc2_ex.txt')
    {'DSC10': ['Suraj'], 'DSC20': ['Marina'], 'DSC30': ['Marina', 'Sooh'], 'DSC40A': ['Janine'], 'DSC40B': ['Wang'], 'DSC80': []}
    '''
    info_dict = {}
    with open(file_path, 'r') as f
        lines = f.readlines
        for line in lines:
            words = line.split()
            line_key = words[0]
            line_values = words[1]
            info_dict[line_key] += line_values
    return info_dict