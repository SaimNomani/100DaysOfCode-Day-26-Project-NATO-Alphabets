import pandas
nato_alphabets_df=pandas.read_csv('nato_phonetic_alphabet.csv')
nato_alphabets_dic={rows.letter:rows.code for(index, rows) in nato_alphabets_df.iterrows()}
name=(input("Enter your name: ")).upper()
nato_alphabets=[nato_alphabets_dic[letter] for letter in name if letter in nato_alphabets_dic.keys()]
print(nato_alphabets)