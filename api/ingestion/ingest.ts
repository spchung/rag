import pdf from "npm:pdf-parse";
 
const dataBuffer = Deno.readFileSync('api/docs/dtn_manufacture.pdf');

pdf(dataBuffer).then(function(data: any) {
  console.log(data.numpages);
  // number of rendered pages
  console.log(data.numrender);
  // PDF info
  console.log(data.info);
  // PDF metadata
  console.log(data.metadata); 
  // PDF.js version
  // check https://mozilla.github.io/pdf.js/getting_started/
  console.log(data.version);
  // PDF text
  console.log(data.text); 
});

