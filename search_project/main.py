import os
import string
from colorama import init, Fore, Style

init()

index = {}

# Build index
for filename in os.listdir("documents"):
    path = os.path.join("documents", filename)

    with open(path, "r") as file:
        text = file.read().lower()
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()

    for word in words:
        if word not in index:
            index[word] = {}

        if filename not in index[word]:
            index[word][filename] = 1
        else:
            index[word][filename] += 1

# Banner
print(Fore.CYAN + "=" * 45)
print("        MINI SEARCH ENGINE")
print("=" * 45)
print("Type words to search documents.")
print("Type 'exit' to quit.")
print("=" * 45 + Style.RESET_ALL)

while True:
    user_input = input("Type word(s) or exit: ")

    if user_input == "exit":
        break

    user_input = user_input.lower()
    search_words = user_input.split()

    results = None

    for word in search_words:
        if word in index:
            if results is None:
                results = index[word].copy()
            else:
                new_results = {}
                for file in results:
                    if file in index[word]:
                        new_results[file] = results[file] + index[word][file]
                results = new_results
        else:
            results = {}
            break

    if results:
        sorted_results = sorted(results.items(), key=lambda x: x[1], reverse=True)

        print(Fore.GREEN + f"\nFound {len(sorted_results)} file(s):" + Style.RESET_ALL)

        for file, score in sorted_results:
            print(Fore.YELLOW + f"\n--- {file} (score: {score}) ---" + Style.RESET_ALL)

            path = os.path.join("documents", file)

            with open(path, "r") as f:
                lines = f.readlines()

            for line in lines:
                original_line = line.strip()
                clean_line = original_line.lower().translate(
                    str.maketrans('', '', string.punctuation)
                )

                match_found = False

                for word in search_words:
                    if word in clean_line:
                        match_found = True

                if match_found:
                    highlighted_line = original_line

                    for word in search_words:
                        highlighted_line = highlighted_line.replace(
                            word, word.upper()
                        ).replace(
                            word.capitalize(), word.upper()
                        )

                    print(Fore.MAGENTA + ">> " + highlighted_line + Style.RESET_ALL)

        print("-" * 45)

    else:
        print("No matching files.")