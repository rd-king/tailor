@ECHO OFF
start cmd.exe /C "E: && cd E:\personal project\tailor && python manage.py runserver "
Set _Delay=5
start C:\"Program Files (x86)"\Google\Chrome\Application\chrome.exe "http://127.0.0.1:8000/customer/viewCustomer"
