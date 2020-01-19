from urllib import request

google_url_loc = 'http://samplecsvs.s3.amazonaws.com/TechCrunchcontinentalUSA.csv'


def download_csv_file(csv_url):
    response = request.urlopen(csv_url)
    csv = response.read()
    str_data = str(csv)
    lines = str_data.split('\\n')
    dst = r'online.csv'
    fp = open(dst, "w")
    for line in lines:
        fp.write(line + "\n")
    fp.close()


download_csv_file(google_url_loc)
