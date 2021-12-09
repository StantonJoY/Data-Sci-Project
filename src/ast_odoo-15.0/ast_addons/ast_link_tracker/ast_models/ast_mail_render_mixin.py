Module(
    body=[
        Import(
            names=[alias(name='re', asname=None)],
        ),
        Import(
            names=[alias(name='markupsafe', asname=None)],
        ),
        ImportFrom(
            module='werkzeug',
            names=[
                alias(name='urls', asname=None),
                alias(name='utils', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='tools', asname=None),
            ],
            level=0,
        ),
        ClassDef(
            name='MailRenderMixin',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='AbstractModel',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='mail.render.mixin', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_shorten_links',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='html', annotation=None, type_comment=None),
                            arg(arg='link_tracker_vals', annotation=None, type_comment=None),
                            arg(arg='blacklist', annotation=None, type_comment=None),
                            arg(arg='base_url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Shorten links in an html content. It uses the '/r' short URL routing\n        introduced in this module. Using the standard Odoo regex local links are\n        found and replaced by global URLs (not including mailto, tel, sms).\n\n        TDE FIXME: could be great to have a record to enable website-based URLs\n\n        :param link_tracker_vals: values given to the created link.tracker, containing\n          for example: campaign_id, medium_id, source_id, and any other relevant fields\n          like mass_mailing_id in mass_mailing;\n        :param list blacklist: list of (local) URLs to not shorten (e.g.\n          '/unsubscribe_from_list')\n        :param str base_url: either given, either based on config parameter\n\n        :return: updated html\n        ", kind=None),
                        ),
                        Assign(
                            targets=[Name(id='base_url', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='base_url', ctx=Load()),
                                    Call(
                                        func=Attribute(
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
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='web.base.url', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='short_schema', ctx=Store())],
                            value=BinOp(
                                left=Name(id='base_url', ctx=Load()),
                                op=Add(),
                                right=Constant(value='/r/', kind=None),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='match', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='findall',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='HTML_TAG_URL_REGEX',
                                        ctx=Load(),
                                    ),
                                    Name(id='html', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='href', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='markupsafe', ctx=Load()),
                                            attr='Markup',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Subscript(
                                                value=Name(id='match', ctx=Load()),
                                                slice=Constant(value=0, kind=None),
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='long_url', ctx=Store())],
                                    value=Subscript(
                                        value=Name(id='match', ctx=Load()),
                                        slice=Constant(value=1, kind=None),
                                        ctx=Load(),
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='label', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=BoolOp(
                                                op=Or(),
                                                values=[
                                                    Subscript(
                                                        value=Name(id='match', ctx=Load()),
                                                        slice=Constant(value=3, kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value='', kind=None),
                                                ],
                                            ),
                                            attr='strip',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            UnaryOp(
                                                op=Not(),
                                                operand=Name(id='blacklist', ctx=Load()),
                                            ),
                                            BoolOp(
                                                op=And(),
                                                values=[
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=ListComp(
                                                            elt=Name(id='s', ctx=Load()),
                                                            generators=[
                                                                comprehension(
                                                                    target=Name(id='s', ctx=Store()),
                                                                    iter=Name(id='blacklist', ctx=Load()),
                                                                    ifs=[
                                                                        Compare(
                                                                            left=Name(id='s', ctx=Load()),
                                                                            ops=[In()],
                                                                            comparators=[Name(id='long_url', ctx=Load())],
                                                                        ),
                                                                    ],
                                                                    is_async=0,
                                                                ),
                                                            ],
                                                        ),
                                                    ),
                                                    UnaryOp(
                                                        op=Not(),
                                                        operand=Call(
                                                            func=Attribute(
                                                                value=Name(id='long_url', ctx=Load()),
                                                                attr='startswith',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='short_schema', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='create_vals', ctx=Store())],
                                            value=Call(
                                                func=Name(id='dict', ctx=Load()),
                                                args=[Name(id='link_tracker_vals', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='url',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='utils', ctx=Load()),
                                                                attr='unescape',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='long_url', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='label',
                                                        value=Call(
                                                            func=Attribute(
                                                                value=Name(id='utils', ctx=Load()),
                                                                attr='unescape',
                                                                ctx=Load(),
                                                            ),
                                                            args=[Name(id='label', ctx=Load())],
                                                            keywords=[],
                                                        ),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='link', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Subscript(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        slice=Constant(value='link.tracker', kind=None),
                                                        ctx=Load(),
                                                    ),
                                                    attr='search_or_create',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='create_vals', ctx=Load())],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='link', ctx=Load()),
                                                attr='short_url',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='new_href', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='href', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='long_url', ctx=Load()),
                                                            Attribute(
                                                                value=Name(id='link', ctx=Load()),
                                                                attr='short_url',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                Assign(
                                                    targets=[Name(id='html', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='html', ctx=Load()),
                                                            attr='replace',
                                                            ctx=Load(),
                                                        ),
                                                        args=[
                                                            Name(id='href', ctx=Load()),
                                                            Name(id='new_href', ctx=Load()),
                                                        ],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='html', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_shorten_links_text',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='content', annotation=None, type_comment=None),
                            arg(arg='link_tracker_vals', annotation=None, type_comment=None),
                            arg(arg='blacklist', annotation=None, type_comment=None),
                            arg(arg='base_url', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[
                            Constant(value=None, kind=None),
                            Constant(value=None, kind=None),
                        ],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Shorten links in a string content. Works like ``_shorten_links`` but\n        targetting string content, not html.\n\n        :return: updated content\n        ', kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='content', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Name(id='content', ctx=Load()),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='base_url', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Name(id='base_url', ctx=Load()),
                                    Call(
                                        func=Attribute(
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
                                            attr='get_param',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='web.base.url', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='shortened_schema', ctx=Store())],
                            value=BinOp(
                                left=Name(id='base_url', ctx=Load()),
                                op=Add(),
                                right=Constant(value='/r/', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='unsubscribe_schema', ctx=Store())],
                            value=BinOp(
                                left=Name(id='base_url', ctx=Load()),
                                op=Add(),
                                right=Constant(value='/sms/', kind=None),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='original_url', ctx=Store()),
                            iter=Call(
                                func=Attribute(
                                    value=Name(id='re', ctx=Load()),
                                    attr='findall',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='tools', ctx=Load()),
                                        attr='TEXT_URL_REGEX',
                                        ctx=Load(),
                                    ),
                                    Name(id='content', ctx=Load()),
                                ],
                                keywords=[],
                            ),
                            body=[
                                If(
                                    test=BoolOp(
                                        op=Or(),
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='original_url', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='shortened_schema', ctx=Load())],
                                                keywords=[],
                                            ),
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='original_url', ctx=Load()),
                                                    attr='startswith',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='unsubscribe_schema', ctx=Load())],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='parsed', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='urls', ctx=Load()),
                                            attr='url_parse',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='original_url', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='scheme',
                                                value=Constant(value='http', kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=BoolOp(
                                        op=And(),
                                        values=[
                                            Name(id='blacklist', ctx=Load()),
                                            Call(
                                                func=Name(id='any', ctx=Load()),
                                                args=[
                                                    GeneratorExp(
                                                        elt=Compare(
                                                            left=Name(id='item', ctx=Load()),
                                                            ops=[In()],
                                                            comparators=[
                                                                Attribute(
                                                                    value=Name(id='parsed', ctx=Load()),
                                                                    attr='path',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                        ),
                                                        generators=[
                                                            comprehension(
                                                                target=Name(id='item', ctx=Store()),
                                                                iter=Name(id='blacklist', ctx=Load()),
                                                                ifs=[],
                                                                is_async=0,
                                                            ),
                                                        ],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ],
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='create_vals', ctx=Store())],
                                    value=Call(
                                        func=Name(id='dict', ctx=Load()),
                                        args=[Name(id='link_tracker_vals', ctx=Load())],
                                        keywords=[
                                            keyword(
                                                arg='url',
                                                value=Call(
                                                    func=Attribute(
                                                        value=Name(id='utils', ctx=Load()),
                                                        attr='unescape',
                                                        ctx=Load(),
                                                    ),
                                                    args=[Name(id='original_url', ctx=Load())],
                                                    keywords=[],
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                Assign(
                                    targets=[Name(id='link', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='self', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='link.tracker', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='search_or_create',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='create_vals', ctx=Load())],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='link', ctx=Load()),
                                        attr='short_url',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='content', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='content', ctx=Load()),
                                                    attr='replace',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Name(id='original_url', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='link', ctx=Load()),
                                                        attr='short_url',
                                                        ctx=Load(),
                                                    ),
                                                    Constant(value=1, kind=None),
                                                ],
                                                keywords=[],
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='content', ctx=Load()),
                        ),
                    ],
                    decorator_list=[
                        Attribute(
                            value=Name(id='api', ctx=Load()),
                            attr='model',
                            ctx=Load(),
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
