const fs = require("fs");

for (let i = 1; i <= 7; i++) {
    const filename = `./b${i}.py`;
    fs.writeFileSync(filename, "", "utf-8");
}