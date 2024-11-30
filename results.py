import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm
import statsmodels.formula.api as smf

df = pd.read_excel("final_data.xlsx")
df = df.rename(columns={"Gender": "is_female"})
df["is_female"] = df["is_female"].fillna(0)


df = df.rename(
    columns={
        "Candidato à Reeleição": "is_incumbent",
        "Foi eleito?": "was_elected",
        "% votos Lula 2022": "lula_vote_share",
    }
)

city_to_region = {
    # Norte
    "Belém": "Norte",
    "Belem": "Norte",
    "Manaus": "Norte",
    "Palmas": "Norte",
    "Porto Velho": "Norte",
    "Rio Branco": "Norte",
    # Nordeste
    "Aracaju": "Nordeste",
    "Fortaleza": "Nordeste",
    "João Pessoa": "Nordeste",
    "Maceio": "Nordeste",
    "Natal": "Nordeste",
    "Recife": "Nordeste",
    "Salvador": "Nordeste",
    "Teresina": "Nordeste",
    # Centro-Oeste
    "Campo Grande": "Centro-Oeste",
    "Cuiabá": "Centro-Oeste",
    "Cuiaba": "Centro-Oeste",
    "Goiânia": "Centro-Oeste",
    # Sudeste
    "Belo Horizonte": "Sudeste",
    "Rio De Janeiro": "Sudeste",
    "São Paulo": "Sudeste",
    # Sul
    "Curitiba": "Sul",
    "Porto Alegre": "Sul",
}

df["region"] = df["City"].map(city_to_region)

df["region"] = df["region"].fillna("Unknown")

# 1. Generate descriptive statistics table with means
numeric_cols = df.select_dtypes(include=[np.number]).columns
descriptive_table = df[numeric_cols].describe().T
descriptive_table.to_latex("descriptive_table.tex")

# 2. Boxplot of populism level by party with left parties in red and others in gray
party_colors = (
    df.groupby("Party")["is_left"]
    .first()
    .apply(lambda x: "red" if x == 1 else "gray")
    .to_dict()
)
parties_order = df["Party"].unique()

plt.figure(figsize=(12, 6))
ax = sns.boxplot(x="Party", y="populist_level", data=df, order=parties_order)
plt.xticks(rotation=90)
plt.title("Populism Level by Party")
plt.xlabel("Party")
plt.ylabel("Populism Level")

# Adjust box colors
for i, artist in enumerate(ax.artists):
    party = parties_order[i]
    col = party_colors.get(party, "gray")
    artist.set_edgecolor("black")
    artist.set_facecolor(col)
    # Adjust whiskers and medians
    for j in range(i * 6, i * 6 + 6):
        line = ax.lines[j]
        line.set_color("black")
        line.set_mfc("black")
        line.set_mec("black")

plt.tight_layout()
plt.savefig("populism_level_by_party.png")

# 2b. Boxplot of populism level by region
regions_order = ["Norte", "Nordeste", "Centro-Oeste", "Sudeste", "Sul"]
plt.figure(figsize=(10, 6))
ax = sns.boxplot(
    x="region", y="populist_level", data=df, order=regions_order, palette="Set3"
)
plt.title("Populism Level by Region")
plt.xlabel("Region")
plt.ylabel("Populism Level")
plt.tight_layout()
plt.savefig("populism_level_by_region.png")

# 3. Regression: populism level ~ is_left + is_incumbent + is_female + city fixed effects
populism_reg = smf.ols(
    formula="populist_level ~ is_left + is_incumbent + is_female + C(region)", data=df
).fit()

with open("populism_regression.tex", "w") as f:
    f.write(populism_reg.summary().as_latex())

# 4. Difference of means in populism level for specified groups
group_vars = ["is_incumbent", "was_elected", "is_left", "is_female"]
diff_means_table = []

for var in group_vars:
    groups = df.groupby(var)["populist_level"]
    mean_0 = groups.mean().get(0, np.nan)
    mean_1 = groups.mean().get(1, np.nan)
    diff = mean_1 - mean_0
    diff_means_table.append(
        {
            "Variable": var,
            "Group 0 Mean": mean_0,
            "Group 1 Mean": mean_1,
            "Difference": diff,
        }
    )

diff_means_df = pd.DataFrame(diff_means_table)
diff_means_df.to_latex("difference_means_table.tex", index=False)

# 5. Regression: was_elected ~ populist_level + lula_vote_share + is_incumbent + is_female + is_left + city fixed effects
election_reg = smf.logit(
    formula="was_elected ~ populist_level + lula_vote_share + is_incumbent + is_female + is_left",
    data=df,
).fit()


with open("election_regression.tex", "w") as f:
    f.write(election_reg.summary().as_latex())
