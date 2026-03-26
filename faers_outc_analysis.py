print("Running OUTC script")

import pandas as pd
import matplotlib.pyplot as plt

demo = pd.read_csv("DEMO25Q4.txt",sep='$',encoding='latin1',low_memory=False)
drug = pd.read_csv("DRUG25Q4.txt", sep='$', encoding='latin1', low_memory=False)
reac = pd.read_csv("REAC25Q4.txt", sep='$', encoding='latin1',low_memory=False)
outc = pd.read_csv("OUTC25Q4.txt", sep='$', encoding='latin1', low_memory=False)

demo = demo[['primaryid']]
drug = drug[['primaryid','drugname']]
reac = reac[['primaryid','pt']]
outc = outc[['primaryid','outc_cod']]

SERIOUS_CODES = ['DE', 'LT', 'HO', 'DS', 'CA', 'RI']
serious_ids = outc[outc['outc_cod'].isin(SERIOUS_CODES)]['primaryid'].drop_duplicates()
non_serious_ids = demo[~demo['primaryid'].isin(serious_ids)]['primaryid'].drop_duplicates()
print(f"Serious IDs: {len(serious_ids)}, Non-serious IDs: {len(non_serious_ids)}")


sample_serious = serious_ids.sample(5000, random_state=42)
sample_non_serious = non_serious_ids.sample(5000, random_state=42)

sample_ids = pd.concat([sample_serious, sample_non_serious])

demo_s = demo[demo['primaryid'].isin(sample_ids)]
drug_s = drug[drug['primaryid'].isin(sample_ids)]
reac_s = reac[reac['primaryid'].isin(sample_ids)]


outc_sample = outc[outc['primaryid'].isin(sample_ids)].copy()
outc_sample['is_serious'] = outc_sample['outc_cod'].isin(SERIOUS_CODES)
outc_agg = outc_sample.groupby('primaryid')['is_serious'].any().reset_index()

df_s = demo_s.merge(drug_s, on='primaryid') \
             .merge(reac_s, on='primaryid') \
             .merge(outc_agg, on='primaryid', how='left')

df_s = df_s.dropna(subset=['pt','drugname'])


df_s['is_serious'] = df_s['is_serious'].fillna(False)

serious_df = df_s[df_s['is_serious'] == True]
non_serious_df = df_s[df_s['is_serious'] == False]

print(f"Serious rows: {len(serious_df)}, Non-serious rows: {len(non_serious_df)}")

overall_pct = df_s['pt'].value_counts(normalize=True).head(10)
serious_pct = serious_df['pt'].value_counts(normalize=True).head(10)
non_serious_pct = non_serious_df['pt'].value_counts(normalize=True).head(10)

comparison = pd.concat([overall_pct, serious_pct, non_serious_pct], axis=1)
comparison.columns = ['Overall', 'Serious', 'Non-serious']
print(comparison)
comparison.to_csv("reaction_comparison_table.csv")

overall_pct.plot(kind='bar', title='Overall Reaction Distribution (Subset)')
plt.tight_layout()
plt.savefig("overall_subset_reactions.png")
plt.show()

serious_pct.plot(kind='bar', title='Serious Reaction Distribution')
plt.tight_layout()
plt.savefig("serious_subset_reactions.png")
plt.show()

non_serious_pct.plot(kind='bar', title='Non-Serious Reaction Distribution')
plt.tight_layout()
plt.savefig("non_serious_subset_reactions.png")
plt.show()