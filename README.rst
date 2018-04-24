==============
Validemail
==============

Validemail is a package for Python that check if an email is valid, properly formatted and really exists.



INSTALLATION
============

First, you must do::

    pip install validemail

Extra
------

For check the domain mx and verify email exits you must have the `dnspython` package installed::

    pip install dnspython


USAGE
=====

Basic usage::

    from validemail import validemail
    is_valid = validemail('example@example.com')


Checking domain has SMTP Server
-------------------------------

Check if the host has SMTP Server::

    from validemail import validemail
    is_valid = validemail('example@example.com',check_mx=True)


Verify email exists
-------------------

Check if the host has SMTP Server and the email really exists::

    from validemail import validemail
    is_valid = validemail('example@example.com',verify=True)


TODOs and BUGS
==============
See: https://github.com/oleg-borodai/validate_email/issues