import pandas as pd

# d = pd.DataFrame(
#     [["Andy", 46, "Engineer"], ["Bob", 23, "HR"], ["Claire", 30, "Manager"]],
#     columns=["Name", "Age", "Position"],
#     index=["ID1", "ID2", "ID3"],
# )
# print(d)
# print(d.Name)
url = "https://en.wikipedia.org/wiki/Python_(programming_language)"
d = pd.read_html(url)[1]
print(d)
