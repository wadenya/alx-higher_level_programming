#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (!error) {
    const todos = JSON.parse(body);
    const completed = {};
    todos.forEach((todo) => {
      if (todo.completed && completed[todo.userId] === undefined) {
        completed[todo.userid] = 1;
      } else if (todo.completed) {
        completed[todo.userid] += 1;
      }
    });
    console.log(completed);
  }
});
