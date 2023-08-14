#!/usr/bin/node
const args = process.argv.slice(2);
const size = parseInt(args[0], 10);

if (isNaN(size)) {
	console.log("Missing size");
}
else {
	for (let y = 0; y < size; y++) {
		console.log('X' repeat(size));
	}
}
