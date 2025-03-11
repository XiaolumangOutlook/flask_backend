from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow all origins

# Sample data
data = [
  {
    'Account Code': 'SYDN1445',
    'Storage Branch': 'Sydney',
    'Account Description': 'The Salvation Army Employment Plus',
    'Barcode': 'SYD01278002',
    'Alternate Code': '',
    'Long Description': '',
    'Contents': '',
    'Object Code': 'C01',
    'Description': '',
    "Add Date": "2013-11-25",
    'Item Status': 'In',
    "Status Date": "2013-11-25",
    'Destroy Date': '',
    'Perm Flag': 'No',
    'Container Barcode': '',
    'From Date': '',
    'To Date': '',
    'User Field 1': '',
    'User Field 2': '',
    'User Field 3': '',
    'User Field 4': '',
    'User Date': '',
    'Access Count': '0'
  },
  {
    'Account Code': 'SYDN1446',
    'Storage Branch': 'Sydney',
    'Account Description': 'The Salvation Army Employment Plus',
    'Barcode': 'SYD01278003',
    'Alternate Code': '',
    'Long Description': '',
    'Contents': '',
    'Object Code': 'C01',
    'Description': '',
    "Add Date": "2013-11-25",
    'Item Status': 'In',
    "Status Date": "2013-11-25",
    'Destroy Date': '',
    'Perm Flag': 'No',
    'Container Barcode': '',
    'From Date': '',
    'To Date': '',
    'User Field 1': '',
    'User Field 2': '',
    'User Field 3': '',
    'User Field 4': '',
    'User Date': '',
    'Access Count': '0'
  },
  {
    'Account Code': 'SYDN1445',
    'Storage Branch': 'Melbourne',
    'Account Description': 'The Salvation Army Employment Plus',
    'Barcode': 'SYD01278004',
    'Alternate Code': '',
    'Long Description': '',
    'Contents': '',
    'Object Code': 'C02',
    'Description': '',
    "Add Date": "2013-11-25",
    'Item Status': 'In',
    "Status Date": "2013-11-25",
    'Destroy Date': '',
    'Perm Flag': 'No',
    'Container Barcode': '',
    'From Date': '',
    'To Date': '',
    'User Field 1': '',
    'User Field 2': '',
    'User Field 3': '',
    'User Field 4': '',
    'User Date': '',
    'Access Count': '0'
  },
  {
    'Account Code': 'SYDN1447',
    'Storage Branch': 'Sydney',
    'Account Description': 'Injury Management',
    'Barcode': 'SYD01278005',
    'Alternate Code': '',
    'Long Description': '',
    'Contents': '',
    'Object Code': 'C02',
    'Description': '',
    "Add Date": "2013-11-25",
    'Item Status': 'In',
    "Status Date": "2013-11-25",
    'Destroy Date': '',
    'Perm Flag': 'No',
    'Container Barcode': '',
    'From Date': '',
    'To Date': '',
    'User Field 1': '',
    'User Field 2': '',
    'User Field 3': '',
    'User Field 4': '',
    'User Date': '',
    'Access Count': '0'
  }]
@app.route('/api/data', methods=['GET'])
def get_data():
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)

