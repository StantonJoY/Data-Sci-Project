Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='time', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[alias(name='models', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo.http',
            names=[alias(name='request', asname=None)],
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
        ClassDef(
            name='IrHttp',
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
                    value=Constant(value='ir.http', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_serve_page',
                    args=arguments(
                        posonlyargs=[],
                        args=[arg(arg='cls', annotation=None, type_comment=None)],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='response', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='IrHttp', ctx=Load()),
                                            Name(id='cls', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_serve_page',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=BoolOp(
                                op=And(),
                                values=[
                                    Name(id='response', ctx=Load()),
                                    Compare(
                                        left=Call(
                                            func=Name(id='getattr', ctx=Load()),
                                            args=[
                                                Name(id='response', ctx=Load()),
                                                Constant(value='status_code', kind=None),
                                                Constant(value=0, kind=None),
                                            ],
                                            keywords=[],
                                        ),
                                        ops=[Eq()],
                                        comparators=[Constant(value=200, kind=None)],
                                    ),
                                    Call(
                                        func=Attribute(
                                            value=Attribute(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                attr='user',
                                                ctx=Load(),
                                            ),
                                            attr='_is_public',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                ],
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='visitor_sudo', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Subscript(
                                                value=Attribute(
                                                    value=Name(id='request', ctx=Load()),
                                                    attr='env',
                                                    ctx=Load(),
                                                ),
                                                slice=Constant(value='website.visitor', kind=None),
                                                ctx=Load(),
                                            ),
                                            attr='_get_visitor_from_request',
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
                                                operand=Name(id='visitor_sudo', ctx=Load()),
                                            ),
                                            Compare(
                                                left=Constant(value='lead_ids', kind=None),
                                                ops=[NotIn()],
                                                comparators=[Name(id='visitor_sudo', ctx=Load())],
                                            ),
                                            UnaryOp(
                                                op=Not(),
                                                operand=Attribute(
                                                    value=Name(id='visitor_sudo', ctx=Load()),
                                                    attr='lead_ids',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='country_code', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='geoip', kind=None),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='session',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='geoip', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='country_code', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='state_code', ctx=Store())],
                                            value=BoolOp(
                                                op=And(),
                                                values=[
                                                    Compare(
                                                        left=Constant(value='geoip', kind=None),
                                                        ops=[In()],
                                                        comparators=[
                                                            Attribute(
                                                                value=Name(id='request', ctx=Load()),
                                                                attr='session',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                    ),
                                                    Call(
                                                        func=Attribute(
                                                            value=Subscript(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='session',
                                                                    ctx=Load(),
                                                                ),
                                                                slice=Constant(value='geoip', kind=None),
                                                                ctx=Load(),
                                                            ),
                                                            attr='get',
                                                            ctx=Load(),
                                                        ),
                                                        args=[Constant(value='region', kind=None)],
                                                        keywords=[],
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Name(id='country_code', ctx=Load()),
                                            body=[
                                                Try(
                                                    body=[
                                                        Assign(
                                                            targets=[Name(id='url', ctx=Store())],
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='httprequest',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='url',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='ip_address', ctx=Store())],
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='httprequest',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='remote_addr',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        If(
                                                            test=UnaryOp(
                                                                op=Not(),
                                                                operand=Name(id='ip_address', ctx=Load()),
                                                            ),
                                                            body=[
                                                                Return(
                                                                    value=Name(id='response', ctx=Load()),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='website_id', ctx=Store())],
                                                            value=Attribute(
                                                                value=Attribute(
                                                                    value=Name(id='request', ctx=Load()),
                                                                    attr='website',
                                                                    ctx=Load(),
                                                                ),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='rules_excluded', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=BoolOp(
                                                                        op=Or(),
                                                                        values=[
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Attribute(
                                                                                        value=Attribute(
                                                                                            value=Name(id='request', ctx=Load()),
                                                                                            attr='httprequest',
                                                                                            ctx=Load(),
                                                                                        ),
                                                                                        attr='cookies',
                                                                                        ctx=Load(),
                                                                                    ),
                                                                                    attr='get',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Constant(value='rule_ids', kind=None)],
                                                                                keywords=[],
                                                                            ),
                                                                            Constant(value='', kind=None),
                                                                        ],
                                                                    ),
                                                                    attr='split',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[Constant(value=',', kind=None)],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='before', ctx=Store())],
                                                            value=Call(
                                                                func=Attribute(
                                                                    value=Name(id='time', ctx=Load()),
                                                                    attr='time',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[],
                                                                keywords=[],
                                                            ),
                                                            type_comment=None,
                                                        ),
                                                        Assign(
                                                            targets=[Name(id='new_rules_excluded', ctx=Store())],
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
                                                                                slice=Constant(value='crm.reveal.view', kind=None),
                                                                                ctx=Load(),
                                                                            ),
                                                                            attr='sudo',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[],
                                                                        keywords=[],
                                                                    ),
                                                                    attr='_create_reveal_view',
                                                                    ctx=Load(),
                                                                ),
                                                                args=[
                                                                    Name(id='website_id', ctx=Load()),
                                                                    Name(id='url', ctx=Load()),
                                                                    Name(id='ip_address', ctx=Load()),
                                                                    Name(id='country_code', ctx=Load()),
                                                                    Name(id='state_code', ctx=Load()),
                                                                    Name(id='rules_excluded', ctx=Load()),
                                                                ],
                                                                keywords=[],
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
                                                                    Constant(value='Reveal process time: [%s], match rule: [%s?], country code: [%s], ip: [%s]', kind=None),
                                                                    BinOp(
                                                                        left=Call(
                                                                            func=Attribute(
                                                                                value=Name(id='time', ctx=Load()),
                                                                                attr='time',
                                                                                ctx=Load(),
                                                                            ),
                                                                            args=[],
                                                                            keywords=[],
                                                                        ),
                                                                        op=Sub(),
                                                                        right=Name(id='before', ctx=Load()),
                                                                    ),
                                                                    Compare(
                                                                        left=Name(id='new_rules_excluded', ctx=Load()),
                                                                        ops=[Eq()],
                                                                        comparators=[Name(id='rules_excluded', ctx=Load())],
                                                                    ),
                                                                    Name(id='country_code', ctx=Load()),
                                                                    Name(id='ip_address', ctx=Load()),
                                                                ],
                                                                keywords=[],
                                                            ),
                                                        ),
                                                        If(
                                                            test=Name(id='new_rules_excluded', ctx=Load()),
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='response', ctx=Load()),
                                                                            attr='set_cookie',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[
                                                                            Constant(value='rule_ids', kind=None),
                                                                            Call(
                                                                                func=Attribute(
                                                                                    value=Constant(value=',', kind=None),
                                                                                    attr='join',
                                                                                    ctx=Load(),
                                                                                ),
                                                                                args=[Name(id='new_rules_excluded', ctx=Load())],
                                                                                keywords=[],
                                                                            ),
                                                                        ],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                            orelse=[],
                                                        ),
                                                    ],
                                                    handlers=[
                                                        ExceptHandler(
                                                            type=Name(id='Exception', ctx=Load()),
                                                            name=None,
                                                            body=[
                                                                Expr(
                                                                    value=Call(
                                                                        func=Attribute(
                                                                            value=Name(id='_logger', ctx=Load()),
                                                                            attr='exception',
                                                                            ctx=Load(),
                                                                        ),
                                                                        args=[Constant(value='Failed to process reveal rules', kind=None)],
                                                                        keywords=[],
                                                                    ),
                                                                ),
                                                            ],
                                                        ),
                                                    ],
                                                    orelse=[],
                                                    finalbody=[],
                                                ),
                                            ],
                                            orelse=[],
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Name(id='response', ctx=Load()),
                        ),
                    ],
                    decorator_list=[Name(id='classmethod', ctx=Load())],
                    returns=None,
                    type_comment=None,
                ),
            ],
            decorator_list=[],
        ),
    ],
    type_ignores=[],
)
