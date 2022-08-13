from PyPDF2 import PdfFileWriter, PdfFileReader
import json
import csv
import sys
import pandas as pd


# Import authentication classes
# Check for User authentication - check if user is logged in before processing file


# Json Chunking

def chunk_jsonfile():

    # Opening JSON file 
    with open(sys.argv[1],'r') as uploadedfile: # instead of f = open('data.json',)

        # returns JSON object as a dictionary
        jsonFile = json.load(uploadedfile)

        # Set Chunk size per file - to be set by user as a variable
        chunkSize = 1400

        # Iterating through the json list
        for i in range(0, len(jsonFile), chunkSize): # xrange is obsolete
            with open(sys.argv[1] + '_' + str(i//chunkSize) + '.json', 'w') as outfile:
                json.dump(jsonFile[i:i+chunkSize], outfile)


# Converting Json to CSV

# Solution 1 using pandas library

# df = pd.read_json (r'../input/data.json')
df = pd.read_json (sys.argv[1],'r')
df.to_csv (r'../jsontocsv/jsonoutput.csv', index = None)



# Solution 2 without pandas

def jsonToCSv():
    if request.method == "POST":
        
        json_upload = request.FILES["jsonfile"]
        file_name = default_storage.save(json_upload)
        file_path = default_storage.path(file_name)

        csv_output_path = f"{settings.MEDIA_ROOT}/jsontocsv/jsonoutput.csv"

        with open(file_path,'r') as json_file:
            jsondata = json.load(json_file)

        data_file = open(csv_output_path, 'w', newline='')
        csv_writer = csv.writer(data_file)

        count = 0
        for data in jsondata:
            if count == 0:
                header = data.keys()
                csv_writer.writerow(header)
                count += 1
            csv_writer.writerow(data.values())

        data_file.close()
        context = {"file": file}
        return render(request, "jsonToCsv.html", context)

    context = {}
    return render(request, "jsonToCsv.html", context)



# #PDF Chunking


# Solution 1

# In case of PDF REad Error, added strict=False
inputpdf = PdfFileReader(open("..\Spindles\sampledoc.pdf", "rb"), strict=False)

for i in range(inputpdf.numPages):
    output = PdfFileWriter()
    output.addPage(inputpdf.getPage(i))
    with open("document-page%s.pdf" % i, "wb") as outputStream:
        output.write(outputStream)


# Solution 2

def pdf_split(fname, start, end=None):
    print('pdf_split', fname, start, end)

    #inputpdf = PdfFileReader(open("document.pdf", "rb"))
    inputpdf = PdfFileReader(open(fname, "rb"))
    output = PdfFileWriter()

    # pages checking and total nos
    num_pages = inputpdf.numPages
    if start:
        start-=1
    if not start:
        start=0
    if not end or end > num_pages:
        end=num_pages

    get_pages = list(range(start,end))
    #print('get_pages', get_pages, 'of', num_pages)

    for i in range(start,end):
        if i < start:
            continue
        #output = PdfFileWriter()
        output.addPage(inputpdf.getPage(i))

    fname_no_pdf = fname
    if fname[:-4].lower() == '.pdf':
        fname_no_pdf = fname[:-4]
    out_filename = f"{fname_no_pdf}-{start+1}-{end}.pdf"
    with open(out_filename, "wb") as outputStream:
        output.write(outputStream)
    print('saved', out_filename)
