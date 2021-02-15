def traverse(json_obj, path_str):
    if not path_str:
        return json_obj
    path_segs = path_str.split('/')
    current_obj = json_obj
    for seg in path_segs:
        if not seg:
            continue
        if type(current_obj) == list:
            current_obj = current_obj[int(seg)]
        else:
            current_obj = current_obj[seg]
    return current_obj