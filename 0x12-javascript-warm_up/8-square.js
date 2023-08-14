#!/usr/bin/node

const size = Math.floor(Number(process.argv[2]));

if (isNaN(size)) {
	console.log("Missing size");
}
else {
	for (let y = 0; y < size; y++) {
		let row = "";
		for (let p = 0; p < size; p++) row += 'X';
		console.log(row);
	}
}
