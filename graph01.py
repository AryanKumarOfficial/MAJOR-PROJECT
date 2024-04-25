import matplotlib.pyplot as plt
from scrapping01 import final,title

print(type(final))

# extract words and their frequencies

words = list(final.keys())
frequencies =list(final.values())

plt.figure(figsize=(10, 6))
bars  =plt.bar(words, frequencies, color="skyblue",edgecolor="black")
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval, round(yval, 1), ha='center', va='bottom')


plt.xlabel("Words",fontdict={"fontsize":14})
plt.ylabel("Occurrences",fontdict={"fontsize":14})
plt.title(f"Comments Frequencies in {title}",fontdict={"fontsize":16})
plt.xticks(rotation=45, ha="right", fontsize=12)

# remove top and right spines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# plt.grid(axis='y', linestyle='--', alpha=0.7)

plt.tight_layout()
plt.show()


