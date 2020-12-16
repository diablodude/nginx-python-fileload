USE AT YOUR OWN RISK! 
this does utilize uwsgi directly with minimal awareness of things you want your webapp to handle nowadays..

this setup makes use of nginx client_body_in_file_only to save a POST request in combination with a python script that handles the renaming.
No PHP/Ruby/Python/whatever included in the upload process, just plain nginx magic!

