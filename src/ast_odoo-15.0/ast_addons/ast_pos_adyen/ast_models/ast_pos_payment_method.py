Module(
    body=[
        Import(
            names=[alias(name='json', asname=None)],
        ),
        Import(
            names=[alias(name='logging', asname=None)],
        ),
        Import(
            names=[alias(name='pprint', asname=None)],
        ),
        Import(
            names=[alias(name='random', asname=None)],
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        Import(
            names=[alias(name='string', asname=None)],
        ),
        ImportFrom(
            module='werkzeug.exceptions',
            names=[alias(name='Forbidden', asname=None)],
            level=0,
        ),
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
                alias(name='api', asname=None),
                alias(name='_', asname=None),
            ],
            level=0,
        ),
        ImportFrom(
            module='odoo.exceptions',
            names=[alias(name='ValidationError', asname=None)],
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
            name='PosPaymentMethod',
            bases=[
                Attribute(
                    value=Name(id='models', ctx=Load()),
                    attr='Model',
                    ctx=Load(),
                ),
            ],
            keywords=[],
            body=[
                Assign(
                    targets=[Name(id='_inherit', ctx=Store())],
                    value=Constant(value='pos.payment.method', kind=None),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_payment_terminal_selection',
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
                        Return(
                            value=BinOp(
                                left=Call(
                                    func=Attribute(
                                        value=Call(
                                            func=Name(id='super', ctx=Load()),
                                            args=[
                                                Name(id='PosPaymentMethod', ctx=Load()),
                                                Name(id='self', ctx=Load()),
                                            ],
                                            keywords=[],
                                        ),
                                        attr='_get_payment_terminal_selection',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                op=Add(),
                                right=List(
                                    elts=[
                                        Tuple(
                                            elts=[
                                                Constant(value='adyen', kind=None),
                                                Constant(value='Adyen', kind=None),
                                            ],
                                            ctx=Load(),
                                        ),
                                    ],
                                    ctx=Load(),
                                ),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='adyen_api_key', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Adyen API key', kind=None),
                            ),
                            keyword(
                                arg='help',
                                value=Constant(value='Used when connecting to Adyen: https://docs.adyen.com/user-management/how-to-get-the-api-key/#description', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='adyen_terminal_identifier', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='[Terminal model]-[Serial number], for example: P400Plus-123456789', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='adyen_test_mode', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Boolean',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Run transactions in the test environment.', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='adyen_latest_response', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field used to buffer the latest asynchronous notification from Adyen.', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_erp_manager', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='adyen_latest_diagnosis', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[
                            keyword(
                                arg='help',
                                value=Constant(value='Technical field used to determine if the terminal is still connected.', kind=None),
                            ),
                            keyword(
                                arg='copy',
                                value=Constant(value=False, kind=None),
                            ),
                            keyword(
                                arg='groups',
                                value=Constant(value='base.group_erp_manager', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_check_adyen_terminal_identifier',
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
                        For(
                            target=Name(id='payment_method', ctx=Store()),
                            iter=Name(id='self', ctx=Load()),
                            body=[
                                If(
                                    test=UnaryOp(
                                        op=Not(),
                                        operand=Attribute(
                                            value=Name(id='payment_method', ctx=Load()),
                                            attr='adyen_terminal_identifier',
                                            ctx=Load(),
                                        ),
                                    ),
                                    body=[Continue()],
                                    orelse=[],
                                ),
                                Assign(
                                    targets=[Name(id='existing_payment_method', ctx=Store())],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='search',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            List(
                                                elts=[
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='id', kind=None),
                                                            Constant(value='!=', kind=None),
                                                            Attribute(
                                                                value=Name(id='payment_method', ctx=Load()),
                                                                attr='id',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                    Tuple(
                                                        elts=[
                                                            Constant(value='adyen_terminal_identifier', kind=None),
                                                            Constant(value='=', kind=None),
                                                            Attribute(
                                                                value=Name(id='payment_method', ctx=Load()),
                                                                attr='adyen_terminal_identifier',
                                                                ctx=Load(),
                                                            ),
                                                        ],
                                                        ctx=Load(),
                                                    ),
                                                ],
                                                ctx=Load(),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='limit',
                                                value=Constant(value=1, kind=None),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Name(id='existing_payment_method', ctx=Load()),
                                    body=[
                                        Raise(
                                            exc=Call(
                                                func=Name(id='ValidationError', ctx=Load()),
                                                args=[
                                                    BinOp(
                                                        left=Call(
                                                            func=Name(id='_', ctx=Load()),
                                                            args=[Constant(value='Terminal %s is already used on payment method %s.', kind=None)],
                                                            keywords=[],
                                                        ),
                                                        op=Mod(),
                                                        right=Tuple(
                                                            elts=[
                                                                Attribute(
                                                                    value=Name(id='payment_method', ctx=Load()),
                                                                    attr='adyen_terminal_identifier',
                                                                    ctx=Load(),
                                                                ),
                                                                Attribute(
                                                                    value=Name(id='existing_payment_method', ctx=Load()),
                                                                    attr='display_name',
                                                                    ctx=Load(),
                                                                ),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                ],
                                                keywords=[],
                                            ),
                                            cause=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                    ],
                    decorator_list=[
                        Call(
                            func=Attribute(
                                value=Name(id='api', ctx=Load()),
                                attr='constrains',
                                ctx=Load(),
                            ),
                            args=[Constant(value='adyen_terminal_identifier', kind=None)],
                            keywords=[],
                        ),
                    ],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_adyen_endpoints',
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
                        Return(
                            value=Dict(
                                keys=[Constant(value='terminal_request', kind=None)],
                                values=[Constant(value='https://terminal-api-%s.adyen.com/async', kind=None)],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_is_write_forbidden',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='fields', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='whitelisted_fields', ctx=Store())],
                            value=Call(
                                func=Name(id='set', ctx=Load()),
                                args=[
                                    Tuple(
                                        elts=[
                                            Constant(value='adyen_latest_response', kind=None),
                                            Constant(value='adyen_latest_diagnosis', kind=None),
                                        ],
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
                                    value=Call(
                                        func=Name(id='super', ctx=Load()),
                                        args=[
                                            Name(id='PosPaymentMethod', ctx=Load()),
                                            Name(id='self', ctx=Load()),
                                        ],
                                        keywords=[],
                                    ),
                                    attr='_is_write_forbidden',
                                    ctx=Load(),
                                ),
                                args=[
                                    BinOp(
                                        left=Name(id='fields', ctx=Load()),
                                        op=Sub(),
                                        right=Name(id='whitelisted_fields', ctx=Load()),
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
                    name='_adyen_diagnosis_request_data',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pos_config_name', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[],
                    ),
                    body=[
                        Assign(
                            targets=[Name(id='service_id', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Constant(value='', kind=None),
                                    attr='join',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='random', ctx=Load()),
                                            attr='choices',
                                            ctx=Load(),
                                        ),
                                        args=[
                                            BinOp(
                                                left=Attribute(
                                                    value=Name(id='string', ctx=Load()),
                                                    attr='ascii_letters',
                                                    ctx=Load(),
                                                ),
                                                op=Add(),
                                                right=Attribute(
                                                    value=Name(id='string', ctx=Load()),
                                                    attr='digits',
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                        keywords=[
                                            keyword(
                                                arg='k',
                                                value=Constant(value=10, kind=None),
                                            ),
                                        ],
                                    ),
                                ],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[Constant(value='SaleToPOIRequest', kind=None)],
                                values=[
                                    Dict(
                                        keys=[
                                            Constant(value='MessageHeader', kind=None),
                                            Constant(value='DiagnosisRequest', kind=None),
                                        ],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='ProtocolVersion', kind=None),
                                                    Constant(value='MessageClass', kind=None),
                                                    Constant(value='MessageCategory', kind=None),
                                                    Constant(value='MessageType', kind=None),
                                                    Constant(value='ServiceID', kind=None),
                                                    Constant(value='SaleID', kind=None),
                                                    Constant(value='POIID', kind=None),
                                                ],
                                                values=[
                                                    Constant(value='3.0', kind=None),
                                                    Constant(value='Service', kind=None),
                                                    Constant(value='Diagnosis', kind=None),
                                                    Constant(value='Request', kind=None),
                                                    Name(id='service_id', ctx=Load()),
                                                    Name(id='pos_config_name', ctx=Load()),
                                                    Attribute(
                                                        value=Name(id='self', ctx=Load()),
                                                        attr='adyen_terminal_identifier',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                            Dict(
                                                keys=[Constant(value='HostDiagnosisFlag', kind=None)],
                                                values=[Constant(value=False, kind=None)],
                                            ),
                                        ],
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='get_latest_adyen_status',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='pos_config_name', annotation=None, type_comment=None),
                        ],
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
                                    attr='ensure_one',
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
                                    attr='proxy_adyen_request',
                                    ctx=Load(),
                                ),
                                args=[
                                    Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_adyen_diagnosis_request_data',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='pos_config_name', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='latest_response', ctx=Store())],
                            value=Attribute(
                                value=Call(
                                    func=Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='sudo',
                                        ctx=Load(),
                                    ),
                                    args=[],
                                    keywords=[],
                                ),
                                attr='adyen_latest_response',
                                ctx=Load(),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='latest_response', ctx=Store())],
                            value=IfExp(
                                test=Name(id='latest_response', ctx=Load()),
                                body=Call(
                                    func=Attribute(
                                        value=Name(id='json', ctx=Load()),
                                        attr='loads',
                                        ctx=Load(),
                                    ),
                                    args=[Name(id='latest_response', ctx=Load())],
                                    keywords=[],
                                ),
                                orelse=Constant(value=False, kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[
                                Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='adyen_latest_response',
                                    ctx=Store(),
                                ),
                            ],
                            value=Constant(value='', kind=None),
                            type_comment=None,
                        ),
                        Return(
                            value=Dict(
                                keys=[
                                    Constant(value='latest_response', kind=None),
                                    Constant(value='last_received_diagnosis_id', kind=None),
                                ],
                                values=[
                                    Name(id='latest_response', ctx=Load()),
                                    Attribute(
                                        value=Call(
                                            func=Attribute(
                                                value=Name(id='self', ctx=Load()),
                                                attr='sudo',
                                                ctx=Load(),
                                            ),
                                            args=[],
                                            keywords=[],
                                        ),
                                        attr='adyen_latest_diagnosis',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='proxy_adyen_request',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='operation', annotation=None, type_comment=None),
                        ],
                        vararg=None,
                        kwonlyargs=[],
                        kw_defaults=[],
                        kwarg=None,
                        defaults=[Constant(value=False, kind=None)],
                    ),
                    body=[
                        Expr(
                            value=Constant(value=" Necessary because Adyen's endpoints don't have CORS enabled ", kind=None),
                        ),
                        If(
                            test=UnaryOp(
                                op=Not(),
                                operand=Name(id='operation', ctx=Load()),
                            ),
                            body=[
                                Assign(
                                    targets=[Name(id='operation', ctx=Store())],
                                    value=Constant(value='terminal_request', kind=None),
                                    type_comment=None,
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_proxy_adyen_request_direct',
                                    ctx=Load(),
                                ),
                                args=[
                                    Name(id='data', ctx=Load()),
                                    Name(id='operation', ctx=Load()),
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
                    name='_proxy_adyen_request_direct',
                    args=arguments(
                        posonlyargs=[],
                        args=[
                            arg(arg='self', annotation=None, type_comment=None),
                            arg(arg='data', annotation=None, type_comment=None),
                            arg(arg='operation', annotation=None, type_comment=None),
                        ],
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
                                    attr='ensure_one',
                                    ctx=Load(),
                                ),
                                args=[],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='TIMEOUT', ctx=Store())],
                            value=Constant(value=10, kind=None),
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
                                    Constant(value='request to adyen\n%s', kind=None),
                                    Call(
                                        func=Attribute(
                                            value=Name(id='pprint', ctx=Load()),
                                            attr='pformat',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='data', ctx=Load())],
                                        keywords=[],
                                    ),
                                ],
                                keywords=[],
                            ),
                        ),
                        Assign(
                            targets=[Name(id='environment', ctx=Store())],
                            value=IfExp(
                                test=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='adyen_test_mode',
                                    ctx=Load(),
                                ),
                                body=Constant(value='test', kind=None),
                                orelse=Constant(value='live', kind=None),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='endpoint', ctx=Store())],
                            value=BinOp(
                                left=Subscript(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_adyen_endpoints',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    slice=Name(id='operation', ctx=Load()),
                                    ctx=Load(),
                                ),
                                op=Mod(),
                                right=Name(id='environment', ctx=Load()),
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='headers', ctx=Store())],
                            value=Dict(
                                keys=[Constant(value='x-api-key', kind=None)],
                                values=[
                                    Attribute(
                                        value=Name(id='self', ctx=Load()),
                                        attr='adyen_api_key',
                                        ctx=Load(),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='req', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Name(id='requests', ctx=Load()),
                                    attr='post',
                                    ctx=Load(),
                                ),
                                args=[Name(id='endpoint', ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='json',
                                        value=Name(id='data', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='headers',
                                        value=Name(id='headers', ctx=Load()),
                                    ),
                                    keyword(
                                        arg='timeout',
                                        value=Name(id='TIMEOUT', ctx=Load()),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='req', ctx=Load()),
                                    attr='status_code',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value=401, kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Dict(
                                        keys=[Constant(value='error', kind=None)],
                                        values=[
                                            Dict(
                                                keys=[
                                                    Constant(value='status_code', kind=None),
                                                    Constant(value='message', kind=None),
                                                ],
                                                values=[
                                                    Attribute(
                                                        value=Name(id='req', ctx=Load()),
                                                        attr='status_code',
                                                        ctx=Load(),
                                                    ),
                                                    Attribute(
                                                        value=Name(id='req', ctx=Load()),
                                                        attr='text',
                                                        ctx=Load(),
                                                    ),
                                                ],
                                            ),
                                        ],
                                    ),
                                ),
                            ],
                            orelse=[],
                        ),
                        If(
                            test=Compare(
                                left=Attribute(
                                    value=Name(id='req', ctx=Load()),
                                    attr='text',
                                    ctx=Load(),
                                ),
                                ops=[Eq()],
                                comparators=[Constant(value='ok', kind=None)],
                            ),
                            body=[
                                Return(
                                    value=Constant(value=True, kind=None),
                                ),
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='req', ctx=Load()),
                                    attr='json',
                                    ctx=Load(),
                                ),
                                args=[],
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
