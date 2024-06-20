// dice_roller.js

function rollDie(numFaces) {
    // Ensure numFaces is a positive integer
    numFaces = Math.floor(numFaces);
    if (numFaces < 1) {
        throw new Error("Number of faces must be a positive integer.");
    }

    // Generate a random number between 1 and numFaces (inclusive)
    var result = Math.floor(Math.random() * numFaces) + 1;
    return result;
}

function roll6() {
    document.getElementById("output").innerHTML = rollDie(6)
}