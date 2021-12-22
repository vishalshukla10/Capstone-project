import main
import trainer as tr

url = "https://www.google.com/"
print(url)
main.process_test_url(url, 'test_features.csv')
return_ans = tr.gui_caller('url_features.csv', 'test_features.csv')
a = str(return_ans).split()
if int(a[1]) == 0:
    print("URL Checker Result", "The URL " + url + " is Benign")
elif int(a[1]) == 1:
    print("URL Checker Result", "The URL " + url + " is Malicious")
else:
    print("URL Checker Result", "The URL " + url + " is Malware")