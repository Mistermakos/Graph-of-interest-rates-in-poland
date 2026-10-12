import matplotlib.pyplot as plt
import xml.etree.ElementTree as ET

plt.style.use("Solarize_Light2")

tree = ET.parse("./data/stopy_procentowe.xml")
root = tree.getroot()

# dict struct: "type": obj, obj: {dates: [str], values: [int]}
series_data = {}

for pozycje in root:
    data_str = str(pozycje.get("obowiazuje_od"))
    data_str = data_str[0:7]

    for pozycja in pozycje:
        id = pozycja.get("id")
        procent = str(pozycja.get("oprocentowanie"))
        procent = float(procent.replace(",","."))

        if id not in series_data:
            series_data[id] = {"dates" : [], "values": []}

        series_data[id]["dates"].append(data_str)
        series_data[id]["values"].append(procent)

for id, tab in series_data.items():
    plt.plot(
      tab["dates"],
      tab["values"],
      label=f"{id}",
      marker="o"
  )
    
plt.legend()
plt.title("Graph of interest rates in time()")
plt.xlabel("Dates")
plt.ylabel("Interest (%)")

plt.xticks(rotation=45)
plt.tight_layout()

plt.show()
