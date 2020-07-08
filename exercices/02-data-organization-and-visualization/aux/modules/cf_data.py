import pandas as pd


limitedColumns = [
    "manufacturer",
    "price",
    "city mpg",
    "highway mpg",
    "horsepower",
    "weight",
    "riskiness",
    "losses"
]


# OK
def getManufacturerNames(pdData):
    return sorted(list(pd.Series(pdData["manufacturer"]).unique()))


# OK
def getManufacturerLabels(pdData):
    return [x.title() for x in getManufacturerNames(pdData)]


# OK
def mapManufacturerId(pdData):
    return {x: i for (i, x) in enumerate(getManufacturerNames(pdData))}


# OK
def getManufacturerIds(pdData):
    return sorted(mapManufacturerId(pdData).values())

# OK
def getRawData():
    data_file = "aux/datasets/automobile.csv"

    return pd.read_csv(data_file)


def getManufacturerData(manufacturer, pdData):
    return pdData[(pdData["manufacturer"] == manufacturer)]


def getManufacturerCount(pdData, lower_bound = 0):
    counts = []
    manufacturers = []

    for manufacturer in getAllManufacturers():
        data = getManufacturerData(manufacturer, pdData)
        count = len(data.index)

        if count >= lower_bound:
            manufacturers.append(manufacturer)
            counts.append(count)

    return(manufacturers, list(zip(manufacturers, counts)))


def getLimitedData(cols = None, lower_bound = None):
    if not cols:
        cols = limitedColumns
        
    data = getRawData()[cols]

    if lower_bound:
        (manufacturers, _) = getManufacturerCount(data, lower_bound)
        data = data[data["manufacturer"].isin(manufacturers)]

    return data


def normalizeColumn(colName, pdData, inverted = False):
    pdData[colName] -= pdData[colName].min()
    pdData[colName] /= pdData[colName].max()

    if inverted:
        pdData[colName] = 1 - pdData[colName]


def normalizeColumns(colNames, pdData):
    for name in colNames:
        normalizeColumn(name, pdData)


def normalizeColumnsInverted(colNames, pdData):
    for colName in colNames:
        normalizeColumn(colName, pdData, inverted = True)


def getAllManufacturers():
    return pd.Series(getRawData()["manufacturer"]).unique()


def getNumericData(pdData):
    return pdData.replace({"manufacturer": mapManufacturerId(pdData)})
