from pymongo import MongoClient
import xlrd

MONGO_HOST = "10.100.99.85"
MONGO_PORT = 27017
SCRIPT_FILE = r"C:\Users\awx739555\PycharmProjects\Script Generator Beta\scriptfile.xls"
DB_NAME = 'script'


def load_text():
    """

    """
    client = MongoClient(MONGO_HOST, MONGO_PORT)
    db = client['script']
    print(db)

    wb = xlrd.open_workbook(SCRIPT_FILE)
    sheet = wb.sheet_by_index(0)
    qs = db.questions
    ans = db.answers

    for i in range(1, sheet.nrows - 1):
        entry_dict = {}
        # unpack excel row into dict
        entry_dict['speaker'] = sheet.cell_value(i, 1)
        entry_dict['type'] = sheet.cell_value(i, 2)
        entry_dict['text'] = sheet.cell_value(i, 3)

        # add dict to appropriate collection
        q_or_a = sheet.cell_value(i, 0)
        if q_or_a == 'question':
            qs.insert_one(entry_dict)
        elif q_or_a == 'answer ':       # where is extra space coming from??? its necessary for some reason...
            ans.insert_one(entry_dict)










