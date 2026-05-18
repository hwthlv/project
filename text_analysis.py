print("\n ТОП-10 САМЫХ ЧАСТЫХ СЛОВ")
word_counts = Counter(words)
top_10 = word_counts.most_common(10)

for i, (word, count) in enumerate(top_10, 1):
    bar_length = min(count, 20)
    bar = " " * bar_length
    print(f"{i:2d}. {word:15s} → {count:3d} раз(а) {bar}")
print("\n ЛЕКСИЧЕСКОЕ РАЗНООБРАЗИЕ (TTR)")
total_words = len(words)
unique_words = len(set(words))
ttr = unique_words / total_words if total_words > 0 else 0

print(f"Всего слов (Tokens):{total_words}")
print(f"Уникальных слов (Types):{unique_words}")
print(f"TTR:{ttr:.4f} ({ttr*100:.2f}%)")

print("\n КОЛЛОКАЦИИ (биграммы, встречающиеся чаще 2 раз)")
if len(words) >= 2:
    bigrams = [f"{words[i]} {words[i+1]}" for i in range(len(words)-1)]
    bigram_counts = Counter(bigrams)
    min_freq = 2
    collocations = {bigram: count for bigram, count in bigram_counts.items() 
                    if count > min_freq}
    
    if collocations:
        print(f"Найдено {len(collocations)} коллокаций:\n")
        sorted_collocations = sorted(collocations.items(), key=lambda x: x[1], reverse=True)
        for bigram, count in sorted_collocations:
            w1, w2 = bigram.split()
            obs_freq = count
            exp_freq = (word_counts[w1] * word_counts[w2]) / len(bigrams)
            pmi = math.log2((obs_freq / len(bigrams)) / (exp_freq / len(bigrams))) if exp_freq > 0 else 0
            print(f" • \"{bigram}\" → {count} раза (PMI: {pmi:.2f})")
    else:
        print("Нет биграмм с частотой выше 2")
else:
    print("Текст слишком короткий для поиска биграмм")

print("\n СРЕДНЯЯ ДЛИНА")

sentence_lengths = []
for sent in sentences:
    sent_words = clean_text(sent)
    sentence_lengths.append(len(sent_words))

word_lengths = [len(word) for word in words]

avg_sentence_len = statistics.mean(sentence_lengths) if sentence_lengths else 0
median_sentence_len = statistics.median(sentence_lengths) if sentence_lengths else 0
avg_word_len = statistics.mean(word_lengths) if word_lengths else 0
median_word_len = statistics.median(word_lengths) if word_lengths else 0

print("\n САМОЕ ДЛИННОЕ ПРЕДЛОЖЕНИЕ")

if sentence_lengths:
    max_len = max(sentence_lengths)
    longest_idx = sentence_lengths.index(max_len)
    longest_sentence = sentences[longest_idx]
    
    print(f"Длина: {max_len} слов / {len(longest_sentence)} символов")
    print(f"Текст: {longest_sentence[:200]}{'...' if len(longest_sentence) > 200 else ''}")
else:
    print("Нет предложений для анализа")


print("ИТОГОВАЯ СТАТИСТИКА")

print(f"Предложений:{len(sentences)}")
print(f"Слов:{total_words}")
print(f"Уникальных слов:{unique_words}")
print(f"TTR:{ttr:.3f}")
print(f"Средн. слово:{avg_word_len:.2f} симв.")
print(f"Средн. предл.:{avg_sentence_len:.1f} слов")
print(f"Коллокаций:{len(collocations) if 'collocations' in dir() else 0}")