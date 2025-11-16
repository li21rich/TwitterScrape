import re


def remove_none(input_string):
    pattern = r":::>\s*#(\d+\.)\s*((?:(?!<:::).)*)\s*<:::(.*?)\s*(?=(?::::>|$))"
    matches = re.findall(pattern, input_string, re.DOTALL)
    tweet_dict = {}
    for match in matches:
        tweet_number = match[0].strip()
        data = match[1].strip()
        content = match[2].strip()
        key = f"{tweet_number} {data}"
        tweet_dict[key] = content
    return tweet_dict

def remove_duplicates(input_string):
    pattern = r":::>\s*#(\d+\.)\s*((?:(?!<:::).)*)\s*<:::(.*?)\s*(?=(?::::>|$))"
    matches = re.findall(pattern, input_string, re.DOTALL)
    tweet_dict = {}
    for match in matches:
        tweet_number = match[0].strip()
        data = match[1].strip()
        content = match[2].strip()
        key = f"{tweet_number} {data}"
        tweet_dict[key] = content
    seen_values = set()
    tweet_dict = {key: value for key, value in tweet_dict.items() if value not in seen_values and not seen_values.add(value)}
    return tweet_dict


def remove_shorts(input_dict, min):
    # you can modify this number to allow shorter or longer tweets through this:
    min_alphabetic_letters = int(min)
    return {key: value for key, value in input_dict.items() if len(re.sub(r'[^a-zA-Z]', '', value)) > min_alphabetic_letters}


