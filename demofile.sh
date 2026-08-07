
mkdir templates 
python3 scaffold.py showcase css_style html_page next_opening
python3 scaffold.py shop name shop_type_id:references opened_on
python3 scaffold.py shop_type name description
python3 scaffold.py anniversary shop_id:references year message
