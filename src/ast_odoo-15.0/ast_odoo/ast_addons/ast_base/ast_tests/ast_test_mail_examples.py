Module(
    body=[
        Assign(
            targets=[Name(id='MISC_HTML_SOURCE', ctx=Store())],
            value=Constant(value='\n<font size="2" style="color: rgb(31, 31, 31); font-family: monospace; font-variant: normal; line-height: normal; ">test1</font>\n<div style="color: rgb(31, 31, 31); font-family: monospace; font-variant: normal; line-height: normal; font-size: 12px; font-style: normal; ">\n<b>test2</b></div><div style="color: rgb(31, 31, 31); font-family: monospace; font-variant: normal; line-height: normal; font-size: 12px; ">\n<i>test3</i></div><div style="color: rgb(31, 31, 31); font-family: monospace; font-variant: normal; line-height: normal; font-size: 12px; ">\n<u>test4</u></div><div style="color: rgb(31, 31, 31); font-family: monospace; font-variant: normal; line-height: normal; font-size: 12px; ">\n<strike>test5</strike></div><div style="color: rgb(31, 31, 31); font-family: monospace; font-variant: normal; line-height: normal; ">\n<font size="5">test6</font></div><div><ul><li><font color="#1f1f1f" face="monospace" size="2">test7</font></li><li>\n<font color="#1f1f1f" face="monospace" size="2">test8</font></li></ul><div><ol><li><font color="#1f1f1f" face="monospace" size="2">test9</font>\n</li><li><font color="#1f1f1f" face="monospace" size="2">test10</font></li></ol></div></div>\n<blockquote style="margin: 0 0 0 40px; border: none; padding: 0px;"><div><div><div><font color="#1f1f1f" face="monospace" size="2">\ntest11</font></div></div></div></blockquote><blockquote style="margin: 0 0 0 40px; border: none; padding: 0px;">\n<blockquote style="margin: 0 0 0 40px; border: none; padding: 0px;"><div><font color="#1f1f1f" face="monospace" size="2">\ntest12</font></div><div><font color="#1f1f1f" face="monospace" size="2"><br></font></div></blockquote></blockquote>\n<font color="#1f1f1f" face="monospace" size="2"><a href="http://google.com">google</a></font>\n<a href="javascript:alert(\'malicious code\')">test link</a>\n', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='EDI_LIKE_HTML_SOURCE', ctx=Store())],
            value=Constant(value='<div style="font-family: \'Lucida Grande\', Ubuntu, Arial, Verdana, sans-serif; font-size: 12px; color: rgb(34, 34, 34); background-color: #FFF; ">\n    <p>Hello {{ object.partner_id.name }},</p>\n    <p>A new invoice is available for you: </p>\n    <p style="border-left: 1px solid #8e0000; margin-left: 30px;">\n       &nbsp;&nbsp;<strong>REFERENCES</strong><br />\n       &nbsp;&nbsp;Invoice number: <strong>{{ object.number }}</strong><br />\n       &nbsp;&nbsp;Invoice total: <strong>{{ object.amount_total }} {{ object.currency_id.name }}</strong><br />\n       &nbsp;&nbsp;Invoice date: {{ object.invoice_date }}<br />\n       &nbsp;&nbsp;Order reference: {{ object.origin }}<br />\n       &nbsp;&nbsp;Your contact: <a href="mailto:{{ object.user_id.email or \'\' }}?subject=Invoice%20{{ object.number }}">{{ object.user_id.name }}</a>\n    </p>\n    <br/>\n    <p>It is also possible to directly pay with Paypal:</p>\n    <a style="margin-left: 120px;" href="{{ object.paypal_url }}">\n        <img class="oe_edi_paypal_button" src="https://www.paypal.com/en_US/i/btn/btn_paynowCC_LG.gif"/>\n    </a>\n    <br/>\n    <p>If you have any question, do not hesitate to contact us.</p>\n    <p>Thank you for choosing {{ object.company_id.name or \'us\' }}!</p>\n    <br/>\n    <br/>\n    <div style="width: 375px; margin: 0px; padding: 0px; background-color: #8E0000; border-top-left-radius: 5px 5px; border-top-right-radius: 5px 5px; background-repeat: repeat no-repeat;">\n        <h3 style="margin: 0px; padding: 2px 14px; font-size: 12px; color: #DDD;">\n            <strong style="text-transform:uppercase;">{{ object.company_id.name }}</strong></h3>\n    </div>\n    <div style="width: 347px; margin: 0px; padding: 5px 14px; line-height: 16px; background-color: #F2F2F2;">\n        <span style="color: #222; margin-bottom: 5px; display: block; ">\n        {{ object.company_id.street }}<br/>\n        {{ object.company_id.street2 }}<br/>\n        {{ object.company_id.zip }} {{ object.company_id.city }}<br/>\n        {{ object.company_id.state_id and (\'%s, \' % object.company_id.state_id.name) or \'\' }} {{ object.company_id.country_id.name or \'\' }}<br/>\n        </span>\n        <div style="margin-top: 0px; margin-right: 0px; margin-bottom: 0px; margin-left: 0px; padding-top: 0px; padding-right: 0px; padding-bottom: 0px; padding-left: 0px; ">\n            Phone:&nbsp; {{ object.company_id.phone }}\n        </div>\n        <div>\n            Web :&nbsp;<a href="{{ object.company_id.website }}">{{ object.company_id.website }}</a>\n        </div>\n    </div>\n</div></body></html>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_BLOCKQUOTE', ctx=Store())],
            value=Constant(value='<html>\n  <head>\n    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">\n  </head>\n  <body text="#000000" bgcolor="#FFFFFF">\n    <div class="moz-cite-prefix">On 05-01-16 05:52, Andreas Becker\n      wrote:<br>\n    </div>\n    <blockquote\ncite="mid:CAEJSRZvWvud8c6Qp=wfNG6O1+wK3i_jb33qVrF7XyrgPNjnyUA@mail.gmail.com"\n      type="cite"><base href="https://www.odoo.com">\n      <div dir="ltr">Yep Dominique that is true, as Postgres was the\n        base of all same as Odoo and MySQL etc came much later.Â \n        <div><br>\n        </div>\n        <div>Unfortunately many customers who ask for and ERP are with\n          hosters which still don\'t provide Postgres and MySQL is\n          available everywhere. Additionally Postgres seems for many\n          like a big black box while MySQL is very well documented and\n          understandable and it has PHPmyAdmin which is far ahead of any\n          tool managing postgres DBs.</div>\n        <br>\n      </div>\n    </blockquote>\n    <br>\n    I don\'t care how much you are highlighting the advantages of Erpnext\n    on this Odoo mailinglist, but when you start implying that Postgres\n    is not well documented it really hurts.<br>\n    <br>\n    <pre class="moz-signature" cols="72">-- \nOpener B.V. - Business solutions driven by open source collaboration\n\nStefan Rijnhart - Consultant/developer\n\nmail: <a class="moz-txt-link-abbreviated" href="mailto:stefan@opener.am">stefan@opener.am</a>\ntel: +31 (0) 20 3090 139\nweb: <a class="moz-txt-link-freetext" href="https://opener.am">https://opener.am</a></pre>\n  </body>\n</html>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_BLOCKQUOTE_IN', ctx=Store())],
            value=List(
                elts=[Constant(value='<blockquote cite="mid:CAEJSRZvWvud8c6Qp=wfNG6O1+wK3i_jb33qVrF7XyrgPNjnyUA@mail.gmail.com" type="cite" data-o-mail-quote-node="1" data-o-mail-quote="1">', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_BLOCKQUOTE_OUT', ctx=Store())],
            value=List(
                elts=[Constant(value='-- \nOpener B.V. - Business solutions driven by open source collaboration\n\nStefan Rijnhart - Consultant/developer', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_THUNDERBIRD_HTML', ctx=Store())],
            value=Constant(value='<html>\n  <head>\n    <meta content="text/html; charset=utf-8" http-equiv="Content-Type">\n  </head>\n  <body text="#000000" bgcolor="#FFFFFF">\n    <div class="moz-cite-prefix">On 01/05/2016 10:24 AM, Raoul\n      Poilvache wrote:<br>\n    </div>\n    <blockquote\ncite="mid:CAP76m_WWFH2KVrbjOxbaozvkmbzZYLWJnQ0n0sy9XpGaCWRf1g@mail.gmail.com"\n      type="cite">\n      <div dir="ltr"><b><i>Test reply. The suite.</i></b><br clear="all">\n        <div><br>\n        </div>\n        -- <br>\n        <div class="gmail_signature">Raoul Poilvache</div>\n      </div>\n    </blockquote>\n    Top cool !!!<br>\n    <br>\n    <pre class="moz-signature" cols="72">-- \nRaoul Poilvache\n</pre>\n  </body>\n</html>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_THUNDERBIRD_HTML_IN', ctx=Store())],
            value=List(
                elts=[Constant(value='<blockquote cite="mid:CAP76m_WWFH2KVrbjOxbaozvkmbzZYLWJnQ0n0sy9XpGaCWRf1g@mail.gmail.com" type="cite" data-o-mail-quote-node="1" data-o-mail-quote="1">', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_THUNDERBIRD_HTML_OUT', ctx=Store())],
            value=List(
                elts=[Constant(value='<pre class="moz-signature" cols="72"><span data-o-mail-quote="1">-- \nRaoul Poilvache\n</span></pre>', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_HOTMAIL_HTML', ctx=Store())],
            value=Constant(value='\n<html>\n<head>\n<style><!--\n.hmmessage P\n{\nmargin:0px=3B\npadding:0px\n}\nbody.hmmessage\n{\nfont-size: 12pt=3B\nfont-family:Calibri\n}\n--></style></head>\n<body class=\'hmmessage\'>\n<div dir=\'ltr\'>I don\'t like that.<br><br>\n<div><hr id="stopSpelling">\nDate: Tue=2C 5 Jan 2016 10:24:48 +0100<br>\nSubject: Test from gmail<br>\nFrom: poilvache@example.com<br>\nTo: tartelette@example.com grosbedon@example.com<br><br>\n<div dir="ltr"><b><i>Test reply. The suite.</i></b>\n<br clear="all"><div><br>\n</div>-- <br><div class="ecxgmail_signature">\nRaoul Poilvache</div>\n</div></div></div></body></html>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_HOTMAIL_HTML_IN', ctx=Store())],
            value=List(
                elts=[Constant(value="I don't like that.<br><br>", kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_HOTMAIL_HTML_OUT', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='<hr id="stopSpelling" data-o-mail-quote="1">', kind='u'),
                    Constant(value='<div dir="ltr" data-o-mail-quote="1"><b data-o-mail-quote="1"><i data-o-mail-quote="1">Test reply. The suite.</i></b>', kind='u'),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_OUTLOOK_HTML', ctx=Store())],
            value=Constant(value='\n<html>\n   <head>\n      <meta http-equiv="Content-Type" content="text/html; charset=3Diso-8859-=\n         1">\n      <style type="text/css" style="display:none;"> P {margin-top:0;margin-bo=\n         ttom:0;}\n      </style>\n   </head>\n   <body dir="ltr">\n      <div id="mail_body">\n         Reply from outlook\n      </div>\n      <div style="font-family: Calibri, Helvetica, sans-serif; font-size: 12pt;=\n         color: rgb(0, 0, 0);">\n         <br>\n      </div>\n      <div id="testing_id">\n         <div id="appendonsend"></div>\n         <div style="font-family:Calibri,Helvetica,sans-serif; font-size:12pt; col=\n            or:rgb(0,0,0)">\n            <br>\n         </div>\n         <hr tabindex="-1" style="display:inline-block; width:98%">\n         <div id="divRplyFwdMsg" dir="ltr">\n            <font face="Calibri, sans-serif" color="#000000" style="font-size:11pt"><b>De :</b> test@example.com<br>\n            <b>=C0 :</b> test@example.com &lt;test@example.com&gt;<br>\n            <b>Objet :</b> Parent message</font>\n            <div>&nbsp;</div>\n         </div>\n         <div>\n            <div dir="ltr">Parent email body</div>\n         </div>\n      </div>\n   </body>\n</html>\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_OUTLOOK_HTML_IN', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='Reply from outlook', kind=None),
                    Constant(value='<div id="mail_body">', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_OUTLOOK_HTML_OUT', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='<div id="testing_id" data-o-mail-quote-container="1">', kind=None),
                    Constant(value='<div id="divRplyFwdMsg" dir="ltr" data-o-mail-quote="1">', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_THUNDERBIRD_1', ctx=Store())],
            value=Constant(value='<div>On 11/08/2012 05:29 PM,\n      <a href="mailto:dummy@example.com">dummy@example.com</a> wrote:<br></div>\n    <blockquote>\n      <div>I contact you about our meeting for tomorrow. Here is the\n        schedule I propose:</div>\n      <div>\n        <ul><li>9 AM: brainstorming about our new amazing business\n            app&lt;/span&gt;&lt;/li&gt;</li>\n          <li>9.45 AM: summary</li>\n          <li>10 AM: meeting with Fabien to present our app</li>\n        </ul></div>\n      <div>Is everything ok for you ?</div>\n      <div>\n        <p>--<br>\n          Administrator</p>\n      </div>\n      <div>\n        <p>Log in our portal at:\n<a href="http://localhost:8069#action=login&amp;db=mail_1&amp;token=rHdWcUART5PhEnJRaXjH">http://localhost:8069#action=login&amp;db=mail_1&amp;token=rHdWcUART5PhEnJRaXjH</a></p>\n      </div>\n    </blockquote>\n    Ok for me. I am replying directly below your mail, using Thunderbird, with a signature.<br><br>\n    Did you receive my email about my new laptop, by the way ?<br><br>\n    Raoul.<br><pre>-- \nRaoul Grosbedonn&#233;e\n</pre>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_THUNDERBIRD_1_IN', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='<a href="mailto:dummy@example.com">dummy@example.com</a> ', kind='u'),
                    Constant(value='<blockquote data-o-mail-quote-node="1" data-o-mail-quote="1">', kind='u'),
                    Constant(value='Ok for me. I am replying directly below your mail, using Thunderbird, with a signature.', kind='u'),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_THUNDERBIRD_1_OUT', ctx=Store())],
            value=List(
                elts=[Constant(value='-- \nRaoul Grosbedonnée\n', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_YAHOO_HTML', ctx=Store())],
            value=Constant(value='\n<html>\n   <head></head>\n   <body>\n      <div class="ydpf6e951dcyahoo-style-wrap">\n      <div></div>\n      <div dir="ltr" data-setdir="false">Reply from Yahoo</div>\n      </div>\n      <div id="yahoo_quoted_8820595126" class="yahoo_quoted">\n         <div style="font-family:\'Helvetica Neue\', Helvetica, Arial, sans-serif;font-size:13px;color:#26282a;">\n            =20\n            <div>\n               Bob a dit:\n            </div>\n            <div><br></div>\n            <div><br></div>\n            <div>\n               <div id="yiv3215395356">\n                  <div dir="ltr">Parent email body</div>\n               </div>\n            </div>\n         </div>\n      </div>\n   </body>\n</html>\n', kind=None),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_YAHOO_HTML_IN', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='Reply from Yahoo', kind=None),
                    Constant(value='<div dir="ltr" data-setdir="false">', kind=None),
                    Constant(value='<div class="ydpf6e951dcyahoo-style-wrap">', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='QUOTE_YAHOO_HTML_OUT', ctx=Store())],
            value=List(
                elts=[Constant(value='<div id="yahoo_quoted_8820595126" class="yahoo_quoted" data-o-mail-quote="1">', kind=None)],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TEXT_1', ctx=Store())],
            value=Constant(value='I contact you about our meeting tomorrow. Here is the schedule I propose:\n9 AM: brainstorming about our new amazing business app\n9.45 AM: summary\n10 AM: meeting with Ignasse to present our app\nIs everything ok for you ?\n--\nMySignature', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TEXT_1_IN', ctx=Store())],
            value=List(
                elts=[Constant(value='I contact you about our meeting tomorrow. Here is the schedule I propose:\n9 AM: brainstorming about our new amazing business app\n9.45 AM: summary\n10 AM: meeting with Ignasse to present our app\nIs everything ok for you ?', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TEXT_1_OUT', ctx=Store())],
            value=List(
                elts=[Constant(value='\n--\nMySignature', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TEXT_2', ctx=Store())],
            value=Constant(value='Salut Raoul!\nLe 28 oct. 2012 à 00:02, Raoul Grosbedon a écrit :\n\n> I contact you about our meeting tomorrow. Here is the schedule I propose: (quote)\n\nOf course. This seems viable.\n\n> 2012/10/27 Bert Tartopoils :\n>> blahblahblah (quote)?\n>> \n>> blahblahblah (quote)\n>> \n>> Bert TARTOPOILS\n>> bert.tartopoils@miam.miam\n>> \n> \n> \n> -- \n> RaoulSignature\n\n--\nBert TARTOPOILS\nbert.tartopoils@miam.miam\n', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TEXT_2_IN', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='Salut Raoul!', kind='u'),
                    Constant(value='Of course. This seems viable.', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='TEXT_2_OUT', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='\n> I contact you about our meeting tomorrow. Here is the schedule I propose: (quote)', kind='u'),
                    Constant(value='\n> 2012/10/27 Bert Tartopoils :\n>> blahblahblah (quote)?\n>> \n>> blahblahblah (quote)\n>> \n>> Bert TARTOPOILS\n>> bert.tartopoils@miam.miam\n>> \n> \n> \n> -- \n> RaoulSignature', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GMAIL_1', ctx=Store())],
            value=Constant(value='Hello,<div><br></div><div>Ok for me. I am replying directly in gmail, without signature.</div><div><br></div><div>Kind regards,</div><div><br></div><div>Demo.<br><br><div>On Thu, Nov 8, 2012 at 5:29 PM,  <span>&lt;<a href="mailto:dummy@example.com">dummy@example.com</a>&gt;</span> wrote:<br><blockquote><div>I contact you about our meeting for tomorrow. Here is the schedule I propose:</div><div><ul><li>9 AM: brainstorming about our new amazing business app&lt;/span&gt;&lt;/li&gt;</li>\n<li>9.45 AM: summary</li><li>10 AM: meeting with Fabien to present our app</li></ul></div><div>Is everything ok for you ?</div>\n<div><p>-- <br>Administrator</p></div>\n\n<div><p>Log in our portal at: <a href="http://localhost:8069#action=login&amp;db=mail_1&amp;login=demo">http://localhost:8069#action=login&amp;db=mail_1&amp;login=demo</a></p></div>\n</blockquote></div><br></div>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GMAIL_1_IN', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='Ok for me. I am replying directly in gmail, without signature.', kind='u'),
                    Constant(value='<blockquote data-o-mail-quote-node="1" data-o-mail-quote="1">', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='GMAIL_1_OUT', ctx=Store())],
            value=List(elts=[], ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='HOTMAIL_1', ctx=Store())],
            value=Constant(value='<div>\n    <div dir="ltr"><br>\n        I have an amazing company, i\'m learning OpenERP, it is a small company yet, but plannig to grow up quickly.\n        <br><br>Kindest regards,<br>xxx<br>\n        <div>\n            <div id="SkyDrivePlaceholder">\n            </div>\n            <hr id="stopSpelling">\n            Subject: Re: your OpenERP.com registration<br>From: xxx@xxx.xxx<br>To: xxx@xxx.xxx<br>Date: Wed, 27 Mar 2013 17:12:12 +0000\n            <br><br>\n            Hello xxx,\n            <br>\n            I noticed you recently created an OpenERP.com account to access OpenERP Apps.\n            <br>\n            You indicated that you wish to use OpenERP in your own company.\n            We would like to know more about your your business needs and requirements, and see how\n            we can help you. When would you be available to discuss your project ?<br>\n            Best regards,<br>\n            <pre>\n                <a href="http://openerp.com" target="_blank">http://openerp.com</a>\n                Belgium: +32.81.81.37.00\n                U.S.: +1 (650) 307-6736\n                India: +91 (79) 40 500 100\n            </pre>\n        </div>\n    </div>\n</div>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='HOTMAIL_1_IN', ctx=Store())],
            value=List(
                elts=[Constant(value='<div dir="ltr"><br>\n        I have an amazing company, i\'m learning OpenERP, it is a small company yet, but plannig to grow up quickly.\n        <br><br>Kindest regards,<br>xxx<br>', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='HOTMAIL_1_OUT', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='<hr id="stopSpelling" data-o-mail-quote="1">', kind='u'),
                    Constant(value='<pre data-o-mail-quote="1">\n                <a href="http://openerp.com" target="_blank" data-o-mail-quote="1">http://openerp.com</a>\n                Belgium: +32.81.81.37.00\n                U.S.: +1 (650) 307-6736\n                India: +91 (79) 40 500 100\n            </pre>', kind='u'),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='MSOFFICE_1', ctx=Store())],
            value=Constant(value='\n<div>\n<div class="WordSection1">\n        <p class="MsoNormal">\n            <span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#1F497D">\n                Our requirements are simple. Just looking to replace some spreadsheets for tracking quotes and possibly using the timecard module.\n                We are a company of 25 engineers providing product design services to clients.\n            </span>\n        </p>\n        <p></p>\n        <p></p>\n        <p class="MsoNormal">\n            <span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#1F497D">\n                I’ll install on a windows server and run a very limited trial to see how it works.\n                If we adopt OpenERP we will probably move to Linux or look for a hosted SaaS option.\n            </span>\n        </p>\n        <p></p>\n        <p></p>\n        <p class="MsoNormal">\n            <span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#1F497D">\n                <br>\n                I am also evaluating Adempiere and maybe others.\n            </span>\n        </p>\n        <p></p>\n        <p></p>\n        <p class="MsoNormal">\n            <span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#1F497D">\n            </span>\n        </p>\n        <p>&nbsp;</p>\n        <p></p>\n        <p class="MsoNormal">\n            <span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#1F497D">\n                I expect the trial will take 2-3 months as this is not a high priority for us.\n            </span>\n        </p>\n        <p></p>\n        <p></p>\n        <p class="MsoNormal">\n            <span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#1F497D">\n            </span>\n        </p>\n        <p>&nbsp;</p>\n        <p></p>\n        <p class="MsoNormal">\n            <span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#1F497D">\n                Alan\n            </span>\n        </p>\n        <p></p>\n        <p></p>\n        <p class="MsoNormal">\n            <span style="font-size:11.0pt;font-family:&quot;Calibri&quot;,&quot;sans-serif&quot;;color:#1F497D">\n            </span>\n        </p>\n        <p>&nbsp;</p>\n        <p></p>\n        <div>\n            <div style="border:none;border-top:solid #B5C4DF 1.0pt;padding:3.0pt 0in 0in 0in">\n                <p class="MsoNormal">\n                    <b><span style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;">\n                        From:\n                    </span></b>\n                    <span style="font-size:10.0pt;font-family:&quot;Tahoma&quot;,&quot;sans-serif&quot;">\n                        OpenERP Enterprise [mailto:sales@openerp.com]\n                        <br><b>Sent:</b> Monday, 11 March, 2013 14:47<br><b>To:</b> Alan Widmer<br><b>Subject:</b> Re: your OpenERP.com registration\n                    </span>\n                </p>\n                <p></p>\n                <p></p>\n            </div>\n        </div>\n        <p class="MsoNormal"></p>\n        <p>&nbsp;</p>\n        <p>Hello Alan Widmer, </p>\n        <p></p>\n        <p>I noticed you recently downloaded OpenERP. </p>\n        <p></p>\n        <p>\n            Uou mentioned you wish to use OpenERP in your own company. Please let me more about your\n            business needs and requirements? When will you be available to discuss about your project?\n        </p>\n        <p></p>\n        <p>Thanks for your interest in OpenERP, </p>\n        <p></p>\n        <p>Feel free to contact me if you have any questions, </p>\n        <p></p>\n        <p>Looking forward to hear from you soon. </p>\n        <p></p>\n        <pre><p>&nbsp;</p></pre>\n        <pre>--<p></p></pre>\n        <pre>Nicolas<p></p></pre>\n        <pre><a href="http://openerp.com">http://openerp.com</a><p></p></pre>\n        <pre>Belgium: +32.81.81.37.00<p></p></pre>\n        <pre>U.S.: +1 (650) 307-6736<p></p></pre>\n        <pre>India: +91 (79) 40 500 100<p></p></pre>\n        <pre>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;<p></p></pre>\n    </div>\n</div>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='MSOFFICE_1_IN', ctx=Store())],
            value=List(
                elts=[Constant(value='Our requirements are simple. Just looking to replace some spreadsheets for tracking quotes and possibly using the timecard module.', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='MSOFFICE_1_OUT', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='I noticed you recently downloaded OpenERP.', kind='u'),
                    Constant(value='Uou mentioned you wish to use OpenERP in your own company.', kind=None),
                    Constant(value='Belgium: +32.81.81.37.00', kind=None),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='BUG1', ctx=Store())],
            value=Constant(value='<pre>Hi Migration Team,\n\nParagraph 1, blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah.\n\nParagraph 2, blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah.\n\nParagraph 3, blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah blah blah blah blah blah blah \nblah blah blah blah blah blah blah blah.\n\nThanks.\n\nRegards,\n\n-- \nOlivier Laurent\nMigration Manager\nOpenERP SA\nChaussée de Namur, 40\nB-1367 Gérompont\nTel: +32.81.81.37.00\nWeb: http://www.openerp.com</pre>', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='BUG_1_IN', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='Hi Migration Team', kind='u'),
                    Constant(value='Paragraph 1', kind='u'),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='BUG_1_OUT', ctx=Store())],
            value=List(
                elts=[Constant(value='\n-- \nOlivier Laurent\nMigration Manager\nOpenERP SA\nChaussée de Namur, 40\nB-1367 Gérompont\nTel: +32.81.81.37.00\nWeb: http://www.openerp.com', kind='u')],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='REMOVE_CLASS', ctx=Store())],
            value=Constant(value='\n<div style="FONT-SIZE: 12pt; FONT-FAMILY: \'Times New Roman\'; COLOR: #000000">\n    <div>Hello</div>\n    <div>I have just installed Odoo 9 and I\'ve got the following error:</div>\n    <div>&nbsp;</div>\n    <div class="openerp openerp_webclient_container oe_webclient">\n        <div class="oe_loading" style="DISPLAY: none">&nbsp;</div>\n    </div>\n    <div class="modal-backdrop in"></div>\n    <div role="dialog" tabindex="-1" aria-hidden="false" class="modal in" style="DISPLAY: block" data-backdrop="static">\n        <div class="modal-dialog modal-lg">\n            <div class="modal-content openerp">\n                <div class="modal-header"> \n                    <h4 class="modal-title">Odoo Error<span class="o_subtitle text-muted"></span></h4>\n                </div>\n                <div class="o_error_detail modal-body">\n                    <pre>An error occured in a modal and I will send you back the html to try opening one on your end</pre>\n                </div>\n            </div>\n        </div>\n    </div>\n</div>\n', kind='u'),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='REMOVE_CLASS_IN', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='<div style="font-size:12pt; font-family:\'Times New Roman\'; color:#000000">', kind='u'),
                    Constant(value='An error occured in a modal and I will send you back the html to try opening one on your end', kind='u'),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='REMOVE_CLASS_OUT', ctx=Store())],
            value=List(
                elts=[
                    Constant(value='<div class="modal-backdrop in">', kind='u'),
                    Constant(value='<div class="modal-content openerp">', kind='u'),
                    Constant(value='<div class="modal-header">', kind='u'),
                ],
                ctx=Load(),
            ),
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
