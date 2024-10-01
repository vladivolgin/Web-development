const net = require("net");

const client = net.connect({ host:"192.168.0.115", port: 3000 }, () => {
  client.write("Creepy potato");
});

client.on("data", (chunk) => {
  console.log("Received chunk: " + chunk.toString());
  client.end();
});