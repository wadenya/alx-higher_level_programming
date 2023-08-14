#!/usr/bin/node

function add (a, b) {
	return a + b
}

console.log(add(Number(process.argv[0]), Number(process.argv[1])));
