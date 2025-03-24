# Word List Comparison Script

This Python script compares word lists from different Excel files and identifies:

- Repeated words (present in both files)
- Non-duplicated words (present only in the first file)

## 📂 Input & Output

### Input Files
- `lex_list.xlsx` — lexical word list
- `sem_list.xlsx` — semantic word list
- `words_450.xlsx` — master word list for comparison

### Output Files
- Repeated and non-duplicated words will be saved as `.csv` files in the same folders as the input lists.

## 🛠 How to Use

1. **Set input and output paths** as needed in the `path_lex`, `path_sem`, and `path_og_words` variables.
2. **Choose the mode:**
   - By default, the script compares **lexical list** (`lex_list.xlsx`) vs **original word list** (`words_450.xlsx`).
   - To compare the **semantic list**, comment out lines 23–24 and uncomment lines 27–28.
3. **Run the script.**
4. Results will be printed in the console and saved in CSV format.

## ✨ Output Example
"Found 215 repeated items: apple banana ... Found 35 non-duplicated items: quokka xylophone ..."


## ✅ Notes

- The script assumes all input Excel files contain one word per row in the first column.
- Encoding issues (e.g., accents in Spanish) are handled by pandas if files are properly saved in UTF-8.

