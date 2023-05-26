Hellfire
========

Ban tool designed to torch fendas, leaving a slight feeling of burnout. Download the latest release `here`_.

.. _here: https://github.com/Celinova/Overburn/releases/latest


How it works
-------------------

Hellfire uses an HTML session using sweeze's NSDotPy library. Using this session, it will load the reports page and handle bans. To abide by NS rules, loading the reports page and banning are done manually. 

**PLEASE NOTE** that if you log into a nation, it will stop functioning and you will have to manually input a login session. NSDotPy also uses the keyboard function, meaning it will work regardless if you are not on the tab of this script.

Usage
-----------------------

Hellfire will ask for the nation name and its password of the nation you will be using to ban. 

Then just keep pressing enter.

TO-DO
-----------------------

- [ ] Set separate keybinds for re-logging and refresing the reports page, in case you happen to log in from another session.
- [ ] Add a fancy logo
- [ ] fully integrate with nsdotpy to make the code cleaner, instead of calling the private methods directly from the session
- [ ] faster pageloads
- [ ] keeps track of banned nations from the reports page so it doesn't have to iterate through already banned nations by other banners
- [ ] more coming ahead
