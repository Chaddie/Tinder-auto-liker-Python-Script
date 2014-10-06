Tinder-auto-liker-Python-Script
===============================

You will need to install the requests module for Python in order to run this script as it requires this so that it can authenticate with the Tinder API.



You can get a Facebook Access token by going to the following URL and copying what appears in the address bar and then extracting the token from the URL string.

<code>https://www.facebook.com/dialog/oauth?client_id=464891386855067&redirect_uri=https://www.facebook.com/connect/login_success.html&scope=basic_info,email,public_profile,user_about_me,user_activities,user_birthday,user_education_history,user_friends,user_interests,user_likes,user_location,user_photos,user_relationship_details&response_type=token</code>



You can find out your facebook ID by going to this URL and entering your Facebook profile vanity URL:
http://findmyfacebookid.com

To install the Requests module, go to the following URL:
<code>http://docs.python-requests.org/en/latest/</code>

Once extracted, run <code>python setup.py install</code> and then check if the module is installed by typing help('modules') in Python.

I will write a tutorial on this in the future on my website: https://chadd.ie
