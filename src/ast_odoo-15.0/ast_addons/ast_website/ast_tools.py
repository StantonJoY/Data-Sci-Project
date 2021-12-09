Module(
    body=[
        Import(
            names=[alias(name='contextlib', asname=None)],
        ),
        Import(
            names=[alias(name='re', asname=None)],
        ),
        ImportFrom(
            module='lxml',
            names=[alias(name='etree', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='psycopg2',
            names=[alias(name='sql', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='unittest.mock',
            names=[
                alias(name='Mock', asname=None),
                alias(name='MagicMock', asname=None),
                alias(name='patch', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='werkzeug', asname=None)],
        ),
        Import(
            names=[alias(name='odoo', asname=None)],
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='DotDict', asname=None)],
            level=0,
        ),
        FunctionDef(
            name='get_video_embed_code',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='video_url', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value=' Computes the valid iframe from given URL that can be embedded\n        (or False in case of invalid URL).\n    ', kind=None),
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Name(id='video_url', ctx=Load()),
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='validURLRegex', ctx=Store())],
                    value=Constant(value='^(http:\\/\\/|https:\\/\\/|\\/\\/)[a-z0-9]+([\\-\\.]{1}[a-z0-9]+)*\\.[a-z]{2,5}(:[0-9]{1,5})?(\\/.*)?$', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ytRegex', ctx=Store())],
                    value=Constant(value='^(?:(?:https?:)?\\/\\/)?(?:www\\.)?(?:youtu\\.be\\/|youtube(-nocookie)?\\.com\\/(?:embed\\/|v\\/|watch\\?v=|watch\\?.+&v=))((?:\\w|-){11})(?:\\S+)?$', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='vimeoRegex', ctx=Store())],
                    value=Constant(value='\\/\\/(player.)?vimeo.com\\/([a-z]*\\/)*([0-9]{6,11})[?]?.*', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='dmRegex', ctx=Store())],
                    value=Constant(value='.+dailymotion.com\\/(video|hub|embed)\\/([^_?]+)[^#]*(#video=([^_&]+))?', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='igRegex', ctx=Store())],
                    value=Constant(value='(.*)instagram.com\\/p\\/(.[a-zA-Z0-9]*)', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='ykuRegex', ctx=Store())],
                    value=Constant(value='(.*).youku\\.com\\/(v_show\\/id_|embed\\/)(.+)', kind=None),
                    type_comment=None,
                ),
                If(
                    test=UnaryOp(
                        op=Not(),
                        operand=Call(
                            func=Attribute(
                                value=Name(id='re', ctx=Load()),
                                attr='search',
                                ctx=Load(),
                            ),
                            args=[
                                Name(id='validURLRegex', ctx=Load()),
                                Name(id='video_url', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                    ),
                    body=[
                        Return(
                            value=Constant(value=False, kind=None),
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[Name(id='embedUrl', ctx=Store())],
                            value=Constant(value=False, kind=None),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ytMatch', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='ytRegex', ctx=Load()),
                                    Name(id='video_url', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='vimeoMatch', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='vimeoRegex', ctx=Load()),
                                    Name(id='video_url', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='dmMatch', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='dmRegex', ctx=Load()),
                                    Name(id='video_url', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='igMatch', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='igRegex', ctx=Load()),
                                    Name(id='video_url', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='ykuMatch', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='ykuRegex', ctx=Load()),
                                    Name(id='video_url', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='ytMatch', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Name(id='len', ctx=Load()),
                                            args=[
                                                Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ytMatch', ctx=Load()),
                                                            attr='groups',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=11, kind=None)],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='embedUrl', ctx=Store())],
                                    value=BinOp(
                                        left=Constant(value='//www.youtube%s.com/embed/%s?rel=0', kind=None),
                                        op=Mod(),
                                        right=Tuple(
                                            elts=[
                                                BoolOp(
                                                    op=Or(),
                                                    values=[
                                                        Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='ytMatch', ctx=Load()),
                                                                    attr='groups',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            slice=Constant(value=0, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        Constant(value='', kind=None),
                                                    ],
                                                ),
                                                Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='ytMatch', ctx=Load()),
                                                            attr='groups',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=1, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[
                                If(
                                    test=Name(id='vimeoMatch', ctx=Load()),
                                    body=[
                                        Assign(
                                            targets=[Name(id='embedUrl', ctx=Store())],
                                            value=BinOp(
                                                left=Constant(value='//player.vimeo.com/video/%s', kind=None),
                                                op=Mod(),
                                                right=Subscript(
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='vimeoMatch', ctx=Load()),
                                                            attr='groups',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    slice=Constant(value=2, kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        If(
                                            test=Name(id='dmMatch', ctx=Load()),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='embedUrl', ctx=Store())],
                                                    value=BinOp(
                                                        left=Constant(value='//www.dailymotion.com/embed/video/%s', kind=None),
                                                        op=Mod(),
                                                        right=Subscript(
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='dmMatch', ctx=Load()),
                                                                    attr='groups',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            slice=Constant(value=1, kind=None),
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[
                                                If(
                                                    test=Name(id='igMatch', ctx=Load()),
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='embedUrl', ctx=Store())],
                                                            value=BinOp(
                                                                left=Constant(value='//www.instagram.com/p/%s/embed/', kind=None),
                                                                op=Mod(),
                                                                right=Subscript(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='igMatch', ctx=Load()),
                                                                            attr='groups',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    slice=Constant(value=1, kind=None),
                                                                    ctx=Load(),
                                                                ),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                    ],
                                                    orelse=[
                                                        If(
                                                            test=Name(id='ykuMatch', ctx=Load()),
                                                            body=[
                                                                Assign(
                                                                    targets=[Name(id='ykuLink', ctx=Store())],
                                                                    value=Subscript(
                                                                        value=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='ykuMatch', ctx=Load()),
                                                                                attr='groups',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        slice=Constant(value=2, kind=None),
                                                                        ctx=Load(),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                                If(
                                                                    test=Compare(
                                                                        left=Constant(value='.html?', kind=None),
                                                                        ops=[In()],
                                                                        comparators=[Name(id='ykuLink', ctx=Load())],
                                                                    ),
                                                                    body=[
                                                                        Assign(
                                                                            targets=[Name(id='ykuLink', ctx=Store())],
                                                                            value=Subscript(
                                                                                value=Call(
                                                                                    func=Attribute(
                                                                                        value=Name(id='ykuLink', ctx=Load()),
                                                                                        attr='split',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    args=[Constant(value='.html?', kind=None)],
                                                                                    keywords=[],
                                                                                ),
                                                                                slice=Constant(value=0, kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            type_comment=None,
                                                                        ),
                                                                    ],
                                                                    orelse=[],
                                                                ),
                                                                Assign(
                                                                    targets=[Name(id='embedUrl', ctx=Store())],
                                                                    value=BinOp(
                                                                        left=Constant(value='//player.youku.com/embed/%s', kind=None),
                                                                        op=Mod(),
                                                                        right=Name(id='ykuLink', ctx=Load()),
                                                                    ),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                            orelse=[
                                                                Assign(
                                                                    targets=[Name(id='embedUrl', ctx=Store())],
                                                                    value=Name(id='video_url', ctx=Load()),
                                                                    type_comment=None,
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                ),
                                            ],
                                        ),
                                    ],
                                ),
                            ],
                        ),
                        Return(
                            value=BinOp(
                                left=Constant(value='<iframe class="embed-responsive-item" src="%s" allowFullScreen="true" frameborder="0"></iframe>', kind=None),
                                op=Mod(),
                                right=Name(id='embedUrl', ctx=Load()),
                            ),
                        ),
                    ],
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='werkzeugRaiseNotFound',
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
                            value=Attribute(
                                value=Name(id='werkzeug', ctx=Load()),
                                attr='exceptions',
                                ctx=Load(),
                            ),
                            attr='NotFound',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    cause=None,
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='MockRequest',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='env', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[
                    arg(arg='routing', annotation=None, type_comment=None),
                    arg(arg='multilang', annotation=None, type_comment=None),
                    arg(arg='context', annotation=None, type_comment=None),
                    arg(arg='cookies', annotation=None, type_comment=None),
                    arg(arg='country_code', annotation=None, type_comment=None),
                    arg(arg='website', annotation=None, type_comment=None),
                    arg(arg='sale_order_id', annotation=None, type_comment=None),
                    arg(arg='website_sale_current_pl', annotation=None, type_comment=None),
                ],
                kw_defaults=[
                    Constant(value=True, kind=None),
                    Constant(value=True, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                    Constant(value=None, kind=None),
                ],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Assign(
                    targets=[Name(id='router', ctx=Store())],
                    value=Call(
                        func=Name(id='MagicMock', ctx=Load()),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='match', ctx=Store())],
                    value=Attribute(
                        value=Attribute(
                            value=Attribute(
                                value=Attribute(
                                    value=Name(id='router', ctx=Load()),
                                    attr='return_value',
                                    ctx=Load(),
                                ),
                                attr='bind',
                                ctx=Load(),
                            ),
                            attr='return_value',
                            ctx=Load(),
                        ),
                        attr='match',
                        ctx=Load(),
                    ),
                    type_comment=None,
                ),
                If(
                    test=Name(id='routing', ctx=Load()),
                    body=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='return_value',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='routing',
                                    ctx=Store(),
                                ),
                            ],
                            value=Dict(
                                keys=[
                                    Constant(value='type', kind=None),
                                    Constant(value='website', kind=None),
                                    Constant(value='multilang', kind=None),
                                ],
                                values=[
                                    Constant(value='http', kind=None),
                                    Constant(value=True, kind=None),
                                    Name(id='multilang', ctx=Load()),
                                ],
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[
                        Assign(
                            targets=[
                                Attribute(
                                    value=Name(id='match', ctx=Load()),
                                    attr='side_effect',
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='werkzeugRaiseNotFound', ctx=Load()),
                            type_comment=None,
                        ),
                    ],
                ),
                If(
                    test=Compare(
                        left=Name(id='context', ctx=Load()),
                        ops=[Is()],
                        comparators=[Constant(value=None, kind=None)],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='context', ctx=Store())],
                            value=Dict(keys=[], values=[]),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='lang_code', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='context', ctx=Load()),
                            attr='get',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='lang', kind=None),
                            Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='env', ctx=Load()),
                                        attr='context',
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='lang', kind=None),
                                    Constant(value='en_US', kind=None),
                                ],
                                keywords=[],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Expr(
                    value=Call(
                        func=Attribute(
                            value=Name(id='context', ctx=Load()),
                            attr='setdefault',
                            ctx=Load(),
                        ),
                        args=[
                            Constant(value='lang', kind=None),
                            Name(id='lang_code', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                ),
                Assign(
                    targets=[Name(id='request', ctx=Store())],
                    value=Call(
                        func=Name(id='Mock', ctx=Load()),
                        args=[],
                        keywords=[
                            keyword(
                                arg='context',
                                value=Name(id='context', ctx=Load()),
                            ),
                            keyword(
                                arg='db',
                                value=Constant(value=None, kind=None),
                            ),
                            keyword(
                                arg='endpoint',
                                value=IfExp(
                                    test=Name(id='routing', ctx=Load()),
                                    body=Subscript(
                                        value=Attribute(
                                            value=Name(id='match', ctx=Load()),
                                            attr='return_value',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value=0, kind=None),
                                        ctx=Load(),
                                    ),
                                    orelse=Constant(value=None, kind=None),
                                ),
                            ),
                            keyword(
                                arg='env',
                                value=Name(id='env', ctx=Load()),
                            ),
                            keyword(
                                arg='httprequest',
                                value=Call(
                                    func=Name(id='Mock', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='host',
                                            value=Constant(value='localhost', kind=None),
                                        ),
                                        keyword(
                                            arg='path',
                                            value=Constant(value='/hello/', kind=None),
                                        ),
                                        keyword(
                                            arg='app',
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='odoo', ctx=Load()),
                                                    attr='http',
                                                    ctx=Load(),
                                                ),
                                                attr='root',
                                                ctx=Load(),
                                            ),
                                        ),
                                        keyword(
                                            arg='environ',
                                            value=Dict(
                                                keys=[Constant(value='REMOTE_ADDR', kind=None)],
                                                values=[Constant(value='127.0.0.1', kind=None)],
                                            ),
                                        ),
                                        keyword(
                                            arg='cookies',
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Name(id='cookies', ctx=Load()),
                                                    Dict(keys=[], values=[]),
                                                ],
                                            ),
                                        ),
                                        keyword(
                                            arg='referrer',
                                            value=Constant(value='', kind=None),
                                        ),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='lang',
                                value=Call(
                                    func=Attribute(
                                        value=Subscript(
                                            value=Name(id='env', ctx=Load()),
                                            slice=Constant(value='res.lang', kind=None),
                                            ctx=Load(),
                                        ),
                                        attr='_lang_get',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='lang_code', ctx=Load())],
                                    keywords=[],
                                ),
                            ),
                            keyword(
                                arg='redirect',
                                value=Attribute(
                                    value=Subscript(
                                        value=Name(id='env', ctx=Load()),
                                        slice=Constant(value='ir.http', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='_redirect',
                                    ctx=Load(),
                                ),
                            ),
                            keyword(
                                arg='session',
                                value=Call(
                                    func=Name(id='DotDict', ctx=Load()),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='geoip',
                                            value=Dict(
                                                keys=[Constant(value='country_code', kind=None)],
                                                values=[Name(id='country_code', ctx=Load())],
                                            ),
                                        ),
                                        keyword(
                                            arg='debug',
                                            value=Constant(value=False, kind=None),
                                        ),
                                        keyword(
                                            arg='sale_order_id',
                                            value=Name(id='sale_order_id', ctx=Load()),
                                        ),
                                        keyword(
                                            arg='website_sale_current_pl',
                                            value=Name(id='website_sale_current_pl', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                            keyword(
                                arg='website',
                                value=Name(id='website', ctx=Load()),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                With(
                    items=[
                        withitem(
                            context_expr=Call(
                                func=Attribute(
                                    value=Name(id='contextlib', ctx=Load()),
                                    attr='ExitStack',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            optional_vars=Name(id='s', ctx=Store()),
                        ),
                    ],
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='odoo', ctx=Load()),
                                            attr='http',
                                            ctx=Load(),
                                        ),
                                        attr='_request_stack',
                                        ctx=Load(),
                                    ),
                                    attr='push',
                                    ctx=Load(),
                                ),
                                args=[Name(id='request', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='s', ctx=Load()),
                                    attr='callback',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Attribute(
                                            value=Attribute(
                                                value=Name(id='odoo', ctx=Load()),
                                                attr='http',
                                                ctx=Load(),
                                            ),
                                            attr='_request_stack',
                                            ctx=Load(),
                                        ),
                                        attr='pop',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='s', ctx=Load()),
                                    attr='enter_context',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='patch', ctx=Load()),
                                        args=[
                                            Constant(value='odoo.http.root.get_db_router', kind=None),
                                            Name(id='router', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Expr(
                            value=Yield(
                                value=Name(id='request', ctx=Load()),
                            ),
                        ),
                    ],
                    type_comment=None,
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
        FunctionDef(
            name='distance',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='s1', annotation=None, type_comment=None),
                    arg(arg='s2', annotation=None, type_comment=None),
                    arg(arg='limit', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[
                    Constant(value='', kind=None),
                    Constant(value='', kind=None),
                    Constant(value=4, kind=None),
                ],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Limited Levenshtein-ish distance (inspired from Apache text common)\n    Note: this does not return quick results for simple cases (empty string, equal strings)\n        those checks should be done outside loops that use this function.\n\n    :param s1: first string\n    :param s2: second string\n    :param limit: maximum distance to take into account, return -1 if exceeded\n\n    :return: number of character changes needed to transform s1 into s2 or -1 if this exceeds the limit\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='BIG', ctx=Store())],
                    value=Constant(value=100000, kind=None),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='s1', ctx=Load())],
                            keywords=[],
                        ),
                        ops=[Gt()],
                        comparators=[
                            Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='s2', ctx=Load())],
                                keywords=[],
                            ),
                        ],
                    ),
                    body=[
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='s1', ctx=Store()),
                                        Name(id='s2', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Name(id='s2', ctx=Load()),
                                    Name(id='s1', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='l1', ctx=Store())],
                    value=Call(
                        func=Name(id='len', ctx=Load()),
                        args=[Name(id='s1', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='l2', ctx=Store())],
                    value=Call(
                        func=Name(id='len', ctx=Load()),
                        args=[Name(id='s2', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=BinOp(
                            left=Name(id='l2', ctx=Load()),
                            op=Sub(),
                            right=Name(id='l1', ctx=Load()),
                        ),
                        ops=[Gt()],
                        comparators=[Name(id='limit', ctx=Load())],
                    ),
                    body=[
                        Return(
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='boundary', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Name(id='min', ctx=Load()),
                            args=[
                                Name(id='l1', ctx=Load()),
                                Name(id='limit', ctx=Load()),
                            ],
                            keywords=[],
                        ),
                        op=Add(),
                        right=Constant(value=1, kind=None),
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='p', ctx=Store())],
                    value=ListComp(
                        elt=IfExp(
                            test=Compare(
                                left=Name(id='i', ctx=Load()),
                                ops=[Lt()],
                                comparators=[Name(id='boundary', ctx=Load())],
                            ),
                            body=Name(id='i', ctx=Load()),
                            orelse=Name(id='BIG', ctx=Load()),
                        ),
                        generators=[
                            comprehension(
                                target=Name(id='i', ctx=Store()),
                                iter=Call(
                                    func=Name(id='range', ctx=Load()),
                                    args=[
                                        Constant(value=0, kind=None),
                                        BinOp(
                                            left=Name(id='l1', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='d', ctx=Store())],
                    value=ListComp(
                        elt=Name(id='BIG', ctx=Load()),
                        generators=[
                            comprehension(
                                target=Name(id='_', ctx=Store()),
                                iter=Call(
                                    func=Name(id='range', ctx=Load()),
                                    args=[
                                        Constant(value=0, kind=None),
                                        BinOp(
                                            left=Name(id='l1', ctx=Load()),
                                            op=Add(),
                                            right=Constant(value=1, kind=None),
                                        ),
                                    ],
                                    keywords=[],
                                ),
                                ifs=[],
                                is_async=0,
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                For(
                    target=Name(id='j', ctx=Store()),
                    iter=Call(
                        func=Name(id='range', ctx=Load()),
                        args=[
                            Constant(value=1, kind=None),
                            BinOp(
                                left=Name(id='l2', ctx=Load()),
                                op=Add(),
                                right=Constant(value=1, kind=None),
                            ),
                        ],
                        keywords=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='j2', ctx=Store())],
                            value=Subscript(
                                value=Name(id='s2', ctx=Load()),
                                slice=BinOp(
                                    left=Name(id='j', ctx=Load()),
                                    op=Sub(),
                                    right=Constant(value=1, kind=None),
                                ),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='d', ctx=Load()),
                                    slice=Constant(value=0, kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Name(id='j', ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='range_min', ctx=Store())],
                            value=Call(
                                func=Name(id='max', ctx=Load()),
                                args=[
                                    Constant(value=1, kind=None),
                                    BinOp(
                                        left=Name(id='j', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='limit', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='range_max', ctx=Store())],
                            value=Call(
                                func=Name(id='min', ctx=Load()),
                                args=[
                                    Name(id='l1', ctx=Load()),
                                    BinOp(
                                        left=Name(id='j', ctx=Load()),
                                        op=Add(),
                                        right=Name(id='limit', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Name(id='range_min', ctx=Load()),
                                ops=[Gt()],
                                comparators=[Constant(value=1, kind=None)],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Subscript(
                                            value=Name(id='d', ctx=Load()),
                                            slice=BinOp(
                                                left=Name(id='range_min', ctx=Load()),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Name(id='BIG', ctx=Load()),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Name(id='range_min', ctx=Load()),
                                    BinOp(
                                        left=Name(id='range_max', ctx=Load()),
                                        op=Add(),
                                        right=Constant(value=1, kind=None),
                                    ),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=Compare(
                                        left=Subscript(
                                            value=Name(id='s1', ctx=Load()),
                                            slice=BinOp(
                                                left=Name(id='i', ctx=Load()),
                                                op=Sub(),
                                                right=Constant(value=1, kind=None),
                                            ),
                                            ctx=Load(),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Name(id='j2', ctx=Load())],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='d', ctx=Load()),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Subscript(
                                                value=Name(id='p', ctx=Load()),
                                                slice=BinOp(
                                                    left=Name(id='i', ctx=Load()),
                                                    op=Sub(),
                                                    right=Constant(value=1, kind=None),
                                                ),
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='d', ctx=Load()),
                                                    slice=Name(id='i', ctx=Load()),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=BinOp(
                                                left=Constant(value=1, kind=None),
                                                op=Add(),
                                                right=Call(
                                                    func=Name(id='min', ctx=Load()),
                                                    args=[
                                                        Subscript(
                                                            value=Name(id='d', ctx=Load()),
                                                            slice=BinOp(
                                                                left=Name(id='i', ctx=Load()),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='p', ctx=Load()),
                                                            slice=Name(id='i', ctx=Load()),
                                                            ctx=Load(),
                                                        ),
                                                        Subscript(
                                                            value=Name(id='p', ctx=Load()),
                                                            slice=BinOp(
                                                                left=Name(id='i', ctx=Load()),
                                                                op=Sub(),
                                                                right=Constant(value=1, kind=None),
                                                            ),
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    keywords=[],
                                                ),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Tuple(
                                    elts=[
                                        Name(id='p', ctx=Store()),
                                        Name(id='d', ctx=Store()),
                                    ],
                                    ctx=Store(),
                                ),
                            ],
                            value=Tuple(
                                elts=[
                                    Name(id='d', ctx=Load()),
                                    Name(id='p', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                    ],
                    orelse=[],
                    type_comment=None,
                ),
                Return(
                    value=IfExp(
                        test=Compare(
                            left=Subscript(
                                value=Name(id='p', ctx=Load()),
                                slice=Name(id='l1', ctx=Load()),
                                ctx=Load(),
                            ),
                            ops=[LtE()],
                            comparators=[Name(id='limit', ctx=Load())],
                        ),
                        body=Subscript(
                            value=Name(id='p', ctx=Load()),
                            slice=Name(id='l1', ctx=Load()),
                            ctx=Load(),
                        ),
                        orelse=UnaryOp(
                            op=USub(),
                            operand=Constant(value=1, kind=None),
                        ),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='similarity_score',
            args=arguments(
                posonlyargs=[],
                args=[
                    arg(arg='s1', annotation=None, type_comment=None),
                    arg(arg='s2', annotation=None, type_comment=None),
                ],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Computes a score that describes how much two strings are matching.\n\n    :param s1: first string\n    :param s2: second string\n\n    :return: float score, the higher the more similar\n        pairs returning non-positive scores should be considered non similar\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='dist', ctx=Store())],
                    value=Call(
                        func=Name(id='distance', ctx=Load()),
                        args=[
                            Name(id='s1', ctx=Load()),
                            Name(id='s2', ctx=Load()),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                If(
                    test=Compare(
                        left=Name(id='dist', ctx=Load()),
                        ops=[Eq()],
                        comparators=[
                            UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                        ],
                    ),
                    body=[
                        Return(
                            value=UnaryOp(
                                op=USub(),
                                operand=Constant(value=1, kind=None),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Assign(
                    targets=[Name(id='set1', ctx=Store())],
                    value=Call(
                        func=Name(id='set', ctx=Load()),
                        args=[Name(id='s1', ctx=Load())],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='score', ctx=Store())],
                    value=BinOp(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='set1', ctx=Load()),
                                        attr='intersection',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='s2', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        op=Div(),
                        right=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='set1', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                    type_comment=None,
                ),
                AugAssign(
                    target=Name(id='score', ctx=Store()),
                    op=Sub(),
                    value=BinOp(
                        left=Name(id='dist', ctx=Load()),
                        op=Div(),
                        right=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[Name(id='s1', ctx=Load())],
                            keywords=[],
                        ),
                    ),
                ),
                AugAssign(
                    target=Name(id='score', ctx=Store()),
                    op=Sub(),
                    value=BinOp(
                        left=Call(
                            func=Name(id='len', ctx=Load()),
                            args=[
                                Call(
                                    func=Attribute(
                                        value=Name(id='set1', ctx=Load()),
                                        attr='symmetric_difference',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='s2', ctx=Load())],
                                    keywords=[],
                                ),
                            ],
                            keywords=[],
                        ),
                        op=Div(),
                        right=BinOp(
                            left=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='s1', ctx=Load())],
                                keywords=[],
                            ),
                            op=Add(),
                            right=Call(
                                func=Name(id='len', ctx=Load()),
                                args=[Name(id='s2', ctx=Load())],
                                keywords=[],
                            ),
                        ),
                    ),
                ),
                Return(
                    value=Name(id='score', ctx=Load()),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
        FunctionDef(
            name='text_from_html',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='html_fragment', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Returns the plain non-tag text from an html\n\n    :param html_fragment: document from which text must be extracted\n\n    :return: text extracted from the html\n    ', kind=None),
                ),
                Assign(
                    targets=[Name(id='tree', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='etree', ctx=Load()),
                            attr='fromstring',
                            ctx=Load(),
                        ),
                        args=[
                            BinOp(
                                left=Constant(value='<p>%s</p>', kind=None),
                                op=Mod(),
                                right=Name(id='html_fragment', ctx=Load()),
                            ),
                            Call(
                                func=Attribute(
                                    value=Name(id='etree', ctx=Load()),
                                    attr='XMLParser',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='recover',
                                        value=Constant(value=True, kind=None),
                                    ),
                                ],
                            ),
                        ],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Return(
                    value=Call(
                        func=Attribute(
                            value=Constant(value=' ', kind=None),
                            attr='join',
                            ctx=Load(),
                        ),
                        args=[
                            Call(
                                func=Attribute(
                                    value=Name(id='tree', ctx=Load()),
                                    attr='itertext',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
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
        FunctionDef(
            name='get_unaccent_sql_wrapper',
            args=arguments(
                posonlyargs=[],
                args=[arg(arg='cr', annotation=None, type_comment=None)],
                vararg=None,
                kwonlyargs=[],
                kw_defaults=[],
                kwarg=None,
                defaults=[],
            ),
            body=[
                Expr(
                    value=Constant(value='\n    Returns a function that wraps SQL within unaccent if available\n    TODO remove when this tool becomes globally available\n\n    :param cr: cursor on which the wrapping is done\n\n    :return: function that wraps SQL with unaccent if available\n    ', kind=None),
                ),
                If(
                    test=Attribute(
                        value=Call(
                            func=Attribute(
                                value=Name(id='odoo', ctx=Load()),
                                attr='registry',
                                ctx=Load(),
                            ),
                            args=[
                                Attribute(
                                    value=Name(id='cr', ctx=Load()),
                                    attr='dbname',
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[],
                        ),
                        attr='has_unaccent',
                        ctx=Load(),
                    ),
                    body=[
                        Return(
                            value=Lambda(
                                args=arguments(
                                    posonlyargs=[],
                                    args=[arg(arg='x', annotation=None, type_comment=None)],
                                    vararg=None,
                                    kwonlyargs=[],
                                    kw_defaults=[],
                                    kwarg=None,
                                    defaults=[],
                                ),
                                body=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='sql', ctx=Load()),
                                                attr='SQL',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='unaccent({wrapped_sql})', kind=None)],
                                            keywords=[],
                                        ),
                                        attr='format',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[
                                        keyword(
                                            arg='wrapped_sql',
                                            value=Name(id='x', ctx=Load()),
                                        ),
                                    ],
                                ),
                            ),
                        ),
                    ],
                    orelse=[],
                ),
                Return(
                    value=Lambda(
                        args=arguments(
                            posonlyargs=[],
                            args=[arg(arg='x', annotation=None, type_comment=None)],
                            vararg=None,
                            kwonlyargs=[],
                            kw_defaults=[],
                            kwarg=None,
                            defaults=[],
                        ),
                        body=Name(id='x', ctx=Load()),
                    ),
                ),
            ],
            decorator_list=[],
            returns=None,
            type_comment=None,
        ),
    ],
    type_ignores=[],
)
