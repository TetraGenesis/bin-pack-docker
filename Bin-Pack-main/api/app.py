import flask
import json
import uuid
from typing import List, Dict

app = flask.Flask(__name__)
problemIDDict: Dict[int, str] = {}

def encodeBinSet(binDict: Dict[int, List[str]]) -> str:
    """Encode the specified bin set into a string"""
    encodedString: str = ''

    for bin in list(binDict.values()):
        if encodedString == '':
            encodedString += '#'
        
        for i in range(len(bin)):
            if i == len(bin) - 1:
                encodedString += str(bin[i])
            else:
                encodedString += str(bin[i]) + '!'

        if not encodedString.endswith('#'):
            encodedString += '#'

    return encodedString

def decodeBinSet(encodedString: str) -> Dict[int, List[str]]:
    """Decode the specified string into a bin set"""
    decodedBinsArr: List[str] = encodedString.split("#")
    decodedBins: Dict[int, List[str]] = {}

    for bin in decodedBinsArr:
        if bin: # if bin is not empty
            items: List[str] = bin.split("!")
            decodedBins[len(decodedBins)] = items
    
    return decodedBins

@app.route('/newproblem/')
def newProblem() -> str:
    """Generate a new problem."""
    problemID: int = uuid.uuid4().int % (10**10)
    problemIDDict[problemID] = encodeBinSet({})

    return json.dumps({
        'ID': problemID,
        'bins': problemIDDict[problemID]
    })

@app.route('/placeitem/<int:problemID>/<int:size>')
def placeItem(problemID: int, size: int) -> str:
    """Place an item in the bin."""
    if problemID not in problemIDDict:
        return json.dumps({'error': 'Invalid problemID'}), 400

    if size > 100 or size <= 0:
        return json.dumps({'error': 'Invalid size. Size must be between 1 and 100 inclusive.'}), 400

    decodedBins: Dict[int, List[str]] = decodeBinSet(problemIDDict[problemID])

    for bin, items in decodedBins.items():
        if not items or sum(map(int, items)) + size <= 100:
            items.append(str(size))
            problemIDDict[problemID] = encodeBinSet(decodedBins)
            return json.dumps({
                'ID': problemID,
                'size': size,
                'loc': bin,
                'bins': problemIDDict[problemID]
            })

    # No bin found, create a new one
    decodedBins[len(decodedBins)] = [str(size)]
    problemIDDict[problemID] = encodeBinSet(decodedBins)

    return json.dumps({
        'ID': problemID,
        'size': size,
        'loc': len(decodedBins) - 1,
        'bins': problemIDDict[problemID]
    })

@app.route('/endproblem/<int:problemID>')
def endproblem(problemID: int) -> str:
    """End the problem."""
    if problemID not in problemIDDict:
        return json.dumps({'error': 'Invalid problemID'}), 400

    decodedBins: Dict[int, List[str]] = decodeBinSet(problemIDDict[problemID])

    total_size: int = sum(int(item) for items in decodedBins.values() for item in items)
    num_items: int = sum(len(items) for items in decodedBins.values())
    finalEncodedBins: str = problemIDDict.pop(problemID)

    return json.dumps({
        'ID': problemID,
        'size': total_size,
        'items': num_items,
        'count': len(decodedBins),
        'wasted': 100 * len(decodedBins) - total_size,
        'bins': finalEncodedBins
    })

if __name__ == "__main__":
    host: str = 'localhost'
    port: int = 5000
    app.run(host=host, port=port, debug=True)