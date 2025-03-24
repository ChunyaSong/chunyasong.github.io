import os
import pandas as pd

path_lex = "G:/reading_battery/reading_battery_sti/lexical"
path_sem = "G:/reading_battery/reading_battery_sti/semantic"
path_og_words = "G:/reading_battery/reading_battery_sti/words_4_antpost"

# 确保输出文件夹存在（不存在则自动创建）
os.makedirs(path_lex, exist_ok=True)

# 构建文件路径
input_file_lex = os.path.join(path_lex, 'lex_list.xlsx')
input_file_sem = os.path.join(path_sem, 'sem_list.xlsx')
input_file_og = os.path.join(path_og_words, 'words_450.xlsx')
output_file_lex_common = os.path.join(path_lex, 'repeated_words.csv')
output_file_lex_unique = os.path.join(path_lex, 'non_duplicated.csv')
output_file_sem_common = os.path.join(path_sem, 'repeated_words.csv')
output_file_sem_unique = os.path.join(path_sem, 'non_duplicated.csv')

# 读取两个 xlsx|csv 文件, header=None确保第一行被视为数据而不是index,index_col=None确保第一列被视为数据而不是index
# df_A = pd.read_excel(input_file_lex, header=None)
# df = pd.read_csv('file.csv', encoding='utf-8')  # 原来的文件是csv文件的话，可以指定编码是utf-8,让其比对特殊字符时不会报错

df_A = pd.read_excel(input_file_lex, header=None)
#df_A = pd.read_excel(input_file_sem, header=None)
df_B = pd.read_excel(input_file_og, header=None)


# df_A = pd.read_excel('G:/reading_battery/reading_battery_sti/lexical/lex_list.xlsx.xlsx', header=None, index_col=None)
# df_B = pd.read_excel('words_450.xlsx', header=None, index_col=None)
# df_A = pd.read_csv('rl_words_450.csv', header=None, index_col=None)
# df_B = pd.read_csv('words_450.csv', header=None, index_col=None)



# 提取 A 文件中的文件名，并去掉 .bmp 后缀
# words_A = df_A.iloc[:, 0].str.replace('.bmp', '', regex=False)
words_A = df_A.iloc[:, 0]

# 提取 B 文件中的单词
words_B = df_B.iloc[:, 0]

# 找出重复项（交集）
common = words_A[words_A.isin(words_B)].drop_duplicates()
non_duplicates = words_A[~words_A.isin(words_B)].drop_duplicates()


# 显示或保存结果
print(f'Found {len(common)} repeated items：')
print(common)
print(f'Found {len(non_duplicates)} non-duplicated items：')
print(non_duplicates)


# 保存结果到输出目录
# 保存到lex文件夹下
# common.to_frame(name='word').to_csv(output_file_lex_common, index=False)
# non_duplicates.to_frame(name='word').to_csv(output_file_lex_unique, index=False)

# 保存到sem文件夹下
common.to_frame(name='word').to_csv(output_file_sem_common, index=False)
non_duplicates.to_frame(name='word').to_csv(output_file_sem_unique, index=False)