def count_token_in_corpus(corpus_path, token):
    count = 0
    try:
        with open(corpus_path, 'r') as f:
            for line in f:
                count += line.lower().split().count(token.lower())
    except FileNotFoundError:
        print(f"Error: The file {corpus_path} does not exist.")
    return count

def report_count(token, corpus_path='corpus.txt'):
    count = count_token_in_corpus(corpus_path, token)
    print(f"The term '{token}' shows up in the corpus {count} times.")

