import os
import pandas as pd

# replace the paths in your need
path_lex = "G:/reading_battery/reading_battery_sti/lexical" 
path_sem = "G:/reading_battery/reading_battery_sti/semantic"
path_og_words = "G:/reading_battery/reading_battery_sti/words_4_antpost"

# make sure the output path exists, or create one
os.makedirs(path_lex, exist_ok=True)

# paths of files that will be input and output
input_file_lex = os.path.join(path_lex, 'lex_list.xlsx')
input_file_sem = os.path.join(path_sem, 'sem_list.xlsx')
input_file_og = os.path.join(path_og_words, 'words_450.xlsx')
output_file_lex_common = os.path.join(path_lex, 'repeated_words.csv')
output_file_lex_unique = os.path.join(path_lex, 'non_duplicated.csv')
output_file_sem_common = os.path.join(path_sem, 'repeated_words.csv')
output_file_sem_unique = os.path.join(path_sem, 'non_duplicated.csv')

# read the files
# compare lex_list.xlsx VS words_450.xlsx
df_A = pd.read_excel(input_file_lex, header=None)
df_B = pd.read_excel(input_file_og, header=None)
# uncomment line 27-28 to compare sem_list.xlsx VS words_450.xlsx, but do not forget to comment line 23-24
# df_A = pd.read_excel(input_file_sem, header=None)
# df_B = pd.read_excel(input_file_og, header=None)

# get words in df_A and df_B
words_A = df_A.iloc[:, 0]
words_B = df_B.iloc[:, 0]

# find the repeated words
common = words_A[words_A.isin(words_B)].drop_duplicates()
non_duplicates = words_A[~words_A.isin(words_B)].drop_duplicates()

# print the results: how many words are repeated or non-duplicated
print(f'Found {len(common)} repeated items：')
print(common)
print(f'Found {len(non_duplicates)} non-duplicated items：')
print(non_duplicates)

# save results to corresponding path
# save results to lexical folder
common.to_frame(name='word').to_csv(output_file_lex_common, index=False)
non_duplicates.to_frame(name='word').to_csv(output_file_lex_unique, index=False)

# uncomment line 49-50 to save results to semantic folder
# common.to_frame(name='word').to_csv(output_file_sem_common, index=False)
# non_duplicates.to_frame(name='word').to_csv(output_file_sem_unique, index=False)
