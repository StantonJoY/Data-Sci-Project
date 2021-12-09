Module(
    body=[
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        Import(
            names=[alias(name='email.policy', asname=None)],
        ),
        Import(
            names=[alias(name='email.message', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='threading', asname=None)],
        ),
        ImportFrom(
            module='odoo.addons.base.models.ir_mail_server',
            names=[alias(name='extract_rfc2822_addresses', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[
                alias(name='BaseCase', asname=None),
                alias(name='TransactionCase', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[
                alias(name='is_html_empty', asname=None),
                alias(name='html_sanitize', asname=None),
                alias(name='append_content_to_html', asname=None),
                alias(name='plaintext2html', asname=None),
                alias(name='email_split', asname=None),
                alias(name='email_domain_normalize', asname=None),
                alias(name='misc', asname=None),
                alias(name='formataddr', asname=None),
                alias(name='prepend_html_content', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module=None,
            names=[alias(name='test_mail_examples', asname=None)],
            level=1,
        ),
        ClassDef(
            name='TestSanitizer',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Test the html sanitizer that filters html to remove unwanted attributes ', kind=None),
                ),
                FunctionDef(
                    name='test_basic_sanitizer',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='yop', kind=None),
                                            Constant(value='<p>yop</p>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='lala<p>yop</p>xxx', kind=None),
                                            Constant(value='<p>lala</p><p>yop</p>xxx', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value="Merci à l'intérêt pour notre produit.nous vous contacterons bientôt. Merci", kind=None),
                                            Constant(value="<p>Merci à l'intérêt pour notre produit.nous vous contacterons bientôt. Merci</p>", kind='u'),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='content', ctx=Store()),
                                    Name(id='expected', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='html', ctx=Store())],
                                    value=Call(
                                        func=Name(id='html_sanitize', ctx=Load()),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='html', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
                                            Constant(value='html_sanitize is broken', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_evil_malicious_code',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value="<IMG SRC=javascript:alert('XSS')>", kind=None),
                                    Constant(value='<IMG SRC=&#106;&#97;&#118;&#97;&#115;&#99;&#114;&#105;&#112;&#116;&#58;&#97;&#108;&#101;&#114;&#116;&#40;&#39;&#88;&#83;&#83;&#39;&#41;>', kind=None),
                                    Constant(value='<IMG SRC=&#x6A&#x61&#x76&#x61&#x73&#x63&#x72&#x69&#x70&#x74&#x3A&#x61&#x6C&#x65&#x72&#x74&#x28&#x27&#x58&#x53&#x53&#x27&#x29>', kind=None),
                                    Constant(value='<IMG SRC="jav&#x0D;ascript:alert(\'XSS\');">', kind=None),
                                    Constant(value='<IMG SRC="jav&#x0A;ascript:alert(\'XSS\');">', kind=None),
                                    Constant(value='<IMG SRC="jav   ascript:alert(\'XSS\');">', kind=None),
                                    Constant(value='<IMG SRC="jav&#x09;ascript:alert(\'XSS\');">', kind=None),
                                    Constant(value='<IMG SRC=" &#14;  javascript:alert(\'XSS\');">', kind=None),
                                    Constant(value='<IMG SRC="javascript:alert(\'XSS\')"', kind=None),
                                    Constant(value='<IMG """><SCRIPT>alert("XSS")</SCRIPT>">', kind=None),
                                    Constant(value='<SCRIPT/XSS SRC="http://ha.ckers.org/xss.js"></SCRIPT>', kind=None),
                                    Constant(value='<SCRIPT/SRC="http://ha.ckers.org/xss.js"></SCRIPT>', kind=None),
                                    Constant(value='<<SCRIPT>alert("XSS");//<</SCRIPT>', kind=None),
                                    Constant(value='<SCRIPT SRC=http://ha.ckers.org/xss.js?< B >', kind=None),
                                    Constant(value='<INPUT TYPE="IMAGE" SRC="javascript:alert(\'XSS\');">', kind=None),
                                    Constant(value='<BODY BACKGROUND="javascript:alert(\'XSS\')">', kind=None),
                                    Constant(value='<IMG DYNSRC="javascript:alert(\'XSS\')">', kind=None),
                                    Constant(value='<IMG LOWSRC="javascript:alert(\'XSS\')">', kind=None),
                                    Constant(value='<TABLE BACKGROUND="javascript:alert(\'XSS\')">', kind=None),
                                    Constant(value='<TABLE><TD BACKGROUND="javascript:alert(\'XSS\')">', kind=None),
                                    Constant(value='<DIV STYLE="background-image: url(javascript:alert(\'XSS\'))">', kind=None),
                                    Constant(value='<DIV STYLE="background-image:\x075\x072\x06C\x028\'\x06a\x061\x076\x061\x073\x063\x072\x069\x070\x074\x03a\x061\x06c\x065\x072\x074\x028.1027\x058.1053\x053\x027\x029\'\x029">', kind=None),
                                    Constant(value='<DIV STYLE="background-image: url(&#1;javascript:alert(\'XSS\'))">', kind=None),
                                    Constant(value='<IMG SRC=\'vbscript:msgbox("XSS")\'>', kind=None),
                                    Constant(value="<BODY ONLOAD=alert('XSS')>", kind=None),
                                    Constant(value='<BR SIZE="&{alert(\'XSS\')}\\>', kind=None),
                                    Constant(value='<LINK REL="stylesheet" HREF="javascript:alert(\'XSS\');">', kind=None),
                                    Constant(value='<LINK REL="stylesheet" HREF="http://ha.ckers.org/xss.css">', kind=None),
                                    Constant(value="<STYLE>@import'http://ha.ckers.org/xss.css';</STYLE>", kind=None),
                                    Constant(value='<META HTTP-EQUIV="Link" Content="<http://ha.ckers.org/xss.css>; REL=stylesheet">', kind=None),
                                    Constant(value='<STYLE>BODY{-moz-binding:url("http://ha.ckers.org/xssmoz.xml#xss")}</STYLE>', kind=None),
                                    Constant(value='<IMG STYLE="xss:expr/*XSS*/ession(alert(\'XSS\'))">', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='content', ctx=Store()),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='html', ctx=Store())],
                                    value=Call(
                                        func=Name(id='html_sanitize', ctx=Load()),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertNotIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='javascript', kind=None),
                                            Name(id='html', ctx=Load()),
                                            Constant(value='html_sanitize did not remove a malicious javascript', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BoolOp(
                                                op=Or(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='ha.ckers.org', kind=None),
                                                        ops=[NotIn()],
                                                        comparators=[Name(id='html', ctx=Load())],
                                                    ),
                                                    Compare(
                                                        left=Constant(value='http://ha.ckers.org/xss.css', kind=None),
                                                        ops=[In()],
                                                        comparators=[Name(id='html', ctx=Load())],
                                                    ),
                                                ],
                                            ),
                                            BinOp(
                                                left=Constant(value='html_sanitize did not remove a malicious code in %s (%s)', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Name(id='content', ctx=Load()),
                                                        Name(id='html', ctx=Load()),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Constant(value="<!--[if gte IE 4]><SCRIPT>alert('XSS');</SCRIPT><![endif]-->", kind=None),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='html_sanitize', ctx=Load()),
                                        args=[Name(id='content', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='silent',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='sanitized_html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='MISC_HTML_SOURCE',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='tag', ctx=Store()),
                            iter=List(
                                elts=[
                                    Constant(value='<div', kind=None),
                                    Constant(value='<b', kind=None),
                                    Constant(value='<i', kind=None),
                                    Constant(value='<u', kind=None),
                                    Constant(value='<strike', kind=None),
                                    Constant(value='<li', kind=None),
                                    Constant(value='<blockquote', kind=None),
                                    Constant(value='<a href', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='tag', ctx=Load()),
                                            Name(id='sanitized_html', ctx=Load()),
                                            Constant(value='html_sanitize stripped too much of original html', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='attr', ctx=Store()),
                            iter=List(
                                elts=[Constant(value='javascript', kind=None)],
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertNotIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='attr', ctx=Load()),
                                            Name(id='sanitized_html', ctx=Load()),
                                            Constant(value='html_sanitize did not remove enough unwanted attributes', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_sanitize_unescape_emails',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='not_emails', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='<blockquote cite="mid:CAEJSRZvWvud8c6Qp=wfNG6O1+wK3i_jb33qVrF7XyrgPNjnyUA@mail.gmail.com" type="cite">cat</blockquote>', kind=None),
                                    Constant(value='<img alt="@github-login" class="avatar" src="/web/image/pi" height="36" width="36">', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='not_email', ctx=Store()),
                            iter=Name(id='not_emails', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='sanitized', ctx=Store())],
                                    value=Call(
                                        func=Name(id='html_sanitize', ctx=Load()),
                                        args=[Name(id='not_email', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='left_part', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='not_email', ctx=Load()),
                                                attr='split',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='>', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertNotIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='misc', ctx=Load()),
                                                    attr='html_escape',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='not_email', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='sanitized', ctx=Load()),
                                            Constant(value='html_sanitize stripped emails of original html', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='left_part', ctx=Load()),
                                            Name(id='sanitized', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_style_parsing',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='test_data', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='<span style="position: fixed; top: 0px; left: 50px; width: 40%; height: 50%; background-color: red;">Coin coin </span>', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='background-color:red', kind=None),
                                                    Constant(value='Coin coin', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='position', kind=None),
                                                    Constant(value='top', kind=None),
                                                    Constant(value='left', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='<div style=\'before: "Email Address; coincoin cheval: lapin";  \n   font-size: 30px; max-width: 100%; after: "Not sure\n    \n          this; means: anything ?#ùµ"\n    ; some-property: 2px; top: 3\'>youplaboum</div>', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='font-size:30px', kind=None),
                                                    Constant(value='youplaboum', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='some-property', kind=None),
                                                    Constant(value='top', kind=None),
                                                    Constant(value='cheval', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='<span style="width">Coincoin</span>', kind=None),
                                            List(elts=[], ctx=Load()),
                                            List(
                                                elts=[Constant(value='width', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='test', ctx=Store()),
                                    Name(id='in_lst', ctx=Store()),
                                    Name(id='out_lst', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='test_data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='new_html', ctx=Store())],
                                    value=Call(
                                        func=Name(id='html_sanitize', ctx=Load()),
                                        args=[Name(id='test', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='sanitize_attributes',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='sanitize_style',
                                                value=Constant(value=True, kind=None),
                                            ),
                                            keyword(
                                                arg='strip_style',
                                                value=Constant(value=False, kind=None),
                                            ),
                                            keyword(
                                                arg='strip_classes',
                                                value=Constant(value=False, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='text', ctx=Store()),
                                    iter=Name(id='in_lst', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='text', ctx=Load()),
                                                    Name(id='new_html', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='text', ctx=Store()),
                                    iter=Name(id='out_lst', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertNotIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='text', ctx=Load()),
                                                    Name(id='new_html', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='new_html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Subscript(
                                        value=Subscript(
                                            value=Name(id='test_data', ctx=Load()),
                                            slice=Constant(value=0, kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='sanitize_attributes',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='strip_style',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='strip_classes',
                                        value=Constant(value=False, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='new_html', ctx=Load()),
                                    Constant(value='<span>Coin coin </span>', kind='u'),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_style_class',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='REMOVE_CLASS',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='sanitize_attributes',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='sanitize_style',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='strip_classes',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='REMOVE_CLASS_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='REMOVE_CLASS_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertNotIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_style_class_only',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='REMOVE_CLASS',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='sanitize_attributes',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='sanitize_style',
                                        value=Constant(value=True, kind=None),
                                    ),
                                    keyword(
                                        arg='strip_classes',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='REMOVE_CLASS_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='REMOVE_CLASS_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertNotIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_edi_source',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='EDI_LIKE_HTML_SOURCE',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value="font-family: 'Lucida Grande', Ubuntu, Arial, Verdana, sans-serif;", kind=None),
                                    Name(id='html', ctx=Load()),
                                    Constant(value='html_sanitize removed valid styling', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='src="https://www.paypal.com/en_US/i/btn/btn_paynowCC_LG.gif"', kind=None),
                                    Name(id='html', ctx=Load()),
                                    Constant(value='html_sanitize removed valid img', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='</body></html>', kind=None),
                                    Name(id='html', ctx=Load()),
                                    Constant(value='html_sanitize did not remove extra closing tags', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_blockquote',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='QUOTE_BLOCKQUOTE',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_BLOCKQUOTE_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_BLOCKQUOTE_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<span data-o-mail-quote="1">%s', kind='u'),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='misc', ctx=Load()),
                                                        attr='html_escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='ext', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_thunderbird',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='QUOTE_THUNDERBIRD_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_THUNDERBIRD_1_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_THUNDERBIRD_1_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<span data-o-mail-quote="1">%s</span>', kind='u'),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='misc', ctx=Load()),
                                                        attr='html_escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='ext', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_hotmail_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='QUOTE_HOTMAIL_HTML',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_HOTMAIL_HTML_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_HOTMAIL_HTML_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='HOTMAIL_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='HOTMAIL_1_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='HOTMAIL_1_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_outlook_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='QUOTE_OUTLOOK_HTML',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_OUTLOOK_HTML_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_OUTLOOK_HTML_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_thunderbird_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='QUOTE_THUNDERBIRD_HTML',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_THUNDERBIRD_HTML_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_THUNDERBIRD_HTML_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_yahoo_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='QUOTE_YAHOO_HTML',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_YAHOO_HTML_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='QUOTE_YAHOO_HTML_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_basic_text',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='test_data', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='This is Sparta!\n--\nAdministrator\n+9988776655', kind=None),
                                            List(
                                                elts=[Constant(value='This is Sparta!', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='\n--\nAdministrator\n+9988776655', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='<p>This is Sparta!\n--\nAdministrator</p>', kind=None),
                                            List(elts=[], ctx=Load()),
                                            List(
                                                elts=[Constant(value='\n--\nAdministrator', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='<p>This is Sparta!<br/>--<br>Administrator</p>', kind=None),
                                            List(
                                                elts=[Constant(value='This is Sparta!', kind=None)],
                                                ctx=Load(),
                                            ),
                                            List(elts=[], ctx=Load()),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='This is Sparta!\n>Ah bon ?\nCertes\n> Chouette !\nClair', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='This is Sparta!', kind=None),
                                                    Constant(value='Certes', kind=None),
                                                    Constant(value='Clair', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='\n>Ah bon ?', kind=None),
                                                    Constant(value='\n> Chouette !', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='test', ctx=Store()),
                                    Name(id='in_lst', ctx=Store()),
                                    Name(id='out_lst', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='test_data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='new_html', ctx=Store())],
                                    value=Call(
                                        func=Name(id='html_sanitize', ctx=Load()),
                                        args=[Name(id='test', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='text', ctx=Store()),
                                    iter=Name(id='in_lst', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='text', ctx=Load()),
                                                    Name(id='new_html', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='text', ctx=Store()),
                                    iter=Name(id='out_lst', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    BinOp(
                                                        left=Constant(value='<span data-o-mail-quote="1">%s</span>', kind='u'),
                                                        op=Mod(),
                                                        right=Call(
                                                            func=Attribute(
                                                                value=Name(id='misc', ctx=Load()),
                                                                attr='html_escape',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='text', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    Name(id='new_html', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_signature',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='test_data', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='<div>Hello<pre>--<br />Administrator</pre></div>', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='<pre data-o-mail-quote="1">--', kind=None),
                                                    Constant(value='<br data-o-mail-quote="1">', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='test', ctx=Store()),
                                    Name(id='in_lst', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='test_data', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='new_html', ctx=Store())],
                                    value=Call(
                                        func=Name(id='html_sanitize', ctx=Load()),
                                        args=[Name(id='test', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                For(
                                    target=Name(id='text', ctx=Store()),
                                    iter=Name(id='in_lst', ctx=Load()),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertIn',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='text', ctx=Load()),
                                                    Name(id='new_html', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_gmail',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='GMAIL_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='GMAIL_1_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='GMAIL_1_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<span data-o-mail-quote="1">%s</span>', kind='u'),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='misc', ctx=Load()),
                                                        attr='html_escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='ext', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_text',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='TEXT_1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='TEXT_1_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='TEXT_1_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<span data-o-mail-quote="1">%s</span>', kind='u'),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='misc', ctx=Load()),
                                                        attr='html_escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='ext', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='TEXT_2',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='TEXT_2_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='TEXT_2_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<span data-o-mail-quote="1">%s</span>', kind='u'),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='misc', ctx=Load()),
                                                        attr='html_escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='ext', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_quote_bugs',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[
                                    Attribute(
                                        value=Name(id='test_mail_examples', ctx=Load()),
                                        attr='BUG1',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='BUG_1_IN',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='ext', ctx=Load()),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ext', ctx=Store()),
                            iter=Attribute(
                                value=Name(id='test_mail_examples', ctx=Load()),
                                attr='BUG_1_OUT',
                                ctx=Load(),
                            ),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertIn',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Constant(value='<span data-o-mail-quote="1">%s</span>', kind='u'),
                                                op=Mod(),
                                                right=Call(
                                                    func=Attribute(
                                                        value=Name(id='misc', ctx=Load()),
                                                        attr='html_escape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='ext', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                            Name(id='html', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_misc',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[Constant(value='', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='html', ctx=Load()),
                                    Constant(value='', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[Constant(value=False, kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='html', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='html', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[Constant(value='<?xml version="1.0" encoding="iso-8859-1"?>\n<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN"\n         "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">\n<html xmlns="http://www.w3.org/1999/xhtml" xml:lang="en" lang="en">\n <head>\n  <title>404 - Not Found</title>\n </head>\n <body>\n  <h1>404 - Not Found</h1>\n </body>\n</html>\n', kind='u')],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='encoding', kind=None),
                                    Name(id='html', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertNotIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<title>404 - Not Found</title>', kind=None),
                                    Name(id='html', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertIn',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='<h1>404 - Not Found</h1>', kind=None),
                                    Name(id='html', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_cid_with_at',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='img_tag', ctx=Store())],
                            value=Constant(value='<img src="@">', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='sanitized', ctx=Store())],
                            value=Call(
                                func=Name(id='html_sanitize', ctx=Load()),
                                args=[Name(id='img_tag', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='sanitize_tags',
                                        value=Constant(value=False, kind=None),
                                    ),
                                    keyword(
                                        arg='strip_classes',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='img_tag', ctx=Load()),
                                    Name(id='sanitized', ctx=Load()),
                                    Constant(value="img with can have cid containing @ and shouldn't be escaped", kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestHtmlTools',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Test some of our generic utility functions about html ', kind=None),
                ),
                FunctionDef(
                    name='test_plaintext2html',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='First \nSecond \nThird\n \nParagraph\n\r--\nSignature paragraph', kind=None),
                                            Constant(value='div', kind=None),
                                            Constant(value='<div><p>First <br/>Second <br/>Third</p><p>Paragraph</p><p>--<br/>Signature paragraph</p></div>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='First<p>It should be escaped</p>\nSignature', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='<p>First&lt;p&gt;It should be escaped&lt;/p&gt;<br/>Signature</p>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='content', ctx=Store()),
                                    Name(id='container_tag', ctx=Store()),
                                    Name(id='expected', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='html', ctx=Store())],
                                    value=Call(
                                        func=Name(id='plaintext2html', ctx=Load()),
                                        args=[
                                            Name(id='content', ctx=Load()),
                                            Name(id='container_tag', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Name(id='html', ctx=Load()),
                                            Name(id='expected', ctx=Load()),
                                            Constant(value='plaintext2html is broken', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_append_to_html',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='test_samples', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='<!DOCTYPE...><HTML encoding="blah">some <b>content</b></HtMl>', kind=None),
                                            Constant(value='--\nYours truly', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='<!DOCTYPE...><html encoding="blah">some <b>content</b>\n<pre>--\nYours truly</pre>\n</html>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='<!DOCTYPE...><HTML encoding="blah">some <b>content</b></HtMl>', kind=None),
                                            Constant(value='--\nYours truly', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='<!DOCTYPE...><html encoding="blah">some <b>content</b>\n<p>--<br/>Yours truly</p>\n</html>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='<html><body>some <b>content</b></body></html>', kind=None),
                                            Constant(value='--\nYours & <truly>', kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=True, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='<html><body>some <b>content</b>\n<pre>--\nYours &amp; &lt;truly&gt;</pre>\n</body></html>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='<html><body>some <b>content</b></body></html>', kind=None),
                                            Constant(value='<!DOCTYPE...>\n<html><body>\n<p>--</p>\n<p>Yours truly</p>\n</body>\n</html>', kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value=False, kind=None),
                                            Constant(value='<html><body>some <b>content</b>\n\n\n<p>--</p>\n<p>Yours truly</p>\n\n\n</body></html>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='html', ctx=Store()),
                                    Name(id='content', ctx=Store()),
                                    Name(id='plaintext_flag', ctx=Store()),
                                    Name(id='preserve_flag', ctx=Store()),
                                    Name(id='container_tag', ctx=Store()),
                                    Name(id='expected', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='test_samples', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='append_content_to_html', ctx=Load()),
                                                args=[
                                                    Name(id='html', ctx=Load()),
                                                    Name(id='content', ctx=Load()),
                                                    Name(id='plaintext_flag', ctx=Load()),
                                                    Name(id='preserve_flag', ctx=Load()),
                                                    Name(id='container_tag', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                            Name(id='expected', ctx=Load()),
                                            Constant(value='append_content_to_html is broken', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_is_html_empty',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='void_strings_samples', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='', kind=None),
                                    Constant(value=False, kind=None),
                                    Constant(value=' ', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='content', ctx=Store()),
                            iter=Name(id='void_strings_samples', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='is_html_empty', ctx=Load()),
                                                args=[Name(id='content', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='void_html_samples', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='<p><br></p>', kind=None),
                                    Constant(value='<p><br> </p>', kind=None),
                                    Constant(value='<p><br /></p >', kind=None),
                                    Constant(value='<p style="margin: 4px"></p>', kind=None),
                                    Constant(value='<div style="margin: 4px"></div>', kind=None),
                                    Constant(value='<p class="oe_testing"><br></p>', kind=None),
                                    Constant(value='<p><span style="font-weight: bolder;"><font style="color: rgb(255, 0, 0);" class=" "></font></span><br></p>', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='content', ctx=Store()),
                            iter=Name(id='void_html_samples', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertTrue',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='is_html_empty', ctx=Load()),
                                                args=[Name(id='content', ctx=Load())],
                                                keywords=[],
                                            ),
                                            BinOp(
                                                left=Constant(value='Failed with %s', kind=None),
                                                op=Mod(),
                                                right=Name(id='content', ctx=Load()),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='valid_html_samples', ctx=Store())],
                            value=List(
                                elts=[
                                    Constant(value='<p><br>1</p>', kind=None),
                                    Constant(value='<p>1<br > </p>', kind=None),
                                    Constant(value='<p style="margin: 4px">Hello World</p>', kind=None),
                                    Constant(value='<div style="margin: 4px"><p>Hello World</p></div>', kind=None),
                                    Constant(value='<p><span style="font-weight: bolder;"><font style="color: rgb(255, 0, 0);" class=" ">W</font></span><br></p>', kind=None),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='content', ctx=Store()),
                            iter=Name(id='valid_html_samples', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertFalse',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='is_html_empty', ctx=Load()),
                                                args=[Name(id='content', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_prepend_html_content',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Constant(value='\n            <html>\n                <body>\n                    <div>test</div>\n                </body>\n            </html>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Constant(value='<span>content</span>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='prepend_html_content', ctx=Load()),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='[\\s\\t]', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='result', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='result', ctx=Load()),
                                    Constant(value='<html><body><span>content</span><div>test</div></body></html>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Constant(value='<div>test</div>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Constant(value='<span>content</span>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='prepend_html_content', ctx=Load()),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='[\\s\\t]', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='result', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='result', ctx=Load()),
                                    Constant(value='<span>content</span><div>test</div>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Constant(value='\n            <body>\n                <div>test</div>\n            </body>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='prepend_html_content', ctx=Load()),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='[\\s\\t]', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='result', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='result', ctx=Load()),
                                    Constant(value='<body><span>content</span><div>test</div></body>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='body', ctx=Store())],
                            value=Constant(value='\n            <html>\n                <body>\n                    <div>test</div>\n                </body>\n            </html>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='content', ctx=Store())],
                            value=Constant(value='\n            <html>\n                <body>\n                    <div>test</div>\n                </body>\n            </html>\n        ', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Name(id='prepend_html_content', ctx=Load()),
                                args=[
                                    Name(id='body', ctx=Load()),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='result', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='sub',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='[\\s\\t]', kind=None),
                                    Constant(value='', kind=None),
                                    Name(id='result', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='result', ctx=Load()),
                                    Constant(value='<html><body><div>test</div><div>test</div></body></html>', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestEmailTools',
            bases=[Name(id='BaseCase', ctx=Load())],
            keywords=[],
            body=[
                Expr(
                    value=Constant(value=' Test some of our generic utility functions for emails ', kind=None),
                ),
                FunctionDef(
                    name='test_email_split',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='John <12345@gmail.com>', kind=None),
                                            List(
                                                elts=[Constant(value='12345@gmail.com', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='d@x; 1@2', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='d@x', kind=None),
                                                    Constant(value='1@2', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value="'(ss)' <123@gmail.com>, 'foo' <foo@bar>", kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='123@gmail.com', kind=None),
                                                    Constant(value='foo@bar', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='"john@gmail.com"<johnny@gmail.com>', kind=None),
                                            List(
                                                elts=[Constant(value='johnny@gmail.com', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='"<jg>" <johnny@gmail.com>', kind=None),
                                            List(
                                                elts=[Constant(value='johnny@gmail.com', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='text', ctx=Store()),
                                    Name(id='expected', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='email_split', ctx=Load()),
                                                args=[Name(id='text', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='expected', ctx=Load()),
                                            Constant(value='email_split is broken', kind=None),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_email_formataddr',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='email', ctx=Store())],
                            value=Constant(value='joe@example.com', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='email_idna', ctx=Store())],
                            value=Constant(value='joe@examplé.com', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='cases', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Name(id='email', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='ascii', kind=None),
                                                    Constant(value='utf-8', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='joe@example.com', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='joe', kind=None),
                                                    Name(id='email', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='ascii', kind=None),
                                                    Constant(value='utf-8', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='"joe" <joe@example.com>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='joe doe', kind=None),
                                                    Name(id='email', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='ascii', kind=None),
                                                    Constant(value='utf-8', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='"joe doe" <joe@example.com>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='joe"doe', kind=None),
                                                    Name(id='email', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='ascii', kind=None),
                                                    Constant(value='utf-8', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='"joe\\"doe" <joe@example.com>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='joé', kind=None),
                                                    Name(id='email', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='ascii', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value='=?utf-8?b?am/DqQ==?= <joe@example.com>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='joé', kind=None),
                                                    Name(id='email', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='utf-8', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value='"joé" <joe@example.com>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Name(id='email_idna', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='ascii', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value='joe@xn--exampl-gva.com', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Name(id='email_idna', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='utf-8', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value='joe@examplé.com', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='joé', kind=None),
                                                    Name(id='email_idna', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='ascii', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value='=?utf-8?b?am/DqQ==?= <joe@xn--exampl-gva.com>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='joé', kind=None),
                                                    Name(id='email_idna', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[Constant(value='utf-8', kind=None)],
                                                ctx=Load(),
                                            ),
                                            Constant(value='"joé" <joe@examplé.com>', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='', kind=None),
                                                    Constant(value='joé@example.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            List(
                                                elts=[
                                                    Constant(value='ascii', kind=None),
                                                    Constant(value='utf-8', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                            Constant(value='joé@example.com', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='pair', ctx=Store()),
                                    Name(id='charsets', ctx=Store()),
                                    Name(id='expected', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='cases', ctx=Load()),
                            body=[
                                For(
                                    target=Name(id='charset', ctx=Store()),
                                    iter=Name(id='charsets', ctx=Load()),
                                    body=[
                                        With(
                                            items=[
                                                withitem(
                                                    context_expr=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='subTest',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[
                                                            keyword(
                                                                arg='pair',
                                                                value=Name(id='pair', ctx=Load()),
                                                            ),
                                                            keyword(
                                                                arg='charset',
                                                                value=Name(id='charset', ctx=Load()),
                                                            ),
                                                        ],
                                                    ),
                                                    optional_vars=None,
                                                ),
                                            ],
                                            body=[
                                                Expr(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='assertEqual',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Call(
                                                                func=Name(id='formataddr', ctx=Load()),
                                                                args=[
                                                                    Name(id='pair', ctx=Load()),
                                                                    Name(id='charset', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                            Name(id='expected', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                ),
                                            ],
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_extract_rfc2822_addresses',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='tests', ctx=Store())],
                            value=List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='"Admin" <admin@example.com>', kind=None),
                                            List(
                                                elts=[Constant(value='admin@example.com', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='"Admin" <admin@example.com>, Demo <demo@test.com>', kind=None),
                                            List(
                                                elts=[
                                                    Constant(value='admin@example.com', kind=None),
                                                    Constant(value='demo@test.com', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='admin@example.com', kind=None),
                                            List(
                                                elts=[Constant(value='admin@example.com', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='"Admin" <admin@example.com>, Demo <malformed email>', kind=None),
                                            List(
                                                elts=[Constant(value='admin@example.com', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='admin@éxample.com', kind=None),
                                            List(
                                                elts=[Constant(value='admin@xn--xample-9ua.com', kind=None)],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Tuple(
                                elts=[
                                    Name(id='rfc2822_email', ctx=Store()),
                                    Name(id='expected', ctx=Store()),
                                ],
                                ctx=Store(),
                            ),
                            iter=Name(id='tests', ctx=Load()),
                            body=[
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='assertEqual',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='extract_rfc2822_addresses', ctx=Load()),
                                                args=[Name(id='rfc2822_email', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Name(id='expected', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='test_email_domain_normalize',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='email_domain_normalize', ctx=Load()),
                                        args=[Constant(value='Test.Com', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value='test.com', kind=None),
                                    Constant(value='Should have normalized the domain', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='email_domain_normalize', ctx=Load()),
                                        args=[Constant(value='email@test.com', kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value='The domain is not valid, should return False', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='email_domain_normalize', ctx=Load()),
                                        args=[Constant(value=False, kind=None)],
                                        keywords=[],
                                    ),
                                    Constant(value=False, kind=None),
                                    Constant(value='The domain is not valid, should return False', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='EmailConfigCase',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_default_email_from',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=arg(arg='args', annotation=None, type_comment=None),
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Email from setting is respected.', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ICP', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ICP', ctx=Load()),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.catchall.domain', kind=None),
                                    Constant(value='example.org', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ICP', ctx=Load()),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.default.from', kind=None),
                                    Constant(value='icp', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.mail_server', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='build_email',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=False, kind=None),
                                    Constant(value='recipient@example.com', kind=None),
                                    Constant(value='Subject', kind=None),
                                    Constant(value='The body of an email', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='From', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='icp@example.org', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='ICP', ctx=Load()),
                                    attr='set_param',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='mail.default.from', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='message', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.mail_server', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='build_email',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value=False, kind=None),
                                    Constant(value='recipient@example.com', kind=None),
                                    Constant(value='Subject', kind=None),
                                    Constant(value='The body of an email', kind=None),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Subscript(
                                        value=Name(id='message', ctx=Load()),
                                        slice=Constant(value='From', kind=None),
                                        ctx=Load(),
                                    ),
                                    Constant(value='settings@example.com', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='patch', ctx=Load()),
                                attr='dict',
                                ctx=Load(),
                            ),
                            args=[
                                Constant(value='odoo.tools.config.options', kind=None),
                                Dict(
                                    keys=[Constant(value='email_from', kind=None)],
                                    values=[Constant(value='settings@example.com', kind=None)],
                                ),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        ClassDef(
            name='TestEmailMessage',
            bases=[Name(id='TransactionCase', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_as_string',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='self', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Constant(value='Ensure all email sent are bpo-34424 and bpo-35805 free', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='message_truth', ctx=Store())],
                            value=Constant(value='From: .+? <joe@example\\.com>\\r\\nTo: .+? <joe@example\\.com>\\r\\nMessage-Id: <[0-9a-z.-]+@[0-9a-z.-]+>\\r\\nReferences: (<[0-9a-z.-]+@[0-9a-z.-]+>\\s*)+\\r\\n\\r\\n', kind=None),
                            type_comment=None,
                        ),
                        ClassDef(
                            name='FakeSMTP',
                            bases=[],
                            keywords=[],
                            body=[
                                Expr(
                                    value=Constant(value='SMTP stub', kind=None),
                                ),
                                FunctionDef(
                                    name='__init__',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[arg(arg='this', annotation=None, type_comment=None)],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='this', ctx=Load()),
                                                    attr='email_sent',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=False, kind=None),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='this', ctx=Load()),
                                                    attr='from_filter',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value='example.com', kind=None),
                                            type_comment=None,
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                FunctionDef(
                                    name='sendmail',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[
                                            arg(arg='this', annotation=None, type_comment=None),
                                            arg(arg='smtp_from', annotation=None, type_comment=None),
                                            arg(arg='smtp_to_list', annotation=None, type_comment=None),
                                            arg(arg='message_str', annotation=None, type_comment=None),
                                            arg(arg='mail_options', annotation=None, type_comment=None),
                                            arg(arg='rcpt_options', annotation=None, type_comment=None),
                                        ],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[
                                            Tuple(elts=[], ctx=Load()),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='this', ctx=Load()),
                                                    attr='email_sent',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertRegex',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='message_str', ctx=Load()),
                                                    Name(id='message_truth', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                                FunctionDef(
                                    name='send_message',
                                    args=arguments(
                                        posonlyargs=[],
                                        args=[
                                            arg(arg='this', annotation=None, type_comment=None),
                                            arg(arg='message', annotation=None, type_comment=None),
                                            arg(arg='smtp_from', annotation=None, type_comment=None),
                                            arg(arg='smtp_to_list', annotation=None, type_comment=None),
                                            arg(arg='mail_options', annotation=None, type_comment=None),
                                            arg(arg='rcpt_options', annotation=None, type_comment=None),
                                        ],
                                        vararg=None,
                                        kwonlyargs=[],
                                        kw_defaults=[],
                                        kwarg=None,
                                        defaults=[
                                            Tuple(elts=[], ctx=Load()),
                                            Tuple(elts=[], ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='message_str', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='message', ctx=Load()),
                                                    attr='as_string',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='this', ctx=Load()),
                                                    attr='email_sent',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Constant(value=True, kind=None),
                                            type_comment=None,
                                        ),
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='assertRegex',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='message_str', ctx=Load()),
                                                    Name(id='message_truth', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    decorator_list=[],
                                    returns=None,
                                    type_comment=None,
                                ),
                            ],
                            decorator_list=[],
                        ),
                        Assign(
                            targets=[Name(id='msg', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='email', ctx=Load()),
                                        attr='message',
                                        ctx=Load(),
                                    ),
                                    attr='EmailMessage',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='policy',
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='email', ctx=Load()),
                                                attr='policy',
                                                ctx=Load(),
                                            ),
                                            attr='SMTP',
                                            ctx=Load(),
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='From', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='"Joé Doe" <joe@example.com>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='To', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='"Joé Doe" <joe@example.com>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='Message-Id', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='<929227342217024.1596730490.324691772460938-example-30661-some.reference@test-123.example.com>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='msg', ctx=Load()),
                                    slice=Constant(value='References', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='<345227342212345.1596730777.324691772483620-example-30453-other.reference@test-123.example.com>', kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='smtp', ctx=Store())],
                            value=Call(
                                func=Name(id='FakeSMTP', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='patch',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='threading', ctx=Load()),
                                            attr='currentThread',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    Constant(value='testing', kind=None),
                                    Constant(value=False, kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='ir.mail_server', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='send_email',
                                    ctx=Load(),
                                ),
                                args=[Name(id='msg', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='smtp_session',
                                        value=Name(id='smtp', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertTrue',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='smtp', ctx=Load()),
                                        attr='email_sent',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
