def get_creators(record: dict) -> list:
    match record:
        case {'type': 'book', 'api': x, 'authors': [*names]}:
            return [names]
        case {'type': 'book', 'api': 1, 'authors': name}:
            return [name]
        case _:
            raise ValueError(f'Invalid record: {record!r}')

# pattern matching with dicts, mapping patterns succeed on partial matches
# if we add a 'title' key to the record, it will match even with that 
# key in the match stmt
