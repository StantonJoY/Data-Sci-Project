Module(
    body=[
        Expr(
            value=Name(id='x', ctx=Load()),
        ),
        Import(
            names=[alias(name='contextlib', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='uuid', asname=None)],
        ),
        ImportFrom(
            module='unittest.mock',
            names=[alias(name='patch', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='exceptions', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.tests.common',
            names=[alias(name='BaseCase', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='pycompat', asname=None)],
            level=0,
        ),
        Assign(
            targets=[Name(id='_logger', ctx=Store())],
            value=Call(
                func=Attribute(
                    value=Name(id='logging', ctx=Load()),
                    attr='getLogger',
                    ctx=Load(),
                ),
                args=[Name(id='__name__', ctx=Load())],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='DEFAULT_ENDPOINT', ctx=Store())],
            value=Constant(value='https://iap.odoo.com', kind=None),
            type_comment=None,
        ),
        FunctionDef(
            name='iap_jsonrpc_mocked',
            args=arguments(
                posonlyargs=[],
                args=[],
                vararg=arg(arg='args', annotation=None, type_comment=None),
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                defaults=[],
            ),
            body=[
                Raise(
                    exc=Call(
                        func=Attribute(
                            value=Name(id='exceptions', ctx=Load()),
                            attr='AccessError',
                            ctx=Load(),
                        ),
                        args=[Constant(value='Unavailable during tests.', kind=None)],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='iap_patch', ctx=Store())],
            value=Call(
                func=Name(id='patch', ctx=Load()),
                args=[
                    Constant(value='odoo.addons.iap.tools.iap_tools.iap_jsonrpc', kind=None),
                    Name(id='iap_jsonrpc_mocked', ctx=Load()),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='setUp',
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
                        func=Name(id='old_setup_func', ctx=Load()),
                        args=[Name(id='self', ctx=Load())],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='iap_patch', ctx=Load()),
                            attr='start',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='self', ctx=Load()),
                            attr='addCleanup',
                            ctx=Load(),
                        ),
                        args=[
                            Attribute(
                                value=Name(id='iap_patch', ctx=Load()),
                                attr='stop',
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
        Assign(
            targets=[Name(id='old_setup_func', ctx=Store())],
            value=Attribute(
                value=Name(id='BaseCase', ctx=Load()),
                attr='setUp',
                ctx=Load(),
            ),
            type_comment=None,
        ),
        Assign(
            targets=[
                Attribute(
                    value=Name(id='BaseCase', ctx=Load()),
                    attr='setUp',
                    ctx=Store(),
                ),
            ],
            value=Name(id='setUp', ctx=Load()),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_MAIL_DOMAIN_BLACKLIST', ctx=Store())],
            value=Call(
                func=Name(id='set', ctx=Load()),
                args=[
                    List(
                        elts=[
                            Constant(value='gmail.com', kind=None),
                            Constant(value='hotmail.com', kind=None),
                            Constant(value='yahoo.com', kind=None),
                            Constant(value='qq.com', kind=None),
                            Constant(value='outlook.com', kind=None),
                            Constant(value='163.com', kind=None),
                            Constant(value='yahoo.fr', kind=None),
                            Constant(value='live.com', kind=None),
                            Constant(value='hotmail.fr', kind=None),
                            Constant(value='icloud.com', kind=None),
                            Constant(value='126.com', kind=None),
                            Constant(value='me.com', kind=None),
                            Constant(value='free.fr', kind=None),
                            Constant(value='ymail.com', kind=None),
                            Constant(value='msn.com', kind=None),
                            Constant(value='mail.com', kind=None),
                            Constant(value='orange.fr', kind=None),
                            Constant(value='aol.com', kind=None),
                            Constant(value='wanadoo.fr', kind=None),
                            Constant(value='live.fr', kind=None),
                            Constant(value='mail.ru', kind=None),
                            Constant(value='yahoo.co.in', kind=None),
                            Constant(value='rediffmail.com', kind=None),
                            Constant(value='hku.hk', kind=None),
                            Constant(value='googlemail.com', kind=None),
                            Constant(value='gmx.de', kind=None),
                            Constant(value='sina.com', kind=None),
                            Constant(value='skynet.be', kind=None),
                            Constant(value='laposte.net', kind=None),
                            Constant(value='yahoo.co.uk', kind=None),
                            Constant(value='yahoo.co.id', kind=None),
                            Constant(value='web.de', kind=None),
                            Constant(value='gmail.com ', kind=None),
                            Constant(value='outlook.fr', kind=None),
                            Constant(value='telenet.be', kind=None),
                            Constant(value='yahoo.es', kind=None),
                            Constant(value='naver.com', kind=None),
                            Constant(value='hotmail.co.uk', kind=None),
                            Constant(value='gmai.com', kind=None),
                            Constant(value='foxmail.com', kind=None),
                            Constant(value='hku.hku', kind=None),
                            Constant(value='bluewin.ch', kind=None),
                            Constant(value='sfr.fr', kind=None),
                            Constant(value='libero.it', kind=None),
                            Constant(value='mac.com', kind=None),
                            Constant(value='rocketmail.com', kind=None),
                            Constant(value='protonmail.com', kind=None),
                            Constant(value='gmx.com', kind=None),
                            Constant(value='gamil.com', kind=None),
                            Constant(value='hotmail.es', kind=None),
                            Constant(value='gmx.net', kind=None),
                            Constant(value='comcast.net', kind=None),
                            Constant(value='yahoo.com.mx', kind=None),
                            Constant(value='linkedin.com', kind=None),
                            Constant(value='yahoo.com.br', kind=None),
                            Constant(value='yahoo.in', kind=None),
                            Constant(value='yahoo.ca', kind=None),
                            Constant(value='t-online.de', kind=None),
                            Constant(value='139.com', kind=None),
                            Constant(value='yandex.ru', kind=None),
                            Constant(value='yahoo.com.hk', kind=None),
                            Constant(value='yahoo.de', kind=None),
                            Constant(value='yeah.net', kind=None),
                            Constant(value='yandex.com', kind=None),
                            Constant(value='nwytg.net', kind=None),
                            Constant(value='neuf.fr', kind=None),
                            Constant(value='yahoo.com.ar', kind=None),
                            Constant(value='outlook.es', kind=None),
                            Constant(value='abv.bg', kind=None),
                            Constant(value='aliyun.com', kind=None),
                            Constant(value='yahoo.com.tw', kind=None),
                            Constant(value='ukr.net', kind=None),
                            Constant(value='live.nl', kind=None),
                            Constant(value='wp.pl', kind=None),
                            Constant(value='hotmail.it', kind=None),
                            Constant(value='live.com.mx', kind=None),
                            Constant(value='zoho.com', kind=None),
                            Constant(value='live.co.uk', kind=None),
                            Constant(value='sohu.com', kind=None),
                            Constant(value='twoomail.com', kind=None),
                            Constant(value='yahoo.com.sg', kind=None),
                            Constant(value='odoo.com', kind=None),
                            Constant(value='yahoo.com.vn', kind=None),
                            Constant(value='windowslive.com', kind=None),
                            Constant(value='gmail', kind=None),
                            Constant(value='vols.utk.edu', kind=None),
                            Constant(value='email.com', kind=None),
                            Constant(value='tiscali.it', kind=None),
                            Constant(value='yahoo.it', kind=None),
                            Constant(value='gmx.ch', kind=None),
                            Constant(value='trbvm.com', kind=None),
                            Constant(value='nwytg.com', kind=None),
                            Constant(value='mvrht.com', kind=None),
                            Constant(value='nyit.edu', kind=None),
                            Constant(value='o2.pl', kind=None),
                            Constant(value='live.cn', kind=None),
                            Constant(value='gmial.com', kind=None),
                            Constant(value='seznam.cz', kind=None),
                            Constant(value='live.be', kind=None),
                            Constant(value='videotron.ca', kind=None),
                            Constant(value='gmil.com', kind=None),
                            Constant(value='live.ca', kind=None),
                            Constant(value='hotmail.de', kind=None),
                            Constant(value='sbcglobal.net', kind=None),
                            Constant(value='connect.hku.hk', kind=None),
                            Constant(value='yahoo.com.au', kind=None),
                            Constant(value='att.net', kind=None),
                            Constant(value='live.in', kind=None),
                            Constant(value='btinternet.com', kind=None),
                            Constant(value='gmx.fr', kind=None),
                            Constant(value='voila.fr', kind=None),
                            Constant(value='shaw.ca', kind=None),
                            Constant(value='prodigy.net.mx', kind=None),
                            Constant(value='vip.qq.com', kind=None),
                            Constant(value='yahoo.com.ph', kind=None),
                            Constant(value='bigpond.com', kind=None),
                            Constant(value='7thcomputing.com', kind=None),
                            Constant(value='freenet.de', kind=None),
                            Constant(value='alice.it', kind=None),
                            Constant(value='esi.dz', kind=None),
                            Constant(value='bk.ru', kind=None),
                            Constant(value='mail.odoo.com', kind=None),
                            Constant(value='gmail.con', kind=None),
                            Constant(value='fiu.edu', kind=None),
                            Constant(value='gmal.com', kind=None),
                            Constant(value='useemlikefun.com', kind=None),
                            Constant(value='google.com', kind=None),
                            Constant(value='trbvn.com', kind=None),
                            Constant(value='yopmail.com', kind=None),
                            Constant(value='ya.ru', kind=None),
                            Constant(value='hotmail.co.th', kind=None),
                            Constant(value='arcor.de', kind=None),
                            Constant(value='hotmail.ca', kind=None),
                            Constant(value='21cn.com', kind=None),
                            Constant(value='live.de', kind=None),
                            Constant(value='outlook.de', kind=None),
                            Constant(value='gmailcom', kind=None),
                            Constant(value='unal.edu.co', kind=None),
                            Constant(value='tom.com', kind=None),
                            Constant(value='yahoo.gr', kind=None),
                            Constant(value='gmx.at', kind=None),
                            Constant(value='inbox.lv', kind=None),
                            Constant(value='ziggo.nl', kind=None),
                            Constant(value='xs4all.nl', kind=None),
                            Constant(value='sapo.pt', kind=None),
                            Constant(value='live.com.au', kind=None),
                            Constant(value='nate.com', kind=None),
                            Constant(value='online.de', kind=None),
                            Constant(value='sina.cn', kind=None),
                            Constant(value='gmail.co', kind=None),
                            Constant(value='rogers.com', kind=None),
                            Constant(value='mailinator.com', kind=None),
                            Constant(value='cox.net', kind=None),
                            Constant(value='hotmail.be', kind=None),
                            Constant(value='verizon.net', kind=None),
                            Constant(value='yahoo.co.jp', kind=None),
                            Constant(value='usa.com', kind=None),
                            Constant(value='consultant.com', kind=None),
                            Constant(value='hotmai.com', kind=None),
                            Constant(value='189.cn', kind=None),
                            Constant(value='sky.com', kind=None),
                            Constant(value='eezee-it.com', kind=None),
                            Constant(value='opayq.com', kind=None),
                            Constant(value='maildrop.cc', kind=None),
                            Constant(value='home.nl', kind=None),
                            Constant(value='virgilio.it', kind=None),
                            Constant(value='outlook.be', kind=None),
                            Constant(value='hanmail.net', kind=None),
                            Constant(value='uol.com.br', kind=None),
                            Constant(value='hec.ca', kind=None),
                            Constant(value='terra.com.br', kind=None),
                            Constant(value='inbox.ru', kind=None),
                            Constant(value='tin.it', kind=None),
                            Constant(value='list.ru', kind=None),
                            Constant(value='hotmail.com ', kind=None),
                            Constant(value='safecoms.com', kind=None),
                            Constant(value='smile.fr', kind=None),
                            Constant(value='sprintit.fi', kind=None),
                            Constant(value='uniminuto.edu.co', kind=None),
                            Constant(value='bol.com.br', kind=None),
                            Constant(value='bellsouth.net', kind=None),
                            Constant(value='nirmauni.ac.in', kind=None),
                            Constant(value='ldc.edu.in', kind=None),
                            Constant(value='ig.com.br', kind=None),
                            Constant(value='engineer.com', kind=None),
                            Constant(value='scarlet.be', kind=None),
                            Constant(value='inbox.com', kind=None),
                            Constant(value='gmaill.com', kind=None),
                            Constant(value='freemail.hu', kind=None),
                            Constant(value='live.it', kind=None),
                            Constant(value='blackwaretech.com', kind=None),
                            Constant(value='byom.de', kind=None),
                            Constant(value='dispostable.com', kind=None),
                            Constant(value='dayrep.com', kind=None),
                            Constant(value='aim.com', kind=None),
                            Constant(value='prixgen.com', kind=None),
                            Constant(value='gmail.om', kind=None),
                            Constant(value='asterisk-tech.mn', kind=None),
                            Constant(value='in.com', kind=None),
                            Constant(value='aliceadsl.fr', kind=None),
                            Constant(value='lycos.com', kind=None),
                            Constant(value='topnet.tn', kind=None),
                            Constant(value='teleworm.us', kind=None),
                            Constant(value='kedgebs.com', kind=None),
                            Constant(value='supinfo.com', kind=None),
                            Constant(value='posteo.de', kind=None),
                            Constant(value='yahoo.com ', kind=None),
                            Constant(value='op.pl', kind=None),
                            Constant(value='gmail.fr', kind=None),
                            Constant(value='grr.la', kind=None),
                            Constant(value='oci.fr', kind=None),
                            Constant(value='aselcis.com', kind=None),
                            Constant(value='optusnet.com.au', kind=None),
                            Constant(value='mailcatch.com', kind=None),
                            Constant(value='rambler.ru', kind=None),
                            Constant(value='protonmail.ch', kind=None),
                            Constant(value='prisme.ch', kind=None),
                            Constant(value='bbox.fr', kind=None),
                            Constant(value='orbitalu.com', kind=None),
                            Constant(value='netcourrier.com', kind=None),
                            Constant(value='iinet.net.au', kind=None),
                            Constant(value='example.com', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        Assign(
            targets=[Name(id='_STATES_FILTER_COUNTRIES_WHITELIST', ctx=Store())],
            value=Call(
                func=Name(id='set', ctx=Load()),
                args=[
                    List(
                        elts=[
                            Constant(value='AR', kind=None),
                            Constant(value='AU', kind=None),
                            Constant(value='BR', kind=None),
                            Constant(value='CA', kind=None),
                            Constant(value='IN', kind=None),
                            Constant(value='MY', kind=None),
                            Constant(value='MX', kind=None),
                            Constant(value='NZ', kind=None),
                            Constant(value='AE', kind=None),
                            Constant(value='US', kind=None),
                        ],
                        ctx=Load(),
                    ),
                ],
                keywords=[],
            ),
            type_comment=None,
        ),
        FunctionDef(
            name='iap_get_endpoint',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='env', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='url', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.config_parameter', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='sudo',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            attr='get_param',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='iap.endpoint', kind=None),
                            Name(id='DEFAULT_ENDPOINT', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='url', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='InsufficientCreditError',
            bases=[Name(id='Exception', ctx=Load())],
            keywords=[],
            body=[Pass()],
            decorator_list=[],
        ),
        FunctionDef(
            name='iap_jsonrpc',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='url', annotation=None, type_comment=None),
                    arg(arg='method', annotation=None, type_comment=None),
                    arg(arg='params', annotation=None, type_comment=None),
                    arg(arg='timeout', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='call', kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=15, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Calls the provided JSON-RPC endpoint, unwraps the result and\n    returns JSON-RPC errors as exceptions.\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='payload', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='jsonrpc', kind=None),
                            Constant(value='method', kind=None),
                            Constant(value='params', kind=None),
                            Constant(value='id', kind=None),
                        ],
                        values=[
                            Constant(value='2.0', kind=None),
                            Name(id='method', ctx=Load()),
                            Name(id='params', ctx=Load()),
                            Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='uuid', ctx=Load()),
                                        attr='uuid4',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='hex',
                                ctx=Load(),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='_logger', ctx=Load()),
                            attr='info',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='iap jsonrpc %s', kind=None),
                            Name(id='url', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='req', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[Name(id='url', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='json',
                                        value=Name(id='payload', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Name(id='timeout', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='req', ctx=Load()),
                                    attr='raise_for_status',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='req', ctx=Load()),
                                    attr='json',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Constant(value='error', kind=None),
                                ops=[In()],
                                comparators=[Name(id='response', ctx=Load())],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='name', ctx=Store())],
                                    value=Subscript(
                                        value=Call(
                                            func=Attribute(
                                                value=Call(
                                                    func=Attribute(
                                                        value=Subscript(
                                                            value=Subscript(
                                                                value=Name(id='response', ctx=Load()),
                                                                slice=Constant(value='error', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            slice=Constant(value='data', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        attr='get',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Constant(value='name', kind=None)],
                                                    keywords=[],
                                                ),
                                                attr='rpartition',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='.', kind=None)],
                                            keywords=[],
                                        ),
                                        slice=UnaryOp(
                                            op=USub(),
                                            operand=Constant(value=1, kind=None),
                                        ),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='message', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Subscript(
                                                    value=Name(id='response', ctx=Load()),
                                                    slice=Constant(value='error', kind=None),
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='data', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='message', kind=None)],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=Name(id='name', ctx=Load()),
                                        ops=[Eq()],
                                        comparators=[Constant(value='InsufficientCreditError', kind=None)],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='e_class', ctx=Store())],
                                            value=Name(id='InsufficientCreditError', ctx=Load()),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Compare(
                                                left=Name(id='name', ctx=Load()),
                                                ops=[Eq()],
                                                comparators=[Constant(value='AccessError', kind=None)],
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='e_class', ctx=Store())],
                                                    value=Attribute(
                                                        value=Name(id='exceptions', ctx=Load()),
                                                        attr='AccessError',
                                                        ctx=Load(),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Compare(
                                                        left=Name(id='name', ctx=Load()),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='UserError', kind=None)],
                                                    ),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='e_class', ctx=Store())],
                                                            value=Attribute(
                                                                value=Name(id='exceptions', ctx=Load()),
                                                                attr='UserError',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        Raise(
                                                            exc=Call(
                                                                func=Attribute(
                                                                    value=Attribute(
                                                                        value=Name(id='requests', ctx=Load()),
                                                                        attr='exceptions',
                                                                        ctx=Load(),
                                                                    ),
                                                                    attr='ConnectionError',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            cause=None,
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                                Assign(
                                    targets=[Name(id='e', ctx=Store())],
                                    value=Call(
                                        func=Name(id='e_class', ctx=Load()),
                                        args=[Name(id='message', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[
                                        Attribute(
                                            value=Name(id='e', ctx=Load()),
                                            attr='data',
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Subscript(
                                        value=Subscript(
                                            value=Name(id='response', ctx=Load()),
                                            slice=Constant(value='error', kind=None),
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='data', kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Name(id='e', ctx=Load()),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='response', ctx=Load()),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='result', kind=None)],
                                keywords=[],
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Tuple(
                                elts=[
                                    Name(id='ValueError', ctx=Load()),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='ConnectionError',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='MissingSchema',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='Timeout',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='requests', ctx=Load()),
                                            attr='exceptions',
                                            ctx=Load(),
                                        ),
                                        attr='HTTPError',
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                            name='e',
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Name(id='exceptions', ctx=Load()),
                                            attr='AccessError',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[
                                                    Constant(value='The url that this service requested returned an error. Please contact the author of the app. The url it tried to contact was %s', kind=None),
                                                    Name(id='url', ctx=Load()),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        ClassDef(
            name='IapTransaction',
            bases=[Name(id='object', ctx=Load())],
            keywords=[],
            body=[
                FunctionDef(
                    name='__init__',
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
                            targets=[
                                Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='credit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value=None, kind=None),
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
        FunctionDef(
            name='iap_authorize',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='key', annotation=None, type_comment=None),
                    arg(arg='account_token', annotation=None, type_comment=None),
                    arg(arg='credit', annotation=None, type_comment=None),
                    arg(arg='dbuuid', annotation=None, type_comment=None),
                    arg(arg='description', annotation=None, type_comment=None),
                    arg(arg='credit_template', annotation=None, type_comment=None),
                    arg(arg='ttl', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=4320, kind=None),
                ],
            ),
            body=[
                Assign(
                    targets=[Name(id='endpoint', ctx=Store())],
                    value=Call(
                        func=Name(id='iap_get_endpoint', ctx=Load()),
                        args=[Name(id='env', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='params', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='account_token', kind=None),
                            Constant(value='credit', kind=None),
                            Constant(value='key', kind=None),
                            Constant(value='description', kind=None),
                            Constant(value='ttl', kind=None),
                        ],
                        values=[
                            Name(id='account_token', ctx=Load()),
                            Name(id='credit', ctx=Load()),
                            Name(id='key', ctx=Load()),
                            Name(id='description', ctx=Load()),
                            Name(id='ttl', ctx=Load()),
                        ],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='dbuuid', ctx=Load()),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='params', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[Constant(value='dbuuid', kind=None)],
                                        values=[Name(id='dbuuid', ctx=Load())],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='transaction_token', ctx=Store())],
                            value=Call(
                                func=Name(id='iap_jsonrpc', ctx=Load()),
                                args=[
                                    BinOp(
                                        left=Name(id='endpoint', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value='/iap/1/authorize', kind=None),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Name(id='params', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='InsufficientCreditError', ctx=Load()),
                            name='e',
                            body=[
                                If(
                                    test=Name(id='credit_template', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='arguments', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='json', ctx=Load()),
                                                    attr='loads',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Subscript(
                                                        value=Attribute(
                                                            value=Name(id='e', ctx=Load()),
                                                            attr='args',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value=0, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='arguments', ctx=Load()),
                                                    slice=Constant(value='body', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='pycompat', ctx=Load()),
                                                    attr='to_text',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Name(id='env', ctx=Load()),
                                                                slice=Constant(value='ir.qweb', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='_render',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='credit_template', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[
                                                Attribute(
                                                    value=Name(id='e', ctx=Load()),
                                                    attr='args',
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Tuple(
                                                elts=[
                                                    Call(
                                                        func=Attribute(
                                                            value=Name(id='json', ctx=Load()),
                                                            attr='dumps',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Name(id='arguments', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Raise(
                                    exc=Name(id='e', ctx=Load()),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[],
                    finalbody=[],
                ),
                Return(
                    value=Name(id='transaction_token', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='iap_cancel',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='transaction_token', annotation=None, type_comment=None),
                    arg(arg='key', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='endpoint', ctx=Store())],
                    value=Call(
                        func=Name(id='iap_get_endpoint', ctx=Load()),
                        args=[Name(id='env', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='params', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='token', kind=None),
                            Constant(value='key', kind=None),
                        ],
                        values=[
                            Name(id='transaction_token', ctx=Load()),
                            Name(id='key', ctx=Load()),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='r', ctx=Store())],
                    value=Call(
                        func=Name(id='iap_jsonrpc', ctx=Load()),
                        args=[
                            BinOp(
                                left=Name(id='endpoint', ctx=Load()),
                                op=Add(),
                                right=Constant(value='/iap/1/cancel', kind=None),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='params',
                                value=Name(id='params', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='r', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='iap_capture',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='transaction_token', annotation=None, type_comment=None),
                    arg(arg='key', annotation=None, type_comment=None),
                    arg(arg='credit', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='endpoint', ctx=Store())],
                    value=Call(
                        func=Name(id='iap_get_endpoint', ctx=Load()),
                        args=[Name(id='env', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='params', ctx=Store())],
                    value=Dict(
                        keys=[
                            Constant(value='token', kind=None),
                            Constant(value='key', kind=None),
                            Constant(value='credit_to_capture', kind=None),
                        ],
                        values=[
                            Name(id='transaction_token', ctx=Load()),
                            Name(id='key', ctx=Load()),
                            Name(id='credit', ctx=Load()),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='r', ctx=Store())],
                    value=Call(
                        func=Name(id='iap_jsonrpc', ctx=Load()),
                        args=[
                            BinOp(
                                left=Name(id='endpoint', ctx=Load()),
                                op=Add(),
                                right=Constant(value='/iap/1/capture', kind=None),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='params',
                                value=Name(id='params', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Name(id='r', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='iap_charge',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='env', annotation=None, type_comment=None),
                    arg(arg='key', annotation=None, type_comment=None),
                    arg(arg='account_token', annotation=None, type_comment=None),
                    arg(arg='credit', annotation=None, type_comment=None),
                    arg(arg='dbuuid', annotation=None, type_comment=None),
                    arg(arg='description', annotation=None, type_comment=None),
                    arg(arg='credit_template', annotation=None, type_comment=None),
                    arg(arg='ttl', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value=False, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=4320, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value="\n    Account charge context manager: takes a hold for ``credit``\n    amount before executing the body, then captures it if there\n    is no error, or cancels it if the body generates an exception.\n\n    :param str key: service identifier\n    :param str account_token: user identifier\n    :param int credit: cost of the body's operation\n    :param description: a description of the purpose of the charge,\n                        the user will be able to see it in their\n                        dashboard\n    :type description: str\n    :param credit_template: a QWeb template to render and show to the\n                            user if their account does not have enough\n                            credits for the requested operation\n    :param int ttl: transaction time to live in hours.\n                    If the credit are not captured when the transaction\n                    expires, the transaction is canceled\n    :type credit_template: str\n    ", kind=None),
                ),
                Assign(
                    targets=[Name(id='transaction_token', ctx=Store())],
                    value=Call(
                        func=Name(id='iap_authorize', ctx=Load()),
                        args=[
                            Name(id='env', ctx=Load()),
                            Name(id='key', ctx=Load()),
                            Name(id='account_token', ctx=Load()),
                            Name(id='credit', ctx=Load()),
                            Name(id='dbuuid', ctx=Load()),
                            Name(id='description', ctx=Load()),
                            Name(id='credit_template', ctx=Load()),
                            Name(id='ttl', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Try(
                    body=[
                        Assign(
                            targets=[Name(id='transaction', ctx=Store())],
                            value=Call(
                                func=Name(id='IapTransaction', ctx=Load()),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='transaction', ctx=Load()),
                                    attr='credit',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='credit', ctx=Load()),
                            type_comment=None,
                        ),
                        Expr(
                            value=Yield(
                                value=Name(id='transaction', ctx=Load()),
                            ),
                        ),
                    ],
                    handlers=[
                        ExceptHandler(
                            type=Name(id='Exception', ctx=Load()),
                            name='e',
                            body=[
                                Assign(
                                    targets=[Name(id='r', ctx=Store())],
                                    value=Call(
                                        func=Name(id='iap_cancel', ctx=Load()),
                                        args=[
                                            Name(id='env', ctx=Load()),
                                            Name(id='transaction_token', ctx=Load()),
                                            Name(id='key', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Raise(
                                    exc=Name(id='e', ctx=Load()),
                                    cause=None,
                                ),
                            ],
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='r', ctx=Store())],
                            value=Call(
                                func=Name(id='iap_capture', ctx=Load()),
                                args=[
                                    Name(id='env', ctx=Load()),
                                    Name(id='transaction_token', ctx=Load()),
                                    Name(id='key', ctx=Load()),
                                    Attribute(
                                        value=Name(id='transaction', ctx=Load()),
                                        attr='credit',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                    ],
                    finalbody=[],
                ),
            ],
            decorator_list=[
                Attribute(
                    value=Name(id='contextlib', ctx=Load()),
                    attr='contextmanager',
                    ctx=Load(),
                ),
            ],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
