Module(
    body=[
        ImportFrom(
            module='odoo',
            names=[
                alias(name='fields', asname=None),
                alias(name='models', asname=None),
            ],
            level=0,
        ),
        Import(
            names=[alias(name='requests', asname=None)],
        ),
        ClassDef(
            name='MailIceServer',
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
                    targets=[Name(id='_name', ctx=Store())],
                    value=Constant(value='mail.ice.server', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='_description', ctx=Store())],
                    value=Constant(value='ICE server', kind=None),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='server_type', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Selection',
                            ctx=Load(),
                        ),
                        args=[
                            List(
                                elts=[
                                    Tuple(
                                        elts=[
                                            Constant(value='stun', kind=None),
                                            Constant(value='stun:', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                    Tuple(
                                        elts=[
                                            Constant(value='turn', kind=None),
                                            Constant(value='turn:', kind=None),
                                        ],
                                        ctx=Load(),
                                    ),
                                ],
                                ctx=Load(),
                            ),
                        ],
                        keywords=[
                            keyword(
                                arg='string',
                                value=Constant(value='Type', kind=None),
                            ),
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                            keyword(
                                arg='default',
                                value=Constant(value='stun', kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='uri', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[Constant(value='URI', kind=None)],
                        keywords=[
                            keyword(
                                arg='required',
                                value=Constant(value=True, kind=None),
                            ),
                        ],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='username', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                Assign(
                    targets=[Name(id='credential', ctx=Store())],
                    value=Call(
                        func=Attribute(
                            value=Name(id='fields', ctx=Load()),
                            attr='Char',
                            ctx=Load(),
                        ),
                        args=[],
                        keywords=[],
                    ),
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_local_ice_servers',
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
                            value=Constant(value='\n        :return: List of up to 5 dict, each of which representing a stun or turn server\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='ice_servers', ctx=Store())],
                            value=Call(
                                func=Attribute(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='sudo',
                                            ctx=Load(),
                                        ),
                                        args=[],
                                        keywords=[],
                                    ),
                                    attr='search',
                                    ctx=Load(),
                                ),
                                args=[List(elts=[], ctx=Load())],
                                keywords=[
                                    keyword(
                                        arg='limit',
                                        value=Constant(value=5, kind=None),
                                    ),
                                ],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='formatted_ice_servers', ctx=Store())],
                            value=List(elts=[], ctx=Load()),
                            type_comment=None,
                        ),
                        For(
                            target=Name(id='ice_server', ctx=Store()),
                            iter=Name(id='ice_servers', ctx=Load()),
                            body=[
                                Assign(
                                    targets=[Name(id='formatted_ice_server', ctx=Store())],
                                    value=Dict(
                                        keys=[Constant(value='urls', kind=None)],
                                        values=[
                                            BinOp(
                                                left=Constant(value='%s:%s', kind=None),
                                                op=Mod(),
                                                right=Tuple(
                                                    elts=[
                                                        Attribute(
                                                            value=Name(id='ice_server', ctx=Load()),
                                                            attr='server_type',
                                                            ctx=Load(),
                                                        ),
                                                        Attribute(
                                                            value=Name(id='ice_server', ctx=Load()),
                                                            attr='uri',
                                                            ctx=Load(),
                                                        ),
                                                    ],
                                                    ctx=Load(),
                                                ),
                                            ),
                                        ],
                                    ),
                                    type_comment=None,
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='ice_server', ctx=Load()),
                                        attr='username',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='formatted_ice_server', ctx=Load()),
                                                    slice=Constant(value='username', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='ice_server', ctx=Load()),
                                                attr='username',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                If(
                                    test=Attribute(
                                        value=Name(id='ice_server', ctx=Load()),
                                        attr='credential',
                                        ctx=Load(),
                                    ),
                                    body=[
                                        Assign(
                                            targets=[
                                                Subscript(
                                                    value=Name(id='formatted_ice_server', ctx=Load()),
                                                    slice=Constant(value='credential', kind=None),
                                                    ctx=Store(),
                                                ),
                                            ],
                                            value=Attribute(
                                                value=Name(id='ice_server', ctx=Load()),
                                                attr='credential',
                                                ctx=Load(),
                                            ),
                                            type_comment=None,
                                        ),
                                    ],
                                    orelse=[],
                                ),
                                Expr(
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='formatted_ice_servers', ctx=Load()),
                                            attr='append',
                                            ctx=Load(),
                                        ),
                                        args=[Name(id='formatted_ice_server', ctx=Load())],
                                        keywords=[],
                                    ),
                                ),
                            ],
                            orelse=[],
                            type_comment=None,
                        ),
                        Return(
                            value=Name(id='formatted_ice_servers', ctx=Load()),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_twilio_credentials',
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
                            value=Constant(value=' To be overridable if we need to obtain credentials from another source.\n        :return: tuple\n        ', kind=None),
                        ),
                        Assign(
                            targets=[Name(id='account_sid', ctx=Store())],
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
                                args=[Constant(value='mail.twilio_account_sid', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Assign(
                            targets=[Name(id='auth_token', ctx=Store())],
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
                                args=[Constant(value='mail.twilio_account_token', kind=None)],
                                keywords=[],
                            ),
                            type_comment=None,
                        ),
                        Return(
                            value=Tuple(
                                elts=[
                                    Name(id='account_sid', ctx=Load()),
                                    Name(id='auth_token', ctx=Load()),
                                ],
                                ctx=Load(),
                            ),
                        ),
                    ],
                    decorator_list=[],
                    returns=None,
                    type_comment=None,
                ),
                FunctionDef(
                    name='_get_ice_servers',
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
                            value=Constant(value='\n        :return: List of dict, each of which representing a stun or turn server,\n                formatted as expected by the specifications of RTCConfiguration.iceServers\n        ', kind=None),
                        ),
                        If(
                            test=Call(
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
                                args=[Constant(value='mail.use_twilio_rtc_servers', kind=None)],
                                keywords=[],
                            ),
                            body=[
                                Assign(
                                    targets=[
                                        Tuple(
                                            elts=[
                                                Name(id='account_sid', ctx=Store()),
                                                Name(id='auth_token', ctx=Store()),
                                            ],
                                            ctx=Store(),
                                        ),
                                    ],
                                    value=Call(
                                        func=Attribute(
                                            value=Name(id='self', ctx=Load()),
                                            attr='_get_twilio_credentials',
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
                                            Name(id='account_sid', ctx=Load()),
                                            Name(id='auth_token', ctx=Load()),
                                        ],
                                    ),
                                    body=[
                                        Assign(
                                            targets=[Name(id='url', ctx=Store())],
                                            value=JoinedStr(
                                                values=[
                                                    Constant(value='https://api.twilio.com/2010-04-01/Accounts/', kind=None),
                                                    FormattedValue(
                                                        value=Name(id='account_sid', ctx=Load()),
                                                        conversion=-1,
                                                        format_spec=None,
                                                    ),
                                                    Constant(value='/Tokens.json', kind=None),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        Assign(
                                            targets=[Name(id='response', ctx=Store())],
                                            value=Call(
                                                func=Attribute(
                                                    value=Name(id='requests', ctx=Load()),
                                                    attr='post',
                                                    ctx=Load(),
                                                ),
                                                args=[Name(id='url', ctx=Load())],
                                                keywords=[
                                                    keyword(
                                                        arg='auth',
                                                        value=Tuple(
                                                            elts=[
                                                                Name(id='account_sid', ctx=Load()),
                                                                Name(id='auth_token', ctx=Load()),
                                                            ],
                                                            ctx=Load(),
                                                        ),
                                                    ),
                                                    keyword(
                                                        arg='timeout',
                                                        value=Constant(value=60, kind=None),
                                                    ),
                                                ],
                                            ),
                                            type_comment=None,
                                        ),
                                        If(
                                            test=Attribute(
                                                value=Name(id='response', ctx=Load()),
                                                attr='ok',
                                                ctx=Load(),
                                            ),
                                            body=[
                                                Assign(
                                                    targets=[Name(id='response_content', ctx=Store())],
                                                    value=Call(
                                                        func=Attribute(
                                                            value=Name(id='response', ctx=Load()),
                                                            attr='json',
                                                            ctx=Load(),
                                                        ),
                                                        args=[],
                                                        keywords=[],
                                                    ),
                                                    type_comment=None,
                                                ),
                                                If(
                                                    test=Name(id='response_content', ctx=Load()),
                                                    body=[
                                                        Return(
                                                            value=Subscript(
                                                                value=Name(id='response_content', ctx=Load()),
                                                                slice=Constant(value='ice_servers', kind=None),
                                                                ctx=Load(),
                                                            ),
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
                            ],
                            orelse=[],
                        ),
                        Return(
                            value=Call(
                                func=Attribute(
                                    value=Name(id='self', ctx=Load()),
                                    attr='_get_local_ice_servers',
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
