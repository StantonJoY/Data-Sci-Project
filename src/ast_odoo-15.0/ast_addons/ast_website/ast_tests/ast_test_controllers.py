Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='tests', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools',
            names=[alias(name='mute_logger', asname=None)],
            level=0,
        ),
        ClassDef(
            name='TestControllers',
            bases=[
                Attribute(
                    value=Name(id='tests', ctx=Load()),
                    attr='HttpCase',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='test_last_created_pages_autocompletion',
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
                                    attr='authenticate',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='admin', kind=None),
                                    Constant(value='admin', kind=None),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='Page', ctx=Store())],
                            value=Subscript(
                                value=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='env',
                                    ctx=Load(),
                                ),
                                slice=Constant(value='website.page', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_5_url_edited', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='base_url', ctx=Store())],
                            value=Call(
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
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='suggested_links_url', ctx=Store())],
                            value=BinOp(
                                left=Name(id='base_url', ctx=Load()),
                                op=Add(),
                                right=Constant(value='/website/get_suggested_links', kind=None),
                            ),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='i', ctx=Store()),
                            iter=Call(
                                func=Name(id='range', ctx=Load()),
                                args=[
                                    Constant(value=0, kind=None),
                                    Constant(value=10, kind=None),
                                ],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='new_page', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='Page', ctx=Load()),
                                            attr='create',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Dict(
                                                keys=[
                                                    Constant(value='name', kind=None),
                                                    Constant(value='type', kind=None),
                                                    Constant(value='arch', kind=None),
                                                    Constant(value='key', kind=None),
                                                    Constant(value='url', kind=None),
                                                    Constant(value='is_published', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='Generic', kind=None),
                                                    Constant(value='qweb', kind=None),
                                                    Constant(value='\n                    <div>content</div>\n                ', kind=None),
                                                    BinOp(
                                                        left=Constant(value='test.generic_view-%d', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='i', ctx=Load()),
                                                    ),
                                                    BinOp(
                                                        left=Constant(value='/generic-%d', kind=None),
                                                        op=Mod(),
                                                        right=Name(id='i', ctx=Load()),
                                                    ),
                                                    Constant(value=True, kind=None),
                                                ],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Compare(
                                        left=BinOp(
                                            left=Name(id='i', ctx=Load()),
                                            op=Mod(),
                                            right=Constant(value=2, kind=None),
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=0, kind=None)],
                                    ),
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='new_page', ctx=Load()),
                                                    attr='_write',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Dict(
                                                        keys=[Constant(value='write_date', kind=None)],
                                                        values=[Constant(value='2020-01-01', kind=None)],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                    orelse=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='last_5_url_edited', ctx=Load()),
                                                    attr='append',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Attribute(
                                                        value=Name(id='new_page', ctx=Load()),
                                                        attr='url',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='res', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='opener',
                                        ctx=Load(),
                                    ),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[
                                    keyword(
                                        arg='url',
                                        value=Name(id='suggested_links_url', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='json',
                                        value=Dict(
                                            keys=[Constant(value='params', kind=None)],
                                            values=[
                                                Dict(
                                                    keys=[Constant(value='needle', kind=None)],
                                                    values=[Constant(value='/', kind=None)],
                                                ),
                                            ],
                                        ),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='resp', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='json', ctx=Load()),
                                    attr='loads',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='res', ctx=Load()),
                                        attr='content',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Constant(value='result', kind=None),
                                ops=[In()],
                                comparators=[Name(id='resp', ctx=Load())],
                            ),
                            msg=None,
                        ),
                        Assign(
                            targets=[Name(id='suggested_links', ctx=Store())],
                            value=Subscript(
                                value=Name(id='resp', ctx=Load()),
                                slice=Constant(value='result', kind=None),
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_modified_history', ctx=Store())],
                            value=Call(
                                func=Name(id='next', ctx=Load()),
                                args=[
                                    GeneratorExp(
                                        elt=Name(id='o', ctx=Load()),
                                        generators=[
                                            comprehension(
                                                target=Name(id='o', ctx=Store()),
                                                iter=Subscript(
                                                    value=Name(id='suggested_links', ctx=Load()),
                                                    slice=Constant(value='others', kind=None),
                                                    ctx=Load(),
                                                ),
                                                ifs=[
                                                    Compare(
                                                        left=Subscript(
                                                            value=Name(id='o', ctx=Load()),
                                                            slice=Constant(value='title', kind=None),
                                                            ctx=Load(),
                                                        ),
                                                        ops=[Eq()],
                                                        comparators=[Constant(value='Last modified pages', kind=None)],
                                                    ),
                                                ],
                                                is_async=0,
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='last_modified_values', ctx=Store())],
                            value=Call(
                                func=Name(id='map', ctx=Load()),
                                args=[
                                    Lambda(
                                        args=arguments(
                                            posonlyargs=[],
                                            args=[arg(arg='o', annotation=None, type_comment=None)],
                                            vararg=None,
                                            kwonlyargs=[],
                                            kw_defaults=[],
                                            kwarg=None,
                                            defaults=[],
                                        ),
                                        body=Subscript(
                                            value=Name(id='o', ctx=Load()),
                                            slice=Constant(value='value', kind=None),
                                            ctx=Load(),
                                        ),
                                    ),
                                    Subscript(
                                        value=Name(id='last_modified_history', ctx=Load()),
                                        slice=Constant(value='values', kind=None),
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='matching_pages', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Call(
                                        func=Name(id='map', ctx=Load()),
                                        args=[
                                            Lambda(
                                                args=arguments(
                                                    posonlyargs=[],
                                                    args=[arg(arg='o', annotation=None, type_comment=None)],
                                                    vararg=None,
                                                    kwonlyargs=[],
                                                    kw_defaults=[],
                                                    kwarg=None,
                                                    defaults=[],
                                                ),
                                                body=Subscript(
                                                    value=Name(id='o', ctx=Load()),
                                                    slice=Constant(value='value', kind=None),
                                                    ctx=Load(),
                                                ),
                                            ),
                                            Subscript(
                                                value=Name(id='suggested_links', ctx=Load()),
                                                slice=Constant(value='matching_pages', kind=None),
                                                ctx=Load(),
                                            ),
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
                                    value=Name(id='self', ctx=Load()),
                                    attr='assertEqual',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Name(id='set', ctx=Load()),
                                        args=[Name(id='last_modified_values', ctx=Load())],
                                        keywords=[],
                                    ),
                                    BinOp(
                                        left=Call(
                                            func=Name(id='set', ctx=Load()),
                                            args=[Name(id='last_5_url_edited', ctx=Load())],
                                            keywords=[],
                                        ),
                                        op=Sub(),
                                        right=Name(id='matching_pages', ctx=Load()),
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Name(id='mute_logger', ctx=Load()),
                            args=[
                                Constant(value='odoo.addons.http_routing.models.ir_http', kind=None),
                                Constant(value='odoo.http', kind=None),
                            ],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[
                Call(
                    func=Attribute(
                        value=Name(id='tests', ctx=Load()),
                        attr='tagged',
                        ctx=Load(),
                    ),
                    args=[
                        Constant(value='post_install', kind=None),
                        Constant(value='-at_install', kind=None),
                    ],
                    keywords=[],
                ),
            ],
        ),
    ],
    type_ignores=[],
)
