Module(
    body=[
        Assign(
            targets=[Name(id='GROUP_TEMPLATE', ctx=Store())],
            value=Constant(value='Return-Path: <whatever-2a840@postmaster.twitter.com>\nTo: {to}\ncc: {cc}\nReceived: by mail1.openerp.com (Postfix, from userid 10002)\n    id 5DF9ABFB2A; Fri, 10 Aug 2012 16:16:39 +0200 (CEST)\nFrom: {email_from}\nSubject: {subject}\nMIME-Version: 1.0\nContent-Type: multipart/alternative;\n    boundary="----=_Part_4200734_24778174.1344608186754"\nDate: Fri, 10 Aug 2012 14:16:26 +0000\nMessage-ID: {msg_id}\n{extra}\n------=_Part_4200734_24778174.1344608186754\nContent-Type: text/plain; charset=utf-8\nContent-Transfer-Encoding: quoted-printable\n\nThis should be posted on a mail.group. Or not.\n\n--\nSylvie\n------=_Part_4200734_24778174.1344608186754\nContent-Type: text/html; charset=utf-8\nContent-Transfer-Encoding: quoted-printable\n\n<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN" "http://www.w3.org/TR/html4/strict.dtd">\n<html>\n <head>=20\n  <meta http-equiv=3D"Content-Type" content=3D"text/html; charset=3Dutf-8" />\n </head>=20\n <body style=3D"margin: 0; padding: 0; background: #ffffff;-webkit-text-size-adjust: 100%;">=20\n\n  <p>This should be posted on a mail.group. Or not.</p>\n\n  <p>--<br/>\n     Sylvie\n  <p>\n </body>\n</html>\n------=_Part_4200734_24778174.1344608186754--\n', kind=None),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
