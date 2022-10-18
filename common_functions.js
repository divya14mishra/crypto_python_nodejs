const crypto = require("crypto");
require("dotenv").config();

var cipher = crypto.createCipheriv(
  process.env.ALGORITHM,
  process.env.SECURITYKEY,
  process.env.INITVECTOR
);
cipher.setAutoPadding(false);
var decipher = crypto.createDecipheriv(
  process.env.ALGORITHM,
  process.env.SECURITYKEY,
  process.env.INITVECTOR
);
decipher.setAutoPadding(false);

function toB64padded(plaintext, blocksize) {
  var bufPlaintext = Buffer.from(plaintext, "utf8");
  var bufPlaintextB64 = Buffer.from(bufPlaintext.toString("base64"), "utf8");
  var bufPadding = Buffer.alloc(
    blocksize - (bufPlaintextB64.length % blocksize)
  );
  return Buffer.concat([bufPlaintextB64, bufPadding]);
}

module.exports = { cipher, decipher, toB64padded };
