import pandas as pd
import matplotlib.pyplot as plt

demo = pd.read_csv("DEMO25Q4.txt", sep='$', encoding='latin1', low_memory=False)
drug = pd.read_csv("DRUG25Q4.txt", sep='$', encoding='latin1', low_memory=False)
reac = pd.read_csv("REAC25Q4.txt", sep='$', encoding='latin1', low_memory=False)

demo = demo.sort_values('caseversion', ascending=False).drop_duplicates('caseid')

drug = drug[['primaryid', 'drugname']]
reac = reac[['primaryid', 'pt']]

drug['drugname'] = drug['drugname'].str.upper().str.strip()

valid_ids = demo['primaryid']
drug = drug[drug['primaryid'].isin(valid_ids)]
reac = reac[reac['primaryid'].isin(valid_ids)]

df = drug.merge(reac, on='primaryid').dropna()

print(df.head())
print(df.shape)

top_reactions = df['pt'].value_counts().head(10)
print(top_reactions)
top_drugs = df['drugname'].value_counts().head(10)
print(top_drugs)

top_reactions.plot(kind='bar', title='Top Adverse Reactions')
plt.tight_layout()
plt.savefig("top_reactions.png")
plt.show()

top_drugs.plot(kind='bar', title='Top Drugs Reported')
plt.tight_layout()
plt.savefig("top_drugs.png")
plt.show()
