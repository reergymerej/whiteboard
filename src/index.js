var http = require('http');
var formidable = require('formidable');
var fs = require('fs');
const path = require('path')

http.createServer(function (req, res) {
  if (req.url == '/fileupload') {
    const form = formidable({ multiples: true });
    form.parse(req, function (err, fields, files) {
      files.filetoupload.forEach(filetoupload => {
        var oldpath = filetoupload.path;
        var newpath = path.resolve(__dirname, '../uploads/' + filetoupload.name)
        fs.rename(oldpath, newpath, function (err) {
          if (err) throw err;
        });
      })
      res.write('File uploaded and moved!');
      res.end();
 });
  } else {
    res.writeHead(200, {'Content-Type': 'text/html'});
    res.write('<form action="fileupload" method="post" enctype="multipart/form-data">');
    res.write('<input type="file" name="filetoupload" multiple><br>');
    res.write('<input type="submit">');
    res.write('</form>');
    return res.end();
  }
}).listen(8080);
