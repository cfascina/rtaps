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


def getAllManufacturers():
    return pd.Series(getRawData()["manufacturer"]).unique()


def getLimitedData(cols = None, lowerBound = None):
    if not cols:
        cols = limitedColumns
        
    pdData = getRawData()[cols]

    if lowerBound:
        (manufacturers, _) = getManufacturerCount(pdData, lowerBound)
        pdData = pdData[pdData["manufacturer"].isin(manufacturers)]

    return pdData


def getManufacturerCount(pdData, lowerBound = 0):
    counts = []
    manufacturers = []

    for manufacturer in getAllManufacturers():
        data = getManufacturerData(manufacturer, pdData)
        count = len(data.index)

        if count >= lowerBound:
            manufacturers.append(manufacturer)
            counts.append(count)

    return(manufacturers, list(zip(manufacturers, counts)))


def getManufacturerData(manufacturer, pdData):
    return pdData[(pdData["manufacturer"] == manufacturer)]


def getManufacturerIds(pdData):
    return sorted(mapManufacturerId(pdData).values())


def getManufacturerLabels(pdData):
    return [x.title() for x in getManufacturerNames(pdData)]


def getManufacturerNames(pdData):
    return sorted(list(pd.Series(pdData["manufacturer"]).unique()))


def getNumericData(pdData):
    return pdData.replace({"manufacturer": mapManufacturerId(pdData)})


def getRawData():
    data_file = "aux/datasets/automobile.csv"

    return pd.read_csv(data_file)


def mapManufacturerId(pdData):
    return {x: i for (i, x) in enumerate(getManufacturerNames(pdData))}


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
        