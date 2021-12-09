Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='http', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.translate',
            names=[alias(name='_', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.tools.misc',
            names=[alias(name='get_lang', asname=None)],
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
            targets=[Name(id='MAPPED_RATES', ctx=Store())],
            value=Dict(
                keys=[
                    Constant(value=1, kind=None),
                    Constant(value=5, kind=None),
                    Constant(value=10, kind=None),
                ],
                values=[
                    Constant(value=1, kind=None),
                    Constant(value=3, kind=None),
                    Constant(value=5, kind=None),
                ],
            ),
            type_comment=None,
        ),
        ClassDef(
            name='Rating',
            bases=[
                Attribute(
                    value=Name(id='http', ctx=Load()),
                    attr='Controller',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                FunctionDef(
                    name='open_rating',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='rate', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/rating is deprecated, use /rate instead', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='rate', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=Constant(value='Incorrect rating', kind=None),
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='action_open_rating',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='token', ctx=Load()),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='MAPPED_RATES', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='rate', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/rating/<string:token>/<int:rate>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='submit_rating',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='_logger', ctx=Load()),
                                    attr='warning',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='/rating is deprecated, use /rate instead', kind=None)],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='rate', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='rate', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='rate', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=5, kind=None),
                                            Constant(value=10, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=Constant(value='Incorrect rating', kind=None),
                        ),
                        Assign(
                            targets=[
                                Subscript(
                                    value=Name(id='kwargs', ctx=Load()),
                                    slice=Constant(value='rate', kind=None),
                                    ctx=Store(),
                                ),
                            ],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='MAPPED_RATES', ctx=Load()),
                                    attr='gate',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rate', ctx=Load())],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='action_submit_rating',
                                    ctx=Load(),
                                ),
                                args=[Name(id='token', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg=None,
                                        value=Name(id='kwargs', ctx=Load()),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/rating/<string:token>/submit_feedback', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='post', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_open_rating',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                            arg(arg='rate', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assert(
                            test=Compare(
                                left=Name(id='rate', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=Constant(value='Incorrect rating', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='rating', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='rating.rating', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='access_token', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='token', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='rating', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='not_found',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='rate_names', ctx=Store())],
                            value=Dict(
                                keys=[
                                    Constant(value=5, kind=None),
                                    Constant(value=3, kind=None),
                                    Constant(value=1, kind=None),
                                ],
                                values=[
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Satisfied', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Okay', kind=None)],
                                        keywords=[],
                                    ),
                                    Call(
                                        func=Name(id='_', ctx=Load()),
                                        args=[Constant(value='Dissatisfied', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='rating', ctx=Load()),
                                    attr='write',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='rating', kind=None),
                                            Constant(value='consumed', kind=None),
                                        ],
                                        values=[
                                            Name(id='rate', ctx=Load()),
                                            Constant(value=True, kind=None),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rating', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='lang',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Call(
                                            func=Name(id='get_lang', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Name(id='lang', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='_render_template',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='rating.rating_external_page_submit', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='rating', kind=None),
                                            Constant(value='token', kind=None),
                                            Constant(value='rate_names', kind=None),
                                            Constant(value='rate', kind=None),
                                        ],
                                        values=[
                                            Name(id='rating', ctx=Load()),
                                            Name(id='token', ctx=Load()),
                                            Name(id='rate_names', ctx=Load()),
                                            Name(id='rate', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[Constant(value='/rate/<string:token>/<int:rate>', kind=None)],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='action_submit_rating',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='token', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=arg(arg='kwargs', annotation=None, type_comment=None),
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='rate', ctx=Store())],
                            value=Call(
                                func=Name(id='int', ctx=Load()),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='kwargs', ctx=Load()),
                                            attr='get',
                                            ctx=Load(),
                                        ),
                                        args=[Constant(value='rate', kind=None)],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assert(
                            test=Compare(
                                left=Name(id='rate', ctx=Load()),
                                ops=[In()],
                                comparators=[
                                    Tuple(
                                        elts=[
                                            Constant(value=1, kind=None),
                                            Constant(value=3, kind=None),
                                            Constant(value=5, kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            msg=Constant(value='Incorrect rating', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='rating', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='rating.rating', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[
                                    List(
                                        elts=[
                                            Tuple(
                                                elts=[
                                                    Constant(value='access_token', kind=None),
                                                    Constant(value='=', kind=None),
                                                    Name(id='token', ctx=Load()),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='rating', ctx=Load()),
                            ),
                            body=[
                                Return(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='request', ctx=Load()),
                                            attr='not_found',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='record_sudo', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Attribute(
                                                    value=Name(id='rating', ctx=Load()),
                                                    attr='res_model',
                                                    ctx=Load(),
                                                ),
                                                ctx=Load(),
                                            ),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='browse',
                                    ctx=Load(),
                                ),
                                args=[
                                    Attribute(
                                        value=Name(id='rating', ctx=Load()),
                                        attr='res_id',
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
                                    value=Name(id='record_sudo', ctx=Load()),
                                    attr='rating_apply',
                                    ctx=Load(),
                                ),
                                args=[Name(id='rate', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='token',
                                        value=Name(id='token', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='feedback',
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='kwargs', ctx=Load()),
                                                attr='get',
                                                ctx=Load(),
                                            ),
                                            args=[Constant(value='feedback', kind=None)],
                                            keywords=[],
                                        ),
                                    ),
                                ],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='lang', ctx=Store())],
                            value=BoolOp(
                                op=Or(),
                                values=[
                                    Attribute(
                                        value=Attribute(
                                            value=Name(id='rating', ctx=Load()),
                                            attr='partner_id',
                                            ctx=Load(),
                                        ),
                                        attr='lang',
                                        ctx=Load(),
                                    ),
                                    Attribute(
                                        value=Call(
                                            func=Name(id='get_lang', ctx=Load()),
                                            args=[
                                                Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='code',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='ir.ui.view', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='with_context',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[
                                            keyword(
                                                arg='lang',
                                                value=Name(id='lang', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    attr='_render_template',
                                    ctx=Load(),
                                ),
                                args=[
                                    Constant(value='rating.rating_external_page_view', kind=None),
                                    Dict(
                                        keys=[
                                            Constant(value='web_base_url', kind=None),
                                            Constant(value='rating', kind=None),
                                        ],
                                        values=[
                                            Call(
                                                func=Attribute(
                                                    value=Name(id='rating', ctx=Load()),
                                                    attr='get_base_url',
                                                    ctx=Load(),
                                                ),
                                                args=[],
                                                keywords=[],
                                            ),
                                            Name(id='rating', ctx=Load()),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='http', ctx=Load()),
                                attr='route',
                                ctx=Load(),
                            ),
                            args=[
                                List(
                                    elts=[Constant(value='/rate/<string:token>/submit_feedback', kind=None)],
                                    ctx=Load(),
                                ),
                            ],
                            keywords=[
                                keyword(
                                    arg='type',
                                    value=Constant(value='http', kind=None),
                                ),
                                keyword(
                                    arg='auth',
                                    value=Constant(value='public', kind=None),
                                ),
                                keyword(
                                    arg='methods',
                                    value=List(
                                        elts=[Constant(value='post', kind=None)],
                                        ctx=Load(),
                                    ),
                                ),
                                keyword(
                                    arg='website',
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
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
