from http.server import BaseHTTPRequestHandler, HTTPServer
import logging, re, json, urllib.request

class S(BaseHTTPRequestHandler):
    def do_GET(self):
        logging.info("GET request,\nPath: %s\nHeaders:\n%s\n", str(self.path), str(self.headers))
        if None != re.search('/api/v1/usd/*', self.path):
            recordID = self.path.split('/')[-1]
            if recordID.isdigit():
                value_rub = self.get_Value_Usd() * int(recordID)
                self.send_response(200)
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
                usd = {'usd': int(recordID),
                       'rub': float(format(value_rub, '.4f'))
                       }
                self.wfile.write(bytes(json.dumps(usd), 'UTF-8'))
            else:
                self.send_response(400, 'Bad Request: record does not exist')
                self.send_header('Content-Type', 'application/json')
                self.end_headers()
        else:
            self.send_response(403)
            self.send_header('Content-Type', 'application/json')
            self.end_headers()

    def get_Value_Usd(self):
        f = urllib.request.urlopen('https://www.cbr-xml-daily.ru/daily_json.js')
        valute_usd = json.loads(f.read().decode('utf-8'))
        value_usd = valute_usd["Valute"]["USD"]["Value"]
        return value_usd

def run(server_class=HTTPServer, handler_class=S, port=8080):
    logging.basicConfig(level=logging.INFO)
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    logging.info('Starting serv...\n')
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        pass
    httpd.server_close()
    logging.info('Stopping serv...\n')

if __name__ == '__main__':
    run()
