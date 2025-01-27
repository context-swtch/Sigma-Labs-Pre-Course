def outed(meet, boss):
  sum_happiness = sum(meet.values()) + meet[boss] 
  average_happiness = sum_happiness / len(meet)  

  if average_happiness <= 5:
      return 'Get Out Now!'
  else:
      return 'Nice Work Champ!'

def boredom(staff):
    boredom_scores = {'accounts': 1, 'finance': 2, 'canteen': 10, 'regulation': 3, 'trading': 6, 
                'change': 6, 'IS': 8, 'retail': 5, 'cleaning': 4, 'pissing about': 25}

    total_score = 0
    for employee, department in staff.items():
        total_score += boredom_scores.get(department, 0)  # Use .get to handle missing departments gracefully

    if total_score <= 80:
        return 'kill me now'
    elif total_score < 100 and total_score > 80:
        return 'i can handle this'
    elif total_score > 100:
        return 'party time!!'


def topKFrequent(self, words: List[str], k: int) -> List[str]:
    string_dictionary = {}

    for j in words:
        if j not in string_dictionary.keys():
            string_dictionary[j] = 1
        else:
            string_dictionary[j] += 1

    sorted_words = sorted(string_dictionary.keys(), key=lambda word: (-string_dictionary[word], word))

    return sorted_words[:k]



def decodeMessage(self, key: str, message: str) -> str:
    i = 0
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 
    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    seen = set()
    key_list = [char for char in key if char != ' ' and char not in seen and not seen.add(char)]
    substitution_table = dict(zip(key_list, alphabet))

    sentence = []
    for c in message:
        if c in substitution_table:
            sentence.append(substitution_table[c])
        else:
            sentence.append(c)

    return ''.join(sentence)



def romanToInt(self, s: str) -> int:
    roman_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    subtraction_cases = {
        'I': {'V', 'X'},
        'X': {'L', 'C'},
        'C': {'D', 'M'}
    }
    total = 0
    skip = False
    for i, x in enumerate(s):
        if skip:
            skip = False
            continue

        if x in subtraction_cases and i + 1 < len(s) and s[i + 1] in subtraction_cases[x]:
            total += roman_dict[s[i + 1]] - roman_dict[x]
            skip = True
        else:
            total += roman_dict[x]

    return total

