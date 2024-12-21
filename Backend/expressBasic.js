const express = require("express");
const app = express();  // App is the real use
const PORT = process.env.PORT || 4500;

app.listen(PORT, ()=> console.log(`Port running on ${PORT}`));

// Get request
// Eg link : http://localhost:4500/
app.get("/",(req, res) => {res.status(200).send("hello world")});

// Route Parameter
// Eg link : http://localhost:4500/route/24/sailash/test
app.get("/route/:id/:name/:temp", (req, res) => {
    console.log(req.params);
    res.status(200).send("I got it!");
})
