Module(
    body=[
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='api', asname=None),
                alias(name='models', asname=None),
                alias(name='exceptions', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.addons.iap.tools',
            names=[alias(name='iap_tools', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='requests.exceptions',
            names=[alias(name='HTTPError', asname=None)],
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
            name='IapAutocompleteEnrichAPI',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='iap.autocomplete.api', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='IAP Partner Autocomplete API', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_DEFAULT_ENDPOINT', ctx=Store())],
                    value=Constant(value='https://partner-autocomplete.odoo.com', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_contact_iap',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='local_endpoint', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=15, kind=None)],
                    ),
                    body=[
                        If(
                            test=Call(
                                func=Attribute(
                                    value=Attribute(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        attr='registry',
                                        ctx=Load(),
                                    ),
                                    attr='in_test_mode',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Attribute(
                                            value=Name(id='exceptions', ctx=Load()),
                                            attr='ValidationError',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='Test mode', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Assign(
                            targets=[Name(id='account', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Subscript(
                                        value=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='env',
                                            ctx=Load(),
                                        ),
                                        slice=Constant(value='iap.account', kind=None),
                                        ctx=Load(),
                                    ),
                                    attr='get',
                                    ctx=Load(),
                                ),
                                args=[Constant(value='partner_autocomplete', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Attribute(
                                    value=Name(id='account', ctx=Load()),
                                    attr='account_token',
                                    ctx=Load(),
                                ),
                            ),
                            body=[
                                Raise(
                                    exc=Call(
                                        func=Name(id='ValueError', ctx=Load()),
                                        args=[
                                            Call(
                                                func=Name(id='_', ctx=Load()),
                                                args=[Constant(value='No account token', kind=None)],
                                                keywords=[],
                                            ),
                                        ],
                                        keywords=[],
                                    ),
                                    cause=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Expr(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='params', ctx=Load()),
                                    attr='update',
                                    ctx=Load(),
                                ),
                                args=[
                                    Dict(
                                        keys=[
                                            Constant(value='db_uuid', kind=None),
                                            Constant(value='account_token', kind=None),
                                            Constant(value='country_code', kind=None),
                                            Constant(value='zip', kind=None),
                                        ],
                                        values=[
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
                                                args=[Constant(value='database.uuid', kind=None)],
                                                keywords=[],
                                            ),
                                            Attribute(
                                                value=Name(id='account', ctx=Load()),
                                                attr='account_token',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Attribute(
                                                            value=Name(id='self', ctx=Load()),
                                                            attr='env',
                                                            ctx=Load(),
                                                        ),
                                                        attr='company',
                                                        ctx=Load(),
                                                    ),
                                                    attr='country_id',
                                                    ctx=Load(),
                                                ),
                                                attr='code',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Attribute(
                                                    value=Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='env',
                                                        ctx=Load(),
                                                    ),
                                                    attr='company',
                                                    ctx=Load(),
                                                ),
                                                attr='zip',
                                                ctx=Load(),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
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
                                args=[
                                    Constant(value='iap.partner_autocomplete.endpoint', kind=None),
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='_DEFAULT_ENDPOINT',
                                        ctx=Load(),
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='iap_tools', ctx=Load()),
                                    attr='iap_jsonrpc',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=BinOp(
                                            left=BinOp(
                                                left=Name(id='base_url', ctx=Load()),
                                                op=Add(),
                                                right=Name(id='local_endpoint', ctx=Load()),
                                            ),
                                            op=Add(),
                                            right=Constant(value='/', kind=None),
                                        ),
                                        op=Add(),
                                        right=Name(id='action', ctx=Load()),
                                    ),
                                ],
                                keywords=[
                                    keyword(
                                        arg='params',
                                        value=Name(id='params', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Name(id='timeout', ctx=Load()),
                                    ),
                                ],
                            ),
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
                    name='_request_partner_autocomplete',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='action', annotation=None, type_comment=None),
                            arg(arg='params', annotation=None, type_comment=None),
                            arg(arg='timeout', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=15, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=' Contact endpoint to get autocomplete data.\n\n        :return tuple: results, error code\n        ', kind=None),
                        ),
                        Try(
                            body=[
                                Assign(
                                    targets=[Name(id='results', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_contact_iap',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            Constant(value='/iap/partner_autocomplete', kind=None),
                                            Name(id='action', ctx=Load()),
                                            Name(id='params', ctx=Load()),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='timeout',
                                                value=Name(id='timeout', ctx=Load()),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                            ],
                            handlers=[
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='exceptions', ctx=Load()),
                                        attr='ValidationError',
                                        ctx=Load(),
                                    ),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Insufficient Credit', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Tuple(
                                        elts=[
                                            Name(id='ConnectionError', ctx=Load()),
                                            Name(id='HTTPError', ctx=Load()),
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='AccessError',
                                                ctx=Load(),
                                            ),
                                            Attribute(
                                                value=Name(id='exceptions', ctx=Load()),
                                                attr='UserError',
                                                ctx=Load(),
                                            ),
                                        ],
                                        ctx=Load(),
                                    ),
                                    name='exception',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='error',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Autocomplete API error: %s', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='exception', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='exception', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Attribute(
                                        value=Name(id='iap_tools', ctx=Load()),
                                        attr='InsufficientCreditError',
                                        ctx=Load(),
                                    ),
                                    name='exception',
                                    body=[
                                        Expr(
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='_logger', ctx=Load()),
                                                    attr='warning',
                                                    ctx=Load(),
                                                ),
                                                args=[
                                                    Constant(value='Insufficient Credits for Autocomplete Service: %s', kind=None),
                                                    Call(
                                                        func=Name(id='str', ctx=Load()),
                                                        args=[Name(id='exception', ctx=Load())],
                                                        keywords=[],
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                        ),
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='Insufficient Credit', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                                ExceptHandler(
                                    type=Name(id='ValueError', ctx=Load()),
                                    name=None,
                                    body=[
                                        Return(
                                            value=Tuple(
                                                elts=[
                                                    Constant(value=False, kind=None),
                                                    Constant(value='No account token', kind=None),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ),
                                    ],
                                ),
                            ],
                            orelse=[],
                            finalbody=[],
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='results', ctx=Load()),
                                    Constant(value=False, kind=None),
                                ],
                                ctx=Load(),
                            ),
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
